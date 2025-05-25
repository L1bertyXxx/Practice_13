class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!\n")

restaurant1 = Restaurant("McDonald's", "фастфуд")
restaurant2 = Restaurant("Harvest", "Европейская")
restaurant3 = Restaurant("Bona Capona", "Итальянская")


print("Описание ресторанов:")
restaurant1.describe_restaurant()
print()
restaurant2.describe_restaurant()
print()
restaurant3.describe_restaurant()