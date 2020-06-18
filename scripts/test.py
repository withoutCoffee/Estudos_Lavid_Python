from LengthenSentence import LengthenSentence
import os
import re

if __name__== "__main__":
    
    folder = 'folder_of_files' #'for-overfitting-v4-manu'
    af = f'{folder}/.'
    
    for name in os.listdir(af):
        if not re.search('DUP|\.txt',name):
            
            path = f'{folder}/{name}'
            for number_of_concat in range(1,2,1):
                LengthenSentence(csv_path = f'{folder}/{name}',
                                number_concat = number_of_concat,
                                random_seed = 2,
                                file_name = name).process()