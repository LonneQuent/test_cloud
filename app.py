from flask import Flask

# Initialize Flask App
app = Flask(__name__)

# Main route
@app.route('/', methods=['GET'])
def main_route():
    return 'Hello World'

# Hetic route
@app.route('/hetic', methods=['GET'])
def hetic_route():
    return 'Hello Hetic'

if __name__ == '__main__':
    app.run("0.0.0.0", port=9999)
