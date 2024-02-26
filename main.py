from fastapi import FastAPI

app = FastAPI()
a = 0
@app.get("/")
async def read_root():
    global a  # Khai báo rằng `a` là một biến global
    a += 1
    return {"Hello": f"World {a}"}
