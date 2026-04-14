from flask import Flask, render_template, request
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

app = Flask(__name__)


app.config['TEMPLATES_AUTO_RELOAD'] = True


data = pd.read_csv("asthma_disease_data.csv")
data.columns = data.columns.str.strip()

X = data[['Wheezing', 'ShortnessOfBreath', 'ChestTightness', 'Coughing', 'NighttimeSymptoms']]
y = data['Diagnosis']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = DecisionTreeClassifier(max_depth=4)
model.fit(X_train, y_train)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        wheezing = int(request.form.get('wheezing'))
        breathlessness = int(request.form.get('breathlessness'))
        chest = int(request.form.get('chest'))
        cough = int(request.form.get('cough'))
        night = int(request.form.get('night'))

        values = [wheezing, breathlessness, chest, cough, night]

        
        if any(v not in [0, 1] for v in values):
            return render_template('index.html', prediction_text="Enter only 0 or 1")

        symptom_count = sum(values)

        input_data = pd.DataFrame([{
            'Wheezing': wheezing,
            'ShortnessOfBreath': breathlessness,
            'ChestTightness': chest,
            'Coughing': cough,
            'NighttimeSymptoms': night
        }])

        prediction = model.predict(input_data)

        
        if symptom_count >= 3:
            result = "Asthma Detected,Please consult a doctor"
        else:
            if prediction[0] == 1:
                result = "Asthma Detected"
            else:
                result = "No Asthma"

    except:
        result = "Please enter valid values (0 or 1)"

    return render_template('index.html', prediction_text=result)


if __name__ == "__main__":
    app.run(debug=True)