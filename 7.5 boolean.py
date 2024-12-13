# main.py

from helpers import in_range

def main():
    # Pobranie danych od użytkownika
    value = int(input('A number: '))
    range_start = int(input('Range start: '))
    range_end = int(input('Range end: '))

    # Sprawdzenie zakresu
    is_in_range = in_range(value, range_start, range_end)
    result = "yes" if is_in_range else "no"

    # Wyświetlenie wyniku
    print(f'Number {value} in the range <{range_start},{range_end}>: {result}')

if __name__ == '__main__':
    main()
