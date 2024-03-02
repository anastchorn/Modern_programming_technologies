from copy import deepcopy
import numpy as np

matrix = np.array([
   [0, 1, 0, 1, 0],
   [0, 1, 0, 1, 0],
   [0, 0, 0, 1, 1],
   [1, 0, 0, 1, 0],
   [0, 1, 0, 0, 0]
])

print("Задане відношення: \n", matrix)


def ref(matrix):
    is_reflexive = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j and matrix[i][j] == 0:
                is_reflexive = 0
                print("Відношення не є рефлексивним")
                return is_reflexive
    print("Відношення рефлексивне")
    return is_reflexive

is_ref = ref(matrix)





def antiref(matrix):
    is_antiref=1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j and matrix[i][j] == 1:
                is_antiref=0
                print("Відношення не є антирефлексивним")
                return is_antiref
    print("Відношення антирефлексивне")
    return is_antiref
is_antiref=antiref(matrix)


def wrap(matrix):
    wrap_matrix= deepcopy(matrix)
    for i in range(len(wrap_matrix)):
        for j in range(i+1, len(wrap_matrix[i])):
            ver=wrap_matrix[j][i]
            wrap_matrix[j][i]=wrap_matrix[i][j]
            wrap_matrix[i][j]=ver
    return wrap_matrix

wrap_matrix=wrap(matrix)

print ("Обернене відношення:\n", wrap_matrix)


def wrap_check(matrix, wrap_matrix):
    transposed_matrix = np.transpose(matrix)
    print("Транспонована матриця:\n", transposed_matrix)
    if np.array_equal(transposed_matrix, wrap_matrix):
        print("Обернене відношення знайдене правильно \n")
    else:
        print("Error\n")
    return
wrap_check(matrix,wrap_matrix)

def symmetry(matrix, wrap_matrix):
    result = np.array_equal(matrix, wrap_matrix)
    if result:
        print("Відношення симетричне")
    else:
        print("Відношення не симетричне")

symmetry(matrix,wrap_matrix)



def antisym(matrix):
    is_antisym=1
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix[i])):
            if i!=j:
                if matrix[i][j]==1 and matrix[j][i]==1:
                    print("Відношення не є антисиметричним")
                    is_antisym=0
                    return is_antisym
    print("Відношення антисиметричне")
    return is_antisym
is_antisym=antisym(matrix)



def asym(matrix):
    is_asym=1
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix[i])):
            if matrix[i][j]==1 and matrix[j][i]==1 :
                print("Відношення не є асиметричним")
                is_asym=0
                return is_asym
    print ("Відношення не є асиметричним")
    return is_asym


is_asym=asym(matrix)

def tranzit(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matrix[i][j] == 1 and matrix[j][k] == 1 and matrix[i][k] == 0:
                    print("Відношення нетранзитивне")
                    return
    print("Відношення транзитивне")
    return





def best(matrix):
    ver=0
    for i in range(len(matrix)):
        sum=0
        for j in range(len(matrix[i])):
            sum+=matrix[i][j]
        if sum==len(matrix):
            print(i+1 , "- індекс найкращого елементу")
            ver=1
    if ver==0: print ("Відношення не має найкращого елементу")
    return

best(matrix)




def worst(matrix):
    ver=0
    for j in range(len(matrix)):
        sum=0
        for i in range(len(matrix[j])):
            sum+=matrix[i][j]
        if sum==len(matrix):
            print(j+1 , "- індекс найгіршого елементу\n")
            ver=1
    if ver==0: print ("Відношення не має найгіршого елементу\n")
    return
worst(matrix)



def strict_with_params(matrix, is_antiref, is_antisym):
     strict_matrix=deepcopy(matrix)
     if is_antisym==0:
          for i in range(len(strict_matrix)):
           for j in range(i+1, len(strict_matrix[i])):
             if i!=j:
                 if strict_matrix[i][j]==1 and strict_matrix[j][i]==1:
                     strict_matrix[i][j]=0
                     strict_matrix[j][i]=0
     if is_antiref==0:
          for i in range(len(strict_matrix)):
           for j in range(len(strict_matrix[i])):
               if i==j and strict_matrix[i][j]==1:
                   strict_matrix[i][j]=0
     return strict_matrix
strict_with_params=strict_with_params(matrix,is_antiref,is_antisym)

print("Строге відношення знайдене за допомогою перетворення до антисиметричного і антирефлексивного:\n", strict_with_params)


def strict_with_devision(matrix,inverted_matrix):
    strict_relation = matrix & ~inverted_matrix
    return strict_relation

strict_matrix=strict_with_devision(matrix,wrap_matrix)

print("Cтроге відношення знайдене за допмогою ділення: \n", strict_matrix)

antiref(strict_matrix)
antisym(strict_matrix)

def max(matrix):
    ver=0
    for j in range(len(matrix)):
        sum=0
        for i in range(len(matrix[j])):
            sum+=matrix[i][j]
        if sum==0:
            print(j+1 , "- індекс max елементу")
            ver=1
    if ver==0: print ("Відношення не має max елементу")
    return
max(strict_matrix)



def min(matrix):
    ver=0
    for i in range(len(matrix)):
        sum=0
        for j in range(len(matrix[i])):
            sum+=matrix[i][j]
        if sum==0:
            print(i+1 , "- індекс min елементу")
            ver=1
    if ver==0: print ("Відношення не має min елементу")
    return
min(strict_matrix)



def complement_relation(matrix):
    n = len(matrix)
    complement_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==0:
                complement_matrix[i][j]=1
    return complement_matrix

print("Доповнення: \n", complement_relation(matrix))
