def arithmetic_sum(n):
    # перевіряємо число <= 0 то арифметическої прогресії буть не може і створюємо ValueError
    if n <= 0:
        raise ValueError("Incorrect number, must be > 0")

    # просто рахуємо арифметическу прогресію до n
    total = 1
    value = 3
    for i in range(n-1):
        total = total + value
    return total