from fastapi import FastAPI

app = FastAPI(
    title="Sponsors API",
    description="Here is the complete description of all the API'S",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {"message": "Hellow World"}




# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)