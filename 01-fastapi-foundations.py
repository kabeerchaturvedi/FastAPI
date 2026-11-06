from fastapi import FastAPI
from fastapi import Request
import uvicorn

app = FastAPI(title="Swiggy Ordering API",
     description=("Internal API for managing orders" 
                "Handle creation, tracking of delivery orders"), 
     version="1.0.0",
     docs_url= "/docs",
     redoc_url = "/redoc",
     openapi_url = "/openapi.json"
     )


@app.get("/")
def read_root():
    """Root endpoint - Health check"""
    return {"message":"Welcome to Swiggy Order Service", 
            "status":"healthy"}
    
@app.get("/about")
def about():
    """Returns API Metadata"""
    return {
        "service":"order-service",
        "team":"backend platform",
        "region":"ap-south-1",
        "version":"1.2.2"
    }    