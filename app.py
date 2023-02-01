from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect("samplestores1.db")
    c = conn.cursor()
    c.execute("SELECT * FROM samples")
    samples = c.fetchall()
    conn.close()
    return render_template("index.html", samples=samples)

if __name__ == "__main__":
    app.run(debug=True)
