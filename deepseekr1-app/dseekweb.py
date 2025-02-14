import streamlit as st
import dseek

st.title("Deepseek-R1 Web App Demo - V3")
st.write("Developed by Wriju Ghosh for demo purposes. [14 February 2025]")
st.write("This is a simple app that demonstrates how to use the ChatCompletionsClient to interact with the deployed DeepSeek-R1 model")

query = st.text_area("Enter your query here:")
client = dseek.create_client()
full_response = ""

if st.button("Submit"):
    with st.spinner("Fetching response..."):
        response_container = st.empty()
        for update in dseek.get_response(client, query):
            if update.choices:
                if update.choices and update.choices[0].delta.content:
                    full_response += update.choices[0].delta.content
                    response_container.markdown(full_response) #update incrementally

        client.close()