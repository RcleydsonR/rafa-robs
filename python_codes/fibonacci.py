def fibonacci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
n = int(input('Quantos termos do fibonacci deseja ver: '))

for val in range(1, n+1):
    print(fibonacci(val))
