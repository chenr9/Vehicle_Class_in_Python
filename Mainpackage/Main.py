#Name:Ruolin Chen
#email:chenr9@mail.uc.edu
#Assignment Title:  
#Course: IS 4010
#Semester/Year: Spring 2024
#Brief Description: 
#Citations:
#Anything else that's relevant: 


#add an import statement for vehicle class


from Vehiclepackage.VehicleClass import *





if __name__ == "__main__":
    #Instantiate an object if type vehicle
    
    
    myCorvette = Vehicle("car",120)   #trigger a call to constructor
    myCorvette.printType()    #invoke the method on the object
    
    #invoke the getter for maximum speed, store the return value in a variable
    #print that to the console
    
    maximum_speed = myCorvette.max_speed
    print("Maximum speed:", maximum_speed)
    
    #instantiate another vehicle object.
    
    
    myCorolla = Vehicle("Car", 80)  #myCorolla is an object of type vehicle
    
    # i want a list of 3 vehicles: car, boat, space ship
    # you can pick the names and properties
    
    
    myVehicle = [ Vehicle("Toyota Camry", 150)
                 ,Vehicle("sailboat", 20)
                 ,Vehicle("Falcon Heavy", 4000)]
    
    # #iterate over the list
    for vehicle in myVehicle:
        vehicle.printType()
        print(vehicle.max_speed)
    
    
    
    
    
    
                
        

    