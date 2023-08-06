print("01. Pętla for")

# Wykorzystamy najbardziej znaną pętle czyli for, dla formatowania listy. A właśnie zrobimy listę obiektów typu Point, to znaczy punktów na płaszczyźnie dwuwymiarowej X oraz Y. W tym przypadku punkty będą budowane zgodnie z zdefiniowaną regułą. Będą znajdować się one na paraboli. To znaczy będą to punkty typu X oraz X2.
# Najpierw stwórzmy pustą listę i dokładnie ją będziemy wypełniać:
l = []

# Teraz organizujemy pętle (for i in range). Lewa granica czyli -5, jest zawarta w tej pętli, natomiast prawa granica czyli 6 już nie)
for i in range(-5, 6):
    # Dalej zaczynają się działania, które będą dokonywać się w każdym przejściu tej pętli. Będziemy dodawać na listę kolejne obiekty
    l.append(i)
print(l)

for el in l:
    l2 = el*2
    print(l2)
    # za pomocą tej pętli el, punkty będą mnożone o 2 oraz wyświetlane jeden pod drugim

print("\n------------------------------------------------------------------\n")

print("02. List comprehension")

# List comprehension to skrótowy sposób tworzenia list w Pythonie. Jest to popularna i przydatna konstrukcja, która pozwala na generowanie listy na podstawie innych sekwencji danych, iteracji i zastosowania określonych warunków w jednolinijkowym zapisie

# Teraz wypiszemy liczby od -5 do 6 używając list comprehension:
numbers = [x for x in range(-5, 7)]
print("Numbers: " + str(numbers))

# Składnia:
# List comprehension jest zapisywane w postaci [wyrażenie for element in sekwencja if warunek]. Może zawierać zarówno wyrażenie, pętlę, jak i warunek, ale część if warunek jest opcjonalna.

# Generowanie listy:
# List comprehension pozwala na wygenerowanie listy w jednym wyrażeniu, co jest bardziej zwięzłe i czytelne niż tradycyjna pętla for z użyciem funkcji append().
#
# Iteracja:
# List comprehension automatycznie iteruje po sekwencji, która może być np. zakresem (range), listą, krotką, zbiorami (set) lub generatorami.
#
# Wyrażenie:
# W części [wyrażenie] możesz określić działanie, które zostanie wykonane dla każdego elementu sekwencji. Może to być dowolne wyrażenie, które zwróci wartość, np. matematyczne działanie, funkcja, zmienne, itp.
#
# Warunek (opcjonalny):
# Część if warunek pozwala na dodanie warunku, który musi zostać spełniony, aby element został dodany do listy wynikowej. Warunek ten jest opcjonalny, ale pozwala na filtrowanie wyników.
#
# Przykład:
# Oto przykład prostego list comprehension, które generuje listę zawierającą kwadraty liczb od 0 do 9:
squares = [x**2 for x in range(10)] # Wynik to [0, 1, 4, 9, 16, 25, 36, 49, 64, 81].
print("The result is: " + str(squares))
#
# Czytelność i zwięzłość:
# List comprehension poprawia czytelność kodu i pozwala na bardziej zwięzły zapis, co ułatwia zrozumienie zastosowanych operacji.
#
# Wydajność:
# List comprehension jest zazwyczaj wydajniejsze od tradycyjnych pętli, ponieważ wykonywane jest wewnątrz interpretera Pythona, co minimalizuje narzut czasowy.
#
# Zagnieżdżanie:
# List comprehension może być zagnieżdżane, co pozwala na bardziej złożone generowanie list zawierających wiele sekwencji i warunków.0
