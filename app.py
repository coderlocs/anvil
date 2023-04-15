from fastapi import FastAPI
from pydantic import BaseModel
from database import PostgresDatabase
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import load_chain

app = FastAPI()

class QueryInput(BaseModel):
    query: str

# Initialize database connection
db = PostgresDatabase()

# Load pre-trained model from database
model_data = db.query("SELECT data FROM models WHERE name = 'engineering'")
text_model_input = bytes(model_data).decode('utf-8')

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_text(text_model_input)

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(texts, embeddings)

chain = load_chain("lc://chains/vector-db-qa/stuff/chain.json", vectorstore=vectorstore)

@app.post("/answer")
async def answer_query(query_input: QueryInput):
    query = query_input.query
    answer = chain.run(query)
    return {"answer": answer}

# Close database connection when the app is shut down
@app.on_event("shutdown")
async def shutdown_event():
    db.close()
