import datetime

# Classe Funcionário/Empregado
# Uma das coisas se notar no python é que a linguagem permite a criaçãod
# de atributos em tempo de execução, o acesso a os mesmo é público.
class Employee:
    # Variável de Classe. A mesma só pode ser acessado de pela classe
    # uma das utilidades é servir de contador de quantas vezes a classe foi instanciada.
    raise_amount = 1.04
    
    # Tornando o atributo de calsse privado com um underscore antes do nome
    number_employees = 0
    
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
        self.email = first +'.'+ last + 'company.com'
        
        Employee.number_employees += 1

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
        
    # Decorator para tornar em método de classe
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls,string):
        """[Este método cria um objeto Empoyee a partir de uma string
        com os atributos do objeto separados por '-']
        
        Arguments:
            string {[str]} -- [stringcom os atributos do objeto separados por '-']
        
        Returns:
            [Employee] -- [Objeto Employee]
        """        
        # Instancia um objeto emp a partir de uma string com os 
        first, last, pay = string.split('-')
        return cls(first,last,pay)
    
    # Decorator paraTornando em um método stático
    @staticmethod
    def is_workday(day):
        """[Este método verifica se um dia trabalho]
        
        Arguments:
            day {[datetime]} -- [Data]
        
        Returns:
            [boolean] -- [Se sim ou não, True ou False]
        """        
        # Verifica se é sábado ou domingo        
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
# Testes
# Instanciando 2 objetos da classe funcionários
emp1 = Employee('jonas','oliveira',10000)
emp2 = Employee('jorge','oliveira',44444)
emp3 = Employee('ana','oliveira',123123)

Employee.set_raise_amt(1.04)

print(emp1.fullname())

emp2.apply_raise()
print(emp2.pay)

string = 'Joe-AA-5000'
new_emp = Employee.from_string(string)
print(new_emp.first)

my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))

