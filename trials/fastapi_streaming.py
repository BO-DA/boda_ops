from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from x_stream_cv import getCameraStream

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "PNP"}

@app.get("/test")
async def test(userName):
    return {"Hello": f"{userName}"}

@app.get("/video")
def video():
    return StreamingResponse(getCameraStream(),
                             media_type="multipart/x-mixed-replace; boundary=PNPframe")

print("Here")
