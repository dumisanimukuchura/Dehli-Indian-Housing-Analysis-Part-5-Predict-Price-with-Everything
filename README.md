
# Dehli Indian Housing Part 5: Predict Price with Everything & Build a Streamlit App

## Project Overview
This project combines all major features from the New Delhi housing dataset to predict rental prices using **Ridge Regression**. Unlike earlier parts that focused on single or paired features, this part integrates multiple variables — including numerical and categorical data — into a unified machine learning model. To make the model accessible and interactive, a full **Streamlit dashboard** was also built.

## Contact Details
- Email: dumisanimukuchura@gmail.com
- LinkedIn: https://www.linkedin.com/in/dumisani-maxwell-mukuchura-4859b7170/

## Objectives
- Combine multiple key features — `house_size_in_sqft`, `location`, and `house_type` — to predict `price_approx_usd`.
- Apply **Ridge Regression** to handle multicollinearity and regularization.
- Create an interactive web-based dashboard using **Streamlit**.
- Learn and demonstrate how to deploy and reuse models via `joblib`.

---

## Dataset Description

| Column                | Description                                          |
|------------------------|------------------------------------------------------|
| `house_size_in_sqft`   | Size of the house in square feet (numerical)         |
| `location`             | Area name in Delhi (categorical, high-cardinality)   |
| `house_type`           | Type of property (e.g., Independent Floor, Villa)    |
| `price_approx_usd`     | Target variable: Rental price in USD                 |

---

## Key Steps

### **1. Data Preparation**
- Imported cleaned housing dataset from Part 1.
- Filtered out outliers using IQR-based filtering.
- Verified null values and handled accordingly.

### **2. Feature Engineering**
- Applied **OneHotEncoding** to `location` and `house_type`.
- Combined encoded categorical variables with `house_size_in_sqft`.
- Split data into training and testing sets.

### **3. Model Building**
- Built a Ridge Regression model to combine all selected features.
- Compared against a baseline model using mean prediction.

### **4. Model Evaluation**
- Evaluated models using **Mean Absolute Error (MAE)**.
- Ridge Regression Model Performance:
  - **Training MAE**: `$1173.99`
  - **Testing MAE**: `$1143.31`

### **5. Model Saving**
python
import joblib
joblib.dump(model, 'model.pkl')

### ** 🚀 Streamlit Dashboard**

### 📱 Features
- Input House Size (slider)  
- Select Location (dropdown)  
- Select House Type (dropdown)  
- Get real-time rental price prediction

### 🛠️ Technologies Used
- Streamlit  
- Pandas  
- Scikit-learn  
- Joblib  
- Ridge Regression Model

---

### ✅ Project Outcome
- Integrated model using multiple key features showed the highest predictive accuracy.  
- Streamlit app created a clean, user-friendly interface to showcase the model.  
- Demonstrated how to save and deploy a model for real-time prediction.



## References
- **Dataset**: [Kaggle](https://www.kaggle.com/datasets/bhavyadhingra00020/india-rental-house-price)