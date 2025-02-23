from llama_index.llms.google import ChatGoogleGenerativeAI

from llama_index.readers import SimpleWebPageReader

from langchain_core.prompts import PromptTemplate


from llama_index import VectorStoreIndex
import llama_index
import os
from dotenv import load_dotenv
load_dotenv()

def main(url:str)->None:
  document=SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
  index=VectorStoreIndex.from_documents(documents=document)
  query_engine=index.as_query_engine()
  response=query_engine.query("what is ai")
  print(response)

if __name__=='__main__':
  main(url="https://medium.com/@raja.gupta20/generative-ai-for-beginners-part-1-introduction-to-ai-eadb5a71f07d")