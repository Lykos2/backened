from typing import Union

from fastapi import FastAPI
from model import get_pipe


app = FastAPI()

neg_prompt = "ugly, blurry, poor quality" # Negative prompt here.
pipe=get_pipe()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    image = pipe(prompt=q, negative_prompt=neg_prompt).images[0]
    return {"item_id": item_id, "image": image}
