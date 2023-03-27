import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import sc2
from sc2 import Race, Difficulty
from sc2 import client
from sc2.constants import *
from sc2.player import Bot, Computer
from sc2.position import Point2, Point3
from sc2.unit import Unit
from sc2.units import Units
from Managers import *
from MapKnowledge.Save_Map import save_map


class S2(sc2.BotAI):
    Controller = controller()
    Client1 = client1(Controller)
    Client2 = client2(Controller)
    savemap = save_map()
    Debug :debug = None
    def __init__(self):
        pass
    
    async def on_start(self):
        self.Controller.assign_client(self.Client1)
        self.Controller.assign_client(self.Client2)
        self.Debug = debug(Controller,self.client)
        self.Controller.assign_client(self.Debug)
        self.savemap.save_map(self.game_info.map_name)

    async def on_step(self,iteration):
        await self.Controller.on_step()
        #stepTime = "{:.2f}".format(self.step_time[3])
        await self.Debug.display_line("Step time : " + "{:.2f}".format(self.step_time[3]))
        



def main():
    sc2.run_game(
        sc2.maps.get("JagannathaAIE"),
        [Bot(Race.Terran, S2()), Computer(Race.Zerg, Difficulty.Medium)],
        realtime=False,
    )


if __name__ == "__main__":
    main()