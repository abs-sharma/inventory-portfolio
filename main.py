import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()
class Stock(BaseModel):
    name: str
    price: float
    quantity: int

c = sqlite3.connect('market.db')
ini = c.cursor()
ini.execute('''CREATE TABLE IF NOT EXISTS stock_prices (
                        name TEXT,
                        price INTEGER,
                        quantity INTEGER
                        )''')


@app.post("/stocks/")
async def create_item(item: Stock):
    ini.execute('''
        INSERT INTO stock_prices (name, price, quantity)
        VALUES (?, ?, ?)
    ''', (item.name, item.price, item.quantity))
    c.commit()
    return {"message": "Item created successfully"}

@app.get("/stocks/")
async def read_all():
    ini.execute('SELECT * FROM stock_prices')
    items = ini.fetchall()
    return {"items": items}

@app.get("/stocks/{name}")
async def read_item(name: str):
    ini.execute('SELECT * FROM stock_prices WHERE name=?', (name,))
    item = ini.fetchone()
    if item:
        return {"name": item[1], "price": item[2], "quantity": item[3]}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.put("/stocks/{name}")
async def update_item(item: Stock):
    ini.execute('''
        UPDATE stock_prices
        SET price=?, quantity=?
        WHERE name=?
    ''', (item.price, item.quantity, item.name))
    c.commit()
    return {"message": "Item updated successfully"}

@app.delete("/stocks/{name}")
async def delete_item(item_name: str):
    ini.execute('DELETE FROM stock_prices WHERE name=?', (item_name,))
    c.commit()
    return {"message": "Item deleted successfully"}

