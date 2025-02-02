from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS to allow GET requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"]
)

# Load student marks from JSON file
with open("q-vercel-python.json", "r") as file:
    students = {entry["name"]: entry["marks"] for entry in json.load(file)}

@app.get("/api")
def get_marks(name: list[str] = Query([])):
    return {"marks": [students.get(n, None) for n in name]}

# Vercel entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
