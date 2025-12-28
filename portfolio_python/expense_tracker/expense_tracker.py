import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

def init_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "Category", "Amount", "Note"])
    except FileExistsError:
        pass


def add_expense():
    date = datetime.now().strftime("%y-%m-%d")
    category = input("Enter category (Food, travel, etc): ").strip()

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return
    
    note = input("Enter note (optional): ").strip()

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

    print("Expenses added successfully.")


def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        print("\nAll Expneses: ")
        for row in reader:
            print(f"{row[0]} | {row[1]} | ${row[2]} | {row[3]}")


def monthly_summary():
    month = input("Enter month (YYYY_MM): ").strip()
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[0].startswith(month):
                total += float(row[2])

    print(f"total expense for {month}: ${total}")

def category_summary():
    summary = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            category = row[1]
            amount = float(row[2])
            summary[category] = summary.get(category, 0) + amount
    
    print("\nCategory-wise Summary:")
    for cat, amt in summary.itmes():
        print(f"{cat}: ${amt}")


def main():
    init_file()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

