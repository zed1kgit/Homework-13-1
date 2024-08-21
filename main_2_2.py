import threading

numbers = []
print("Введите 5 чисел:")
for i in range(5):
    x = input()
    numbers.append(int(x))


def print_sum(event_for_wait, event_for_set):
    """Выводит сумму из введенного списка"""
    for _ in range(5):
        event_for_wait.wait()
        event_for_wait.clear()
        print(f"Сумма - {sum(numbers)}")
        event_for_set.set()


def print_avg(event_for_wait, event_for_set):
    """Выводит среднеарифметическое из введенного списка"""
    for _ in range(5):
        event_for_wait.wait()
        event_for_wait.clear()
        print(f"Среднеарифметическое - {sum(numbers) // len(numbers)}")
        event_for_set.set()


event1 = threading.Event()
event2 = threading.Event()

thread_1 = threading.Thread(target=print_sum, args=(event1, event2))
thread_2 = threading.Thread(target=print_avg, args=(event2, event1))

thread_1.start()
thread_2.start()

event1.set()

thread_1.join()
thread_2.join()
