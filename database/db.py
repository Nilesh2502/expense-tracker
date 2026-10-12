import sqlite3
from werkzeug.security import generate_password_hash

DATABASE = "spendly.db"

def get_db():
    """Returns a SQLite connection with row_factory and foreign keys enabled."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    """Creates all tables using CREATE TABLE IF NOT EXISTS."""
    with get_db() as conn:
        # Users table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Expenses table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL,
                description TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        conn.commit()

def seed_db():
    """Inserts sample data for development if the database is empty."""
    with get_db() as conn:
        # Check if users already exist to prevent duplication
        user_count = conn.execute("SELECT count(*) FROM users").fetchone()[0]
        if user_count > 0:
            return

        # Insert demo user
        demo_password = generate_password_hash("demo123")
        cursor = conn.execute(
            "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
            ("Demo User", "demo@spendly.com", demo_password)
        )
        user_id = cursor.lastrowid

        # Fixed categories list
        categories = ["Food", "Transport", "Bills", "Health", "Entertainment", "Shopping", "Other"]

        # Sample expenses (8 items, covering all categories)
        sample_expenses = [
            (user_id, 12.50, "Food", "2026-10-01", "Lunch at cafe"),
            (user_id, 45.00, "Transport", "2026-10-02", "Weekly gas"),
            (user_id, 120.00, "Bills", "2026-10-03", "Internet bill"),
            (user_id, 30.00, "Health", "2026-10-05", "Pharmacy"),
            (user_id, 15.00, "Entertainment", "2026-10-07", "Movie ticket"),
            (user_id, 60.00, "Shopping", "2026-10-10", "New shirt"),
            (user_id, 5.00, "Other", "2026-10-11", "Parking fee"),
            (user_id, 22.00, "Food", "2026-10-12", "Dinner"),
        ]

        conn.executemany(
            "INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
            sample_expenses
        )
        conn.commit()
