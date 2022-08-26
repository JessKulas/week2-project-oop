"""Your parking gargage class should have the following methods:
- takeTicket
   - This should decrease the amount of tickets available by 1
   - This should decrease the amount of parkingSpaces available by 1
- payForParking
   - Display an input that waits for an amount from the user and store it in a variable
   - If the payment variable is not empty then (meaning the ticket has been paid) ->  display a message to the user that their ticket has been paid and they have 15mins to leave
   - This should update the "currentTicket" dictionary key "paid" to True
-leaveGarage
   - If the ticket has been paid, display a message of "Thank You, have a nice day"
   - If the ticket has not been paid, display an input prompt for payment
      - Once paid, display message "Thank you, have a nice day!"
   - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
   - Update tickets list to increase by 1 (meaning add to the tickets list)
  """



class Garage:
    def __init__(self, ticket, parking_spaces, current_ticket):
        self.ticket = ticket
        self.parking_space = parking_spaces
        self.current_ticket = current_ticket

    def takeTicket(self):
        self.ticket -= 1
        self.parking_spaces -= 1

    def payForParking(self):


    def leaveGarage(self):
        self.parking_spaces += 1