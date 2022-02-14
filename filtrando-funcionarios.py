"""
Lista1 = Funcionários que tem carro e trabalham a noite
Lista2 = Funcionários que tem carro e trabalham de dia
Lista3 = Funcionários que não tem carro
"""

funcionarios = ['Ana', 'Marcus', 'Alice', 'Pedro', 'Raphael', 'Sophia', 'Antonio']
turno_dia = ['Ana', 'Marcus','Alice', 'Pedro']
turno_noite = ['Raphael', 'Sophia', 'Antonio']
tem_carro = ['Ana', 'Raphael','Alice', 'Antonio']

#Lista1
lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

#Lista2
lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

#Lista3
lista3 = set(funcionarios).difference(tem_carro)
print(lista3)
