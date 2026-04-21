import streamlit as st
from langchain_openai import OpenAI
from langchain.text_splitter import CharacterTextSplitter
#from langchain_openai import OpenAIEmbeddings
#from langchain_community.vectorstores import Chroma
#from langchain.chains import RetrievalQA

def generate_response(file, api_key, query):
    from openai import OpenAI

    client = OpenAI(api_key=api_key)

    text = file.read().decode("utf-8")

    prompt = f"""
    Answer the question based on the document below.

    Document:
    {text}

    Question:
    {query}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
# Page title
st.set_page_config(page_title='🦜🔗 Ask the Doc App')
st.title('🦜🔗 Ask the Doc App')

# File upload
uploaded_file = st.file_uploader('Upload an article', type='txt')
# Query text
query_text = st.text_input('Enter your question:', placeholder = 'Please provide a short summary.', disabled=not uploaded_file)

# Form input and query
result = []
with st.form('myform', clear_on_submit=True):
    openai_api_key = st.text_input('OpenAI API Key', type='password', disabled=not (uploaded_file and query_text))
    submitted = st.form_submit_button('Submit', disabled=not(uploaded_file and query_text))
    if submitted and openai_api_key.startswith('sk-'):
        with st.spinner('Calculating...'):
            response = generate_response(uploaded_file, openai_api_key, query_text)
            result.append(response)
            del openai_api_key

if len(result):
    st.info(response)








