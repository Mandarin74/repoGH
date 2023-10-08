##1) Напишите функцию для транспонирования матрицы

# def transpose(matr):
#     res=[]
#     n=len(matr)
#     m=len(matr[0])
#     for j in range(m):
#         tmp=[]
#         for i in range(n):
#             tmp=tmp+[matr[i][j]]
#         res=res+[tmp]
#     matr[:] = res
#     return matr


# arr = [[1, 2, 3], [4, 5, 6]]
# print(transpose(arr))

# #2) Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. 
# # Если ключ не хешируем, используйте его строковое представление.

# def revers_(**kwargs):
#     return {v if v.__hash__ is not None else str(v):k for k,v in kwargs.items()}

# print(revers_(arg1='hello', b=2, c=[1,2,3,4,5,6]))

# #3) банкоман на функциях

# class bnkmt():

#     def __init__(self, balance = 0.0):
#         self.balance = balance
    

#     def deposite(self):
#         dob = float(input('Введите сумму для внесения: '))
#         self.balance = dob + self.balance
#         print(f'Ваш баланс - {self.balance}')
#         text_2 = open("depsnt.txt", +a)
#         text_2.write(f"\n Внесено - {dob}", "\n                                      ")
    
#     def snt(self):
#         sntt = float(input("Комиссия 1,5% от суммы снятия. Введите сумму которую хотите снять: "))
#         if self.balance >= sntt*1.015:
#             self.balance = self.balance - sntt*1.015
#             print(f"Ваш баланс - {self.balance}")
#             text_1 = open("depsnt.txt", +a)
#             text_1.write(f'\n Снято - {sntt} Комиссия 1.5% {sntt*1.015}', "\n                                       ")
#         else:
#             print("Не хватает средств")

# s = bnkmt()

# print('Выберите операцию которую вы хотите сделать')
# while 1:
#     print("""1. Посмотреть баланс
# 2. Внесение наличных
# 3. Снятие наличных
# 4. Завершение операции""")

#     z = int(input(' - '))
    
#     if z == 1:
#         print(f'Ваш баланс - {s.balance}')
    
#     elif z == 2:
#         s.deposite()
    
#     elif z == 3:
#         s.snt()

#     elif z == 4:
#         print('Всего хорошего.')
#         break
    
#     else:
#         continue