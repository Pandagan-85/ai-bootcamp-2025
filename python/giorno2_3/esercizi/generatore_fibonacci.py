# Generatore usato per la squenza dei numeri di Fibonacci
def fib(number):
	a = 0
	b = 1
	for i in range(number):
		yield a
		temp = a
		a = b
		b = temp + b

## Stampo i numeri della sequenza fino al 20°
for x in fib(21):
	print(x)
