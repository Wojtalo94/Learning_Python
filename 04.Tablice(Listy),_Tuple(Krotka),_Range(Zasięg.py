print("01. Tablice (Listy)")
# Tablice w Pythonie reprezentowane są za pomocą nawiasów kwadratowych [ ]. Są to dynamiczne i zmiennego rozmiaru struktury danych, które mogą przechowywać różne typy elementów, w tym liczby, napisy, obiekty, itp. Elementy tablicy są indeksowane od 0, co oznacza, że pierwszy element znajduje się pod indeksem 0, drugi pod indeksem 1, itd. Możesz również modyfikować, dodawać i usuwać elementy z tablicy w czasie działania programu.

table = [1, 2, 3, 'four', 5.0]
print(table[0])  # Wyświetli: 1
table.append(6)  # Dodanie nowego elementu za pomocą funkcji append o wartości 6 na końcu tablicy
print(table)  # Wyświetli: [1, 2, 3, 'four', 5.0, 6]

print("The length of the List  is: " + str(len(table)))  # w ten sposób poznamy długość tablicy

print("Is element 7 in the List? The answer is: " + str(7 in table)) # sprawdzanie czy dany element znajduje sie w tablicy

# posortujmy teraz nową listę

table = [1, 5, 3, 7, 2, 8]
print("List before sorting: " + str(table))
table.sort()  # funkcja sort sortuje listę bez tworzenia nowej listy
#table2 = sorted(table)  # funkcja sort sortuję listę tworząc nową listę o nazwie table2
print("List after sorting: " + str(table))







print("\n------------------------------------------------------------------\n")

print("02. Tuple (Krotka)")
# To inny typ struktury danych w języku Python. Krotka jest podobna do listy, ale ma kilka kluczowych różnic. Główną różnicą między tuplem a listą jest to, że tuple są niemutowalne, co oznacza, że nie można zmieniać ich zawartości po ich utworzeniu. W przeciwieństwie do list, które reprezentowane są za pomocą nawiasów kwadratowych [ ], tuple reprezentowane są za pomocą nawiasów okrągłych ( ).
# Główne cechy krotek:
    # Niemutowalność: Po zdefiniowaniu krotki nie można jej zmieniać, tj. nie można dodawać, usuwać ani zmieniać elementów.
    # Indeksowanie: Krotki są indeksowane, podobnie jak listy, co oznacza, że można uzyskiwać dostęp do ich elementów za pomocą indeksów.
    # Przechowywanie różnych typów: Krotki mogą zawierać różne typy danych, takie jak liczby, napisy, inne krotki itp.


Tuple = (1, 'dwa', 3.14)
print(Tuple[0])  # Wyświetli: 1

# Poniższy kod spowoduje błąd, ponieważ krotki nie można zmieniać:
# Tuple[1] = 'dwa_zmienione'  # To wywoła TypeError

# Przykład Tuple zawierającej inne Tuple:
Tuple_in_Tuple = ((1, 2), (3, 4), (5, 6))
print(Tuple_in_Tuple)  # Wyświetli: ((1, 2), (3, 4), (5, 6))
# Tuple są szczególnie użyteczne, gdy chcemy przechować zestaw elementów, które nie będą się zmieniać podczas działania programu. Ich niemutowalność zapewnia, że dane w nich są bezpieczne i niepodatne na przypadkowe zmiany.

# Korzystając z krotek wygodniej jest pisać takie przypisanie:
(d, m, y) = (10, 12, 2004)

print("Day: " + str(d))
print("Month: " + str(m))
print("Year: " + str(y))


print("\n------------------------------------------------------------------\n")

print("03. Range (Zasięg)")
# Range w Pythonie jest wbudowaną funkcją, która służy do generowania sekwencji liczb całkowitych w określonym zakresie. W przeciwieństwie do listy lub krotki, range nie tworzy fizycznej listy wszystkich liczb w pamięci. Zamiast tego generuje liczby na żądanie, gdy są potrzebne, co pozwala na efektywne wykorzystanie pamięci, szczególnie przy dużych zakresach.
# Funkcja range ma trzy różne sygnatury:
    # range(stop): Generuje sekwencję liczb od 0 do stop - 1.
    # range(start, stop): Generuje sekwencję liczb od start do stop - 1.
    # range(start, stop, step): Generuje sekwencję liczb od start do stop - 1, z krokiem step.


print("\nExample 1:\n")

# Przykład 1:
for i in range(5):
    print(i)

# Wynik:
# 0
# 1
# 2
# 3
# 4

print("\nExample 2:\n")

# Przykład 2:
for i in range(2, 8):
    print(i)

# Wynik:
# 2
# 3
# 4
# 5
# 6
# 7

print("\nExample 4:\n")

# Przykład 3:
for i in range(1, 10, 2):
    print(i)

# Wynik:
# 1
# 3
# 5
# 7
# 9

print("\nExample 5:\n")

# Warto zauważyć, że obiekt range jest "leniwym" generatorem, co oznacza, że nie przechowuje wszystkich liczb w pamięci. Zamiast tego wylicza kolejne liczby na żądanie. Dzięki temu można wykorzystać range do iteracji przez duże zakresy liczb z minimalnym zużyciem pamięci.
# Jeśli potrzebujesz pełnej listy liczb z zakresu range, możesz użyć funkcji list() do przekształcenia obiektu range w listę:
list_of_numbers = list(range(1, 6))
print(list_of_numbers)  # Wyświetli: [1, 2, 3, 4, 5]
# Podsumowując, range jest funkcją do generowania sekwencji liczb całkowitych w określonym zakresie, ale nie jest to struktura danych podobna do listy. Zamiast tego, range to wydajny generator, który generuje liczby na żądanie.



