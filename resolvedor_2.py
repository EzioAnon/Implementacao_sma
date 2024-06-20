import spade
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
import random
class Resolvedor_2grau(Agent):
   class resolver(CyclicBehaviour):
        async def run(self):
            x = []
            y = []
            i = 0
            
            while True:
                x.append(random.randint(-1000, 1000))
                msg = Message(to="ezioanon@jix.im")
                msg.set_metadata("performative", "inform")

                msg.body = str(x[i])
                await self.send(msg)

                res = await self.receive(timeout=5)
                if res:
                    y.append(int(res.body))
                    if y[i] == 0:
                        await self.agent.stop()

                    if i == 1:
                        x_zero = x[1] - (((x[1] - x[0]) ** 2 * (y[1]- y[2]) - (x[1] - x[2])** 2 * (y[1]- y[0]))/2*((x[1]- x[0])* (y[1]-y[2]) - (x[1] - x[2]* (y[1]- y[0])) ))# Interpolação quadratica
                        msg = Message(to="ezioanon@jix.im")
                        msg.set_metadata("performative", "inform")
                        msg.body = str(x_zero)
                        await self.send(msg)
                    i += 1

   async def setup(self):
        b = self.resolver()
        self.add_behaviour(b)


    
    
    
async def main():
    resolvedor2 = Resolvedor_2grau( "ezioanon_resolvedor2@jix.im","senhamuitoforte")
    await resolvedor2.start()

if __name__ == "__main__":
    spade.run(main())
a