import csv
import pandas as pd
import re
import random

class LengthenSentence:
    """Creates long phrases by concatentating internal phrases"""

    def __init__(self,*args, **kwargs):
        self._match_GR = r'\.|!|\?'
        self._match_GI = r'\[PONTO]|\[INTERROGAÇÃO]|\[EXCLAMAÇÃO]'
        
        try:
            self._number_concat = kwargs.get('number_concat')
            self._csv = kwargs.get('csv_path')
            self._fd = open(self._csv, 'r', encoding='utf-8')
            self._reader = pd.read_csv(self._fd,header=None)
            self._reader_size = len(self._reader) - 1
            self._writer = open(f'concat_x{self._number_concat}.csv','w',encoding='utf-8')
            random.seed(kwargs.get('random_seed'))

        except KeyError:
            raise ValueError('csv path required')

    def process(self):
    
        try:
            for gr,gi in zip(self._reader[0], self._reader[1]):
                data = self.generate(gr,gi)
                self._writer.write(f'{data[0]},{data[1]}\n')
        except Exception as e:
            print(e)

    def generate(self,gr,gi):
        
        new_gi = self.clean(GI = gi)
        new_gr = self.clean(GR = gr)
        if self._number_concat <=0:
            raise ValueError('number_concat is invalid!, number_concat <= 0')

        for i in range(self._number_concat - 1):
            index = random.randint(0,self._reader_size)

            append_gr = self._reader[0][index]
            append_gi = self._reader[1][index]

            #clean [PONTO]
            new_gi = new_gi + self.clean(GI = append_gi)
            new_gr = new_gr + self.clean(GR = append_gr)
        
        index = random.randint(0,self._reader_size)

        new_gr = new_gr + self._reader[0][index]
        new_gi = new_gi + self._reader[1][index]
        
        return [new_gr,new_gi]

    def clean(self,GR = None, GI = None):
        if GR:
            return re.sub(self._match_GR,' ',GR)
        elif GI:
            return re.sub(self._match_GI,' ',GI)
    
    def __del__(self):
        if self._fd or self._writer:
            self._fd.close()
            self._writer.close()

if __name__== "__main__":
    ls = LengthenSentence(csv_path = 'raw.csv',number_concat=1,random_seed=0);
    ls.process()
    