from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Route to view all licenses
@app.route('/admin/licenses', methods=['GET'])
def view_licenses():
    # Connect to the database
    conn = sqlite3.connect('licenses.db')
    c = conn.cursor()

    # Fetch all licenses from the database
    c.execute("SELECT * FROM licenses")
    licenses = c.fetchall()

    # Close the connection to the database
    conn.close()

    # Render the licenses.html template, passing the licenses to it
    return render_template('licenses.html', licenses=licenses)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
