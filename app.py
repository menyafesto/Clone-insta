from flask import Flask, render_template
import os  # ← Bunu eklemeyi unutma

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f"Gelen kullanıcı adı: {username}")
        print(f"Gelen şifre: {password}")
        return f"Kullanıcı adı: {username}, Şifre: {password}"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
