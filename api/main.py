
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

app = FastAPI()


app.mount("/static", StaticFiles(directory="_build/html"), name="static")


class Message(BaseModel):
    message: str


@app.post("/chat")
def chat(message: Message):
    return JSONResponse({"message": "from server mirror: " + message.message})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
