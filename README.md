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
OPENAI_API_VERSION = "2024-07-01-preview"
OPENAI_EMBEDDING_API_VERSION = "2024-07-01-preview"

AZURE_OPENAI_API_KEY = ""
AZURE_OPENAI_ENDPOINT = ""

AZURE_OPENAI_COMPLETION_MODEL = ""
AZURE_OPENAI_COMPLETION_DEPLOYMENT_NAME = ""

DEPLOYMENT_ENDPOINT=""
DEPLOYMENT_NAME=""
DEPLOYMENT_TOKEN=""
```

## Use Jupyter Notebook to test your code
Use Jupyter Notebook to test your code. This is a great way to explore fast and fail fast. 

Please refer the notebook in this repo, file name ending with `.ipynb`.

```python
# Jupyter Notebook sample code
import openai
import os
from dotenv import load_dotenv

# Load environment variables
if load_dotenv():
    print("Found Azure OpenAI API Base Endpoint: " + os.getenv("AZURE_OPENAI_ENDPOINT"))
else: 
    print("Azure OpenAI API Base Endpoint not found. Have you configured the .env file?")


from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key = os.getenv("AZURE_OPENAI_API_KEY"),
    api_version = os.getenv("OPENAI_API_VERSION")
)


userprompt = "Bellandu, Bengaluru" # st.text_input('Locality where you want to find vegan restaurants', 'Bellandur, Bengaluru')

# if st.button('Submit'):
response = client.chat.completions.create(
model = os.getenv("AZURE_OPENAI_COMPLETION_DEPLOYMENT_NAME"),
messages = [{"role" : "assistant", "content" : "Tell the resturants which serves vegan. in the area : " + userprompt}],
)


print(response.choices[0].message.content)


```

## Test the Streamlit
Streamlit is a great library to do a quick PoC. This helps build and host web interface for any kind of application with minimal effort. 

Save a file as `demoweb.py`

```python
# Sample Streamlit code
```

## Run the Streamlit app locally
To run the Streamlit app for the file `demoweb.py` locally, type the below command,

```sh
streamlit run demoweb.py
```

## Dockerfil

## Build docker image

## Run Docker locally

## Connect to the DockerHub

## Push the local docker image to DockerHub

## Deploy it to Azure Container App/Kubernetes/AppService/Azure Container Instance
