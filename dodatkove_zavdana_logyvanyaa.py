def execution_time_decorator(func):
    """
    Декоратор для вимірювання часу виконання функції.

    :param func: Функція для декорування
    :return: Обгорнута функція
    """
    def wrapper(*args, **kwargs):
        start_time = time_ns()
        result = func(*args, **kwargs)
        end_time = time_ns()
        execution_time = (end_time - start_time) / 1_000_000_000 
        print(f"Функція '{func.__name__}' виконувалась {execution_time:.6f} секунд")
        return result
    return wrapper

def time_ns():
    """
    Отримує поточний час у наносекундах.
    """
    with open("/proc/uptime", "r") as f:
        uptime = float(f.read().split()[0])
    return int(uptime * 1_000_000_000)

@execution_time_decorator
def test_function_decorator(n):
    total = 0
    for i in range(n):
        total += i
    return total

result = test_function_decorator(10**6)
print(f"Результат: {result}")