import spade
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
import random
class Resolvedor_1grau(Agent):
    class resolver(CyclicBehaviour):
        async def run(self):
            msg = Message(to= "ezioanon@jix.im")
            msg.set_metadata = ("performative","inform")
            x_zero = x[0] - ((x[1] - x[0])*y[0])/(y[1]- y[0])


    
    
    
async def main():
    resolvedor1 = Resolvedor_1grau( "ezio_resolvedor1@jix.im","senhamuitoforte")
    await resolvedor1.start()

if __name__ == "__main__":
    spade.run(main())
#só pra dar push