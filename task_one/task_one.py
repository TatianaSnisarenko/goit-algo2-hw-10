import random
import timeit
import matplotlib.pyplot as plt


def randomized_quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


def measure_execution_time():
    sizes = [10_000, 50_000, 100_000, 500_000]
    results_randomized = []
    results_deterministic = []

    for size in sizes:
        arr = [random.randint(0, 1_000_000) for _ in range(size)]

        randomized_time = timeit.timeit(
            stmt="randomized_quick_sort(arr.copy())",
            globals={"randomized_quick_sort": randomized_quick_sort, "arr": arr},
            number=5,
        )
        results_randomized.append(randomized_time / 5)

        deterministic_time = timeit.timeit(
            stmt="deterministic_quick_sort(arr.copy())",
            globals={"deterministic_quick_sort": deterministic_quick_sort, "arr": arr},
            number=5,
        )
        results_deterministic.append(deterministic_time / 5)

    for i, size in enumerate(sizes):
        print(f"Розмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {results_randomized[i]:.4f} секунд")
        print(f"   Детермінований QuickSort: {results_deterministic[i]:.4f} секунд")
        print()

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, results_randomized, label="Рандомізований QuickSort", marker="o")
    plt.plot(sizes, results_deterministic, label="Детермінований QuickSort", marker="o")
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунди)")
    plt.title("Порівняння рандомізованого та детермінованого QuickSort")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    measure_execution_time()
