import random
help(random)
for method in dir(random):
    print(method)

# seed - використовується для ініціалізації генератора випадкових чисел
# triangular - повертає випадкове плаваюче число між двома вказаними числами
# choices - повертає список із випадково вибраним елементом із зазначеної послідовності