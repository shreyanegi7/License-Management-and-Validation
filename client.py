import requests
from cryptography.fernet import Fernet

# Use the generated key here
encryption_key = b'c4m3VAXbVh2BRzZ5MRp5Q5WoG68ZjKcZ3vD--9H5cP0='  # Example, replace with your generated key
fernet = Fernet(encryption_key)

# Encrypt license data using Fernet (symmetric encryption)
def encrypt_license(license_data):
    return fernet.encrypt(license_data.encode())

# Simulated client-side validator
def validate_license(license_key):
    url = "http://localhost:5000/validate"  # URL of the server
    encrypted_license = encrypt_license(license_key)
    response = requests.post(url, json={'license_key': encrypted_license.decode()})

    if response.status_code == 200:
        print("License is valid!")
    else:
        print("Invalid license!")

# Use a valid license key that matches what the server expects
license_key = "valid-license-key-123"  # Ensure this matches a valid key on the server

# Call the license validation (simulating the request)
validate_license(license_key)
