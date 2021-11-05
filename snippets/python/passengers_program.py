class Passenger:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display(self):
        print(f"Passenger: {self.first_name} {self.last_name}")

    @staticmethod
    def from_input():
        first_name = input()
        last_name = input()

        return Passenger(first_name, last_name)

lisa = Passenger("Lisa", "Ha")
# user = Passenger.from_input()

lisa.display()
# user.display()
