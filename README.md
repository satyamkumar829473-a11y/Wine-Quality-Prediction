# Wine Quality Prediction

A Machine Learning-based web application that predicts the quality of wine based on its physicochemical properties. The project uses a trained Machine Learning model to estimate wine quality and provides predictions through a simple Flask web interface.

---

## Internship Project Details

- **Intern ID:** CITS1773
- **Name:** Satyam Kumar
- **Project Name:** Wine Quality Prediction
- **Project Duration:** 6 Weeks

---

## Project Overview

Wine quality prediction is an important application of Machine Learning in the food and beverage industry. This project analyzes various chemical properties of wine and predicts its quality using a trained Machine Learning model.

The application allows users to input wine characteristics and instantly receive a quality prediction.

---

## Features

- Predicts wine quality using Machine Learning
- User-friendly web interface
- Fast and accurate predictions
- Flask-based backend
- Responsive design
- Model training script included

---

## Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML5
- CSS3
- Pickle

---

## Project Structure

```
Wine-Quality-Prediction/
│
├── app.py
├── train_model.py
├── winequality.csv
├── wine_quality_model.pkl
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── images/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Wine-Quality-Prediction.git
cd Wine-Quality-Prediction
```

### Install Dependencies

```bash
pip install flask pandas numpy scikit-learn
```

### Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Model Training

To retrain the model:

```bash
python train_model.py
```

This generates:

- `wine_quality_model.pkl`

---

## Working Process

1. Enter the physicochemical properties of the wine.
2. Click the **Predict** button.
3. The input data is processed by the trained model.
4. The predicted wine quality score is displayed.

---

## Dataset

The project uses the **winequality.csv** dataset containing physicochemical properties of different wine samples for training and testing the model.

---

## Applications

- Wine Industry
- Quality Control
- Food & Beverage Analytics
- Research and Development
- Educational Machine Learning Projects

---

## Future Enhancements

- Improve prediction accuracy
- Support both Red