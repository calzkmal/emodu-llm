from langchain_community.llms import Ollama

llm = Ollama(model="llama3.2")
print(llm.invoke("Aku merasa sedih. Motivasi aku", stop=['<|eot_id|>']))