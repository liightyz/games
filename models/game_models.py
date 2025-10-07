from db import db

class GameModel(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(80), nullable=False)
    genero = db.Column(db.String(80), nullable=False)
    desenvolvedor = db.Column(db.String(80), nullable=False)
    plataforma = db.Column(db.String(80), nullable=False)

    def json(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'genero': self.genero,
            'desenvolvedor': self.desenvolvedor,
            'plataforma': self.plataforma
        }