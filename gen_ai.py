#!/usr/bin/env python
# coding: utf-8

# In[1]:


from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate


# In[2]:

from dotenv import load_dotenv
import os

# =========================
# LOAD ENV VARIABLES
# =========================

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY is None:
    raise ValueError(
        "GOOGLE_API_KEY not found. Please add it to your .env file."
    )



# In[3]:


def get_llm(path):

    loader = DirectoryLoader(
        path=path,
        glob = "**/*.pdf",
        loader_cls = PyPDFLoader
    )

    documents=loader.load()
    print('total pages=',len(documents))

    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=300
    )

    docs= text_splitter.split_documents(documents)
    print('total chubks=', len(docs))

    embeddings=HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2")

    print("embedding work successfully")

    vectorstore = FAISS.from_documents(
        docs,
        embeddings
    )

    print('FAISS OKAY')

    retriever = vectorstore.as_retriever(
        search_type='similarity',
        search_kwargs={'k':6}
    )

    print('Retriever is ready')

    llm = ChatGoogleGenerativeAI(
        model = 'gemini-2.5-flash',
        google_api_key=GOOGLE_API_KEY,
        temperature=0.3)

    print('model loading')

    prompt_template = """
    Use the following context to answer the question accurately.
    If answer is present in the context, answer directly and clearly.
    Do not add extra information.

    Context:
    {context}

    Question:
    {question}

    Answer:
    
    """

    PROMPT=PromptTemplate(
        template=prompt_template,
        input_variables=['context','question']
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=retriever,
    chain_type_kwargs={'prompt':PROMPT}
    )

    print('Rag pipline is ready')

    return qa_chain
    


# In[ ]:


#get_ipython().system('jupyter nbconvert --to script gen_ai.ipynb')


# In[ ]:





# In[ ]:




