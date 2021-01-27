class Road:
   def __init__(self, width, length):
       self.width=width
       self.length=length
   def asphalt_weight(self):
        asphalt_weight= self.width*self.length*25*5
        print(asphalt_weight)

a=Road(23, 16)
a.asphalt_weight()