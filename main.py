from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import pytz

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def read_root():
    current_time = datetime.now(pytz.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")  # Exact ISO format
    return {
        "email": "your-email@example.com",
        "current_datetime": current_time,
        "github_url": "https://github.com/yourusername/your-repo"
    }