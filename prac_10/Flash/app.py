from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/greet')
@app.route('/greet/Mitchell')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f')
@app.route('/f/<int:celsius>')
def convert_celsius_to_fahrenheit(celsius=""):
    """Convert celsius to fahrenheit."""
    return "{:.2f}".format(int(celsius) * 9.0 / 5 + 32)


@app.route('/c/')
@app.route('/c/<int:fahrenheit>')
def convert_fahrenheit_to_celsius(fahrenheit=""):
    """Convert fahrenheit to celsius."""
    return "{:.2f}".format(5 / 9 * (int(fahrenheit) - 32))


if __name__ == '__main__':
    app.run()
