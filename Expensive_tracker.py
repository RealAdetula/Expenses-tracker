import requests
import time
from datetime import datetime

def conversion(from_currency, to_currency="USD"):
    url = f"https://open.er-api.com/v6/latest/{from_currency}"
    
    try:
        response = requests.get(url)
        data = response.json()
    except:
        return None  # Network or API error

    if data.get("result") == "success":
        return data["rates"].get(to_currency)
    return None


def record_expenses():
    print("\n___Personal Expense Tracker___\n")

    Salary_earn = input("Enter Salary amount: ").strip()
    Currency_code = input("Enter your currency code (USD, NGN, EUR): ").strip().upper()
    amount = input("Enter expenses amount: ").strip()
    categories = input("Enter category (Food, transport, etc): ").strip()
    description = input("Enter description: ").strip()

    # Validate amount
    try:
        amount = float(amount)
    except ValueError:
        print("Amount must be a number.")
        return False

    if not amount or not categories:
        print("Expenses amount and category are required.")
        return False

    print(f"Amount recorded before deduction from salary: {Currency_code}{amount}")

    # Validate salary
    try:
        Salary_earn = float(Salary_earn)
    except ValueError:
        print("Salary must be a number.")
        return False

    # Convert to USD
    rate = conversion(Currency_code, "USD")

    if not rate:
        print("Couldn't get conversion rate")
        return False  

    Salary_usd = Salary_earn * rate
    amount_usd = amount * rate

    print(f"Your Salary in USD is: ${Salary_usd}")
    print(f"Expenses amount in USD: ${amount_usd}")

    print("\n___These are your details___")
    time.sleep(1)
    print(f"Expenses Amount: {Currency_code}{amount}")
    print(f"Category: {categories}")
    print(f"Description: {description}")

    # Date/Time
    date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    print(f"Date: {date}")

    # Remaining money
    savings = Salary_usd - amount_usd
    savings = round(savings, 2)

    print(f"Saving: ${savings}")

    # Save to file
    with open("tracker.txt", "a") as file:
        file.write(f"{date}  | {amount} | {categories} | {description}\n")

    print("Expense recorded successfully!")
    return True


def goodbye_message():
    print("\nThank you for using the Expense Tracker!")
    print("See you next time!")
    time.sleep(1)


def main():
    while True:
        success = record_expenses()

        if success:
            again = input("Add another expense? (y/n): ").lower().strip()
            yeah_keywords = ["yes", "y", "yeah", "ye"]

            if any(again == y for y in yeah_keywords):
                continue
            else:
                goodbye_message()
                break


if __name__ == "__main__":
    main()




    