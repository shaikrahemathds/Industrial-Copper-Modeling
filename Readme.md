# 🏭 **Industrial Copper Modeling**

## 📖 **Overview**

This project leverages machine learning to predict the **selling price** and **status** of copper. It showcases a complete pipeline, from data preprocessing to model deployment, ensuring accuracy and usability.  

### ✨ Highlights:
- 🧹 **Data Preparation:** Cleaned and processed the dataset with proper data types, handling missing values, skewness, and outliers.
- 🔍 **Feature Engineering:** Conducted correlation analysis and selected significant predictors.
- 🤖 **Model Development:**
  - A **Random Forest Regression Model** for predicting selling prices.
  - An **Extra Trees Classification Model** for predicting the status of copper.
- 🌐 **Interactive Application:**  
  A user-friendly **Streamlit app** for real-time predictions:
  - Dynamic data input.
  - Interactive and clear result displays.

---

## 🌟 **Features**

### **1. Data Preprocessing**
- 📊 Converted data into appropriate types to ensure consistency.  
- 🩹 Handled missing values by substituting the **mean** or **median** based on skewness analysis.  
- ✂️ Removed outliers using a custom **IQR-based function** and clipping.  
- 🔄 Applied **log transformations** to normalize highly imbalanced columns.  
- 🖼️ Created a **correlation heatmap** to identify feature relationships and removed highly correlated features (**correlation > 0.8**) to reduce multicollinearity.  

### **2. Predictive Modeling**

#### **Regression Models:**  
- 🔬 Evaluated six algorithms:  
  - **Linear Regression**  
  - **Decision Tree Regressor**  
  - **Extra Trees Regressor**  
  - **Random Forest Regressor**  
  - **Gradient Boosting Regressor**  
  - **XGBoost Regressor**  
- 📏 Metrics Used:  
  - **Mean Absolute Error (MAE)**  
  - **Mean Squared Error (MSE)**  
  - **Root Mean Squared Error (RMSE)**  
  - **R² Score**  
- 🏆 **Best Algorithm:** **Extra Trees Regressor**  
  - **MAE:** 0.0298  
  - **RMSE:** 0.0505  
  - **R² Score:** 0.9609  

- 🎯 **Optimization:**  
  - Tuned hyperparameters with **RandomizedSearchCV**.  
  - Saved the final model using **Pickle**.  

#### **Classification Models:**  
- 🔬 Evaluated five algorithms:  
  - **Decision Tree Classifier**  
  - **Extra Trees Classifier**  
  - **Random Forest Classifier**  
  - **Gradient Boosting Classifier**  
  - **XGBoost Classifier**  
- ⚖️ Balanced class categories using **SMOTE** (Synthetic Minority Oversampling Technique).  
- 📏 Metrics Used:  
  - **Accuracy**  
  - **Precision**  
  - **Recall**  
  - **F1-Score**  
- 🏆 **Best Algorithm:** **Extra Trees Classifier**  
  - **Accuracy:** 98.24%  
  - **Precision:** 99.01%  
  - **Recall:** 97.43%  
  - **F1-Score:** 98.21%  

### **3. Interactive Streamlit Application**  
- 🖥️ User-friendly interface for dynamic input.  
- ⚡ Real-time predictions for **selling price** and **status**.  
- 📊 Clear and intuitive result displays for better decision-making.  

---

## 🏗️ **Domain**

This project focuses on the **manufacturing sector**, leveraging machine learning to optimize decisions in the copper market.  

---

## 🛠️ **Technology and Skills Takeaway**

This project provided hands-on experience with the following tools and technologies:  

- 🐍 **Python:** Core language for data manipulation and modeling.  
- 📐 **NumPy:** For numerical computations.  
- 🗃️ **Pandas:** For data cleaning, preprocessing, and exploration.  
- 🧠 **Scikit-Learn:** To implement and evaluate machine learning models.  
- 📦 **Pickle:** For saving and loading trained models.  
- 🌐 **Streamlit:** To create an interactive web application for real-time predictions.  

---

## 📬 **Contact Information**

Feel free to reach out for collaboration or inquiries:  

- 💼 **LinkedIn:** [Shaik Rahemath](https://www.linkedin.com/in/rahemath/)  
- 📧 **Email:** [shaikrahemathds@gmail.com](mailto:shaikrahemathds@gmail.com)  

---

### 🚀 Ready to dive into the world of machine learning? Explore the code and gain insights into the manufacturing domain! 🌟
