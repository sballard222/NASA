class Animal:
   """
      Author:   K. Holcomb
   """
   def __init__(self,feed,wtperday,name="No name yet"):
      self.feed=feed
      self.wtperday=wtperday
      self.name=name

   def get_name(self):
      return self.name

   def feeding(self):
      print self.name+" eats "+str(self.wtperday)+" kg per day of "+",".join(self.feed)
