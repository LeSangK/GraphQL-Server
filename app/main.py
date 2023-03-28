# app/main.py

from fastapi import FastAPI
from strawberry.asgi import GraphQL
from app.graphql.schema import schema
from app.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
graphql_app = GraphQL(schema)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*",
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_route("/", graphql_app)

# @app.exception_handler(Exception)
# async def handle_exceptions(request, exc):
#     return {"error": str(exc)}


# @app.middleware("http")
# async def graphql_middleware(request, call_next):
#     response = await graphql_app(request.scope, request.receive, request.send)
#     await response(receive=request.receive, send=request.send)
#     return response


# create database tables if not exist
Base.metadata.create_all(bind=engine)
