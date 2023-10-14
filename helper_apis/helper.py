import os

from dotenv import load_dotenv
from fastapi import FastAPI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langserve import add_routes

from prompt_templates.citation_chain import return_citation_template

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)
load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

prompt = return_citation_template()
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
add_routes(
    app,
    prompt | llm,
    path="/citation_chain",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
