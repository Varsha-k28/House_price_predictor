# 🏠 House Price Predictor

A Machine Learning web application that predicts house prices based on property features using the **Random Forest Regression** algorithm. The application is built with **Python, Flask, HTML, CSS, Bootstrap, and Scikit-learn** and provides instant house price predictions through a user-friendly web interface.

---

## 🚀 Live Demo

🔗 https://house-price-predictor-atgi.onrender.com

---

## 📌 Features

- Predict house prices instantly
- Random Forest Regression model
- Responsive user interface
- Real-time prediction
- Clean and modern design
- Mobile-friendly layout
- Built using Flask and Bootstrap

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Font Awesome

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Random Forest Regressor
- NumPy
- Joblib

## 📊 Dataset

The model is trained using the **Kaggle House Prices Dataset**, containing over **1,460 real-world housing records** with multiple property features.

Features used for prediction include:

- Overall Quality
- Living Area
- Garage Capacity
- Basement Area
- Number of Full Bathrooms
- Year Built


## 📷 Application Preview

### Home Page
<img src="static/images/image.png" width="800">


## 📁 Project Structure

```
House_price_predictor/
│
├── app.py
├── model.pkl
├── requirements.txt
├── Procfile
├── runtime.txt
│
├── static/
│   ├── css/
│   │     └── style.css
│   └── images/
│         ├── about-house.png
│         ├── house.jpg
│         ├── logo.png
│         └── image.png
│
└── templates/
      └── index.html
```

---

## ⚙️ Installation
Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/House_price_predictor.git
```

Move into the project directory

```bash
cd House_price_predictor
```

Create a virtual environment

```bash
python -m venv .venv
```
Activate the virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```
Open your browser

```
http://127.0.0.1:5000
```

## 📈 Machine Learning Model
**Algorithm Used**
- Random Forest Regression

**Model Accuracy**
- Approximately **89%**

## 🌐 Deployment
The application is deployed using **Render**.

**📜 License**

This project is developed for educational and portfolio purposes.
