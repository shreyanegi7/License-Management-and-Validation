from crud_operations import add_license, get_all_licenses, update_license, delete_license
from models import app

with app.app_context():
    # Add a license
    add_license('valid-license-key-123')

    # Read licenses
    licenses = get_all_licenses()
    print("All Licenses:", licenses)

    # Update a license
    update_license('valid-license-key-123', 'revoked')
    print("Updated Licenses:", get_all_licenses())

    # Delete a license
    delete_license('valid-license-key-123')
    print("All Licenses after deletion:", get_all_licenses())
