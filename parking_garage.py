class ParkingGarage():
    """
    Description of my parking garage and methods
    
    size expected to be an integer (the number of parking spaces for each garage)
    tickets expected to be a list, though it should/could be the same as size
    parkingSpaces expected to be a dictionary (made more sense to me in the context of the program to make it a dict)
        I used __init__ to populate the dictionary with spot numbers (integers) as the keys and boolean False as the value
    currentTicket expected to be a dictionary, starts as a blank dictionary. TBH I feel like this could be a local Boolean and be easier to handle
    """

    def __init__(self, size, tickets, currentTicket = {}, parkingSpaces = {}):
        self.size = size
        self.tickets = tickets
        self.currentTicket = currentTicket
        self.parkingSpaces = parkingSpaces
        for space in range(self.size): # Probably not very pythonic, but I wanted each instance to start with a clean empty dictionary
            parkingSpaces[space+1] = False     
    
    def totalSpacesAvailable(self):
        result = 0
        # result = (is_empty for is_empty in self.parkingSpaces.values() if is_empty == False)
        for is_empty in self.parkingSpaces.values(): # List comprehension here?
           if is_empty == False:
                result += 1
        return result
    
    def takeTicketAndPark(self):
        # For this we need to first find out how many spaces are available, take that difference from .size and add 1
        open_space = (self.size - self.totalSpacesAvailable()) +1
        self.parkingSpaces[open_space] = True # references the correct spot number and fills it with a car (True)
        self.tickets -= 1
        self.currentTicket['paid'] = False
        return f"Spot {str(open_space)} has been taken and ticketed."
        # decrease available tickets by 1; parkingSpaces has already been accounted for and debited accordingly

    def payForParking(self):
        payment = input("Parking is a suggested donation of $5. Please input the amount paid: ")
        if int(payment) >= 5:
            print("Thank you for your payment! You have 15 minutes to exit the garage.")
            self.currentTicket['paid'] = True
        elif int(payment) < 5:
            print("Wow...cheapskate. I mean, I know it's a tough economy out there, but a program's gotta make a living.")
            self.currentTicket['paid'] = True
        self.leaveGarage()

    def leaveGarage(self):
        if self.currentTicket['paid'] == True:
            print("Thank You, have a nice day")
            open_space = (self.size - self.totalSpacesAvailable())
            self.parkingSpaces[open_space] = False # references the correct spot number and fills it with a car (True)
            self.tickets += 1
            self.currentTicket['paid'] = False # Have to reset the paid marker so these scoundrels can't sneak out
        else:
            print("Ticket needs to be paid first: ")
            self.payForParking()

# Testing

MyGarage = ParkingGarage(10,10)
print(MyGarage.size)
print(MyGarage.parkingSpaces)
print(MyGarage.totalSpacesAvailable())
print(MyGarage.takeTicketAndPark())
print(MyGarage.takeTicketAndPark())
print(MyGarage.takeTicketAndPark())

print(MyGarage.totalSpacesAvailable())
print(MyGarage.parkingSpaces)
print(MyGarage.currentTicket)
print(MyGarage.leaveGarage())
print(MyGarage.parkingSpaces)
