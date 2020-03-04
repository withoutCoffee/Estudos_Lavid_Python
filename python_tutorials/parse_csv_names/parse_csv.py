"""[Script para cópia de arquivo CSV]
 Copia o arquivo names.csv para o arquivo new_names.csv com edições no formato
 
"""
import csv 

path  = 'names.csv'

#abrindo arquivo no modo leitura, porém com uso do WITH não há necesssidade fechar o arquivo 
with open(path,'r') as csv_file:
    
    #lendo CSV como dicionário
    csv_reader  = csv.DictReader(csv_file)
    
    with open('new_names.csv','w') as new_file:
        
        #nomes dos atributos do dicionário
        fieldnames = ['first_name','last_name','email']
        
        #criando arquivo CSV a partir de um dicionário
        #com atributos var <fieldnames> e delimitador como um TAB        
        csv_writer = csv.DictWriter(new_file,fieldnames = fieldnames, delimiter = '\t')
        
        #escrevendo cabeçalho do CSV
        csv_writer.writeheader()
        
        for line in csv_reader:
            csv_writer.writerow(line)
            
        
    