# 1. tinh giai thua cua mot so nhap vao n (bat ngoai le)
# Cach tinh giai thua 
#       Neu n = 0 => 0! = 1
#       Neu n > 0 => n! = 1.2.3...n = n.(n-1).(n-2)…2.1 = n.(n-1)! => n! = n.(n-1)!

# chuong trinh ko co function
import sys


#n = int(input('Nhap vao mot so nguyen (n) can tinh giai thua: '))
def fact(n):
    # if n is not type(int()):
    #     raise ValueError('phai nhap so nguyen')
    try:
        if n==0:
            return 1
        else:
            return n*fact(n-1)
    except  (TypeError) as e: print(f'Erro {e!r}',
                file=sys.stderr)
    raise

print(fact('103'))




