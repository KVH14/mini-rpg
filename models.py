import random
from models import GameState

def reset_game():
    return GameState(player_hp=100, enemy_hp=100, turn=1, message="Nueva partida iniciada automáticamente.")

def enemy_turn(game):
    dmg = random.randint(5, 15)
    game.player_hp -= dmg
    game.message += f" | El enemigo atacó y causó {dmg} de daño."
    return game

def process_action(game: GameState, action: str):

    # Si la partida terminó, reiniciar automáticamente
    if game.player_hp <= 0 or game.enemy_hp <= 0:
        return reset_game()

    game.message = ""

    # ===== Acciones del jugador =====
    if action == "attack":
        dmg = random.randint(10, 20)
        game.enemy_hp -= dmg
        game.message = f"Atacaste e hiciste {dmg} de daño."

    elif action == "defend":
        block = random.randint(5, 15)
        game.message = f"Te defendiste y bloqueaste {block} de daño."

    elif action == "heal":
        heal = random.randint(10, 20)
        game.player_hp += heal
        game.player_hp = min(game.player_hp, 100)
        game.message = f"Te curaste {heal} puntos."

    else:
        game.message = "Acción inválida."
        return game

    # ===== Turno enemigo =====
    game = enemy_turn(game)

    # ===== Si alguien muere, reiniciar automáticamente =====
    if game.player_hp <= 0 or game.enemy_hp <= 0:
        return reset_game()

    game.turn += 1
    return game
