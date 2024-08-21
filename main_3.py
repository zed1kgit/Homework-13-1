import threading
from random import randint
from time import sleep

numbers = []


def random_numbers(event_for_set):
    """Генерирует список из случайных чисел от 10 до 99"""
    for i in range(10):
        sleep(0.1)
        numbers.append(randint(10, 99))
    print(numbers)
    event_for_set.set()


def print_sum(event_for_wait):
    """Выводит сумму из сгенерированного списка"""
    event_for_wait.wait()
    print(f"Сумма - {sum(numbers)}")


def print_avg(event_for_wait):
    """Выводит среднеарифметическое из сгенерированного списка"""
    event_for_wait.wait()
    print(f"Среднеарифметическое - {sum(numbers) // len(numbers)}")


event = threading.Event()

thread_1 = threading.Thread(target=random_numbers, args=(event,))
thread_2 = threading.Thread(target=print_sum, args=(event,))
thread_3 = threading.Thread(target=print_avg, args=(event,))

thread_1.start()
thread_2.start()
thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()
