import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # Create a dummy user table
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY, username TEXT, password TEXT, balance INTEGER)''')
    
    # Insert dummy data (The "Victims")
    c.execute("INSERT OR IGNORE INTO users (id, username, password, balance) VALUES (1, 'admin', 'supersecret', 1000)")
    c.execute("INSERT OR IGNORE INTO users (id, username, password, balance) VALUES (2, 'guest', 'guest123', 50)")
    c.execute("INSERT OR IGNORE INTO users (id, username, password, balance) VALUES (3, 'alice', 'alice123', 500)")
    
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully!")

if __name__ == "__main__":
    init_db()