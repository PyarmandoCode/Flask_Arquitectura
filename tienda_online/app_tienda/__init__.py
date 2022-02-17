from flask import  Flask
from app_tienda import config
from flask_sqlalchemy import SQLAlchemy

#todo creando la aplicacion
app=Flask(__name__)

#todo Conexion con la BD

app.config.from_object(config.Config)
db=SQLAlchemy(app)

from app_tienda import routers,models