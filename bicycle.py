class Wheel:
    # This class represents a wheel with a model name, weight, and cost to produce
    def __init__(self, model_name, weight, cost_to_produce):
        self.model_name = model_name
        self.weight = weight
        self.cost_to_produce = cost_to_produce

class Frame:
    # This class represents a frame with a material type, weight, and cost to produce
    def __init__(self, material, weight, cost_to_produce):
        self.material = material
        self.weight = weight
        self.cost_to_produce = cost_to_produce

class Bicycle:
    # This class represents a bicycle composed of two wheels and a frame, and includes a manufacturer
    def __init__(self, model_name, front_wheel, rear_wheel, frame, manufacturer):
        self.model_name = model_name
        self.front_wheel = front_wheel
        self.rear_wheel = rear_wheel
        self.frame = frame
        self.manufacturer = manufacturer
        self.weight = front_wheel.weight + rear_wheel.weight + frame.weight
        self.cost_to_produce = front_wheel.cost_to_produce + rear_wheel.cost_to_produce + frame.cost_to_produce
        self.selling_price = self.cost_to_produce * (1 + manufacturer.margin / 100)

class BikeShop:
    # This class represents a bike shop with a name, profit margin, inventory, and sold bicycles
    def __init__(self, name, margin):
        self.name = name
        self.margin = margin
        self.inventory = {}
        self.sold_bicycles = []

    # Adds a specified quantity of bicycles to the shop's inventory
    def add_bicycle(self, bicycle, quantity):
        self.inventory[bicycle] = quantity

    # Sells a bicycle from the inventory if available
    def sell_bicycle(self, bicycle):
        if self.inventory[bicycle] > 0:
            self.inventory[bicycle] -= 1
            self.sold_bicycles.append(bicycle)
            return True
        else:
            return False

    # Calculates the total profit made from selling bicycles
    def get_profit(self):
        profit = 0
        for bicycle in self.sold_bicycles:
            profit += (bicycle.selling_price - bicycle.cost_to_produce) * self.margin / 100
        return profit

class Customer:
    # This class represents a customer with a name, budget, and owned bicycle
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.bicycle = None

    # Allows the customer to buy a bicycle if they have sufficient budget
    def buy_bicycle(self, bicycle):
        price = bicycle.selling_price * (1 + 0.2)  # Bike shop sells at 20% over cost
        if self.budget >= price:
            self.budget -= price
            self.bicycle = bicycle
            return True
        else:
            return False

class BicycleManufacturer:
    # This class represents a bicycle manufacturer that can produce bicycles
    def __init__(self, name, margin):
        self.name = name
        self.margin = margin
        self.produced_bicycles = []

    # Produces a bicycle with the given specifications
    def produce_bicycle(self, model_name, front_wheel, rear_wheel, frame):
        bicycle = Bicycle(model_name, front_wheel, rear_wheel, frame, self)
        self.produced_bicycles.append(bicycle)
        return bicycle

# Creating manufacturers
manufacturer1 = BicycleManufacturer("Manufacturer 1", 10)
manufacturer2 = BicycleManufacturer("Manufacturer 2", 15)
manufacturer3 = BicycleManufacturer("Manufacturer 3", 20)

# Creating wheels
wheel1 = Wheel("Wheel 1", 2, 50)
wheel2 = Wheel("Wheel 2", 2.5, 60)
wheel3 = Wheel("Wheel 3", 3, 70)

# Creating frames
frame1 = Frame("Aluminum", 10, 200)
frame2 = Frame("Carbon", 8, 300)
frame3 = Frame("Steel", 12, 150)

# Creating bicycles with the new composition and manufacturers
bicycles = [
    manufacturer1.produce_bicycle("Model 1", wheel1, wheel1, frame1),
    manufacturer1.produce_bicycle("Model 2", wheel2, wheel2, frame2),
    manufacturer1.produce_bicycle("Model 3", wheel3, wheel3, frame3),
    manufacturer2.produce_bicycle("Model 4", wheel1, wheel1, frame2),
    manufacturer2.produce_bicycle("Model 5", wheel2, wheel2, frame3),
    manufacturer2.produce_bicycle("Model 6", wheel3, wheel3, frame1)
]

# Create a bicycle shop that has 6 different bicycle models in stock. The shop should charge its customers 20% over the cost of the bikes.
shop = BikeShop("Bike Shop", 20)
for bicycle in bicycles:
    shop.add_bicycle(bicycle, 10)

# Create three customers. One customer has a budget of $200, the second $500, and the third $1000.
customers = [Customer("Customer 1", 200), Customer("Customer 2", 500), Customer("Customer 3", 1000)]

# Print the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget. Make sure you price the bikes in such a way that each customer can afford at least one.
for customer in customers:
    affordable_bicycles = []
    for bicycle, quantity in shop.inventory.items():
        if customer.budget >= bicycle.selling_price * 1.2:
            affordable_bicycles.append(bicycle)
    print(f"{customer.name} can afford the following bicycles:")
    for bicycle in affordable_bicycles:
        print(f"- {bicycle.model_name} by {bicycle.manufacturer.name}")

# Print the initial inventory of the bike shop for each bike it carries.
print("\nInitial inventory of the bike shop:")
for bicycle, quantity in shop.inventory.items():
    print(f"- {bicycle.model_name}: {quantity}")

# Have each of the three customers purchase a bike
for customer in customers:
    for bicycle, quantity in shop.inventory.items():
        if customer.buy_bicycle(bicycle):
            shop.sell_bicycle(bicycle)
            print(f"{customer.name} purchased {bicycle.model_name} by {bicycle.manufacturer.name} for ${bicycle.selling_price * 1.2:.2f}. Remaining budget: ${customer.budget:.2f}")
            break

# Print the bicycle shop's remaining inventory for each bike and the profit made
print("\nRemaining inventory of the bike shop:")
for bicycle, quantity in shop.inventory.items():
    print(f"- {bicycle.model_name}: {quantity}")

print(f"\nTotal profit made by the bike shop: ${shop.get_profit():.2f}")
