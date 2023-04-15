from fastapi import FastAPI
from jupyter_server_proxy import ServerProxy
from jupyter_client import AsyncKernelManager, KernelManager
from nbformat.current import read

app = FastAPI()

# Serve the static HTML and JavaScript for the web app
# app.mount("/", StaticFiles(directory="static"), name="static")

# Launch the Jupyter notebook server as a subprocess
notebook_server = ServerProxy(
    command=["jupyter", "notebook", "longchain_over_docs.ipynb", "--no-browser"],
    uri='/jupyter',
    prefix='notebooks/',
    port=8888,
    timeout=120,
)

async def get_notebook():
    kernel_manager = KernelManager(kernel_name='python3')
    await kernel_manager.start_kernel()
    kernel_client = kernel_manager.client()
    kernel_client.start_channels()

    kernel = await AsyncKernelManager(kernel_manager=kernel_manager).connect_kernel()
    notebook = read(open('notebook.ipynb', 'r'), 'json')
    await kernel.execute("")
    await kernel.execute("\n".join([cell.source for cell in notebook.cells if cell.cell_type == "code"]))

    return kernel

# Define a route for the web app to display the results of the Jupyter notebook
# @app.get("/results")
# async def results():
#     kc.execute("result = user_query('What is Basic Engineering', ' ')")
#     # Load the results HTML file generated by the Jupyter notebook
#     msg_id = kc.execute("result")
#     response = kc.get_shell_msg(msg_id)["content"]["data"]["text/plain"]

#     # Close the connection to the Jupyter notebook server
#     km.shutdown_kernel()

#     return {"result": response}

@app.post("/query")
async def post_query(text1: str, text2: str):
    nb = await get_notebook()
    result = await nb.run_cell(f"user_query('What is Basic Engineering', ' ')")
    return {"result": result.result}