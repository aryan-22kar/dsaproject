"""
DSA Algorithms Toolkit
A beginner-friendly, menu-driven Python 3 project.

Features:
1. Linear Search
2. Binary Search (sorts input first)
3. Bubble Sort
4. Selection Sort
5. Insertion Sort
6. Balanced Bracket Checker
7. Duplicate Removal (preserves first-seen order)
"""

def read_integers():
    """Read a space-separated list of integers from the user."""
    raw = input("Enter integers separated by spaces: ").strip()
    if not raw:
        return []
    try:
        return [int(item) for item in raw.split()]
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")
        return None


def linear_search(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def binary_search(values, target):
    """Binary search on a sorted copy of values."""
    sorted_values = sorted(values)
    low, high = 0, len(sorted_values) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_values[mid] == target:
            return mid, sorted_values
        if sorted_values[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, sorted_values


def bubble_sort(values):
    result = values.copy()
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


def selection_sort(values):
    result = values.copy()
    n = len(result)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if result[j] < result[min_index]:
                min_index = j
        result[i], result[min_index] = result[min_index], result[i]
    return result


def insertion_sort(values):
    result = values.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def balanced_brackets(expression):
    pairs = {")": "(", "]": "[", "}": "{"}
    opening = set(pairs.values())
    stack = []

    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack


def remove_duplicates(values):
    seen = set()
    result = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def show_menu():
    print("\\n========== DSA ALGORITHMS TOOLKIT ==========")
    print("1. Linear Search")
    print("2. Binary Search (sorts input first)")
    print("3. Bubble Sort")
    print("4. Selection Sort")
    print("5. Insertion Sort")
    print("6. Balanced Bracket Checker")
    print("7. Remove Duplicates")
    print("0. Exit")
    print("============================================")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Thank you for using DSA Algorithms Toolkit!")
            break

        if choice in {"1", "2", "3", "4", "5", "7"}:
            values = read_integers()
            if values is None:
                continue

            if choice == "1":
                try:
                    target = int(input("Enter the value to search for: "))
                except ValueError:
                    print("Invalid target. Please enter an integer.")
                    continue
                index = linear_search(values, target)
                if index == -1:
                    print("Value not found.")
                else:
                    print(f"Value found at index {index} (0-based index).")

            elif choice == "2":
                try:
                    target = int(input("Enter the value to search for: "))
                except ValueError:
                    print("Invalid target. Please enter an integer.")
                    continue
                index, sorted_values = binary_search(values, target)
                print("Sorted input:", sorted_values)
                if index == -1:
                    print("Value not found.")
                else:
                    print(f"Value found in sorted list at index {index} (0-based index).")

            elif choice == "3":
                print("Sorted:", bubble_sort(values))

            elif choice == "4":
                print("Sorted:", selection_sort(values))

            elif choice == "5":
                print("Sorted:", insertion_sort(values))

            elif choice == "7":
                print("After duplicate removal:", remove_duplicates(values))

        elif choice == "6":
            expression = input("Enter an expression containing brackets: ")
            if balanced_brackets(expression):
                print("Brackets are balanced.")
            else:
                print("Brackets are not balanced.")

        else:
            print("Invalid option. Please choose an option from the menu.")


if __name__ == "__main__":
    main()
