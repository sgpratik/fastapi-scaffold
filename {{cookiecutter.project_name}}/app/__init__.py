from fastapi import FastAPI

from app.api import router

docs_description = """ ## Description.
## Who are these API documentation for ?
For **developers** and **technical users**.
This documentation will help **frontend developers**
to learn the workings APIs, and to understand
how the requests and responses are handled."""



def create_app():
    fastapi_app = FastAPI(
        title="{{cookiecutter.tool_name}} Tool Backend",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    fastapi_app.include_router(router)

    return fastapi_app
