def measure_execution_time(func, *args, **kwargs):
    """
    Вимірює час виконання функції.
    
    :param func: Функція для вимірювання
    :param args: Аргументи для передачі у функцію
    :param kwargs: Іменовані аргументи для передачі у функцію
    :return: Результат виконання функції та час виконання
    """
    start_time = time_ns()  
    result = func(*args, **kwargs)
    end_time = time_ns()
    execution_time = (end_time - start_time) / 1_000_000_000  
    return result, execution_time

def time_ns():
    """
    Отримує поточний час у наносекундах.
    """
    return int(open("/proc/uptime", "r").read().split()[0].replace('.', '')) * 1_000_000

def test_function(n):
    total = 0
    for i in range(n):
        total += i
     