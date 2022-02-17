from flask import render_template,request
from app_tienda import app,db
from app_tienda.models import Usuarios

@app.route('/')
def index():
    template_name="index.html"
    usuarios=Usuarios.query.all()
    return render_template(template_name,usuarios=usuarios)