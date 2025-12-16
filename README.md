# Car Price Prediction App

A Machine Learning web application that predicts the market price of a used car based on its specifications (make, model, year, engine, etc.).

🔗 **Live Demo:** [https://car-price-predictor-xeeh.onrender.com](https://car-price-predictor-xeeh.onrender.com)

## 🛠 Tech Stack
* **Python 3.9**
* **Scikit-Learn** (Random Forest Regressor)
* **Streamlit** (Frontend)
* **Pandas** (Data Processing)
* **Docker** (Containerization)
* **Render** (Cloud Deployment)

## Project Structure

* `EDA.ipynb` - Jupyter Notebook containing Exploratory Data Analysis (EDA), data cleaning, feature engineering, and model training/tuning.
* `app.py` - The main Python script that runs the Streamlit web application.
* `predict_test.py` - A standalone script to test the model's prediction logic without the web interface.
* `load_data.py` - Utility script to download the raw dataset from the source URL.
* `Dockerfile` - Configuration file for building the Docker image.
* `requirements.txt` - List of Python dependencies required to run the project.
* `model_C=1.0.bin` - The saved trained model and vectorizer (Pickle file).
* `used_cars.csv` - The dataset used for dropdown menus in the app.

## Project Features
* **Smart Imputation:** Handles missing values for engine HP and other features.
* **Dynamic UI:** Dependent dropdowns (selecting 'BMW' filters models to show only BMW cars).
* **Model Performance:** Achieved RMSE ~0.117 (approx. 11% error rate) on test data.

## How to Run Locally

### Option 1 (using Docker)
```bash
docker build -t car-price-app .
docker run -p 8501:8501 car-price-app
```


### Option 2 (if you don't have Docker installed)
```bash
pip install -r requirements.txt
streamlit run app.py