
class Fibonacci:
    """[Class Fibonacci interator]
    
    Raises:
        StopIteration: [Objeto de parada]
    
    Returns:
        [Fibonacci] -- [Objeto Fibonacci]
    """    
    
    def __init__(self, max=500000):
        """[Constutor]
        """
        #incializa os dois primeiros números        
        self.current_elemet = 0
        self.next_element = 1
        
        self.max = max
        
    def __iter__(self):
        """[Função que retorna objeto retornável]
        
        Returns:
            [Fibonacci] -- [Objeto Fibonacci]
        """        
        return self
        
    def __next__(self):
        """[Next do interator/StopInteration]
        """
        #critério de parada
        if self.current_elemet > self.max:
            
            raise StopIteration
        
        #valor de retorno
        return_value = self.current_elemet
        
        self.current_elemet,self.next_element = self.next_element, self.current_elemet + self.next_element
        
        return return_value

 
    