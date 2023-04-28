# Exercise 1 - Turn the shopping cart program into an object-oriented program
# Create a class called cart that retains items and has methods to add, remove, and show

class Cart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.cart = []
        
    def add_to_cart(self, new_item):
        self.cart.append(new_item)
        print(f"{new_item.name} added to cart.")
    
    def remove_from_cart(self, item_name):
        for item in self.cart:
            if item.name == item_name:
                self.cart.remove(item)
                print(f"{item.name} removed!")
                return
        print(f"{item_name} is not in your cart.")
    
    def show_cart(self):
        print(f"{self.customer_name}'s cart:")
        total_price = 0
        for item in self.cart:
            print(f"{item.name} - {item.quantity} - ${item.price}")
            total_price += item.price * item.quantity
    
class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        
    def get_product_total(self):
        return self.quantity * self.price
    
    
def run():
    cust_name = input('Welcome. What is your name? ')
    my_cart = Cart(cust_name)
    while True:
        ask = input('What would you like to do? Add/Remove/Show/Quit ').lower()
        if ask == 'quit':
            break
        elif ask == 'add':
            item = input('What would you like to add? ')
            my_cart.add_to_cart(item)
        elif ask == 'remove':
            item_name = input('What would you like to remove? ')
            my_cart.remove_from_cart(item_name)
            
        elif ask == 'show':
            my_cart.show_cart()
            
        elif ask == 'quit':
            print('Thank you!')
            break
        else:
            print('Invalid action.')
            
    
run()

# Exercise 2 - Write a Python class for an Animal that has a name and energy attributes. The animal class should also have methods for eat, sleep, and play that will take in an integer and increase/decrease the energy of the animal with a formatted print statement
 
# Example 1
# buddy = Animal('Buddy', 10)
# buddy.play(5) # -> "Buddy is playing for 5 minutes. His energy is now 5"
# buddy.sleep(10) # -> "Buddy is sleeping for 10 minutes. His energy is now 15"

class Animal:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def eat(self, energy_gain):
        self.energy += energy_gain
        print(f"{self.name} is eating and gained {energy_gain} energy. His energy is {self.energy}")

    def sleep(self, energy_gain):
        self.energy += energy_gain
        print(f"{self.name} is sleeping and gained {energy_gain} energy. His energy is  {self.energy}")

    def play(self, energy_loss):
        self.energy -= energy_loss
        print(f"{self.name} is playing and lost {energy_loss} energy. His energy is  {self.energy}")


