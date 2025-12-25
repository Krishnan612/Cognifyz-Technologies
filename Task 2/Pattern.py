def palindromic_pyramid(n: int) -> None:
        for i in range(n):
            print(" " * (n-i-1),"*" * (2*i+1))
def incremental_number_pattern(n: int) -> None:
     for i in range(1,n+1):
        print('*' * i)
def decremental_number_pattern(n: int) -> None:
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print('*', end=' ')
        print()
def inverted_pyramid(n: int) -> None:
    for i in range(n):
        print(" " * i + "*" * (2 * (n - i) - 1))

if __name__ == "__main__":
    rows = int(input("Number of rows: ").strip())
    type_of_pattern = input("Type of pattern (Pyramid=1/Incremental=2/Decremental=3/Inverted pyramid=4): ").strip().lower()
    match type_of_pattern:
        case "1":
            palindromic_pyramid(rows)
        case "2":
            incremental_number_pattern(rows)
        case "3":
            decremental_number_pattern(rows)
        case "4":
            inverted_pyramid(rows)
        case _:
            print("Invalid pattern type. Please choose Correctly.")