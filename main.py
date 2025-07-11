# main.py
from fasthtml.common import *
from fastapi.templating import Jinja2Templates  # NEW
from starlette.requests import Request           # NEW

app, rt = fast_app()

# NEW: Jinja2 setup
templates = Jinja2Templates(directory="templates")

@rt("/")
def get(request: Request):                       # NEW: accept request
    # NEW: use Jinja2 instead of FastHTML helpers
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "FastHTML + Jinja2 on Render"}
    )

serve()