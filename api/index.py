from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from fastapi.middleware.cors import CORSMiddleware
import resend
import os

app = FastAPI()

resend.api_key = os.environ.get("RESEND_API_KEY")
MY_MAIL = os.environ.get("MY_MAIL")

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

@app.post("/api/send-mail")
async def send_mail(form_data: ContactForm):
    try:
        params = {
            "from": "EckeEcke.github.io <onboarding@resend.dev>",
            "to": [MY_MAIL],
            "subject": f"Neue Nachricht von {form_data.name}",
            "html": f"""
                <h3>Neue Kontaktanfrage</h3>
                <p><strong>Name:</strong> {form_data.name}</p>
                <p><strong>Email:</strong> {form_data.email}</p>
                <p><strong>Nachricht:</strong></p>
                <p>{form_data.message}</p>
            """
        }
        
        email = resend.Emails.send(params)
        return {"status": "success", "id": email["id"]}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))