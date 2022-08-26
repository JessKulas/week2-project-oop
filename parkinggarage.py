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

   You will need a few attributes as well:
- tickets -> list
- parkingSpaces -> list
- currentTicket -> dictionary
  """



class Garage:
    def __init__(self, current_ticket, ticket = 500, parking_spaces = 500):
        self.current_ticket = current_ticket
        self.ticket = ticket
        self.parking_spaces = parking_spaces
        

    def takeTicket(self):
         self.ticket -= 1
         while True:
            duration = input("Select hours: 8 or 24?: ")
            if duration == 8:
                  print("It will cost you $96.")
            elif duration == 24:
                  print("It will cost you $288.")
                  self.parking_spaces -= 1

    def payForParking(self):
         amount = input("Make a payment for your ticket: ")
         self.ticket -= amount
         print("Thank you for paying for your ticket. You have 15mins to leave the garage.")
         current_ticket.dict["paid"] = True

    def leaveGarage(self):
         if current_ticket.paid == True:
            print("Thank you, have a nice day!")
         elif current_ticket.paid == False:
            print("Make payment: " )
         self.parking_spaces += 1
         self.ticket += 1



current_ticket = {
   "Status": "paid", 
   "Amount": "amount",
}        