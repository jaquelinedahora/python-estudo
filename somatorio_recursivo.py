num = int(input("insira um numero: "))

def fib(num):
  if num == 0:
    return 0
  if num == 1:
    return 1
  else:
    return fib(num - 1) + fib(num - 2)

for n in range(0, num):
  print(fib(n), end=' ')

#print(somatorio(num))



