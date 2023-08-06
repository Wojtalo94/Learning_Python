# Specjalna konstrukcja lambda w Pythonie odnosi się do funkcji anonimowej, czyli funkcji bez nazwy. Jest to bardzo krótka funkcja, która może zawierać tylko jedno wyrażenie. Są tworzone za pomocą wyrażenia lambda, które pozwala na zdefiniowanie funkcji bez potrzeby nadawania jej nazwy.
# Składnia wyrażenia lambda jest następująca:

# lambda arguments: expression
# Gdzie arguments to lista argumentów, a expression to pojedyncze wyrażenie, które zostanie obliczone i zwrócone przez funkcję.

# Przykłady użycia konstrukcji lambda:

print("\nExample 1. Adding two numbers:\n")
add = lambda x, y: x + y
print(add(3, 5))  # Wynik: 8

print("\nExample 2. Calculating the square of a number:\n")
square = lambda x: x**2
print(square(4))  # Wynik: 16

print("\nExample 3. Sorting a list of numbers based on the last digit:\n")
numbers = [23, 11, 56, 7, 89]
sorted_numbers = sorted(numbers, key=lambda x: x % 10)
print(sorted_numbers)  # Wynik: [11, 23, 56, 7, 89]

print("\nExample 4. Filtering even numbers from a list:\n")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Wynik: [2, 4, 6, 8, 10]

# Warto pamiętać, że konstrukcje lambda są przydatne w prostych przypadkach, gdy funkcja jest krótka i jednorazowego użytku. W bardziej złożonych przypadkach lepiej jest użyć zwykłych funkcji zdefiniowanych za pomocą def, które pozwalają na bardziej rozbudowaną logikę i większą czytelność kodu
