#Name:Ruolin Chen
#email:chenr9@mail.uc.edu
#Assignment Title:  
#Course: IS 4010
#Semester/Year: Spring 2024
#Brief Description: 
#Citations:
#Anything else that's relevant: 


class Vehicle:        
    '''
    Vehicle Class
    This class models a vehicle on a used car lot
    change order: we need to add maximum speed to the model
    change order: need a way to 'read'the maximum speed from the model
    change order: some developers need to use the constructor without having to provide a max speed
    
    '''
    #constructor. It's called when... an instantiate an object if vehicle type
    def __init__(self, type, max_speed = None):
        
        '''
        @param type: the kind of vehicle
        @param max_speed: Maximum speed of the vehicle, defaults to None
        '''
        self.type = type;
        self.thisisprivate = 42    # This is a weak attempt to 'support'data
        self.max_speed = max_speed
        
    # A instance method. It operates on an instance of the Vehicle class
        
    def printType(self):
        print(self.type);
        
        
if __name__ == "__main__":
# Some code to test the class would go here.
# If there's no code, just pass
    pass
