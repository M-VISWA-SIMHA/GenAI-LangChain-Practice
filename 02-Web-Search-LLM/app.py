#Connecting websearch with the LLM
#python -m pip install -U ddgs
#pip install -U ddgs
from langchain_ollama import ChatOllama
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(
    model="smollm:135m",
    temperature=1.3
)

search = DuckDuckGoSearchRun()
parser = StrOutputParser()
query = "Who won the latest chess world championship?"

search_result = search.invoke(query)
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant. "
        "STRICTLY Answer the question by only using the provided web search results."
    ),
    (
        "user",
        """Question: {question}
        Web Search Results: {search_results}

Give a Summarised answer completely relying on the search results."""
    )
])

chain = prompt | model | parser

response = chain.invoke({
    "question": query,
    "search_results": search_result
})

print(response)