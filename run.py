import sc2, sys
from __init__ import run_ladder_game
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer

# Load bot
from S2 import S2

bot = Bot(Race.Terran, S2())

# Start game
if __name__ == "__main__":
    if "--LadderServer" in sys.argv:
        # Ladder game started by LadderManager
        print("Starting ladder game...")
        result, opponentid = run_ladder_game(bot)
        print(result, " against opponent ", opponentid)
    else:
        # Local game
        print("Starting local game...")
        sc2.run_game(sc2.maps.get("2000AtmospheresAIE"), [bot, Computer(Race.Protoss, Difficulty.Easy)], realtime=True)
