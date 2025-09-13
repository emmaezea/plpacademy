class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    def show_info(self):
        print(f"{self.brand} {self.model} - Battery: {self.battery}%")

    def charge(self, amount):
        self.battery += amount
        if self.battery > 100:
            self.battery = 100
        print(f"{self.brand} charged to {self.battery}%")


class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery, cooling_system):
        super().__init__(brand, model, battery)
        self.cooling_system = cooling_system

    def show_info(self):  # polymorphism (overriding)
        print(f"{self.brand} {self.model} (Gaming Phone) - Battery: {self.battery}%, Cooling: {self.cooling_system}")

    def play_game(self, game_name):
        if self.battery > 20:
            self.battery -= 20
            print(f"Playing {game_name} 🎮 ... Battery now {self.battery}%")
        else:
            print("Battery too low to play games!")


# Testing the classes
phone1 = Smartphone("Apple", "iPhone 15", 50)
phone1.show_info()
phone1.charge(30)

gaming_phone = GamingPhone("Asus", "ROG Phone 7", 100, "Liquid Cooling")
gaming_phone.show_info()
gaming_phone.play_game("PUBG")
