import threading
from random import randint
from time import sleep

numbs_path = input()


def random_numbers(event_for_set):
    """Генерирует случайные числа от 1 до 15 в numbs_path"""
    sleep(0.1)
    with open(numbs_path, "w", encoding="utf-8") as fh:
        for _ in range(10):
            fh.write(f"{randint(1, 15)} ")
        event_for_set.set()


def read_file():
    """Читает числа из numbs_path и делает из них int список"""
    with open(numbs_path, "r", encoding="utf-8") as fh:
        numbs = list(map(lambda x: int(x), fh.read().split(" ")[:-1:]))
        return numbs


def create_prime_numbers(event_for_wait):
    """Создает файл prime_numbers.txt с простыми числами из numbs_path"""
    event_for_wait.wait()
    numbs = read_file()
    with open("prime_numbers.txt", "w", encoding="utf-8") as fh:
        for numb in numbs:
            for i in range(2, numb):
                if not numb % i:
                    break
            else:
                fh.write(f"{numb} ")


def create_factorial_numbers(event_for_wait):
    """Создает файл factorial_numbers.txt с факториалами чисел из numbs_path"""
    event_for_wait.wait()
    numbs = read_file()
    with open("factorial_numbers.txt", "w", encoding="utf-8") as fh:
        for numb in numbs:
            result = 1
            for i in range(2, numb + 1):
                result = result * i
            fh.write(f"{result} ")


event = threading.Event()

thread_1 = threading.Thread(target=random_numbers, args=(event, ))
thread_2 = threading.Thread(target=create_prime_numbers, args=(event, ))
thread_3 = threading.Thread(target=create_factorial_numbers, args=(event, ))

thread_1.start()
thread_2.start()
thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()
