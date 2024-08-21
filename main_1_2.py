import threading

numbers = []
print("Введите 5 чисел:")
for i in range(5):
    x = input()
    numbers.append(x)


def print_max(event_for_wait, event_for_set):
    """Выводит максимальное число из введенного списка"""
    for _ in range(5):
        event_for_wait.wait()
        event_for_wait.clear()
        print(f"Максимум - {max(numbers)}")
        event_for_set.set()


def print_min(event_for_wait, event_for_set):
    """Выводит минимальное число из введенного списка"""
    for _ in range(5):
        event_for_wait.wait()
        event_for_wait.clear()
        print(f"Минимум - {min(numbers)}")
        event_for_set.set()


event1 = threading.Event()
event2 = threading.Event()

thread_1 = threading.Thread(target=print_max, args=(event1, event2))
thread_2 = threading.Thread(target=print_min, args=(event2, event1))

thread_1.start()
thread_2.start()

event1.set()

thread_1.join()
thread_2.join()
