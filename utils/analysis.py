from config import OPEN_AI_API_KEY

from langchain.llms import OpenAI

llm = OpenAI(openai_api_key=OPEN_AI_API_KEY)