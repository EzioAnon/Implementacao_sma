from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.behaviour import OneShotBehaviour
from spade.message import Message
import random
import asyncio

class Gerador(Agent):
    class GrauFuncao(OneShotBehaviour):
        async def run(self):
            # grau = random.randint(1, 3) 
            grau =3
            print(f"Grau da função gerado pelo Gerador: {grau}")

            x = random.randint(-1000, 1000)
            print(f"X da Função: {x}")

            msg = await self.receive(timeout=10)
            if msg:
                print(f"Mensagem recebida pelo Gerador: {msg.body}")
                response = Message(to=str(msg.sender), body=str(int(grau)), thread=msg.thread)
                response.set_metadata("performative", "inform")
                await self.send(response)
                print("Grau enviado")
            
            if grau == 1:
                a = random.randint(-100, 100)
                b = -1 * (a * x)
                print(f"Função 1gi grau: {a}x^2 + ({b}x) ")
                self.agent.add_behaviour(self.agent.Grau1(a, b, x))
            elif grau == 2:
                a = random.randint(-100, 100)
                b = random.randint(-100, 100)
                c = -1 * (a * x**2 + b * x)
                print(f"Função 2 grau: {a}x^2 {b}x {c}")
                self.agent.add_behaviour(self.agent.Grau2(a, b, c, x))
            elif grau == 3:
                a = random.randint(-100, 100)
                b = random.randint(-100, 100)
                c = random.randint(-100, 100)
                d = -1 * (a * x**3 + b * x**2 + c * x)
                print(f"Função 3 grau: {a}x^3 + ({b}x^2) +  ({c}x) + ({d})")
                self.agent.add_behaviour(self.agent.Grau3(a, b, c, d, x))    

    class Grau1(CyclicBehaviour):
        def __init__(self, a, b, x):
            super().__init__()
            self.a = a
            self.b = b
            self.x = x

        async def run(self):
            msg = await self.receive(timeout=20)
            if msg:
             x_resolvedor = float(msg.body)  
             resultado = self.a * x_resolvedor + self.b  
             res = Message(to=str(msg.sender), body=str(int(resultado)), thread=msg.thread)
             await self.send(res)

             

    class Grau2(CyclicBehaviour):
        def __init__(self, a, b, c, x):
            super().__init__()
            self.a = a
            self.b = b
            self.c = c
            self.x = x
            

        async def run(self):
            msg = await self.receive(timeout=20)
            if msg:
             x_resolvedor = float(msg.body)
             resultado = self.a * x_resolvedor**2 + self.b * x_resolvedor + self.c  
             res = Message(to=str(msg.sender), body=str(int(resultado)), thread=msg.thread)
             await self.send(res)

    class Grau3(CyclicBehaviour):
        def __init__(self, a, b, c, d, x):
            super().__init__()
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.x = x

        async def run(self):
            msg = await self.receive(timeout=20)
            if msg: 
             x_resolvedor = float(msg.body)  
             resultado = self.a * x_resolvedor**3 + self.b * x_resolvedor**2 + self.c * x_resolvedor + self.d
             res = Message(to=str(msg.sender), body=str(int(resultado)), thread=msg.thread)
             await self.send(res)
  
            

    async def setup(self):
        print("Gerador iniciando...")
        self.add_behaviour(self.GrauFuncao())

async def main():
    generator_agent = Gerador("ezioanon@jix.im", "senhaforte")
    await generator_agent.start()
    print("Gerador iniciado")

    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
