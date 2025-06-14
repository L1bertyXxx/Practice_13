class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!\n")

newRestaurant = Restaurant("McDonalds", "фастфуд")

print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)

newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()