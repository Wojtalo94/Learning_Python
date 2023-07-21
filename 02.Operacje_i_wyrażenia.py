print("1) Operacje logiczne")

res = 5 < 10
print("Zmienna res ma typ bool i znaczenie: " + str(res))

x = 5

res = x > 0 and x < 10
print("Zmienna res ma typ bool i znaczenie: " + str(res))

res = x <= 0 or x >= 5
print("Zmienna res ma typ bool i znaczenie: " + str(res))

# Oprócz operacji logicznych "and" i "or" w pythonie możemy też sprawdzić negację.
res = not(x > 0 and x < 5)
print("Zmienna res ma typ bool i znaczenie: " + str(res))

# Operacja porównania piszę się używajc ==
res = x == x
print("Wartość x jest równa wartości x: " + str(res))

# Operacja zaprzeczenia piszę się używajc !=
y = 15
res = x != y
print("Wartość x nie jest równa wartości y: " + str(res))

print("------------------------------------------------------------------")

print("2) Funkcje")

#Co to jest funkcja? Najlepiej zobaczyć na poniższy kod.
print("Hello world")
# Funkcją jest pierwsze słowo, a więc "print". Pisząc to słowo wywołujemy funkcję, która wyświetli nam tzw. parametry, czyli to co napiszemy w cudzysłowie, który znajduje się między nawiasami i po słowie, funkcji "print".
# Funkcja "print" została już zdefiniowana w podstawowe bibliotece pythona.

#  Zdefiniujemy funkcję.
# Na począku znajduje się słowo kluczowe def (pochodzi od słowa define lub definition, czyli definiowanie), po tym słowie nazywamy sobie funkcję czyli "hello". Każda funkcja ma swoją nazwę i właśnie po tej nazwie, odwołujemy się do konkretnej funkcji. W nawiasach opisujemy parametry funkcji, ale na razie to zostawiamy. Poniżej definiujemy co ta funkcja ma robić, a więc drukować napis "Hello wordl!".


def hello():
    print("Hello world!")


# Poniżej wywołujemy utworzoną funkcję hello
hello()
hello()
hello()
hello()
hello()

# Właśnie ta walka z powielaniem kodu jest jednym z najgłówniejszych zadań, które jest rozwiązywane za pomocą funkcji.
# W pythonie jedną z najważniejszych zasad, jest pamiętać o wcięciach. Ponieważ możemy mieć nieprawidłową strukturę kodu.
# Kolejną ważną rzeczą, jest aby definicja funkcji zawsze była przed jej użyciem. Inaczej kod nie będzie działał
# Najpierw zdefiniowanie, potem zastosowanie.

# Aby można była tak odwoływać sie do funkcji, muszą być w niej opisane parametry. Robimy to w miejscu gdzie mamy zdefiniowaną funkcję, po jej nazwie w nawiasach.
# W okrągłych nawiasach po nazwie funkcji, podajem nazwę zmiennej, której automatycznie podczas wywoływania przypisano przekazywaną wartość
# Te zmienne nazywają się parametrami funkcji. Teraz ten parametr należy w jakiś sposób wykorzystać wewnątrz naszej funkcji


def hello(s):
    print("Hello, " + s + "!!!")


hello("world")
hello("python")
hello("jak")
hello("sie")
hello("masz")

print("\n------------------------------------------------------------------\n")


# Stwórzym nową funkcję która na wejściu przyjmuje dwa parametry (x, y).
def percent(x, y):
    # Ta funkcja będzie definiować ile procentów od x ma y. Napiszmy dokumentację do tej funkcji. Aby napisać dokumentację, stosuje się trzy cudzysłowy """.
    """What percentage of x is y"""
    # Stwórzymy zmienne pomocnicze.
    one_percent = x / 100
    # Na początku określami ile to będzie 1% od x, potem definiujemy tą wielkość, która jest nam właściwie potrzebna. Czyli y podzielić przez jeden procent przez x.
    result = y / one_percent
    # Teraz wydrukujmy wynik.
    print(str(y) + " is " + str(result) + " percents of " + str(x))


# odwołujemy się do tej funkcji
percent(80, 7)


print("\n------------------------------------------------------------------")


# Pierwsza funkcja o nazwie percents wykonuje nam obliczenia. Dodatkowo dopisaliśmy linijkę "return result". To sprawia że ta funkcja zwraca nam wynik po wyliczeniach. Ten wynik może być zastosowany w jakieś innej funkcji.
def percents(a, b):
    """What percentage of x is y"""
    one_percent = a / 100
    result = b / one_percent
    return result


