import spade
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
import random
class Resolvedor_3grau(Agent):
    class resolver(CyclicBehaviour):
        x = random.randint(-1000,1000)
        


    
    
    
async def main():
    resolvedor1 = Resolvedor_3grau( "ezio_resolvedor3@jix.im","senhamuitoforte")
    await resolvedor1.start()

if __name__ == "__main__":
    spade.run(main())
