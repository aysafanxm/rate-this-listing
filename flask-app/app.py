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
        bedrooms  = result['bedrooms']
        bathrooms = result['bathrooms']
        beds  = result['beds']
        cleaning_fee  = result['cleaning_fee']
        amenities_airconditioning = result['amenities_airconditioning']
        amenities_bathtub = result['amenities_bathtub']
        amenities_breakfast  =  result['amenities_breakfast']
        amenities_cabletv = result['amenities_cabletv']
        amenities_coffeemaker = result['amenities_coffeemaker']
        amenities_cookingbasics  =  result['amenities_cookingbasics']
        amenities_dishwasher  = result['amenities_dishwasher']
        amenities_dryer  =  result['amenities_dryer']
        amenities_elevator = result['amenities_elevator']
        amenities_essentials  = result['amenities_essentials']
        amenities_extrapillowsandblankets = result['amenities_extrapillowsandblankets']
        amenities_familykidfriendly  =  result['amenities_familykidfriendly']
        amenities_freestreetparking  =  result['amenities_freestreetparking']
        amenities_heating = result['amenities_heating']
        amenities_internet = result['amenities_internet']
        amenities_kitchen = result['amenities_kitchen']
        amenities_lockonbedroomdoor  =  result['amenities_lockonbedroomdoor']
        amenities_petsallowed = result['amenities_petsallowed']
        amenities_pool = result['amenities_pool']
        amenities_privateentrance = result['amenities_privateentrance']
        amenities_selfcheckin = result['amenities_selfcheckin']
        amenities_smokingallowed  = result['amenities_smokingallowed']
        amenities_tv  = result['amenities_tv']
        amenities_washer  = result['amenities_washer']
        amenities_wheelchairaccessible = result['amenities_wheelchairaccessible']
        amenities_wifi = result['amenities_wifi']
        bed_type_couch = result['bed_type_couch']
        bed_type_futon = result['bed_type_futon']
        bed_type_pull_out_sofa = result['bed_type_pull_out_sofa']
        bed_type_real_bed = result['bed_type_real_bed']
        room_type_entire_home_apt = result['room_type_entire_home_apt']
        room_type_private_room = result['room_type_private_room']
        room_type_shared_room = result['room_type_shared_room']
        neighbourhood_cleansed__bayview = result['neighbourhood_cleansed__bayview']
        neighbourhood_cleansed__bernal_heights = result['neighbourhood_cleansed__bernal_heights']
        neighbourhood_cleansed__castro_upper_market = result['neighbourhood_cleansed__castro_upper_market']
        neighbourhood_cleansed__chinatown  = result['neighbourhood_cleansed__chinatown']
        neighbourhood_cleansed__crocker_amazon = result['neighbourhood_cleansed__crocker_amazon']
        neighbourhood_cleansed__diamond_heights = result['neighbourhood_cleansed__diamond_heights']
        neighbourhood_cleansed__downtown_civic_center  = result['neighbourhood_cleansed__downtown_civic_center']
        neighbourhood_cleansed__excelsior  = result['neighbourhood_cleansed__excelsior']
        neighbourhood_cleansed__financial_district = result['neighbourhood_cleansed__financial_district']
        neighbourhood_cleansed__glen_park  = result['neighbourhood_cleansed__glen_park']
        neighbourhood_cleansed__golden_gate_park  =  result['neighbourhood_cleansed__golden_gate_park']
        neighbourhood_cleansed__haight_ashbury = result['neighbourhood_cleansed__haight_ashbury']
        neighbourhood_cleansed__inner_richmond = result['neighbourhood_cleansed__inner_richmond']
        neighbourhood_cleansed__lakeshore  = result['neighbourhood_cleansed__lakeshore']
        neighbourhood_cleansed__marina = result['neighbourhood_cleansed__marina']
        neighbourhood_cleansed__mission = result['neighbourhood_cleansed__mission']
        neighbourhood_cleansed__nob_hill  =  result['neighbourhood_cleansed__nob_hill']
        neighbourhood_cleansed__noe_valley = result['neighbourhood_cleansed__noe_valley']
        neighbourhood_cleansed__north_beach = result['neighbourhood_cleansed__north_beach']
        neighbourhood_cleansed__ocean_view = result['neighbourhood_cleansed__ocean_view']
        neighbourhood_cleansed__outer_mission  = result['neighbourhood_cleansed__outer_mission']
        neighbourhood_cleansed__outer_richmond = result['neighbourhood_cleansed__outer_richmond']
        neighbourhood_cleansed__outer_sunset  =  result['neighbourhood_cleansed__outer_sunset']
        neighbourhood_cleansed__pacific_heights = result['neighbourhood_cleansed__pacific_heights']
        neighbourhood_cleansed__potrero_hill  =  result['neighbourhood_cleansed__potrero_hill']
        neighbourhood_cleansed__russian_hill  =  result['neighbourhood_cleansed__russian_hill']
        neighbourhood_cleansed__seacliff  =  result['neighbourhood_cleansed__seacliff']
        neighbourhood_cleansed__south_of_market = result['neighbourhood_cleansed__south_of_market']
        neighbourhood_cleansed__visitacion_valley  = result['neighbourhood_cleansed__visitacion_valley']
        neighbourhood_cleansed__western_addition  =  result['neighbourhood_cleansed__western_addition']
        cancellation_policy_flexible  = result['cancellation_policy_flexible']
        cancellation_policy_moderate  = result['cancellation_policy_moderate']
        cancellation_policy_strict = result['cancellation_policy_strict']
        cancellation_policy_super_strict_30  =  result['cancellation_policy_super_strict_30']
        cancellation_policy_super_strict_60  =  result['cancellation_policy_super_strict_60']
        host_response_time_a_few_days_or_more = result['host_response_time_a_few_days_or_more']
        host_response_time_within_a_day  =  result['host_response_time_within_a_day']
        host_response_time_within_a_few_hours = result['host_response_time_within_a_few_hours']
        host_response_time_within_an_hour = result['host_response_time_within_an_hour']

        
        #Prepare the feature vector for prediction
        pkl_file = open('comb_vecstack_stack.pkl', 'rb')
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