# Druga funkcja o nazwie print_percents drukuje nam wynik z pierwszej funkcji. Wynik zostaje pobrany z funkcji, a nie z zmiennej, ponieważ użyto słowa kluczowego return, który zwraca wynik z zmiennej do funkcji.
def print_percents(a, b):
    """Print what percentage of x is y"""
    print(str(b) + " is " + str(percents(a, b)) + " percents of " + str(a))


# Obie funkcje przyjmują dwa parametry wejściowe (czyli a, b).
# Czyli używając słowa return, zwracamy wynik który mamy w result i przesyłamy go do funkcji def percents(a, b). Teraz ta funkcja przechowuje wynik z obliczeń. Dlatego drukując wynik, używamy nazwę funkcji czyli def percents(a, b), a nie nazwy zmiennej która ta wynik przechowuje czyli result, ponieważ ją zwróciliśmy do funkcji.
print_percents(200, 50)

print("\n------------------------------------------------------------------\n")

print("3) Praca z bibliotekami. Konstrukcja import.")

# Jeśli napiszemy w kodzie:
# math.sin(0)
# to kod nam nie zadziała, ponieważ math nie będzie zdefiniowany.
# Należy zaimportować moduły najpierw z biblioteki i dopiero w tedy będzie można z nich korzystać.

# 1. Importujemy moduł (np. math)

import math

# Jeśli teraz napiszemy w kodzie:
mat = math.sin(0)
# Otrzymamy 0.0.
print("Wynik to: " + str(mat))

# Natomiast jeśli napiszemy
# sin(0)
# To niestety to nie zadziała i otrzymamy że sin nie jest zdefiniowany.

# 2. Importujemy nazwę konkretnej funkcji (np. sin) z modułu (np. math)
from math import sin
# Teraz nasza funkcja sin z modułu tego modułu importowana jest bezpośrednio do naszej przestrzeni nazw.
# Z niej można korzystać bez prefixu (np. math).

# Teraz jak napiszemy
mat = sin(0)
# To otrzymamy poprawny wynik 0.0.
print("Wynik to: " + str(mat))

# 3. Import wszystkich funkcji które znajdują się w jakimś module. (ten najlepiej nie korzystać, ze względu na możliwe i bardzo częste konflikty w kodzie).
# from math import *
# Teraz zostaną zaimportowane wszystkie funkcje które znajdują się w module math. Czyli wszystko z punktu 9.2 z dokumentacji biblioteki python.
# Ten sposób nie jest jednak polecany, ponieważ potencjalnie może on prowadzić do konfliktów. Najlepiej importować tylko te funkcje, które będą nam potrzebne.

# 4. 	Import funkcji z innej przestrzeni nazw.
# Jeśli ona konfliktuje z jakąś inną funkcją, można zmienić jej nazwy, robimy to tak:
# from math import sin as sinus
# Więc importujemy funkcję sin z modułu math, zmieniając jej nazwę na sinus.


print("\n------------------------------------------------------------------\n")

print("4) Klasy i obiekty.")

# Klasa to forma, szablon, opis tego jak powinny być zbudowane obiekty i wszystkie obiekty tej klasy powstają według jednego szablonu, wszystkie mają jednakowy zbiór właściwości, ale konkretne znaczenie tych właściwości różni się (np. data, jest jedna, natomiast możemy ją różnie zapisać, zmienia się).
# W dokumentacji bibliotek python-a, znajdźmy moduł datetime, który zawiera klasy przeznaczone z datą i czasem

# Zaimportujmy ten moduł w cmd z wykorzystaniem ipython. W ten sposób zaimportowaliśmy nie tylko funkcje, ale także klasy. Musimy wskazać 3 atrybuty, a jest to w tym przypadku rok, miesiąc i dzień.
from datetime import date
# datetime - to nazwa modułu
# date - to nazwa klasy

date_in_past = date(2000, 1, 15)

print("Utworzona data to: " + str(date_in_past))

# Jest możliwość otrzymanie oddzielnie atrybutów stworzonego obiektu o nazwie date_in_past
print("Utworzony rok to: " + str(date_in_past.year))
print("Utworzony miesiąc to: " + str(date_in_past.month))
print("Utworzony dzień to: " + str(date_in_past.day))

# date - to klasa, dlatego wywołujemy metodę w klasie, a nie w obiekcie
today_day = date.today()
print("Dzisiejsza data to: " + str(today_day))


print("\n------------------------------------------------------------------\n")

print("5) Własne klasy.")

# Wykonamy funkcję która definiuje odległość pomiędzy dwoma punktami na płaszczyźnie.
# sqrt - funkcja wyciągania pierwiastka kwadratowego, znajdującego się w pakiecie math, więc musimy ją zaimportować

