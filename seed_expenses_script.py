import random
import sqlite3
from datetime import datetime, timedelta
from database.db import get_db

def seed_expenses(user_id, count, months):
    categories = {
        "Food": {"range": (50, 800), "weight": 30, "desc": ["Swiggy order", "Zomato dinner", "Grocery from Blinkit", "Street food", "Tea and snacks"]},
        "Transport": {"range": (20, 500), "weight": 20, "desc": ["Auto rickshaw", "Uber ride", "Petrol refill", "Metro recharge", "Ola cab"]},
        "Bills": {"range": (200, 3000), "weight": 15, "desc": ["Electricity bill", "Water bill", "WiFi recharge", "Phone bill", "Rent payment"]},
        "Health": {"range": (100, 2000), "weight": 5, "desc": ["Pharmacy meds", "Doctor consultation", "Health checkup", "Vitamin supplements", "Dental clinic"]},
        "Entertainment": {"range": (100, 1500), "weight": 5, "desc": ["Movie ticket", "Netflix subscription", "Gaming zone", "Bowling", "Concert ticket"]},
        "Shopping": {"range": (200, 5000), "weight": 15, "desc": ["Amazon purchase", "Myntra clothes", "Shopper's Stop", "New shoes", "Electronics accessory"]},
        "Other": {"range": (50, 1000), "weight": 10, "desc": ["Gift for friend", "Donation", "Laundry service", "Stationery", "Miscellaneous"]}
    }

    cat_names = list(categories.keys())
    weights = [categories[c]["weight"] for c in cat_names]

    conn = get_db()
    try:
        cursor = conn.cursor()

        expenses_to_insert = []
        dates = []

        for _ in range(count):
            category = random.choices(cat_names, weights=weights)[0]
            amount = round(random.uniform(*categories[category]["range"]), 2)
            description = random.choice(categories[category]["desc"])

            # Random date within the last 'months' months
            days_back = random.randint(0, months * 30)
            date_obj = datetime.now() - timedelta(days=days_back)
            date_str = date_obj.strftime("%Y-%m-%d")

            expenses_to_insert.append((user_id, amount, category, date_str, description))
            dates.append(date_str)

        cursor.executemany(
            "INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
            expenses_to_insert
        )
        conn.commit()

        # Verification sample
        cursor.execute(
            "SELECT amount, category, date, description FROM expenses WHERE user_id = ? ORDER BY id DESC LIMIT 5",
            (user_id,)
        )
        sample = cursor.fetchall()

        print(f"Successfully inserted {count} expenses.")
        print(f"Date range: {min(dates)} to {max(dates)}")
        print("\nSample records:")
        for row in sample:
            print(f"₹{row['amount']} | {row['category']} | {row['date']} | {row['description']}")

    except Exception as e:
        conn.rollback()
        print(f"Error occurred: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    seed_expenses(2, 3, 5)
