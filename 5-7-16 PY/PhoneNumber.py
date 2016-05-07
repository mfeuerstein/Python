class PhoneNumber:

    def __init__(self, number):

        self.areaCode = number[ 0:3 ]
        self.exchange = number[ 3:6 ]
        self.line = number[ 6:11 ]

    def __str__( self ):

        return "(%s)%-s-%-s" % ( self.areaCode, self.exchange, self.line )

def test():

    newNumber = input("Enter phone number in form (123) 456-7890:\n")

    phone = PhoneNumber(newNumber)
    print("The phone number is: ")
    print (phone) #invokes phone.__str__()

if __name__ == "__main__":
    test()
