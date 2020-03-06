import os

def rename(path, sep):
    """[Esta função renomea arquivos no formato
        title <sep> course <sep> number <sep> <.ext>]
    
    Arguments:
        path {[str]} -- [path of files]
        split {[str]} -- [sep]
    
    Returns:
        [list] -- [new names]
        [list] -- [last names]
    """
    
    # Altera o diretório de trabalho atual para o caminho especificado
    os.chdir(path)
    
    new_names = []
    last_names = []
            
    for f in os.listdir():
        
        file_name, file_ext = os.path.splitext(f)
        
        #guardando o nome errado para outros testes
        last_names.append(file_name+file_ext)
        
        f_title, f_course, f_num = file_name.split(sep)
        
        #retirando espaços
        f_title = f_title.strip()
        f_course = f_course.strip()
        f_num = f_num.strip()[1:].zfill(2)
        
        new_name = '{}-{}{}'.format(f_num, f_course, file_ext)
        
        #renomeado arquivo
        os.rename(f,new_name)
        
        new_names.append(new_name)
        
    return new_names, last_names

path = '/home/jonas_oliveira/estudos_lavid/python_tutorials/automate_parsing_renaming_files/temp/'

new_names, last_names = rename(path,'-')

print(f"lastname:{last_names}, new_names: {new_names}")

        
        