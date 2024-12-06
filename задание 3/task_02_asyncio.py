import asyncio
import time
import math

# Функции для АТ-03

async def fibonacci(n):  # содержимое функции не менять
    """Возвращает последнюю цифру n-го числа Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(f'fibonacci = {b % 10}')
    return b % 10

async def trapezoidal_rule(f, a, b, n):  # содержимое функции не менять
    """Вычисляет определенный интеграл функции f от a до b методом трапеций с n шагами."""
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        integral += f(a + i * h)
    print(f'trapezoidal_rule = {integral * h}')
    return integral * h

async def main():
    start_time = time.perf_counter()

    # Создаем задачи для асинхронного выполнения
    fib_task = asyncio.create_task(fibonacci(700003))
    trap_task = asyncio.create_task(trapezoidal_rule(math.sin, 0, math.pi, 20000000))

    # Ожидаем завершения обеих задач
    await fib_task
    await trap_task

    end_time = time.perf_counter()
    print(f'processes time: {end_time - start_time:0.2f} seconds\n')

if __name__ == '__main__':
    asyncio.run(main())
