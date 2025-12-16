import pickle
import numpy as np

model_file = 'model_C=1.0.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

car_to_value = {
    'make': 'audi',
    'model': 'a4',
    'year': 2017,
    'engine_hp': 190.0,
    'engine_cylinders': 4.0,
    'transmission_type': 'automatic',
    'driven_wheels': 'front_wheel_drive',
    'number_of_doors': 4.0,
    'market_category': 'luxury',
    'vehicle_size': 'midsize',
    'vehicle_style': 'sedan',
    'highway_mpg': 37,
    'city_mpg': 27,
    'popularity': 3105
}

X = dv.transform([car_to_value])
price = np.expm1(model.predict(X)[0])
print(f"Model prediction: ${price:,.2f}")