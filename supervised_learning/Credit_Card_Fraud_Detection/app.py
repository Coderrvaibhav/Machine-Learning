from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    user_input = request.form['user_input']
    return render_template('result.html', user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)
