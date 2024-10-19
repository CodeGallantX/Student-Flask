from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard/<name>')
def dashboard(name):
    return render_template('dashboard.html', name=name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        if user:
            return redirect(url_for('dashboard', name=user))
    else:
        return redirect(url_for('home'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)