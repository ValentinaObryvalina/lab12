from tkinter import *


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe(self):
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open(self):
        print("The restaurant is open.")


class IceCreamRestaurant(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='IceCream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = [
            'Карамель',
            'Вишня',
            'Ананас',
            'Кофе'
        ]

    def all_flavors(self, canvas):
        canvas.create_text(100, 100, text="В " + self.restaurant_name.title() +
                                          " есть такие вкусы :", fill='red')
        y = 120
        for flavor in self.flavors:
            canvas.create_text(100, y, text=flavor, fill='red')
            y += 20


ice_car = IceCreamRestaurant('IceCar')
ice_car.all_flavors(Canvas())

root = Tk()
root.title("Вкусы:")
canvas = Canvas(root)
canvas.pack()
canvas.create_text(100, 50, text='Вкусы:', fill='red')
ice_car.all_flavors(canvas)
root.mainloop()
