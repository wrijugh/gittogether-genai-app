# Intelligent Application Development using Generative AI

**Introduction**
Imagine you are going to build an application which will leverage the power of Generative AI. Here is the step-by-step approach to handle it.

## Setup a GitHub Account
Setup a new GitHub Account or use an existing one. Create a repository and clone it to your local development environment or use codespace. 

## Select a Programming Language
Here we will use Python. But you can select any programming language of your choice. 

## Install the libraries
Install the following Python libraries: `python-dotenv`, `openai`, `streamlit`

```sh
pip install python-dotenv openai streamlit
```
> **Note:** In your machine pip3 might work.

## Create .env file for secrets
Create a `.env` to store the secrets. 

```bash
DEPLOYMENT_ENDPOINT=""
DEPLOYMENT_NAME=""
DEPLOYMENT_TOKEN=""
```

## Use Jupyter Notebook to test your code
Use Jupyter Notebook to test your code. This is a great way to explore fast and fail fast. 

Please refer the notebook in this repo, file name ending with `.ipynb`.

[Deepseek-R1 Python Jupyter Notebook](deepseekr1-app/deepseekr1-test.ipynb)

## Test the Streamlit
Streamlit is a great library to do a quick PoC. This helps build and host web interface for any kind of application with minimal effort. 

Save a file such as [dseekweb.py](deepseekr1-app/dseekweb.py)


## Run the Streamlit app locally
To run the Streamlit app for the file `demoweb.py` locally, type the below command,

```sh
streamlit run dseekweb.py
```

## Dockerfil

[DeepSeekR1-App Dockerfile](deepseekr1-app/Dockerfile)

>Check the last line in above Dockerfile  
```sh
ENTRYPOINT ["streamlit", "run", "dseekweb.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## Build docker image

```sh
docker build -t wrijughosh/deepseek-web:v3 .
```
>**Note:** `wrijughosh` is the name of public docker hub account based on which the repo will be created. Use proper name as per your information. 


## Run Docker locally

```sh
docker run -p 8501:8501  wrijughosh/deepseek-web:v3
```


## Connect to the DockerHub

```sh
docker login
```

## Push the local docker image to DockerHub

```sh
docker push wrijughosh/deepseek-web:v3
```

## Deploy it to Azure Container App/Kubernetes/AppService/Azure Container Instance
