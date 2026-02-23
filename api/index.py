from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContactForm(BaseModel):
    name: str
    email: EmailStr
    message: str

@app.get("/api/health")
def health_check():
    return {"status": "Backend is running on Vercel"}

@app.post("/api/send-mail")
async def receive_contact(form_data: ContactForm):
    print(f"Received: {form_data.name}")
    return {"status": "success", "received": form_data.name}