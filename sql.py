import os
import sys


from langchain_community.utilities import SQLDatabase
import constants
import pandas as pd

os.environ['OPENAI_API_KEY'] = constants.OPENAI_API_KEY

from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine

from langchain_openai import ChatOpenAI

from langchain_community.agent_toolkits import create_sql_agent, SQLDatabaseToolkit

df = pd.read_csv("Moneiva.csv")
engine = create_engine("moneiva.db")
#df.to_sql("moneiva", engine, index=False)
df.to_sql('moneiva', engine, if_exists='replace')
# print(df.shape)
# print(df.columns.tolist())

db = SQLDatabase(engine=engine)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

toolkit = SQLDatabaseToolkit(db=db, llm=llm)


agent_executor = create_sql_agent(llm, toolkit, agent_type="openai-tools", verbose=True)
agent_executor.invoke({"input": "what's the load_number?"})