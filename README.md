# README - Projeto de Gerador e Resolvedor de Funções Polinomiais

Este projeto foi desenvolvido como parte da disciplina de Sistemas Inteligentes. Ele implementa dois agentes: Gerador e Resolvedor, que trabalham juntos para criar e resolver funções polinomiais de diferentes graus.

## Agentes e Funcionalidades

### Gerador

O agente Gerador é responsável por criar funções polinomiais de 1º, 2º e 3º graus. Cada função gerada é então passada para o agente Resolvedor, que tenta encontrar a raiz da função.

- **1º Grau (Linear)**: Utiliza interpolação linear para criar a função.
  
- **2º Grau**: Monta um sistema de equações com base na função quadrática para encontrar os coeficientes a, b e c. O método de resolução envolve aplicar a fórmula de Bhaskara para determinar as raízes.
  
- **3º Grau**: Aplica um método Método de Cardano-Tartaglia para criar e resolver a função cúbica.

  **Nota:** Pode haver problemas com arredondamento ao calcular raízes de funções de 3º grau.

### Resolvedor

O agente Resolvedor recebe as funções geradas pelo Gerador e tenta encontrar o valor de x que zera a função (encontra a raiz). Para isso, ele utiliza diferentes abordagens de acordo com o grau da função:

- Chute inicial de valores de x para obter os valores de y.
- Aplicação de métodos específicos para cada grau de função (interpolação linear, sistema de equações, etc.).

## Dependências

Para utilizar este projeto, certifique-se de ter as seguintes bibliotecas instaladas:

- **spade**: Biblioteca para comunicação entre agentes em sistemas multiagente.
- **numpy**: Biblioteca para computação numérica.
- **random**: Biblioteca padrão do Python para geração de números aleatórios.
- **asuncio**: (Nota: É necessário verificar esta biblioteca, pois não encontrei referências diretas; talvez haja um erro de digitação ou uma biblioteca específica que precise ser identificada corretamente.)

Você pode instalar as bibliotecas usando o pip:

```bash
pip install spade numpy
