class Employee:
    raise_amount = 1.04

    def __init__(self, first,last, pay):
        """[Construtor da classe]
        
        Arguments:
            first {[str]} -- [Primeiro Nome]
            last {[str]} -- [Últime Nome]
            pay {[float]} -- [Salário]
        """        
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.'+ last + '@company.com'
    
    def fullname(self):
        """[Este método concatena o primeiro com o
        ultimo nome do funcionário e retorna uma string]
        
        Returns:
            [str] -- [Nome Completo]
        """        
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        """[Este método aplica um aumento no salário de 4%]
        """        
        self.pay  = self.pay * self.raise_amount

# Herança da classe Employee, a classe Developer herda os atributos e métodos da classe Employee 
class Developer(Employee):
    
    raise_amount = 1.10
    
    # Reescrita do método construtor para Developer
    def __init__(self, first, last, pay, prog_lang):
        
        super().__init__(first,last,pay)
        
        self.prog_lang = prog_lang    
        
class Manager(Employee):
    
    def __init__(self, first, last, pay,employees = None):
        
        super().__init__(first, last, pay)
        
        if employees is None:
             self.employees = []
        else:
            self.employees = employees
        
    def add_emp(self, emp):
        self.employees.append(emp)
        
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for cont,emp in enumerate(self.employees):
            print(f"[{cont}] {emp.fullname()}")
        
        
ep = Employee('Jonas','Oliveira',123123)
print(ep.email)

dev = Developer('Jonas','Oliveira',123123,'Python')
print(dev.prog_lang)

dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev])


print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()