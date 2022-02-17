from app_tienda import db

class Usuarios(db.Model):
    cod_usuario=db.Column(db.String(4),primary_key=True)
    username=db.Column(db.String(20))
    email =db.Column(db.String(20))
    password=db.Column(db.String(8))