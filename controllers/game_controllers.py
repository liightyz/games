from models.game_models import GameModel
from db import db
import json
from flask import make_response, request

def get_all_games():
    games = GameModel.query.all()

    response = make_response(
        json.dumps({
            "message": "Games retrieved successfully",
            "data": [game.json() for game in games]
        }, ensure_ascii=False, sort_keys=True),
    )
    response.headers['Content-Type'] = 'application/json'
    return response

def get_game_by_id(game_id):
    game = GameModel.query.get(game_id)
    if game:
        response = make_response(
            json.dumps({
                "message": "Game retrieved successfully",
                "data": game.json()
            }, ensure_ascii=False, sort_keys=True),
        )
    else:
        response = make_response(
            json.dumps({
                "message": "Game not found"
            }, ensure_ascii=False, sort_keys=True),
            404
        )
    response.headers['Content-Type'] = 'application/json'
    return response

def get_games_by_title(title):
    games = GameModel.query.filter(GameModel.titulo.ilike(f'%{title}%')).all()
    if games:
        response = make_response(
            json.dumps({
                "message": "Games retrieved successfully",
                "data": [game.json() for game in games]
            }, ensure_ascii=False, sort_keys=True),
        )
    else:
        response = make_response(
            json.dumps({
                "message": "No games found with the given title"
            }, ensure_ascii=False, sort_keys=True),
            404
        )
    response.headers['Content-Type'] = 'application/json'
    return response

def create_game(data):
    
    new_game = GameModel(
        titulo=data.get('titulo'),
        genero=data.get('genero'),
        plataforma=data.get('plataforma'),
        desenvolvedor=data.get('desenvolvedor')
    )
    db.session.add(new_game)
    db.session.commit()

    response = make_response(
        json.dumps({
            "message": "Game created successfully",
            "data": new_game.json()
        }, ensure_ascii=False, sort_keys=True),
        201
    )
    response.headers['Content-Type'] = 'application/json'
    return response

def update_game(game_id, data):
    game = GameModel.query.get(game_id)
    if not game:
        response = make_response(
            json.dumps({
                "message": "Game not found"
            }, ensure_ascii=False, sort_keys=True),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    game.titulo = data.get('titulo', game.titulo)
    game.genero = data.get('genero', game.genero)
    game.plataforma = data.get('plataforma', game.plataforma)
    game.desenvolvedor = data.get('desenvolvedor', game.desenvolvedor)

    db.session.commit()

    response = make_response(
        json.dumps({
            "message": "Game updated successfully",
            "data": game.json()
        }, ensure_ascii=False, sort_keys=True),
    )
    response.headers['Content-Type'] = 'application/json'
    return response