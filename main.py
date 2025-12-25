from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Python Transaction API")

# Transaction model
class Transaction(BaseModel):
    id: int
    amount: float
    description: str

# In-memory storage
transactions: List[Transaction] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to Python Transaction API!"}

@app.post("/transactions/")
def create_transaction(transaction: Transaction):
    transactions.append(transaction)
    return transaction

@app.get("/transactions/")
def get_transactions():
    return transactions
