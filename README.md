# Food Delivery Time Prediction
This project builds a machine learning model to predict delivery time. It involves data preprocessing, save piple line data, and save clean data for model training, evaluation, create a pipeline and Streamlit deployment.

---
## Project Structure

```
├── Data/                  
├── notebook/  
|    ├── Data_cleanning.ipynb          
│    └── Model_training.ipynb       
├── Model_deploy/
│   ├── App.py              
│   └── model.pkl           
├── requirements.txt          
├── README.md          
├── .gitignore 
```

## Objective

To predict Food delivery time.
---


'Delivery_Time_min'
num_col = ['Distance_km', 'Preparation_Time_min', 'Courier_Experience_yrs']
obj_col = ['Weather', 'Traffic_Level', 'Time_of_Day', 'Vehicle_Type', 'Distance_category']



## Features Used
- Distance_km
- Preparation_Time_min	 
- Courier_Experience_yrs	 
- Weather	 
- Traffic_Level	 
- Time_of_Day	 
- Weight	 
- Vehicle_Type	 
- Distance_category	 
- Delivery_Time_min	     
---

##  Technologies Used

- Python (Pandas, NumPy, seaborn, matplotlib, Scikit-learn)
- Streamlit (for deployment)
- Joblib (for model saving/loading)

---

## Model & Evaluation

- **Model Used:** e.g., RandomForestRegressor / XGBoostRegressor
- **Evaluation Metrics:**
  - R2 score 
  - Adjusted r2, Mean absolute error, mean squared error
  - R2 gap

---

## How to Run the App

1. Clone the repository:
   ```bash
   git clone https://github.com/Priyanshu-techp/Food-Delivery-Time-Prediction.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run "Model_deploy/App.py"
   ```
---

## Deploy link
[Streamlit app link](https://laptop-price-prediction-mod.streamlit.app/)

## Results

- **Best r2-score:** ~0.81 
- **Overall Accuracy:** ~0.80
- **R2 gap:** ~0.039

---

## Author

**Priyanshu Pandey**  
Diploma in Automation & Robotics  
Aspiring Data Scientist  
[LinkedIn Profile](https://www.linkedin.com/in/priyanshu-pandey-672767320)