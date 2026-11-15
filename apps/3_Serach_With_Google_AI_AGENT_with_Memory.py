from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver



llm = ChatGroq(model="openai/gpt-oss-20b")
search = GoogleSerperAPIWrapper()
memory = InMemorySaver()
# Same thread ID for the complete conversation
config = {"configurable": {"thread_id": "1"}}


while True:
    query = input("User: ")
    if query.lower() =="bye":
        print("Thank you")
        break
    agent = create_agent(model=llm,
                        tools=[search.run],
                        checkpointer=memory,
                         system_prompt="you are a agent and search with anythings with google" )

    response = agent.invoke({"messages":[{"role":"user", "content":query}]}, config)
    print("AI: ",response["messages"][-1].content)

