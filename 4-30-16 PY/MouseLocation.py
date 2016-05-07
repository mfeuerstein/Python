from tkinter import *

class MouseLocation ( Frame ):

    def __init__(self):

        self.loc = True
        Frame.__init__(self)
        self.pack( expand = YES, fill = BOTH)
        self.master.title("Demonstrating mouse events")
        self.master.geometry("275x100")

        self.mousePosition = StringVar() # displays mouse potition
        self.mousePosition.set( "Mouse outside window" )
        self.positionLabel = Label( self,
                                    textvariable = self.mousePosition)
        self.positionLabel.pack( side = BOTTOM )

        self.bind( "<Button-1>", self.buttonPressed )
        self.bind( "<ButtonRelease-1>", self.buttonReleased )
        self.bind( "<Enter>", self.enteredWindow )
        self.bind( "<Leave>", self.exitedWindow )
        self.bind( "<B1-Motion>", self.mouseDragged )

    def buttonPressed( self, event):
        self.mousePosition.set( "Pressed at [ " + str( event.x ) +
                                ", " + str( event.y ) + " ] ")

    def buttonReleased( self, event):
        self.mousePosition.set( "Released at [ " + str( event.x ) +
                                ", " + str( event.y ) + " ] ")

    def enteredWindow( self, event):
        self.mousePosition.set( "Mouse in window")
        self.loc = True

    def exitedWindow( self, event):
        self.mousePosition.set( "Mouse outside window")
        self.loc = False

    def mouseDragged( self, event):
        self.mousePosition.set( "Dragged " + ("inside" if self.loc else "outside") + " [ " + str( event.x ) +
                                ", " + str( event.y ) + " ] ")

def main():
    MouseLocation().mainloop()

if __name__ == '__main__':
    main()
