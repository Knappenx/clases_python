user_input = int(input("Introduce un numero de 1 al 99 para detener el conteo: "))

for num in range(50, 100):
    fizz = num % 3
    buzz = num % 5
    if fizz == 0 and buzz == 0:
        print("Fizz Buzz")
    elif fizz == 0:
        print("Fizz")
    elif buzz == 0:
        pass
    else:
        print(num)
    if num == user_input:
        break