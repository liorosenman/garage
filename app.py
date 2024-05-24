from enum import Enum
import json
from icecream import ic
cars = []
new_car = {"color": "red", "model":1995, type:"mercedes"}

def menu():
    while True:
        print("1 - Print the garage")
        print("2 - Add a car")
        print("3 - Update a car")
        choise = input("What do you want to do? ")
        choise_int = int(choise)
        if (choise_int == actions.PRINT.value):
            print_the_cars()
        if (choise_int == actions.ADD.value):
            add_car()
        if(choise_int == actions.UPDATE.value):
            update_car()

def print_the_cars():
    try:
        with open('cars.json', 'r') as file:
            cars = json.load(file)
        ic(cars)
    except:
        print("There are no cars to print")

def add_car():
    try:
        with open('cars.json', 'r') as file:
            cars = json.load(file)
    except FileNotFoundError:
        cars = []
    new_car_color = input("COLOR:")
    new_car_model = input("MODEL:")
    new_car_type = input("TYPE:")
    new_car = {"color":new_car_color, "model":new_car_model,"type":new_car_type}
    cars.append(new_car)
    with open('cars.json', 'w') as file:
        json.dump(cars, file, indent=4)
    ic(cars)

def update_car():
        try:
            with open('cars.json', 'r') as file:
                cars = json.load(file)
            garage_length = len(cars)
            index_to_upd = int(input("What car to update? "))
            if(index_to_upd > garage_length):
                print("There is no such car")
            elif garage_length == 0: print("The garage is empty")
            else:
                    new_car_color = input("COLOR:")
                    new_car_model = input("MODEL:")
                    new_car_type = input("TYPE:")
                    cars[index_to_upd -1]['color'] = new_car_color
                    cars[index_to_upd -1]['model'] = new_car_model
                    cars[index_to_upd -1]['type'] = new_car_type
                    with open('cars.json', 'w') as file:
                        json.dump(cars, file, indent=4)
                    ic(cars)
                    
        except:
            print("The garage is empty!!!")

       

         
        

class actions(Enum):
    PRINT = 1
    ADD = 2
    UPDATE = 3

if __name__ == "__main__":
    menu()