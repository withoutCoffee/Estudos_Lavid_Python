
from operator import attrgetter

class Employee():
    def __init__(self, name, age ,salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def __repr__(self):
        """[A função __repr__ retorna uma representação do objeto,
        ela deve retornar uma string, caso contrário um erro será gerado.]
        """       
        return f'({self.name},{self.age},{self.salary})'

e1 = Employee('Name4',12,300)
e2 = Employee('Name2',40,3555)  
e3 = Employee('Name3',45,300)

employess = [e1,e2,e3]

# Como o função sorted não pode ordenar objetos por padrã, é preciso a
# construção de um nova função para passar como como parâmetro key no sorted
def e_sort(emp):
    return emp.name

s_employee = sorted(employess, key=e_sort)

print(s_employee)

#utilizando lambda functions
s_employee = sorted(employess, key=lambda e: e.salary)
print(s_employee)

#utilizando attrgetter
s_employee = sorted(employess, key=attrgetter('age'))
print(s_employee)



