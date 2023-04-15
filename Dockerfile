# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Set up Jupyter notebook
RUN jupyter notebook --generate-config && \
    echo "c.NotebookApp.allow_origin = '*'" >> ~/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.token = ''" >> ~/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password = ''" >> ~/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.open_browser = False" >> ~/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.ip = '0.0.0.0'" >> ~/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.notebook_dir = '/app'" >> ~/.jupyter/jupyter_notebook_config.py

# Expose the Jupyter notebook port
EXPOSE 8888

# Set up the entry point for running the Jupyter notebook and FastAPI app
CMD ["sh", "-c", "jupyter notebook & uvicorn main:app --host 0.0.0.0 --port 8000 --workers 1"]
