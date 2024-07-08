#napisz pętle, która bedzie odliczała od 1000 do 0 z krokiem 50 i wyświetlała przy tym odliczana wartości
print("zad 1")
i = 1000
while i >= 0:
    print(i)
    i = i - 50

print("zad 2")
# napisz pętle, która bedzie odliczała od 0 do 1000 z krokiem 25 i wyświetlała przy tym odliczana wartości
i = 0
while i <= 1000:
    print(i)
    i = i + 25

print("zad 3")
#napisz klase ktora bedzie obliczala predkosc pojazdu na podstawie czasu w jakim pokonal on okreslony odcinek.
class Predkosc:
    def __init__(self, czas, droga):
        self.czas = czas
        self.droga = droga
    def predkosc(self):
        return self.czas/self.droga

predkosc_1 = Predkosc(10,20)
print(predkosc_1.predkosc())

print("zad 4")
#Napisz program obliczający sumę liczb nieparzystych poczynając od liczby x, a kończąc na liczbie y.
x = int(input("Podaj x:"))
y = int(input("Podaj y:"))
suma = 0
while x <= y:
    if (x % 2 == 1):
        suma += x
    x += 1
print("suma=", suma)

print("zad 5")
#Napisz program sumujący wartości ciągu n liczb podawanych przez użytkownika. Ilość liczb podaje użytkownik jako pierwszą wartość.
n = int(input("Podaj n:"))
suma = 0
for i in range(1, n + 1):
    liczba = int(input("Podaj liczbę: "))
    suma += liczba
print("suma=", suma)

print("zad 6")
#Napisz program wyświetlający liczby całkowite z ciągu 0, 5, 15, 30, 50, 75, 105 … (wyświetl 10 pierwszych wartości)
liczba = 0
roznica = 5

for i in range(1, 11):
    print(liczba)
    liczba += roznica
    roznica += 5

print("zad 7")
for liczba in range(1, 11):
    print(liczba)
    if liczba == 5:
        break

print("zad 8")
for liczba in range(1, 11):
    if 4 <= liczba <= 6:
        continue
    print(liczba)

print("zad 9")
liczba = 1
while liczba <= 10:
    print(liczba)
    if liczba == 5:
        break
    liczba += 1

print("zad 10")
#drukuje w nieskończoność
n = int(input("Podaj n:"))
while n <= 10:
    print(n)
    break

print("zad 11")
print("0, 1, 2, 3, 4 , 5, 6, 7, 8, 9")
n = int(input("Wylosuj zwycięzką liczbę:"))
while n == 5:
    print("Wygrałeś!")
    break
while n != 5:
    print("Przegrałeś")
    break

print("zad 12")
def notatnik():
    liczba_1 = input("1 liczba")
    liczba_2 = input("2 liczba")
    for idx, _ in enumerate(liczba_1):
        print(liczba_1[idx], liczba_2[idx],end='')

print("zad 13")
def filter_words_ending_with_a():
    wyraz = input("Podaj wyrazy oddzielone spacją: ").split()
    wyrazy_konczce_sie_na_a = [wyraz for wyraz in wyraz if wyraz.endswith('a')]

    print("Wyrazy kończące się na 'a':")
    for wyraz in wyrazy_konczce_sie_na_a:
        print(wyrazy_konczce_sie_na_a)

filter_words_ending_with_a()

def jakas_funkcja():
    return len([i for i in range(0,1000) if i % 2==0])

print(jakas_funkcja())

def inny_case():
    no = 0
    for i in range (0,1000):
        if i%2==0:
            no+=1

    return no

print(inny_case())

def inny_case_2():
    licznik_petli=0
    no=0
    while True:
        licznik_petli+=1
        if licznik_petli%2==0:
            no+=1
        if licznik_petli>1000:
            break
    return no

print(inny_case_2())

def aa():
    liczba_podana = int(input("Podaj liczbe końcową: "))
    for liczba in range(liczba_podana + 1):
        if liczba % 5 == 0:
            print(liczba)

aa()