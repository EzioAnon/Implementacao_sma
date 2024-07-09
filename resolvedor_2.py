from spade.agent import Agent
from spade.behaviour import CyclicBehaviour,OneShotBehaviour
from spade.message import Message
import random
import asyncio
import numpy as np

class Resolvedor(Agent):
    class Grau(OneShotBehaviour):
        async def run(self):
            
            msg = Message(to="ezioanon@jix.im", body="Qual o grau da Função?", thread="unique-thread-id")
            msg.set_metadata("performative", "request")
            await self.send(msg)
            print("Mensagem enviada para o Gerador")

            
            response = await self.receive(timeout=20)
            if response:
                grau = int(response.body)
                print(f"Grau recebido do Gerador: {grau}")

                
                if grau == 1:
                    self.agent.add_behaviour(self.agent.Grau1())
                elif grau == 2:
                    self.agent.add_behaviour(self.agent.Grau2())
                elif grau == 3:
                    self.agent.add_behaviour(self.agent.Grau3())
            
    class Grau1(CyclicBehaviour):
        async def on_start(self):
            self.i = 0
            self.y = []
            self.x = []

        async def run(self):
            if self.i > 1:
                self.x.append(self.x[0] - ((self.x[1] - self.x[0]) * self.y[0]) / (self.y[1] - self.y[0]))  # Lógica para primeiro grau
                x_zero = self.x[self.i]
            else:
                self.x.append(random.randint(-1000, 1000))
                x_zero = self.x[self.i]

            print(f"Enviando valor {x_zero} para função de 1º grau")

            msg = Message(to="ezioanon@jix.im", body=str(float(x_zero)), thread="unique-thread-id")
            await self.send(msg)

            response = await self.receive(timeout=20)
            if response:
                self.y.append(int(response.body))
                print(f"Resultado da função de 1º grau para {self.x[self.i]}: {self.y[self.i]}")
                if self.y[self.i] == 0:
                    print("Resultado zero encontrado!")
                    await self.agent.stop()
                    self.kill()

                self.i += 1
                        

    class Grau2(CyclicBehaviour):
        async def on_start(self):
            self.i = 0
            self.y = []
            self.x = []
            self.a = 0
            self.b = 0
            self.c = 0
            self.raiz_x = 0

        async def run(self):
            if self.i == 3:
                self.a = (self.y[0]- self.y[2] - (((self.y[1]-self.y[2]) * (self.x[0] - self.x[2]))/(self.x[1] - self.x[2]))) / ((self.x[0]**2 - self.x[2]**2) - (((self.x[1]**2 - self.x[2]**2)*(self.x[0] - self.x[2]))/(self.x[1] - self.x[2])))
                self.b = ((self.y[1] - self.y[2])- self.a * (self.x[1]**2 - self.x[2]**2))/(self.x[1] - self.x[2])
                self.c = self.y[2] - self.a * self.x[2]**2 - self.b*self.x[2]
                delta = self.b**2 - 4 * (self.a)*(self.c)
                if self.raiz_x == 0:
                 self.x.append((-self.b + np.sqrt(delta))/(2 * self.a))
                 x_zero = self.x[self.i]
                 self.raiz_x +=1
                 
                else:
                 self.x.append((-self.b - np.sqrt(delta))/(2 * self.a))
                 x_zero = self.x[self.i]
                 
                
                print(f"a:{self.a}, b:{self.b}, c:{self.c}, raiz_1: {x_zero}")
                
                
            else:
                self.x.append(random.randint(-1000, 1000))
                x_zero = self.x[self.i]

            print(f"Enviando valor {x_zero} para função de 2º grau")

            msg = Message(to="ezioanon@jix.im", body=str(float(x_zero)), thread="unique-thread-id")
            await self.send(msg)

            response = await self.receive(timeout=20)
            if response:
                self.y.append(int(response.body))
                print(f"Resultado da função de 2º grau para {self.x[self.i]}: {self.y[self.i]}")
                if self.y[self.i] == 0:
                    print("Resultado zero encontrado!")
                    await self.agent.stop()
                    self.kill()
                if self.i < 5: self.i += 1
                else: 
                    self.i = 0
                    self.x = []
                    self.y = []
                    self.raiz_x = 0

                        
                        

    class Grau3(CyclicBehaviour):
        async def on_start(self):
            self.i = 0
            self.y = []
            self.x = []
            self.a = 0
            self.b = 0
            self.c = 0
            self.d = 0
            self.raiz_x = 0

        async def run(self):
            if self.i==4:
                x = np.array(self.x)
                y = np.array(self.y)
                matriz = np.column_stack([x**3,x**2,x,np.ones_like(x)])
                coeficientes = np.linalg.solve(matriz,y)
                self.a,self.b,self.c,self.d = coeficientes
                q = 2*self.b**3 - 9*self.a*self.b*self.c + 27*self.a**2 * self.d/27*self.a**3
                p = 3*self.a*self.c -self.b/3*self.a
                delta = (q/2)** 2 + (p/3)**3
                raiz = np.cbrt(-q/2 + np.sqrt(delta)) + np.cbrt(-q/2 - np.sqrt(delta))
                
                self.x.append(raiz)
                
                x_zero = self.x[self.i]
                print(f"a:{self.a}, b:{self.b}, c:{self.c},d:{self.d}, raiz_1: {x_zero}")
            else:
                self.x.append(random.randint(-1000, 1000))
                x_zero = self.x[self.i]

            print(f"Enviando valor {x_zero} para função de 3º grau")

            msg = Message(to="ezioanon@jix.im", body=str(float(x_zero)), thread="unique-thread-id")
            await self.send(msg)

            response = await self.receive(timeout=20)
            if response:
                self.y.append(int(response.body))
                print(f"Resultado da função de 3º grau para {self.x[self.i]}: {self.y[self.i]}")
                if self.y[self.i] == 0:
                    print("Resultado zero encontrado!")
                    await self.agent.stop()
                    self.kill()

                self.i += 1

    async def setup(self):
        print("Resolvedor iniciando . . .")
        self.add_behaviour(self.Grau())

async def main():
    resolver_agent = Resolvedor("ezio_resolvedor1@jix.im", "senhamuitoforte")
    await resolver_agent.start()
    print("Resolvedor iniciado")

    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
