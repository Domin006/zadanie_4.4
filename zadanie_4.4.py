# zadanie_4.4

# Definiowanie funkcji
def dodawanie(a, b):
    return a + b
def odejmowanie(a, b):
    return a - b
def mnozenie(a, b):
    return a * b
def dzielenie(a, b):
    return a / b
# działania
print("Wybierz działanie.")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie")
# wybór działania
wybor = input("Wprowadź wybór(1/2/3/4): ")
# sprawdzanie wyboru
if wybor in ('1', '2', '3', '4', '5'):
    liczba1 = float(input("Wprowadź pierwszą liczbę: "))
    liczba2 = float(input("Wprowadź drugą liczbę: "))
    if wybor == '1':
        print(liczba1, "+", liczba2, "=", dodawanie(liczba1, liczba2))
    elif wybor == '2':
        print(liczba1, "-", liczba2, "=", odejmowanie(liczba1, liczba2))
    elif wybor == '3':
        print(liczba1, "*", liczba2, "=", mnozenie(liczba1, liczba2))
    elif wybor == '4':
        print(liczba1, "/", liczba2, "=", dzielenie(liczba1, liczba2))
