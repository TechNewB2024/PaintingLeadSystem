import sqlite3
import datetime

def init_db():
    conn = sqlite3.connect('painting_leads.db')
    cursor = conn.cursor()
    # Recreate table with correct schema matching service_requested
    cursor.execute('DROP TABLE IF EXISTS leads')
    cursor.execute('''
        CREATE TABLE leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            county TEXT,
            client_name TEXT,
            phone TEXT,
            service_requested TEXT,
            status TEXT,
            date_added TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_lead(county, client_name, phone, service_requested):
    init_db() # Ensure schema is fresh and matched
    conn = sqlite3.connect('painting_leads.db')
    cursor = conn.cursor()
    date_added = datetime.date.today().isoformat()
    cursor.execute('''
        INSERT INTO leads (county, client_name, phone, service_requested, status, date_added)
        VALUES (?, ?, ?, ?, 'New', ?)
    ''', (county, client_name, phone, service_requested, date_added))
    conn.commit()
    conn.close()
    print(f"[SUCCESS] Logged lead for {client_name} in {county} ({service_requested}). Cost: .00")

if __name__ == '__main__':
    log_lead("Mason County", "Sample Homeowner", "360-555-0199", "Deck Staining & Exterior Painting")
