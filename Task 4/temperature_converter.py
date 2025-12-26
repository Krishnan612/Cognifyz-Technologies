def main():
    print("Temperature Converter")
    while True:
        choice = input("Choose: (1) C->F  (2) F->C  (q) Quit: ").strip().lower()
        if choice in ("q", "quit"):
            print("Goodbye!")
            break
        if choice not in ("1", "2"):
            print("Please enter 1, 2, or q.")
            continue
        val = input("Enter temperature: ").strip()
        try:
            t = float(val)
        except ValueError:
            print("That's not a valid number.")
            continue
        if choice == "1":
            r = t * 9 / 5 + 32
            print(f"{t} °C → {r:.2f} °F")
        else:
            r = (t - 32) * 5 / 9
            print(f"{t} °F → {r:.2f} °C")
        print()

if __name__ == '__main__':
    main()