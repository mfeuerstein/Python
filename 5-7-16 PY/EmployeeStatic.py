class Employee:

    numberOfEmployees = 0
    maxEmployees = 10

    def isCrowded(): # static

        return Employee.numberOfEmployees > Employee.maxEmployees

    isCrowded = staticmethod( isCrowded )

    def __init__( self, firstName, lastName ):

        self.first = firstName
        self.last = lastName
        Employee.numberOfEmployees += 1

    def __del__( self ):

        Employee.numberOfEmployees -= 1

    def __str__( self ):

        return "%s %s" % ( self.first, self.last )

def main():

    answers = ["No", "Yes"]

    employeeList = []

    print ("Employees are crowded?")
    print (answers[ Employee.isCrowded() ])
    print ("\nCreating 11 objects of class Employee..." )

    for i in range(11):
        employeeList.append( Employee( "John", "Doe" + str( i ) ) )

        print ("Employees are crowded?")
        print (answers[ Employee.isCrowded() ])

    print ("\nRemoving one employee...")
    del employeeList[0];

    print ("Employees are crowded?")
    print (answers[ Employee.isCrowded() ])

if __name__ == "__main__":
    main()
  
