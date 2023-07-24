from math import sqrt

#  napiszemy funkcję w języku Python, która akurat będzie rozwiązywać równanie kwadratowe. Jako parametry będą udzielać się trzy liczby: a, b, c. To współczynniki do odpowiednich członków równania kwadratowego. A jako wynik będzie ona wyświetlać w konsoli rozwiązanie tego równania kwadratowego. Będziemy ją testować w trzech wariantach:
# x2 + x + 1   --> pierwszy przypadek, współczynniki 1, 1, 1 - brak rozwiązania
# x2 + 2x + 1 --> drugi przypadek, współczynniki 1, 2, 1 - jedno rozwiązanie
# x2 + 5x + 6 --> trzeci przypadek, współczynniki 1, 5, 6 - dwa rozwiązania

# stwórzmy metodę o nazwie solve. Na wejściu  będzie ona przyjmować trzy parametry, a, b, c.
def solve(a, b, c):
    # Zaczynami pisać realizację. Najpierw wyliczamy deltę
    d = b*b - 4*a*c
    # Niezależnie od wyniku funkcji, będziemy mieć różne warianty postępowania. Więc musimy zacząć od słowa if, i jeśli delta (d) jest mniejsza od zera (< 0), a to dokładnie tak samo jak w definiowaniu funkcji, na końcu warunku wstawiamy dwukropek (:), to znaczy że dalej zaczyna się nowy blok.
    if d < 0:
        # Wracając d < 0 to pierwszy przypadek, a więc brak rozwiązania
        print("No solutions.")
        # Teraz kolejny przypadek. Użyliśmy słowo if, teraz należy użyć słowo elif Dalej nadchodzi blok kodu alternatywnego. Ten który dokonuje się w przypadku, gdy dyskryminanta nie jest mniejsza od zera (>0). Wychodzi nam słowo kluczowe elif, które jest skrótem od else i if.
    elif d == 0:
        x = -b / (2*a)
        print("One solution: " + str(x))
    # Jeżeli ani pierwszy warunek if d < 0, ani drugi elif d == 0 nie dokonał się, to w tedy w tedy trafiamy do ostaniego trzeciego bloku else
    else:
        x1 = (-b + sqrt(d)) / (2*a)
        x2 = (-b - sqrt(d)) / (2*a)
        print("Two solutions:" + str(x1) + " and " + str(x2))


# Trzy takie kwadratowe równania będzie rozwiązywać nasza funkcja i powinna wydać trzy różne wyniki.
solve(1, 1, 1)
solve(1, 2, 1)
solve(1, 5, 6)











