import sqlite3

def view_all_leads():
    conn = sqlite3.connect('painting_leads.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, county, client_name, phone, service_requested, status, date_added FROM leads')
    leads = cursor.fetchall()
    conn.close()

    print("=" * 80)
    print(f"{'ID':<4} | {'County':<15} | {'Client Name':<20} | {'Phone':<15} | {'Service Requested'}")
    print("-" * 80)
    for lead in leads:
        print(f"{lead[0]:<4} | {lead[1]:<15} | {lead[2]:<20} | {lead[3]:<15} | {lead[4]}")
    print("=" * 80)

if __name__ == '__main__':
    view_all_leads()
