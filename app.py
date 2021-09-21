from flask import Flask, render_template, Response
from main import test
from train import trains

app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video')
def video():
    return Response(test(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/training')
def training():
    return Response(trains(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)