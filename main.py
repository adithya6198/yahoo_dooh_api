from fastapi import FastAPI
from ad_log_request import AdlogsGHExtractionRequest
app = FastAPI()

@app.post("/")
async def adlogs_gh_extraction(request_body: AdlogsGHExtractionRequest):
    return request_body

@app.get("/")
async def root():
    return {"message": "Hello World!"}
