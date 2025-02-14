

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

import streamlit as st
st.title('Welcome to Streamlit!')

userprompt = st.text_input('Locality where you want to find vegan restaurants', 'Bellandur, Bengaluru')

if st.button('Submit'):
    response = client.chat.completions.create(
    model = os.getenv("AZURE_OPENAI_COMPLETION_DEPLOYMENT_NAME"),
    messages = [{"role" : "assistant", "content" : "Tell the resturants which serves vegan. in the area " + userprompt}],
    )


    st.write(response.choices[0].message.content)
