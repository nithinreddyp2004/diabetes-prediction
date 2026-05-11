# 🩺 Diabetes Prediction App

A machine learning web application that predicts whether a patient is diabetic based on medical diagnostic measurements. Built with Python, Scikit-learn, and deployed using Streamlit.

---

## 🚀 Live Demo

👉 **[Click here to try the live app!](https://diabetes-prediction-23.streamlit.app/)**

> Deployed on Streamlit Cloud

---

## 📌 Problem Statement

Diabetes affects over 400 million people worldwide. Early detection is critical for treatment and prevention of complications. This app allows patients and doctors to quickly assess diabetes risk based on simple medical inputs.

---

## 🔧 Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Pandas & NumPy | Data manipulation and analysis |
| Matplotlib & Seaborn | Data visualization and EDA |
| Scikit-learn | Machine learning model building |
| Streamlit | Web app deployment |
| Pickle | Model saving and loading |

---

## 📊 Dataset

- **Source:** PIMA Indians Diabetes Dataset (UCI Machine Learning Repository)
- **Records:** 768 patients
- **Features:** 8 medical features (Glucose, BMI, Age, Insulin, Blood Pressure, etc.)
- **Target:** Diabetic (1) or Not Diabetic (0)

---

## 🧪 ML Pipeline

1. **Exploratory Data Analysis (EDA)** — Analyzed feature distributions and correlations
2. **Data Preprocessing** — Handled zero values (invalid medical readings), scaled features
3. **Feature Selection** — Identified most important predictors of diabetes
4. **Model Building** — Trained and evaluated:
   - Logistic Regression
5. **Model Evaluation** — Accuracy, Confusion Matrix, Classification Report
6. **Deployment** — Saved model as `.pkl` and built interactive Streamlit app

---

## 📈 Model Performance

| Model | Accuracy |
|-------|----------|
| Logistic Regression | ~78% |

---

## 🖥️ How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/nithinreddyp2004/diabetes-prediction.git

# 2. Navigate to the project folder
cd diabetes-prediction

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py
```

---

## 📁 Project Structure

```
diabetes-prediction/
│
├── model_training.ipynb     # Jupyter notebook with EDA and model training
├── app.py                   # Streamlit web application
├── model_logistic.pkl       # Saved trained model
├── diabetes.csv             # Dataset
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🔍 Key Insights from EDA

- **Glucose level** is the strongest predictor of diabetes
- Patients with **higher BMI** are at greater risk
- **Age** above 45 shows significantly higher diabetes rates
- **Insulin levels** show high variance — requires careful handling

---

## 🩺 Input Features Used

| Feature | Description |
|---------|-------------|
| Pregnancies | Number of times pregnant |
| Glucose | Plasma glucose concentration |
| Blood Pressure | Diastolic blood pressure (mm Hg) |
| Skin Thickness | Triceps skin fold thickness (mm) |
| Insulin | 2-Hour serum insulin (mu U/ml) |
| BMI | Body mass index |
| Diabetes Pedigree Function | Diabetes likelihood based on family history |
| Age | Age in years |

---

## 👨‍💻 Author

**Nithin Reddy**
- GitHub: [@nithinreddyp2004](https://github.com/nithinreddyp2004)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
