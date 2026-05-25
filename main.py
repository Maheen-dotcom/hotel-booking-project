from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from database import cursor, conn
import models

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/book")
def book(
    full_name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    check_in: str = Form(...),
    check_out: str = Form(...),
    room_type: str = Form(...),
    guests: int = Form(...),
    requests: str = Form(...)
):

    cursor.execute("""
    INSERT INTO bookings
    (full_name, email, phone, check_in, check_out, room_type, guests, requests)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        full_name,
        email,
        phone,
        check_in,
        check_out,
        room_type,
        guests,
        requests
    ))

    conn.commit()

    return {
        "message": "Booking Saved Successfully"
    }