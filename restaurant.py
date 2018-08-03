class Restaurant():
    def __init__(self,name,cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type
        #self.number_served=number_served
        self.number_served=0
    def describe_resaurant(self):
        print('This resaurant name is:'+self.name)
        print('the type of cuisine is:'+self.cuisine_type)
        print('\n'+str(self.number_served)+' people are in the resaurant. ')
    def open_resaurant(self):
        print(self.name+' is opening now!')
    def set_number_served(self,num):
        self.number_served=num
        print('\nNow we have '+str(num)+' people in it!')
    def increment_number_served(self,add):
        self.number_served+=add
class IceCreamStand(Restaurant):
    def __init__(self,name,cuisine_type):
        super().__init__(name,cuisine_type)
    def flavor(self,flavor):
        self.flavor=flavor
        print('Our ice cream has '+self.flavor+' flavor！')
my_icecream=IceCreamStand('kfc','sweet')
my_icecream.describe_resaurant()
my_icecream.flavor('mango')




