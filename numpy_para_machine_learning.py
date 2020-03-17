"""numpy-para-machine-learning.ipynb

import numpy as np

"""## Preencher matrizes com números expecíficos

Criando uma matriz com o numpy.array()
"""

myArray = np.array([1,2,3,4,5,6,7,8,9,0])
print(myArray)

"""Criando uma matriz bidimensional 3 x 2"""

matriz_bi = np.array([[6 , 5], [11 , 4], [5 , 9] ])
print(matriz_bi)

"""Prencher um matriz com uma sequência de numeros, numpy.arange()"""

metodArange = np.arange(5, 12)
print(metodArange)

"""## Preencher matrizes com sequência de números
Numpy possui varias funções para preencher matrizes com números aleatórios em determinados intervalos.
***numpy.random.randint*** gera números inteiros aleatórios entre um valor baixo e alto.
"""

aleatorio_randint = np.random.randint(low = 10, high=100, size=(10))
print(aleatorio_randint)

"""Criar valores aleatórios de ponto flutuante entre 0,0 e 1,0 use **numpy.random.random()**"""

float_random = np.random.random([10])
print(float_random)

"""O Numpy possui um truque chamado broadcasting que expande virtualmente o operando menor para dimensões compatíveis com a álgebra linear."""

random_floats_2_e_3 = float_random + 2.0
print (random_floats_2_e_3)

"""## Tarefa 1: Criar um conjunto de dados linear
Seu objetivo é criar um conjunto de dados simples que consiste em um único recurso e um rótulo da seguinte maneira:
1. Atribua uma sequência de números inteiros de 6 a 20 (inclusive) a uma matriz NumPy denominada `feature`.
2.Atribua 15 valores a uma matriz NumPy denominada de labelmodo que:

```
   label = (3)(feature) + 4
```
Por exemplo, o primeiro valor para `label`deve ser:

```
  label = (3)(6) + 4 = 22
 ```
"""
recurso = np.arange(6, 21)
print(feature)
rotulo = (feature * 3) + 4
print(label)

"""## Tarefa 2: adicionar algum ruído ao conjunto de dados

Para tornar seu conjunto de dados um pouco mais realista, insira um pouco de ruído aleatório em cada elemento da labelmatriz que você já criou. Para ser mais preciso, modifique cada valor atribuído rótulo, adicionando um valor de ponto flutuante aleatório diferente entre -2 e +2.

ão confie na transmissão. Em vez disso, crie um ruido na matriz com a mesma dimensão que rótulo.
"""

ruido = (np.random.random([15]) * 4) -2
print(noise)
rotulo += ruido
print(rotulo)
