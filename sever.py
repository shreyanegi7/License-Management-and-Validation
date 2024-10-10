from flask import Flask, render_template
from models import db, License

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///licenses.db'
db.init_app(app)

# Route to view licenses (Admin Interface)
@app.route('/admin/licenses', methods=['GET'])
def view_licenses():
    print("Route /admin/licenses accessed")  # Debug print
    licenses = License.query.all()
    return render_template('licenses.html', licenses=licenses)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
