import os

from dotenv import load_dotenv
from fastapi import FastAPI
from langchain.chat_models import ChatOpenAI
from langserve import add_routes

from helper_services.helper_chain import HelperChain

app = FastAPI(
    title="LangChain Helper APIs",
    version="1.0",
    description="Helper APIs to augment language models",
)
load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
helper_chain = HelperChain(llm=llm)

add_routes(
    app,
    helper_chain.get_chain("citation"),
    path="/citation_chain",
)

add_routes(
    app,
    helper_chain.get_chain("token_count"),
    path="/token_count",
)

add_routes(
    app,
    helper_chain.get_chain("presidio_pii_de_identify"),
    path="/presidio_pii_de_identify",
)

add_routes(
    app,
    helper_chain.get_chain("prompt_injection_chain"),
    path="/check_prompt_injection",
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
