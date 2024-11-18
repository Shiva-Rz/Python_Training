''' We want to manufacture key rings with the car makes found in the people_cars dictionary below. 
    The size of each key ring will depend on the number of letters in the car make name. 
    Create the set and add all unique car make length values to it.'''
	
people_cars = {'Adam': 'Volvo', 'Kate': 'BMW', 'Mark': 'BMW', 'Hannah': 'Ford', 'Max': 'Volvo', 'Celine':'Fiat'}

key_size = { len(car_name) for car_name in people_cars.items() }
print(key_size)