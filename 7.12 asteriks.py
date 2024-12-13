"""
returns a string of n asterisks, separated by a slash sign
"""

N = 4


def get_asterisks(n):             #Tworzy liste z 4 gwiazdkami
    return '/'.join(['*'] * n)      #laczy je / tworzac ciag '*/*/*/*'


def main():                           #funkcja main wywoluje get_asteriks(N) i daje na ekran wynik
    print(f'{get_asterisks(N)}')           #wpisuje wynik na ekran w formacie f string
    

if __name__ == '__main__':        #Ten kod urochamia programm
    main()