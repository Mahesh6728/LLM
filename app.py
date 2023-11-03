# Q&A Chatbot
from langchain.llms import OpenAI

#from dotenv import load_dotenv

#load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
os.environ["OPEN_API_KEY"] = "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"


## Function to load OpenAI model and get respones

def get_openai_response(question):
    llm=OpenAI(openai_api_key = os.getenv("OPEN_API_KEY"),model_name="text-davinci-003",temperature=0.5)
    response=llm(question)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")
st.markdown(""" <style> custom.css </style>""", unsafe_allow_html=True)
st.subheader("Ask any questions, Get Answers!")


# with open("index.html", "r") as f:
#     html_content = f.read()
# st.components.v1.html(html_content,width = 700, height = 500)


input=st.text_input("Input: ",key="input")
response=get_openai_response(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    with st.spinner("loading...."):
        response=get_openai_response(input)
    st.subheader("The Response is")
    st.write(response)



