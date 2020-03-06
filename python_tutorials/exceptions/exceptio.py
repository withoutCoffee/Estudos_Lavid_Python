import os
# Retorna o diretório atual   
current_dir = os.getcwd()

# Retorna uma lista com os nomes as entradas no diretório
os.listdir()

file_path = 'text_file.txt'
print(file_path)

# O try escuta o disparo de uma exceção, onde no bloco execept há a especificação do tipo de exceção 
# recebida. Caso haja mais de uma exceção disparada é necessário a utilização de outro bloco except.
try:
    f  = open(file_path,'r')
    #f  = open(le_path,'r') bad open
    #var = bar_var
except FileNotFoundError:
    print ("Erro ao abrir o arquivo!")
except Exception as e:
    print(e)
else:
# O try/except possui o comando else, colocado depois de todos ecepts
#  para código que precisa ser executado se nenhuma exceção foi lançada.
    print(f"O arquivo tem {len(f.readlines())} palavras")
    f.close()
finally:
# finally, Sua finalidade é permitir a implementação de ações de limpeza,
#  que sempre devem ser executadas independentemente da ocorrência de exceções
    print("Executando o finally!")
    
