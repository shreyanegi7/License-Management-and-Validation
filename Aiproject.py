from models import db, License  # Import db and the License model

# Create a new license
def add_license(license_key, status='active'):
    new_license = License(license_key=license_key, status=status)
    db.session.add(new_license)
    db.session.commit()

# Read licenses
def get_all_licenses():
    return License.query.all()  # Returns a list of all licenses

def get_license_by_key(license_key):
    return License.query.filter_by(license_key=license_key).first()

# Update a license
def update_license(license_key, new_status):
    license_to_update = get_license_by_key(license_key)
    if license_to_update:
        license_to_update.status = new_status
        db.session.commit()
        return True
    return False

# Delete a license
def delete_license(license_key):
    license_to_delete = get_license_by_key(license_key)
    if license_to_delete:
        db.session.delete(license_to_delete)
        db.session.commit()
        return True
    return False
