import spade
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
import random
class Resolvedor_2grau(Agent):
    class resolver(CyclicBehaviour):
        x = random.randint(-1000,1000)#testar um valor qualquer, com os resultados obtidos tentar direcionar
        


    
    
    
async def main():
    resolvedor1 = Resolvedor_2grau( "ezioanon_resolvedor2@jix.im","senhamuitoforte")
    await resolvedor1.start()

if __name__ == "__main__":
    spade.run(main())