from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/userreview',methods=['POST','GET'])
def user_review():
    if request.method=='POST':
        result=request.form
		property_type_apartment = result['property_type_apartment']
        property_type_apartment = result['property_type_bed_breakfast']
		property_type_apartment = result['property_type_condominium']
		property_type_apartment = result['property_type_dorm']
		property_type_apartment = result['property_type_hostel']
		property_type_apartment = result['property_type_house']
        property_type_apartment = result['property_type_loft']
        property_type_apartment = result['property_type_townhouse']
        
		#Prepare the feature vector for prediction
        pkl_file = open('cat', 'rb')
        index_dict = pickle.load(pkl_file)
        new_vector = np.zeros(len(index_dict))
        
        try:
            new_vector[index_dict['property_type_apartment'+str(result['property_type_apartment'])]] = 1
        except:
            pass
        
        try:
            new_vector[index_dict['property_type_bed_breakfast'+str(result['property_type_bed_breakfast'])]] = 1
        except:
            pass
        
        try:
            new_vector[index_dict['property_type_condominium'+str(result['property_type_condominium'])]] = 1
        except:
            pass
        
        
        try:
            new_vector[index_dict['property_type_dorm'+str(result['property_type_dorm'])]] = 1
        except:
            pass
        
        try:
            new_vector[index_dict['property_type_hostel'+str(result['property_type_hostel'])]] = 1
        except:
            pass
 
        try:
            new_vector[index_dict['property_type_house'+str(result['property_type_house'])]] = 1
        except:
            pass

        try:
            new_vector[index_dict['property_type_loft'+str(result['property_type_loft'])]] = 1
        except:
            pass


        try:
            new_vector[index_dict['property_type_townhouse'+str(result['property_type_townhouse'])]] = 1
        except:
            pass

        
        pkl_file = open('./data/comb_vecstack_clf.pkl', 'rb')
        model = pickle.load(pkl_file)
        prediction = model.predict(new_vector)
        
        return render_template('result.html',prediction=prediction)

    
if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')