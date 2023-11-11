from typing import Union

from fastapi import FastAPI
from model import get_pipe
from PIL import Image 
import io 
from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse


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




@app.get("/get_image")
def get_image(q: Union[str, None] = None):
    # Replace this with your logic to generate or fetch the image
    image = pipe(prompt=q, negative_prompt=neg_prompt).images[0]

    # Convert the image to bytes
    image_bytes = io.BytesIO()
    image.save(image_bytes, format="JPEG")

    # Set the content type to image/jpeg
    content_type = "image/jpeg"

    # Return a StreamingResponse with the image bytes and content type
    return StreamingResponse(io.BytesIO(image_bytes.getvalue()), media_type=content_type)