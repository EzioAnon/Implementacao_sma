import spade
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
import random

class Resolvedor_1grau(Agent):
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
                        x_zero = x[0] - ((x[1] - x[0]) * y[0]) / (y[1] - y[0])
                        msg = Message(to="ezioanon@jix.im")
                        msg.set_metadata("performative", "inform")
                        msg.body = str(x_zero)
                        await self.send(msg)
                    i += 1

    async def setup(self):
        b = self.resolver()
        self.add_behaviour(b)

async def main():
    resolvedor1 = Resolvedor_1grau("ezio_resolvedor1@jix.im", "senhamuitoforte")
    await resolvedor1.start()

if __name__ == "__main__":
    spade.run(main())
