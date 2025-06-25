from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# -------- Database Initialization --------
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS voters (
            id TEXT PRIMARY KEY,
            name TEXT,
            voted INTEGER DEFAULT 0
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            votes INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# -------- Routes --------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if request.method == 'POST':
        name = request.form['name']
        voter_id = request.form['voter_id']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('SELECT * FROM voters WHERE id = ?', (voter_id,))
        user = c.fetchone()
        if user:
            if user[2] == 1:
                flash('ID already used for voting!')
                return redirect('/vote')
            else:
                return redirect(url_for('candidates', name=name, voter_id=voter_id))
        else:
            c.execute('INSERT INTO voters (id, name, voted) VALUES (?, ?, 0)', (voter_id, name))
            conn.commit()
            return redirect(url_for('candidates', name=name, voter_id=voter_id))
    return render_template('vote.html')

@app.route('/candidates')
def candidates():
    name = request.args.get('name')
    voter_id = request.args.get('voter_id')
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM candidates')
    candidates = c.fetchall()
    return render_template('candidates.html', candidates=candidates, name=name, voter_id=voter_id)

@app.route('/submit_vote', methods=['POST'])
def submit_vote():
    voter_id = request.form['voter_id']
    candidate_id = request.form['candidate']
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('UPDATE candidates SET votes = votes + 1 WHERE id = ?', (candidate_id,))
    c.execute('UPDATE voters SET voted = 1 WHERE id = ?', (voter_id,))
    conn.commit()
    conn.close()
    flash('Vote submitted successfully!')
    return redirect(url_for('index'))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        password = request.form['password']
        if password == 'admin123':
            return redirect('/admin_panel')
        else:
            flash('Wrong password!')
            return redirect('/admin')
    return render_template('admin_login.html')

@app.route('/admin_panel')
def admin_panel():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM candidates')
    candidates = c.fetchall()
    return render_template('admin_panel.html', candidates=candidates)

@app.route('/add_candidate', methods=['POST'])
def add_candidate():
    name = request.form['candidate_name']
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO candidates (name) VALUES (?)', (name,))
    conn.commit()
    return redirect('/admin_panel')

@app.route('/delete_candidate/<int:id>')
def delete_candidate(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('DELETE FROM candidates WHERE id = ?', (id,))
    conn.commit()
    return redirect('/admin_panel')

@app.route('/reset_votes')
def reset_votes():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('UPDATE candidates SET votes = 0')
    c.execute('UPDATE voters SET voted = 0')
    conn.commit()
    return redirect('/admin_panel')

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


