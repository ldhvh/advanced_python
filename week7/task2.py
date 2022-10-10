from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello!"}


@app.get("/about")
def about():
    return {"message": "О сайте"}
