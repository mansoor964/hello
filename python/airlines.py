
class Airlines:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

airlines = Airlines(3)
peoples = ['ahmad', 'muhammad', 'osman', 'hasan']

for person in peoples:
    if airlines.add_passenger(person):
        print(f'{person} added successfully')
    else:
        print(f'No seat availabe for {person}')
