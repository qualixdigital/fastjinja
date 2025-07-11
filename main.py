# main.py  –  FastHTML + Jinja2 only
from fasthtml.common import *
from jinja2 import Environment, FileSystemLoader

# 1) FastHTML app
app, rt = fast_app()

# 2) Jinja2 setup
jinja_env = Environment(loader=FileSystemLoader("templates"))

# 3) helper that wraps Jinja2 rendering
def render(template_name, **ctx):
    return HTMLResponse(jinja_env.get_template(template_name).render(**ctx))

# 4) route returning a Jinja2 template
@rt("/")
def get():
    return render("index.html", title="FastHTML + Jinja2")

# 5) start server
serve()