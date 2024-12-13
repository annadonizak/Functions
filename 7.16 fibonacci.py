"""
returns the n-th value of the Fibonacci sequence
"""
N = 9     #Zmienna N określa, który element ciągu Fibonacciego obliczamy (Każdy element to suma dwóch poprzednich)


def fibonacci_number(n):       #Funkcja fibonacci_number iteracyjnie oblicza n-ty element ciąg
    if n <= 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1  # First two numbers
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def main():
    print(f'{fibonacci_number(N)}')
    

if __name__ == '__main__':
    main()