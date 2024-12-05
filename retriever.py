from langchain_chroma import Chroma
from path_helper import get_absolute_path
from langchain.agents import Tool

from langchain_openai import OpenAIEmbeddings

from constants import OPENAI_API_KEY
from split_text import test_split_text

import chromadb

def retriever():
    chroma_client = chromadb.Client()

    df_document = test_split_text("training_data2.jsonl")

    model_name = 'text-embedding-ada-002'

    embed = OpenAIEmbeddings(
        model=model_name,
        openai_api_key=OPENAI_API_KEY
    )


# load it into Chroma
    db = Chroma.from_documents(df_document, embed)
    return db

# def query(q):
# query it

    # docs = db.similarity_search(q)
    # return docs[0].page_content

# print results
# print(docs[0].page_content)



