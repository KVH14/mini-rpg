from fastapi import FastAPI
from models import GameState, ActionRequest
from logic import process_action, reset_game

app = FastAPI()

game = GameState()

@app.post("/start")
def start_game():
    global game
    game = reset_game()
    return {"message": "Juego iniciado", "estado": game}

@app.post("/action")
def do_action(action: ActionRequest):
    global game
    game = process_action(game, action.action)
    return {"estado": game}

@app.get("/status")
def get_status():
    return {"estado": game}
