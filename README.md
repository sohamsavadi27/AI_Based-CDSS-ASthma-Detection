AI-Based Clinical Decision Support System (CDSS) for Asthma Prediction
Overview

This project is a web-based Clinical Decision Support System (CDSS) designed to predict the likelihood of asthma based on patient symptoms. The system uses a machine learning model along with rule-based logic to assist in early detection and decision-making.

The application is built using Flask for the backend and HTML for the frontend, and it is deployed as a web application.

Features:
Takes user input for symptoms such as:
1)Wheezing
2)Shortness of breath
3)Chest tightness
4)Coughing
5)Nighttime symptoms

Uses a Decision Tree Classifier for prediction
Combines machine learning with rule-based logic for improved accuracy
Provides instant output indicating whether asthma is likely or not
Simple and user-friendly web interface.

Technologies Used:
->Python
->Flask
->Scikit-learn
->Pandas
->HTML/CSS

Machine Learning Model

The system uses a Decision Tree Classifier trained on a dataset containing patient symptoms and diagnosis labels. The model classifies input data into two categories:

Asthma Detected
No Asthma

Additionally, a rule-based approach is used by counting the number of symptoms to improve prediction reliability.

Project Structure
AI-CDSS-Asthma/
│
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md

Installation and Setup
Clone the repository:
git clone https://github.com/your-username/AI-CDSS-Asthma.git
cd AI-CDSS-Asthma
Install dependencies:
pip install -r requirements.txt
Run the application:
python app.py
Open in browser:
http://127.0.0.1:5000/
Deployment

The application can be deployed using platforms such as Render. The platform installs dependencies from the requirements.txt file and runs the Flask application using the start command.

Use Case

This system can assist healthcare professionals by providing preliminary analysis based on symptoms, helping prioritize patients and supporting early diagnosis.

Limitations
The model is trained on a limited dataset
It is intended for educational purposes only
It should not be used as a substitute for professional medical diagnosis
Future Scope
Integration with real-time medical data
Use of advanced machine learning models
Integration with Electronic Health Records (EHR)
Improved UI/UX for better usability

Author

Soham Savadi
