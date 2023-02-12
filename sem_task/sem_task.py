import copy

# ПРОВЕРКА 1
def check(mat1, mat2):
    lmat1, lmat2, llmat1, llmat2 = len(mat1), len(mat2), len(mat1[0]), len(mat2[0])
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return 'error'
    for i in range(lmat1):
        for j in range(llmat1):
            if type(mat1[i][j]) != int:
                return 'error'
            if type(mat2[i][j]) != int:
                return 'error'


def summa(mat1, mat2):
    if check(mat1, mat2) == 'error':
        return 'error'

    else:

        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                mat1[i][j] += mat2[i][j]
        return mat1


def mul(A1, A2):
    summa = 0
    if uslovie(A1, A2) and len(A1[0]) == len(A2):
        rez = []
        A3 = []
        for i in range(len(A1)):
            for j in range(len(A2[0])):
                for k in range(len(A1[0])):
                    summa += A1[i][k] * A2[k][j]
                rez.append(summa)
                summa = 0
            A3.append(rez)
            rez = []
        return A3
    else:
        return 'error'
    

def diff(A1,A2):
    if uslovie(A1, A2) and (det(A2)!=0) and len(A2) == len(A2[0]):
        rez = 0
        temp_det= det(A2)
        mx2 = transp(alg(A2))
        for i in range(len(A2)):
            for j in range(len(A2)):
                A2[i][j] = A2[i][j]*(1/temp_det)
        rez = mul(A1,mx2)
        for i in range(len(rez)):
            for j in range(len(rez[0])):
                rez[i][j] = round(rez[i][j],2)
        return rez
    else:
        return 'error'


def det(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if type(A[i][j]) == str:
                return 'error'
    m = len(A)
    n = len(A[0])
    if m != n:
        return 'error'
    if n == 1:
        return A[0][0]
    signum = 1
    determinant = 0
    for j in range(n):
        determinant += A[0][j] * signum * det(minor(A, 0, j))
        signum *= -1
    return determinant


def print_matrix(A):
    for strA in A:
        print(strA)


def minor(A, i, j):
    M = copy.deepcopy(A) 
    del M[i]
    for i in range(len(A[0]) - 1):
        del M[i][j]
    return M


def transp(mat1):
    return [list(x) for x in zip(*mat1)]


# ПРОВЕРКА 2
def ch_rank(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if type(A[i][j]) == str:
                return 'error'


def rank(A):
    if ch_rank(A) != 'error':
        return min(len(A), len(A[0]))
    else:
        return 'error'


# СУММА ЭЛЕМЕНТОВ В СТОЛБЦЕ
def uslovie(x, y):
    for i in x:
        for j in i:
            if type(j) != int:
                return False
    for i in y:
        for j in i:
            if type(j) != int:
                return False
    return True


def L1(A):
    if uslovie(A, A):
        maxim = 0
        s = 0
        for i in range(len(A)):
            for j in range(len(A[i])):
                    if A[i][j] < 0:
                        A[i][j] = A[i][j] * (-1)
                    s += A[i][j]
            if s > maxim:
                maxim = s
            s=0
        return maxim
    else:
        return 'error'
    

# ПОДСЧЕТ НУЛЕЙ
def L0(A):
    if uslovie(A, A):
        x = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]!=0:
                    x+=1
        return x
    else:
        return 'error'


# 3х3
def det3(A):
    if uslovie(A, A):
        if len(A) >= 3 and len(A[0]) >= 3:
            rez = (A[0][0]*A[1][1]*A[2][2] + A[0][2]*A[1][0]*A[2][1] + A[2][0]*A[0][1]*A[1][2] - A[2][0]*A[1][1]*A[0][2] -A[0][0]*A[1][2]*A[2][1] - A[2][2]*A[0][1]*A[1][0])
            return rez
        else:
            return 'error'
    else:
        return 'error'
    

# 2х2
def det2(A):
    if uslovie(A, A):
        if len(A) >= 2 and len(A[0]) >= 2:
            rez = A[0][0]*A[1][1] -A[0][1]*A[1][0]
    return rez

# temp
def alg(A):
    mx_temp=[]
    list_temp=[]
    for i in range(len(A)):
        for j in range(len(A)):
            list_temp.append(A[i][j])
        mx_temp.append(list_temp)
        list_temp=[]
    for k in range(len(mx_temp)):
        for l in range(len(mx_temp)):
            A[k][l] = ((-1)**(k+l))*(det3(minor(mx_temp,k,l)))
    return A

