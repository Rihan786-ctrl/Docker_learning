from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>My Flask App</title>
</head>
<body>
    <h1>Welcome to My Flask App</h1>
    <p>This is a simple Flask application.</p>
    <form action="/submit" method="post">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name">
        <input type="submit" value="Submit">
    </form>
</body>
</html>
'''

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f'<h1>Hello, {name}, Welcome to this app for Docker demonstartion. please enjoy!</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)