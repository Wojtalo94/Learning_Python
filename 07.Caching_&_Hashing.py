# Zarówno cachowanie (keszowanie) jak i hashowanie (haszowanie) są narzędziami optymalizacyjnymi, które mogą znacznie poprawić wydajność i efektywność operacji w Pythonie.

print("01. Caching")

# Caching (keszowanie) jest techniką przechowywania wyników kosztownych obliczeń, aby uniknąć ich ponownego obliczania w przyszłości. W momencie, gdy funkcja otrzymuje te same argumenty, co wcześniej, zamiast wykonania obliczeń ponownie, po prostu zwróci wynik z wcześniej zapisanego "keszu" (cache'a). To może znacznie przyspieszyć działanie aplikacji, gdyż czasochłonne operacje nie muszą być wykonywane za każdym razem, gdy funkcja jest wywoływana z tymi samymi danymi wejściowymi.
# Oto prosty przykład cachowania z wykorzystaniem dekoratora functools.lru_cache, który jest wbudowany w Python:


from functools import lru_cache


@lru_cache(maxsize=None)
def expensive_calculation(n):
    print(f"Performing expensive calculation for {n}")
    return n * n


result1 = expensive_calculation(5)  # Pierwsze obliczenie, wyświetli "Performing expensive calculation for 5"
result2 = expensive_calculation(5)  # Odczyt wyniku z keszu, nie wykonuje ponownie kosztownego obliczenia

print("Result 1: " + str(result1))  # Output: 25
print("Result 2: " + str(result2))  # Output: 25

# Widzimy, że przy drugim wywołaniu funkcji expensive_calculation(5) wynik zostaje od razu pobrany z cache'a, a kosztowne obliczenia nie są ponawiane. Caching jest bardzo przydatny w przypadku funkcji, które mają kosztowne operacje, które są często wykonywane z tymi samymi argumentami.

print("\n------------------------------------------------------------------\n")

print("02. Hashing ")

# Hashing (haszowanie) to technika konwersji danych o różnych długościach na unikalny identyfikator o stałej długości, zwany haszem. Hasze są używane do identyfikowania i porównywania danych, a także do zapisywania danych w tzw. strukturach danych typu "hash table" (tablica haszująca).
# Haszowanie jest używane w wielu aspektach programowania, w tym do szybkiego wyszukiwania danych, porównywania danych, zabezpieczania haseł i wielu innych celów. W Pythonie można użyć funkcji hash() do uzyskania hasza dla obiektu.

data = "hello"
data_hash = hash(data)

print(f"Data: {data}")
print(f"Hash: {data_hash}")

# Hasze są używane do przyspieszania procesów wyszukiwania i porównywania danych, ponieważ umożliwiają szybkie odnalezienie odpowiedniego rekordu na podstawie jego unikalnego hasza, zamiast porównywania wszystkich elementów sekwencji.

# Podsumowując, zarówno caching (keszowanie) jak i hashing (haszowanie) są narzędziami optymalizacyjnymi, które pomagają zwiększyć wydajność i efektywność kodu Pythona. Caching pozwala na unikanie ponownego obliczania kosztownych operacji, a hashing pozwala na szybkie porównywanie i wyszukiwanie danych. Są to użyteczne techniki w sytuacjach, gdy liczy się wydajność i optymalizacja czasu wykonania programu.
