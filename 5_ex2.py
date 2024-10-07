N = int(input("Введіть кількість N: "))
if N>=2 and N<99:
    for i in range(1, N+1):
        print(i,i)
        num1 = i * 100 + 10
        num2 = i * 100 + 30
        print(f"{num1} 0 {num2} 0")
else:
    print("N має бути в діапазоні від 2 до 99.")
