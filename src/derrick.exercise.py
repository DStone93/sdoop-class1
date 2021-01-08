class LunchCoolerBox:
    # how do I hide items until called?
    items = ["sammich", "granola bar", "water bottle"]
    #

    def __init__ (isOpen, contents, isFull, newItem):
        self.isOpen = False
        self.contents = False
        self.isFull = False
        self.newItem: str

    def isOpen(self):
        self.isOpen = True
    
    def hasNoContents(self):
        return self.contents
    
    def hasContents(self):
        if (self.isOpen == True):
            self.contents == True
    
    def insertContents(self):
        self.isOpen and self.items.append()
        return self.items

    def tippedUpsideDown (self):
        self.contents = False

    def closeLid (self):
        self.isOpen = False

    def maxItems (self):
        if(self.items.length >= 3):
            self.isFull = True
            
example1 = LunchCoolerBox()
example1.openLid()
example1.hasContents()

printexample1

example2 = LunchCoolerBox()
example2.hasContents()
example2.maxItems()
example2.tippedUpsidedown()

print "Example 2", example2
