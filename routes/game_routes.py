from flask import blueprints, request
from controllers.game_controllers import get_all_games, get_game_by_id
from controllers.game_controllers import create_game, update_game
from controllers.game_controllers import get_games_by_title

game_routes = blueprints.Blueprint("game_routes", __name__)


@game_routes.route("/games", methods=["GET"])
def fetch_all_games():
    return get_all_games()


@game_routes.route("/games/<int:game_id>", methods=["GET"])
def fetch_game_by_id(game_id):
    return get_game_by_id(game_id)

def fetch_games_by_title(title):
    return get_games_by_title(title)

@game_routes.route("/games/create", methods=["POST"])
def create_new_game():
    data = request.json
    return create_game(data)

@game_routes.route("/games/<int:game_id>", methods=["PUT"])
def update_existing_game(game_id):
    data = request.json
    return update_game(game_id, data)