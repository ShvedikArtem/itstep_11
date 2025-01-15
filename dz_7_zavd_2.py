result = []

def divider(a, b):
    if a < b:
        raise ValueError("Число a має бути більше або рівне b")
    if b > 100:
        raise IndexError("Число b не може бути більше 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4} 

for key in data:
    try:
        res = divider(int(key), data[key])  
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError, TypeError) as e:
        print(f"Помилка з елементом {key}:{data[key]} - {e}")

print(result)

def calculate(expression):
    return eval(expression)

def calculator_decorator(func):
    def wrapper(expression):
        try:
            allowed_chars = "0123456789+-*/()"  
            if not all(char in allowed_chars for char in expression):
                raise ValueError("Вираз містить недопустимі символи")
            return func(expression)
        except ZeroDivisionError:
            return "Помилка: ділення на нуль"
        except SyntaxError:
            return "Помилка: неправильний синтаксис виразу"
        except Exception as e:
            return f"Помилка: {e}"
    return wrapper

calculate = calculator_decorator(calculate)  

print(calculate("10 + 5 * 2"))
print(calculate("10 / 0"))
print(calculate("10 + abc"))
print(calculate("10 + (5 * 2)"))