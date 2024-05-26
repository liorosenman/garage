from enum import Enum
import json
from icecream import ic
import os

cars = []
new_car = {"color": "red", "model":1995, type:"mercedes"}
json_file_path = "cars.json"

def menu():
    while True:
        print("1 - Print the garage")
        print("2 - Add a car")
        print("3 - Update a car")
        print("4 - Delete a car")
        print("5 - How many cars")
        print("6 - Clear data")
        choise = input("What do you want to do? ")
        choise_int = int(choise)
        if (choise_int == actions.PRINT.value):
            print_the_cars()
        if (choise_int == actions.ADD.value):
            add_car()
        if(choise_int == actions.UPDATE.value):
            update_car()
        if(choise_int == actions.DELETE.value):
            delete_car()
        if(choise_int == actions.AMOUNT.value):
            amount_of_cars()
        if(choise_int == actions.CLEAR.value):
            clear_data()

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
            if (garage_length == 0):
                print("The garage is empty!!!")
                return
            index_to_upd = int(input("What car to update? "))
            if(index_to_upd > garage_length):
                print("There is no such car")
                return
            updated_car = {"color":input("COLOR: "), "model":input("MODEL: "), "kind":input("KIND: ")}
            cars[index_to_upd - 1] = updated_car
            with open('cars.json', 'w') as file:
                json.dump(cars, file, indent=4)
            ic(cars)
                    
        except:
            print("The garage is empty!!!")

def delete_car():
        try:
            with open('cars.json', 'r') as file:
                cars = json.load(file)
            garage_length = len(cars)
            if (garage_length == 0):
                print("The garage is empty!!!")
                return
            index_to_del = int(input("What car to delete? "))
            if(index_to_del > garage_length):
                print("There is no such car")
                return
            cars.pop(index_to_del - 1)
            with open('cars.json', 'w') as file:
                json.dump(cars, file, indent=4)
            ic(cars)
        except:
            print("The garage is empty!!!")

def amount_of_cars():
    try:
        with open('cars.json', 'r') as file:
            cars = json.load(file)
        garage_length = len(cars)
        if (garage_length == 0):
            print("The garage is empty!!!")
            return
        else:
            print(f"There are {garage_length} cars in the garage")
    except:
        print("The garage is empty!!!")

def clear_data():
    if os.path.exists(json_file_path):
        os.remove(json_file_path)
        print(f"{json_file_path} has been deleted.")
    else:
        print(f"{json_file_path} does not exist.")
    cars = []

     
class actions(Enum):
    PRINT = 1
    ADD = 2
    UPDATE = 3
    DELETE = 4
    AMOUNT = 5
    CLEAR = 6

if __name__ == "__main__":
    menu()