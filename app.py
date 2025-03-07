from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('database/routes.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home page, shows all routes
@app.route('/')
def index():
    conn = get_db_connection()
    routes = conn.execute('SELECT * FROM routes').fetchall()
    conn.close()
    return render_template('index.html', routes=routes)

# Add a new route
@app.route('/add', methods=['GET', 'POST'])
def add_route():
    if request.method == 'POST':
        name = request.form['name']
        difficulty = request.form['difficulty']
        conn = get_db_connection()
        conn.execute('INSERT INTO routes (name, difficulty, status) VALUES (?, ?, ?)', 
                     (name, difficulty, 'active'))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_route.html')

# Mark a route as removed
@app.route('/remove/<int:id>')
def remove_route(id):
    conn = get_db_connection()
    conn.execute('UPDATE routes SET status = ? WHERE id = ?', ('removed', id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
