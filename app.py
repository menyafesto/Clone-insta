from flask import Flask, request, render_template

app = Flask(__name__)

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
