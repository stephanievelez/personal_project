from constants import OPENAI_API_KEY
from langchain_openai import OpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.chains import RetrievalQA
from retriever import retriever
from langchain.agents import Tool
from langchain.agents import create_react_agent
from langchain import hub
from langchain.agents import AgentExecutor

db = retriever()

#print(query("What is the recommendation for amitryptilline for someone with a *17/*17 diplotype?"))
llm=OpenAI(openai_api_key=OPENAI_API_KEY,
           temperature=0.0)

conversational_memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=4, #Number of messages stored in memory
    return_messages=True #Must return the messages in the response.
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=db.as_retriever(),
)

#print(qa.invoke("What is the recommendation for amitryptilline for someone with a *17/*17 diplotype?"))

#Defining the list of tool objects to be used by LangChain.
tools = [
    Tool(
        name='Medical KB',
        func=qa.invoke,
        description=(
            """use this tool when answering how to dose a medication given a phenotype and or a diplotype"""
        )
    )
]

prompt = hub.pull("hwchase17/react-chat")
agent = create_react_agent(
    tools=tools,
    llm=llm,
    prompt=prompt,
)


agent_executor = AgentExecutor(agent=agent,
                               tools=tools,
                               verbose=True,
                               memory=conversational_memory,
                               max_iterations=30,
                               max_execution_time=600,
                               handle_parsing_errors=True
                               )

#response = agent_executor.invoke({"input": "I have a patient that is an intermediate metabolizer for citalopram, what is the recommendation?"})


if __name__ == "__main__":
    while True:
        client_prompt = {"input": input("You: ")}
        if client_prompt["input"].lower() in ["quit", "exit", "bye"]:
            break

        elif client_prompt["input"].lower() in ["clear", "reset"]:
            agent_executor.memory.clear()
            print("Memory cleared.")
            continue

        answer = agent_executor.invoke(client_prompt)
        print(answer["output"])

