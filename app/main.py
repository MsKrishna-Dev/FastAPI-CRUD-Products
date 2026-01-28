from fastapi import FastAPI, HTTPException, Query
from service.products import get_all_products

app = FastAPI()

@app.get('/')

def root():
    return {"Message" : "Welcome to FastAPI"}


# @app.get('/products/')
# def get_products():
#    return get_all_products()

@app.get('/products')
def list_products(name:str | None = Query(
    default=None,
    min_length=1,
    max_length=50,
    description="Search by product name"
    ),
    sort_by_price:bool = Query(
        default=False,
        description="Sort products by price"
    ),
    order : str = Query(
        default="asc",
        description="Sort order when sort_by_price = true (asc, desc)"
    ),
    limit : int = Query(
    default=5,
    ge = 1,
    le=100,
    description="Number of items return"
    ),
    offset : int = Query(
    default=0,
    ge =0,
    description="Pagination Offset"
    )
):
    products = get_all_products()

    if name: 
        needle = name.strip().lower()
        products = [p for p in products if needle in p.get("name", "").lower()]

    if not products:
        raise HTTPException(status_code=404, detail=f"No product found matching name={name}"
        )

    if sort_by_price:
        reverse = order == "desc"
        products = sorted(products, key=lambda p: p.get("price", 0), reverse=reverse)

    products = products[offset:offset+limit]

    return {
        "Total" : len(products),
        "Limit" : limit,
        "items" : products
    }

