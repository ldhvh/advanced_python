from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/users/{name}/{age}")
def users(name,age):
    return {"user_name":name,"user_age":age}