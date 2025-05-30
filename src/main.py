from fastapi import FastAPI
from src.routers import category
from src.routers import products

app = FastAPI()
app.include_router(category.router)
app.include_router(products.router)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)