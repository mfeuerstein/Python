from tkinter import *
import tkinter.messagebox as box

class EntryDemo( Frame ):

    def __init__(self):

        Frame.__init__(self)
        self.pack( expand = YES, fill = BOTH)
        self.master.title("Testing Entry components")
        self.master.geometry("325x100")

        self.frame1 = Frame(self)
        self.frame1.pack( pady = 5 )

        self.text1 = Entry ( self.frame1, name = "text1" )
        self.text1.bind( "<Return>", self.showContents )
        self.text1.pack( side = LEFT, padx = 5 )
        
        self.text2 = Entry ( self.frame1, name = "text2" )
        self.text2.insert( INSERT, "Enter text here" )
        self.text2.bind( "<Return>", self.showContents )
        self.text2.pack( side = LEFT, padx = 5 )

        self.frame2 = Frame(self)
        self.frame2.pack( pady = 5 )

        self.text3 = Entry ( self.frame2, name = "text3" )
        self.text3.insert( INSERT, "Uneditable text field" )
        self.text3.config ( state = DISABLED )
        self.text3.bind( "<Return>", self.showContents )
        self.text3.pack( side = LEFT, padx = 5 )

        self.text4 = Entry ( self.frame2, name = "text4",
                             show = "*")
        self.text4.insert( INSERT, "Hidden text" )
        self.text4.config ( state = DISABLED )
        self.text4.bind( "<Return>", self.showContents )
        self.text4.pack( side = LEFT, padx = 5 )

    def showContents( self, event ):

        theName = event.widget.winfo_name()

        contents = event.widget.get()
        messagebox.showinfo( "Message", theName + ": " + contents ) #not defined

def main():
    EntryDemo().mainloop()

if __name__ == '__main__':
    main()
