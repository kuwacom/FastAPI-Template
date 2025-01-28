from fastapi import APIRouter, HTTPException
from models.hello import Hello

helloRouter = APIRouter()

@helloRouter.get("/", response_model=Hello)
async def hello():
    try:
        helloDict = Hello(
            name="hello",
            hellos=list("hello")
        )
        return helloDict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
