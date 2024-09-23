import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

LLM = ChatOpenAI(model = "gpt-4o-2024-05-13", temperature = 0.6)