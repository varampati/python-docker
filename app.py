from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!  Welcome to DevOps !! Course will be start very Sooooon!! '

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)

