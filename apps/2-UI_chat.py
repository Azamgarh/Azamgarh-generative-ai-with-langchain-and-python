from  dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
import streamlit as st

load_dotenv()
llm = ChatAnthropic(model="claude-haiku-5-5")

st.title("🤖 Ask Question AI Bot")
st.markdown("My Question with LangChain with Claude")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)


query = st.chat_input("Ask anything ?")

if query:
    st.session_state.messages.append({"role":"user", "content":query})
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.chat_message("ai").markdown(res.content)
    st.session_state.messages.append({"role":"ai", "content":res.content})


