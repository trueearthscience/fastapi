from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def example():
    return {
        "FastAPI":"The fastest modern web framework!"
    }
    
@app.get("/greetings")
def greetings():
    return {"Hello"}
    
if __name__ == "__main__":
    uvicorn.run("main:app")