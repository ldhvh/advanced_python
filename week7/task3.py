from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse, HTMLResponse


app = FastAPI()


@app.get("/text", response_class = PlainTextResponse)
def root_text():
    return "Hello World!"
@app.get("/html", response_class = HTMLResponse)
def root_html():
    return "<h2>Hello World!</h2>"