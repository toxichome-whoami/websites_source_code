from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Setting the secret key

@app.route('/')
def hello_world():
    return render_template('toxic_home_website.html')

if __name__ == "__main__":
    app.run(debug=True)
