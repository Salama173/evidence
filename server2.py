import os
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

# تحميل متغيرات البيئة
load_dotenv()

app = FastAPI(title="Evidence Server")

EVIDENCE_URL = os.getenv("EVIDENCE_URL", "https://server1.example.com/evidence")
AGENCY_NAME  = os.getenv("AGENCY_NAME", "الإدارة العامة لمكافحة الجرائم الإلكترونية")
AGENCY_NAME_EN = os.getenv("AGENCY_NAME_EN", "General Department of Cybercrime Control")
LOGO_URL     = os.getenv("LOGO_URL", "https://i.ibb.co/fdKfbpGx/IMG-1398.jpg")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "EVIDENCE_URL": EVIDENCE_URL,
        "AGENCY_NAME": AGENCY_NAME,
        "AGENCY_NAME_EN": AGENCY_NAME_EN,
        "LOGO_URL": LOGO_URL
    })

@app.get("/open-evidence")
def open_evidence():
    return RedirectResponse(EVIDENCE_URL, status_code=302)
