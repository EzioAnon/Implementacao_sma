import spade
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.template import Template
from spade.message import Message

class resolvedor_1grau(Agent):
    grau = 0
    #recebe grau pela mensagem

    if(grau == 1):
        print(1)
    
    
    
    elif(grau == 2):
        2
        #chamar agente resolvedor 2
    
    else:
        3
        #chamar agente resolvedor 3

