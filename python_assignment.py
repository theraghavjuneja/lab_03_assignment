import numpy as np

class Flight:
    def __init__(self):
        self.array1 = self.makeArray()
        
    def makeArray(self):
        array1 = np.array([["FlightID", "From", "To", "Price"],
                           ["AI161E90", "BLR", "BOM", "5600"],
                           ["BR161F91", "BOM", "BBI", "6750"],
                           ["AI161F99", "BBI", "BLR", "8210"],
                           ["VS171E20", "JLR", "BBI", "5500"],
                           ["AS171G30", "HYD", "JLR", "4400"],
                           ["AI131F49", "HYD", "BOM", "3499"]])
        return array1
        
    def givenFlightId(self, flightID):
        for i in range(1, len(self.array1)):
            if self.array1[i][0] == flightID:
                print( self.array1[i])
        
            
    def givenSourceCity(self, From):
        for i in range(1, len(self.array1)):
            if self.array1[i][1] == From:
                print(self.array1[i])
     
           
    def givenDestinationCity(self, To):
        for i in range(1, len(self.array1)):
            if self.array1[i][2] == To:
                print(self.array1[i])
  

fl1 = Flight()
a = True
while a:
    print("Click 1 for Flight Id, 2 for source city, 3 for destination city")
    ab = int(input())
    if ab == 1:
        b = input("Enter flight ID: ")
        fl1.givenFlightId(b)
    elif ab == 2:
        b = input("Enter source city: ")
        fl1.givenSourceCity(b)
    elif ab == 3:
        b = input("Enter destination city: ")
        fl1.givenDestinationCity(b)
    else:
        a = False
