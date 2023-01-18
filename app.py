import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(
  open(
    "build_pipeline.pkl",
    "rb"
  )
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    """
    For rendering results on HTML GUI
    """
    final_features = [x for x in request.form.values()]
    prediction = model.predict(final_features)

    output = prediction[0]

    return render_template(
        "index.html", prediction_text="Loan Approval Status: {}".format(output)
    )


if __name__ == "__main__":
    app.run(debug=True)
