# Marriage Age Prediction

This project is a web-based application designed to predict the likely age of marriage based on various user inputs like gender, religion, caste, mother tongue, country, and height. The app is developed using Flask for the backend, and it employs a pre-trained model to make predictions on user inputs.

### Developed by: Vigneshwar B.

---

## Project Structure

```
├── templates/
│   └── index.html             # HTML template for the home page
├── __pycache__/               # Directory for cached Python files
├── picklee/
│   └── model.pkl              # Serialized machine learning model file
├── marriage.csv               # Dataset for training
├── year_of_marriage.ipynb     # Jupyter notebook for model training and experimentation
├── app.py                     # Flask application script
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies
```

## Requirements

Install the necessary dependencies using:

```bash
pip install -r requirements.txt
```

## Libraries and Frameworks Used

- **Flask** for building the web application
- **Pickle** for model serialization and deserialization
- **Flask-CORS** to allow cross-origin requests

## Dataset

The dataset `marriage.csv` was used to train the model, containing attributes such as gender, religion, caste, mother tongue, country, and height.

## Model Training

Model training and evaluation were done in `year_of_marriage.ipynb`. The model was saved as `model.pkl` in the `picklee` folder.

## Web App

The Flask web application provides a user-friendly interface for making predictions. The app routes are defined as follows:

- **Homepage** (`/`): Displays the input form for marriage age prediction.
- **Predict Page** (`/predict`): Predicts and returns the estimated marriage age based on user inputs.

### Running the App

To run the app locally, use:

```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000`.

## Usage

1. Go to the homepage and enter values for gender, religion, caste, mother tongue, country, and height.
2. Submit the form to receive an estimated marriage age.

---
