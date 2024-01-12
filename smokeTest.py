from llama_index.llms import Ollama

llm = Ollama(model="mistral")
response = llm.complete("How many GPU does a macbook pro m1 has?")
print(response)