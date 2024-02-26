from fastapi import FastAPI

app = FastAPI()
a = 0
@app.get("/")
async def read_root():
    a += 1
    return {"Hello": "World" + a}
