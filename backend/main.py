from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.tickets import router as tickets_router
import uvicorn
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title="DecentraPass API",
    description="NFT Ticketing System API",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins in development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(tickets_router, prefix="/api/v1", tags=["tickets"])

@app.get("/", tags=["root"])
async def read_root():
    return {
        "message": "Welcome to DecentraPass NFT Ticketing System API",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True  # Enable auto-reload in development
    )