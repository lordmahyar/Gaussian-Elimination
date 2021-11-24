import numpy as np
from numpy import linalg as la
from fractions import Fraction


# LANGUAGE TRANSLATE SETTINGS
def _(text):
    if lang.upper() not in ['P', 'E']:
        return text

    translate_dict = {
        'Rahnama': ('INSTRUCTIONS', 'راهنما'),
        'Tedade moadelat ra vared konid': ('Enter number of equations', 'تعداد معادلات را وارد کنید'),
        'Zarib va javab moadele ra ba fasele vared konid': ('Enter values & answer with space', 'صریب و جواب معادله را با فاصله وارد کنید'),
        'Mesal': ('Example', 'مثال'),
        'jame': ('Add', 'جمع'),
        'Taqsime': ('Divide', 'تقسیم'),
        'satre': ('row', 'سطر'),
        'barabar': ('multiply by', 'برابر'),
        'bar': ('by', 'بر'),
        'ba': ('to', 'با'),
    }

    for key, value in translate_dict.items():
        text = text.replace(key, value[0] if lang == 'E' else value[1])

    return text


# GET MATRIX BY ENTER EACH EQUATION
def Get():
    number = int(input('Tedade moadelat ra vared konid: '))
    equations = []
    equations_ = []
    for i in range(number):
        inp = input().split(' ')
        equation = list(map(lambda x: Fraction(x).limit_denominator(), inp))
        equation_ = list(map(float, inp))
        equations.append(equation)
        equations_.append(equation_)
    print('\n')
    return equations, equations_


# SHOW MATRIX IN PRETTY FORMAT
def Show(mat):
    for i, sat in enumerate(mat):
        for j, sot in enumerate(sat):
            if j == n-1:
                print(f' = {str(Fraction(mat[i][j]).limit_denominator()):^7}')
                continue
            z = str(Fraction(mat[i][j]).limit_denominator())
            if z == '0':
                print(f'{"":^7}', end=' ')
                continue
            print(
                f'{"("+str(Fraction(mat[i][j]).limit_denominator())+f")X{j+1}":^7}', end=' ')
    print('-' * len(sat) * 6, end='\n' * 1)


# SOLVE MATRIX WITH NUMPY & SHOW VALUES
def SOLVE(equations):
    a = []
    b = []
    for i in range(len(equations)):
        a.append(equations[i][:-1])
        b.append(equations[i][-1])

    a = np.array(a)
    b = np.array(b).reshape((-1, 1))
    s = ''
    try:
        result = la.solve(a, b)
        for i in range(len(equations)):
            s += f'X{i + 1} = {Fraction(result[i][0]).limit_denominator(20)}\n'
        print(s)
    except la.LinAlgError as e:
        print(e)


lang = input('F for Finglish (default), P for Persian, E for English: ').upper()

# PRINT INSTRUCTIONS
print(_("""
[Rahnama]
1.Tedade moadelat ra vared konid.
2.Zarib va javab moadele ra ba fasele vared konid.

Mesal 1:
3
1 1 0 1
6 0 -2 -8
0 3 -1 -3

Mesal 2:
3
3 2 -4 3
2 3 3 15
5 -3 1 14

"""))

A, A_ = Get()  # GET MATRIX FROM USER
m, n = len(A), len(A[0])  # Matrix Dimensions
Show(A)  # SHOW ENTERED MATRIX

# SOLVE STEP BY STEP
for i in range(m):
    k = A[i][i]
    if k != 1:
        for num in range(i, n):
            A[i][num] /= k
        print(_(f'Taqsime satre {i + 1} bar {Fraction(k).limit_denominator()}:'))
        print(f'R{i + 1} / ({Fraction(k).limit_denominator()}): \n')
        Show(A)

    for j in range(i+1, m):
        k2 = -A[j][i]
        if k2 != 0:
            for num in range(n):
                A[j][num] += A[i][num] * k2
            print(_(f'jame satre {j + 1} ba {Fraction(k2).limit_denominator()} barabar satre {i + 1}:'))
            print(f'R{j + 1} + ({Fraction(k2).limit_denominator()})R{i + 1} :\n')
            Show(A)

# SHOW SOLVED VALUES
SOLVE(A_)
