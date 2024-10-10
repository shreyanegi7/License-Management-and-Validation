import sqlite3
from cryptography.fernet import Fernet

# Initialize DB connection
conn = sqlite3.connect('licenses.db')
c = conn.cursor()

# Create licenses table
c.execute('''CREATE TABLE IF NOT EXISTS licenses
             (id INTEGER PRIMARY KEY, license_key TEXT, status TEXT)''')
conn.commit()

# Add a new license
def add_license(license_key, status='active'):
    encrypted_key = fernet.encrypt(license_key.encode()).decode()
    c.execute("INSERT INTO licenses (license_key, status) VALUES (?, ?)", (encrypted_key, status))
    conn.commit()

# Revoke a license
def revoke_license(license_key):
    encrypted_key = fernet.encrypt(license_key.encode()).decode()
    c.execute("UPDATE licenses SET status = 'revoked' WHERE license_key = ?", (encrypted_key,))
    conn.commit()

# Fetch a license (example usage)
def get_license(license_key):
    encrypted_key = fernet.encrypt(license_key.encode()).decode()
    c.execute("SELECT status FROM licenses WHERE license_key = ?", (encrypted_key,))
    return c.fetchone()

# Example of adding and revoking licenses
fernet = Fernet(Fernet.generate_key())
add_license("valid-license-key-123")
print(get_license("valid-license-key-123"))
revoke_license("valid-license-key-123")
print(get_license("valid-license-key-123"))
