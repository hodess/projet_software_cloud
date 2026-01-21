from fastapi import FastAPI
import os

app = FastAPI()

# Route GET qui renvoie hello
@app.get("/")
async def root():
    return {"message": "hello"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 3000))
    uvicorn.run(app, host="0.0.0.0", port=port)

