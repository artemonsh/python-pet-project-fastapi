from contextlib import asynccontextmanager

from fastapi import FastAPI, Body, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

from db import Base, engine, get_user_requests, add_request_data
from gemini_client import get_answer_from_gemini


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    print("Все таблицы созданы")
    yield

app = FastAPI(
    title="Мой стартап",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
        "http://localhost:5501",
        "http://127.0.0.1:5501",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/requests")
def get_my_requests(request: Request):
    user_ip_address = request.client.host
    print(f"{user_ip_address=}")
    user_requests = get_user_requests(ip_address=user_ip_address)
    return jsonable_encoder(user_requests)


@app.post("/requests")
def send_prompt(
        request: Request,
        prompt: str = Body(embed=True),
):
    user_ip_address = request.client.host
    answer = get_answer_from_gemini(prompt)
    add_request_data(
        ip_address=user_ip_address,
        prompt=prompt,
        response=answer,
    )
    return {"answer": answer}
