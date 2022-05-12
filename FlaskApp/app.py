from flask import Flask, request, render_template
from title_preparation import *
import pickle


with open(f'model.pkl', 'rb') as file:
    model = pickle.load(file)

# Create flask app
flask_app = Flask(__name__)


@flask_app.route("/")
def home():
    return render_template("index.html")


@flask_app.route("/predict", methods=["POST"])
def predict():
    title = [*request.form.values()][0]
    title_data = title_to_data(title)
    prediction = model.predict(title_data)[0]

    # return {"results": prediction}
    return render_template("index.html", prediction_text=f"Predicted category - {prediction}, for the title: {title}\n")


@flask_app.route("/test")
def test_ok():
    return {"result": "ok"}


if __name__ == "__main__":
    flask_app.run(debug=True)
