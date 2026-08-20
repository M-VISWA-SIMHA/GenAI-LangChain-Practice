#ollama pull smollm:1.7b
#ollama list
from langchain_ollama import ChatOllama
model = ChatOllama(model="smollm:135m")
#model = ChatOllama(model="qwen2.5:1.5b")
s = []
while True:
    a = input("Human:")
    if a == "0":
        break
    s.append(("human", a))
    response = model.invoke(s)
    s.append(("ai", response.content))
    print("AI:" + response.content)
