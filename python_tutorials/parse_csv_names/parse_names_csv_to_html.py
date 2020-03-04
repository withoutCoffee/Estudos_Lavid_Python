import csv

file_path = 'patrons.csv'

def parse_csv_to_html(file_path):
        
    html_output = ''

    names = []

    with open(file_path,'r') as file:
        
        #lendo arquivo csv na forma padrão
        #csv_data = csv.reader(file)
        
        #lendo arquivo csv como dicionário
        csv_data = csv.DictReader(file)
        
        #não queremos cabeçalhos ou primeira linha ou dados errados...
        next(csv_data)
        #adicionando os nome na lista names
        for item in csv_data:
        
            if item['FirstName'] == 'No Reward':
                break        
            names.append(f"{item['FirstName']} {item['LastName']}")
            
        html_output = f"<p>< There ares currently {len(names)} public contributors. Thank You!./p>"     
        
        #concatenando linhas na string html_ouput
        for name in names:
            html_output += f"\n\t<li>{name}</li>"
            
    return html_output, names    

html_output, names = parse_csv_to_html(file_path)
    
print(html_output)

