from dotenv import load_dotenv
load_dotenv()

from langchain_anthropic import ChatAnthropic


llm = ChatAnthropic(model="claude-haiku-5-5")

history =[]

while True:
    prompts = input("User : ")
    if prompts.lower() in ["bye", "exit"]:
        print("Thank you")
        break

    history_data = history.append({"role":"user", "content":prompts})
    res = llm.invoke(history)
    history.append({"role":"ai", "content":res.content})

    print("AI : ", res.content)

 










