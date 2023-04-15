import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.chains import load_chain

app = FastAPI()

class QueryInput(BaseModel):
    query: str

with open('model.txt', 'r') as f:
    data = f.read()


loader = TextLoader('model.txt')
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_text(data)

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(texts, embeddings)

chain = load_chain("lc://chains/vector-db-qa/stuff/chain.json", vectorstore=vectorstore)

@app.post("/answer")
async def answer_query(query_input: QueryInput):
    query = query_input.query
    answer = chain.run(query)
    return {"answer": answer}
