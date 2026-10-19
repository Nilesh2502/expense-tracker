import random
from datetime import datetime
from werkzeug.security import generate_password_hash
from database.db import get_db

def generate_indian_user():
    first_names = ["Rahul", "Anjali", "Arjun", "Priya", "Amit", "Sonia", "Vikram", "Kavita", "Rohan", "Deepika", "Sanjay", "Meera", "Aditya", "Ishani", "Karan", "Sneha"]
    last_names = ["Sharma", "Verma", "Gupta", "Malhotra", "Singh", "Iyer", "Reddy", "Patel", "Chatterjee", "Nair", "Joshi", "Kulkarni", "Yadav", "Mistra", "Deshmukh", "Choudhury"]

    first = random.choice(first_names)
    last = random.choice(last_names)
    name = f"{first} {last}"

    # Create email: first.last + random 2-3 digit suffix
    suffix = random.randint(10, 999)
    email = f"{first.lower()}.{last.lower()}{suffix}@gmail.com"

    return name, email

def seed_user():
    # Hashed password as per requirement
    password_hash = generate_password_hash("password123")
    created_at = datetime.now().isoformat()

    while True:
        name, email = generate_indian_user()

        with get_db() as conn:
            # Check if email exists
            exists = conn.execute("SELECT 1 FROM users WHERE email = ?", (email,)).fetchone()
            if not exists:
                # Insert user
                cursor = conn.execute(
                    "INSERT INTO users (name, email, password_hash, created_at) VALUES (?, ?, ?, ?)",
                    (name, email, password_hash, created_at)
                )
                conn.commit()

                print(f"Successfully seeded user:")
                print(f"id: {cursor.lastrowid}")
                print(f"name: {name}")
                print(f"email: {email}")
                break

if __name__ == "__main__":
    seed_user()
