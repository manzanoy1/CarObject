#Yanira Manzano
#11/11/2019
#Car Object Exercise

class Car_details:
    company = "Acura"
    model = "MDX"
    type_of_car = ""
    year = 0
    mileage = 0
    color = ""

    def __init__(self, company, model, type_of_car, year, mileage, color):
        self.company = company
        self.model = model
        self.type_of_car = type_of_car
        self.year = year
        self.mileage = mileage
        self.color = color

    def car_input (self, company, model, type_of_car, year, mileage, color):
        car = company, model, type_of_car, year, mileage, color
