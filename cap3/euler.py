def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
aaaaaa
def euler(n):
    if n == 0:
        return 1
    else:
        return 1 / fatorial(n) + euler(n - 1)

resultado = euler(20)

print(f"euler(20) = {resultado:.5f}")
