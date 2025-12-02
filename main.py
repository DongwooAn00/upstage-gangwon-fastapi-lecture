from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/hello")
def hello():
    return {"message": "Hello FastAPI!"}


@app.get("/error500")
def hello():
    raise Exception("Something went wrong!")



# Frontend routes
@app.get("/")
async def read_index():
    return FileResponse('template/index.html')
