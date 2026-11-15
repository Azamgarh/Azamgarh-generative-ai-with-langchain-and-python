from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
import streamlit as st


llm = ChatGroq(model="openai/gpt-oss-20b", streaming=True)
search = GoogleSerperAPIWrapper()
tool = search.run


config = {"configurable":{"thread_id":"1"}}


if "memory" not in st.session_state:
    st.session_state.memory = InMemorySaver()
    st.session_state.history = []

agent = create_agent(
    model=llm,
    tools=[tool],
    checkpointer=st.session_state.memory,
    system_prompt="You are a amazing AI agent and can search on google as well"
)


### Building UI Interface
st.subheader("💬 QuickAnswer Chatbot -  Speed of thought")

for message in st.session_state.history:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask Anything ? ")
if query:
    st.chat_message("user").markdown(query)
    st.session_state.history.append({"role":"user", "content":query})

    response = agent.stream(
        {"messages":[{"role":"user","content":query}]},
        config,
        stream_mode="messages"
    )

    ai_container = st.chat_message("ai")
    with ai_container:
        space = st.empty()
        message = ""
        for chunk in response:
            message = message + chunk[0].content
            space.write(message)
        st.session_state.history.append({"role":"ai", "content":message})