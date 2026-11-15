from  dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm = ChatAnthropic(model="claude-haiku-5-5")

while True:
    query = input("User: ")

    if query.lower() in ["bye", "exit"]:
        print("Goodbye!")
        break

    res = llm.invoke(query)

    print("AI:", res.content)