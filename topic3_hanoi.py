"""Тема 3. Ханойські башти (рекурсія)."""


def hanoi(n: int, source: str, target: str, auxiliary: str, state: dict) -> None:
    if n == 0:
        return
    hanoi(n - 1, source, auxiliary, target, state)
    disk = state[source].pop()
    state[target].append(disk)
    print(f"Перемістити диск з {source} на {target}: {disk}")
    print(f"Проміжний стан: {state}")
    hanoi(n - 1, auxiliary, target, source, state)


def main() -> None:
    n = int(input("Кількість дисків: "))
    state = {"A": list(range(n, 0, -1)), "B": [], "C": []}
    print(f"Початковий стан: {state}")
    hanoi(n, "A", "C", "B", state)
    print(f"Кінцевий стан: {state}")


if __name__ == "__main__":
    main()
