import spade
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.template import Template
from spade.message import Message
import random

class Gerador(Agent):
    
    grau = random.randint(1, 3)
    x = random.randint(-1000,1000)


    if grau == 1:
        a = random.randint(-100,100)
        b = -1*(a*x)
    elif grau == 2:
        a = random.randint(-100,100)
        b = random.randint(-100,100)
        c = -1*(a*x**2 + b*x)
    else:
        a = random.randint(-100,100)
        b = random.randint(-100,100)
        c = random.randint(-100,100)
        d = -1*(a*x**3 + b*x**2 + c*x)
    
    class funcao_grau(CyclicBehaviour):
     async def run(self):
        res = await self.receive(timeout=5)
        if res:
            x = float(res.body)
            if Gerador.grau == 1:
                y = Gerador.a * x + Gerador.b
            elif Gerador.grau == 2:
                y = Gerador.a * x**2 + Gerador.b * x + Gerador.c
            else:
                y = Gerador.a * x**3 + Gerador.b * x**2 + Gerador.c * x + Gerador.d

            print(f"Enviou para {res.sender} f({res.body}) = {y} => {int(y)}")
            msg = Message(to=str(res.sender))
            msg.set_metadata("performative", "inform")
            msg.body = str(int(y))
            await self.send(msg)
    
    class tipo_funcao(CyclicBehaviour):
        async def run(self):
            msg = await self.receive(timeout=5)
            if msg:
                resposta = f"{Gerador.grau}grau"
                print(f"Respondeu para {msg.sender} com {resposta}")
                resposta_msg = Message(to=str(msg.sender))
                resposta_msg.set_metadata("performative", "inform")
                resposta_msg.body = resposta
                await self.send(resposta_msg)
    
    async def setup(self):
        t = Template()
        t.set_metadata("performative", "subscribe")

        tf = self.funcao_grau()
        print(f"Funcao de {Gerador.grau}o grau: ", Gerador.x)
        msg = Message()
        msg.set_metadata("performativa","inform")
        if Gerador.grau == 1:
            print(f"Funcao: {Gerador.a}x + ({Gerador.b})")
            msg.to = "ezio_resolvedor1@jix.im","senhamuitoforte"
            msg.body = "Função de 1oGrau"
        elif Gerador.grau == 2:
            print(f"Funcao: {Gerador.a}x^2 + ({Gerador.b}x) + ({Gerador.c})")
            msg.to = "ezioanon_resolvedor2@jix.im","senhamuitoforte"
            msg.body = "Função de 2oGrau"
        else:
            print(f"Funcao: {Gerador.a}x^3 + ({Gerador.b}x^2) + ({Gerador.c}x) + ({Gerador.d})")
            msg.to = "ezio_resolvedor3@jix.im","senhamuitoforte"
            msg.body = "Função de 3oGrau"

        self.add_behaviour(tf, t)

        ft = self.tipo_funcao()
        template = Template()
        template.set_metadata("performative", "request")
        self.add_behaviour(ft, template)
    
    
    
    
async def main():
    gerador = Gerador("ezioanon@jix.im", "senhaforte")
    await gerador.start()

if __name__ == "__main__":
    spade.run(main())