from math import sqrt


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return sqrt(dx*dx + dy*dy)


print("Wynik to: " + str(distance(0, 0, 3, 4)))
# Wynik powinien być 5.0.

# Utwórzmy klasę "Point" i ta klasa powinna mieć konstruktora, po to abyśmy mogli tworzyć obiekty tej klasy. Ale kiedy odwołujemy się do konstruktora, to wywołujemy go po imieniu, które pokrywa się z imieniem klasy, ale w trakcie definiowania konstruktora ma on specjalną nazwę "init" otoczoną z dwóch stron podwójnym podkreśleniem.

from math import sqrt

# Teraz parametry konstruktora.
# 1. Obiekt który jest konstruowany (self)
# 2. Chcemy konstruować punkty przekazując 2 parametry współrzędne x i y
class Point:
    def __init__(self, x, y):
# Te wartości które są przekazywane w parametrach x i y, musimy przypisać do atrybutów do obiektu self.
# self.x = x to dwie całkiem różne jednostki.
# x - w tym wypadku to jest zmienna parametr, w niej mieści się ta wartość, którą przekazujemy w wywołaniu na końcu funkcji
# x przy (self.x) - to jest atrybut przy self, nazwa atrybutu (x) zawsze jest poprzedzana nazwą obietku (self), a atrybut jest częścią obiektu, częścią klasy
        self.x = x
        self.y = y

# Konstruktor jest gotowy.


# Teraz stwórzmy na nowo funkcję, która wylicza odległość. Aby w charakterze parametrów przyjmowa nie cztery liczby jak wcześniej (x1, y1, x2, y2), a dwa punkty (p1, p2), dwa obiekty typu point.
# Teraz pracujemy nie z liczbami, a z obiektami.
def distance(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    return sqrt(dx*dx + dy*dy)
# Gdy otrzymujemy atrybut tego obiektu, to otrzymujemy go właśnie takim sposobem, czyli nazwa obiektu "p2", kropka ".", nazwa atrybutu "x".


# Teraz odwołujemy się do obiektów drukując je.
print("Wynik to: " + str(distance(Point(0, 0), Point(3, 4))))
# Wynik powinien być znów: 5.0

# Teraz zmieńmy funkcje distance w metodę która będzie obliczała odległość między dwoma punktami, ale odwoływać się do niej należy już inaczej. Aby ta funkcja stała się metodą, należy ją umieścić wewnątrz klasy.
# Powyżej funkcja distance znajduje się na tej samej wysokości wcięć co klasa Point, więc nie jest jej częścią, następuje ona po klasie. Chodzi o formatowanie w pythonie za pomocą wcięć i strukturowanie kodu.

# Import funkcji wyciągania pierwiastka kwadratowego z pakietu math:
from math import sqrt


# Wykonaliśmy klasę:
class Point:
    # W tej klasie zdefiniowaliśmy konstruktora ...
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # ... oraz matodę ...
    def distance(p1, p2):
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        return sqrt(dx*dx + dy*dy)

# Teraz funkcja distance stała się częścią klasy Point, ponieważ są odpowiednie wcięcia, a funkcja distance teraz stała się metodą distance.
# Gdy staje się metodą, to znaczy że powinna przyjmować w charakterze pierwszego parametru obiekt w którym ta metoda jest wywoływana, który przyjęto nazywać się słowem self.
# Teraz nie mamy funkcji distance, ponieważ stał on się metodą distance, dlatego jej nie wywołamy do drukowania.

# Teraz dodatkowo zdefiniujmy operację porównania. Nazywa się ona def __eq__.
    # ... a także operacje aby działała według znaczenia, porównywała obiekty tak chcemy
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# Teraz ta funkcja distance która przyjmuje dwa parametry  "Point(0.0)" oraz "Point(3, 4)"sądząc po zdefiniowaniu, jest metodą, a pierwszy paramert "Point(0.0)" to obiekt w którym jest wywoływana. Drugi parametr to ten który jest przekazywany do tej metody w okrągłych nawiasach czyli  "(Point(3, 4))".
# Można też to zrobić za pomocą lokalnych zmiennych a i b.
# Następnie skonstruowaliśmy dwa obiekty:
a = Point(0, 0)
b = Point(3, 4)
# Wywołaliśmy metodę:
print(a.distance(b))
# oraz sprawdziliśmy czy działa operacja porównania:
print(a == b)
print(a == Point(0, 0))

print("\n------------------------------------------------------------------\n")

# ---- przejrzeż dalej notatki od V. GitHub w zwyż szukając co tutaj można dodać, np listy, pętle itp.