from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # TODO Später auf GitHub Pages Domain einschränken
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContactForm(BaseModel):
    name: str
    email: EmailStr
    message: str

@app.get("/")
def read_root():
    return {"status": "Backend is running"}

@app.post("/send-mail")
async def receive_contact(form_data: ContactForm):
    print("--- New message received ---")
    print(f"Name: {form_data.name}")
    print(f"Email: {form_data.email}")
    print(f"Message: {form_data.message}")
    
    return {"status": "success", "received": form_data.name}