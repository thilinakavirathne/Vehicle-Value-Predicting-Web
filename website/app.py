from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

def prediction(lst):
    filename = 'model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

@app.route('/', methods=['POST', 'GET'])
def index():
    pred_value = 0
    if request.method == 'POST':
        medication = request.form['medication']
        company = request.form['company']
        condition = request.form['condition']
        fuel = request.form['fuel']
        performance_type = request.form['performance_type']
        drive_type = request.form['drive_type']
        country = request.form['country']
        body_style = request.form['body_style']

        feature_list = []
        feature_list.append(int(medication))

        company_list = ['Aston Martin', 'Cadilla', 'Chevrolet', 'Dodge', 'Fiat', 'Honda', 'Hummer', 'Jaguar', 'Land Rover', 'Mazda',
                        'Mercedes-Benz', 'Nissan', 'Other', 'Pagani', 'Peugeot', 'Ram', 'Subaru', 'Suzuki', 'Tesla', 'Toyota', 'Volvo',]
        condition_list = ['Brand New', 'recondition']
        fuel_list = ['Petrol', 'Diesel', 'Electric', 'Hybrid', 'Gas']
        performance_type_list = ['Super', 'Sports', 'Hyper', 'Plug-in Hybrid (PHEV)']
        body_style_list = ['Coupe-SUV', 'SUV', 'Convertible', 'Crossover', 'Estate/Wagon', 'Hatchback', 'Pickup Truck', 'Roadster', 'Minivan', 'Sedan',]
        drive_type_list = ['Drive Type_All-Wheel Drive (AWD)', 'Drive Type_Four-Wheel Drive (4WD)',
                           'Drive Type_Front-Wheel Drive (FWD)', 'Drive Type_Rear-Wheel Drive (RWD)',]
        country_list = ['Country_American', 'Country_Asian', 'Country_British', 'Country_European']

        def traverse_list(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)

        traverse_list(company_list, company)
        traverse_list(condition_list, condition)
        traverse_list(fuel_list, fuel)
        traverse_list(performance_type_list, performance_type)
        traverse_list(body_style_list, body_style)
        traverse_list(drive_type_list, drive_type)
        traverse_list(country_list, country)

        pred_value = prediction(feature_list)
        pred_value = np.round(pred_value[0], 2)

    return render_template("index.html", pred_value=pred_value)

if __name__ == '__main__':
    app.run(debug=True)




