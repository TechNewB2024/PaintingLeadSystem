import sqlite3
import datetime

BUSINESS_NAME = "Reliable Solutions Painting & Contracting"
TARGET_COUNTIES = ["Mason County", "Thurston County", "Kitsap County"]
CORE_SERVICE = "Residential & Commercial Painting (Interior/Exterior)"
TRAVEL_POLICY = "Free estimates in Mason County;  travel fee for Bremerton & Gig Harbor"

def init_db():
    conn = sqlite3.connect('painting_leads.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            county TEXT,
            client_name TEXT,
            phone TEXT,
            project_type TEXT,
            status TEXT,
            date_added TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("[INFO] Database 'painting_leads.db' initialized successfully. Cost: .00")

def display_campaign_targets():
    print("=" * 50)
    print(f"CAMPAIGN: {BUSINESS_NAME}")
    print(f"PRIMARY FOCUS: {CORE_SERVICE}")
    print(f"TERRITORIES: {', '.join(TARGET_COUNTIES)}")
    print(f"PRICING/POLICY: {TRAVEL_POLICY}")
    print("=" * 50)

if __name__ == '__main__':
    init_db()
    display_campaign_targets()
