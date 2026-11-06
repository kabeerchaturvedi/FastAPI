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
    
@app.get("/orders")
def list_orders():
    """List recent orders"""
    return {
        "orders":[{"id":1, "item":"Pizza", "status":"delivered"},
                  {"id":2, "item":"Burger", "status":"in-transit"},
                  {"id":3, "item":"Pasta", "status":"preparing"}]
    }   
    
@app.get("/orders/status")
def order_status():
    """Get order status"""
    return {
        "total_today": 2_340_23,
        "top_city":"Bangalore", 
    }   
    
@app.get("/debug/request-info")
async def request_info(request: Request):
    """Inspect the raw request object"""
    return {
        "headers": dict(request.headers),
        "method": request.method,
        "url": str(request.url),
        "path_params": request.path_params,
        "query_params": dict(request.query_params),
    }    
    
@app.get("/orders/active",
          summary="Get active orders",
          description=(
          "Returns all orders that are currently being prepared"
          "or are out for delivery"
          ),
    tags=["orders"],
    response_description="List of active orders", 
    deprecated=False
)
def get_active_orders():
     """This docstring appears in docs"""
     return {
         "active_orders":[
             {"id":1,"item":"Dosa","status":"preparing"},
         ]
     }
     
@app.get("/restaurants", tags=["Restaurants"])
def list_restaurants():
    """List all restaurants"""
    return {
        "restaurants":[
            {"id":1,"name":"Pizza Hut"},
            {"id":2,"name":"Dominos"},
            {"id":3,"name":"Burger King"},
        ]
    }     