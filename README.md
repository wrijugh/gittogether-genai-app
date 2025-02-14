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
ENDPOINT=""
KEY=""
API-VERSION=""

MODEL-DEPLOYMENT-NAME=""
```

## Use Jupyter Notebook to test your code
Use Jupyter Notebook to test your code. This is a great way to explore fast and fail fast. 

Please refer the notebook in this repo, file name ending with `.ipynb`.

Sample code block:
```python

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
