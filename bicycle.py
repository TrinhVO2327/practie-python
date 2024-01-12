class Bicycle:
    def __init__(self, model_name, weight, cost_to_produce):
        self.model_name = model_name
        self.weight = weight
        self.cost_to_produce = cost_to_produce

class BikeShop:
    def __init__(self, name, margin):
        self.name = name
        self.margin = margin
        self.inventory = {}

    def add_bicycle(self, bicycle, quantity):
        self.inventory[bicycle] = quantity

    def sell_bicycle(self, bicycle):
        if self.inventory[bicycle] > 0:
            self.inventory[bicycle] -= 1
            return True
        else:
            return False

    def get_profit(self):
        profit = 0
        for bicycle, quantity in self.inventory.items():
            profit += (bicycle.cost_to_produce * self.margin / 100) * quantity
        return profit

class Customer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.bicycle = None

    def buy_bicycle(self, bicycle):
        if self.budget >= bicycle.cost_to_produce * 1.2:
            self.budget -= bicycle.cost_to_produce * 1.2
            self.bicycle = bicycle
            return True
        else:
            return False

# Create a bicycle shop that has 6 different bicycle models in stock. The shop should charge its customers 20% over the cost of the bikes.
shop = BikeShop("Bike Shop", 20)
bicycles = [Bicycle("Model 1", 10, 100), Bicycle("Model 2", 20, 200), Bicycle("Model 3", 30, 300), Bicycle("Model 4", 40, 400), Bicycle("Model 5", 50, 500), Bicycle("Model 6", 60, 600)]
for bicycle in bicycles:
    shop.add_bicycle(bicycle, 10)

# Create three customers. One customer has a budget of $200, the second $500, and the third $1000.
customers = [Customer("Customer 1", 200), Customer("Customer 2", 500), Customer("Customer 3", 1000)]

# Print the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget. Make sure you price the bikes in such a way that each customer can afford at least one.
for customer in customers:
    affordable_bicycles = []
    for bicycle, quantity in shop.inventory.items():
        if customer.budget >= bicycle.cost_to_produce * 1.2:
            affordable_bicycles.append(bicycle)
    print(f"{customer.name} can afford the following bicycles:")
    for bicycle in affordable_bicycles:
        print(f"- {bicycle.model_name}")

# Print the initial inventory of the bike shop for each bike it carries.
print("Initial inventory of the bike shop:")
for bicycle, quantity in shop.inventory.items():
    print(f"- {bicycle.model_name}: {quantity}")
    

