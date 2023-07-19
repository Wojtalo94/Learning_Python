print("1) Obliczamy pole i obwód kwadratu")
# Przyjmijmy że bok jest równy 5
x = 5
print("Pole kwadratu o boku równym 5 wynosi: " + str(x*x))
print("Obwód kwadratu o boku równym 5 wynosi: " + str(x*4))

# Zmienna "x" przechowuje nam wartość "5" którą możemy wykorzystać, żeby ciągle nie zmieniać jej wszędzie, tylko w 1 miejscu. Ułatwia to i przyspiesza naprawę kodu.
# Aby to sobie wyobrazić, to puste pudełko nazwijmy x które może "coś przechowywać", a następnie wrzućmy do niego wartość "5".
# Powyższa procedura nosi nazwę "przypisanie".
# W języku programowania zapisujemy ją jak wcześniej, matematycznie czyli: x = 5
# W języku python, zmienne nie mają typów, czyli w nich możemy umieścić cokolwiek chcemy. Natomiast typy mają "znaczenia", a nie ma ich w "zmiennych". Czyli typ jest w wartości zmiennej (np. 5 lub 'string'), a nie w zmiennej.
# Zmieniając wartość zmiennej z "3" na na przykład "s", zmieniamy typ nie zmiennej lecz wartości zmiennej. Wartości takie mogą być pisane zarówno w cudzysłowach(") jak i w apostrofach (').

x = 's'
print("\nWartość x wynosi teraz: " + x + "\nA więc jest to wartość typu 'str'.")

#Jest możliwość utworzenia zmiennej, bez podawania wartości
x = None
print("\nWartość x wynosi teraz: " + str(x) + "\nA więc teraz zmienna " + str(x) + " jest bez typu wartości.")
