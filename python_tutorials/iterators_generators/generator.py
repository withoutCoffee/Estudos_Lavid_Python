#memory_profiler é um módulo de monitoramento de consumo de memmória
from memory_profiler import memory_usage as mu

import random
import time

names = [f'name 0{i}' for i in range(5)]
majors = [f'ID[0{i}]' for i in range(5)]

#
print(f'Memory (Before): {mu()} Mb\n')

def people_list(num_people):
    """[Está função cria um lista de pessoas
    com nomes sorteados e cursos sorteados]
    
    Arguments:
        num_people {[int]} -- [Número de pessoas a serem criadas]
    
    Returns:
        [list] -- [Vetor de pessoas json]
    """    
    result = []
    for i in range(num_people):
        #json com objeto pessoa
        person  = {
            'id':i,
            'name':random.choice(names),#sorteia um nome na lista de nomes
            'major':random.choice(majors)#sorteia um nome na lista de cursos
        }
        result.append(person)
        
    return result

def people_generator(num_people):
    """[Função generator que cria um lista de pessoas
    com nomes sorteados e cursos sorteados.]
    
    Arguments:
        num_people {[int]} -- [Número de pessoas]
    
    Yields:
        [json] -- [Pessoa json]
    """    
    for i in range(num_people):
        #json com objeto pessoa
        person  = {
            'id':i,
            'name':random.choice(names),#sorteia um nome na lista de nomes
            'major':random.choice(majors)#sorteia um nome na lista de cursos
        }
        yield person

# Testes de performace com generator
t1 = time.clock()
#people_list(5000000)
people_generator(5000000)
t2 = time.clock()

#total de memória usada
print(f'\nMemory (After): {mu()} Mb')
print(f'Total de segundos para criação das pessoas:{t2-t1}s')

    
    
    


