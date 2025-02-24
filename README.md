# Calories Burned Prediction App
This is a Streamlit web application that predicts the number of calories burned based on user input features such as gender, age, height, exercise duration, heartrate, body temperature, and BMI. The app uses a pre-trained machine learning model to make the predictions.
# Features
- **User Input**: Users can input their details using sliders and select boxes in the sidebar.
- **Calories Burned Prediction**: The app predicts the number of calories burned based on the input features.
- **Funny Quotes**: The app displays a random funny quote related to exercise and calories.
- **Feedback**: The app provides feedback based on the predicted calories burned.

## File Structure
- app.py :The main Streamlit application script
- model.pkl : The pre-trained machine learning model used for prediction
- READ.md: This file, providing an overview of the project.

# Requirements
- Python 3.6+
- Streamlit
- Pandas
- Numpy
- Scikit-learn

## Liscence
This project is licensed under the MIT Licence. See the LISENCE file for details.

# Acknowledgments
- The pre-trained model used in this was was created using Scikit-learn.
- Funny quotes were collected from various sources on the internet.

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/calories-burned-prediction-app.git
   cd calories-burned-prediction-app
2. **Install Dependencies**:
   Make sure you have Python installed. Then,
   install the required packages using pip:
  pip install streamlit pandas numpy scikit-learn
3. **Run the App**
   streamlit run app.py
