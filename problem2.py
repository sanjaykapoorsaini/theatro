"""
Problem 2
---------

In Lumberville, there is a company running a fleet of lumber-trucks. The main-road
to their garage is rather narrow and allows only one truck to pass at once.
As a saving grace, there happens to be an equally narrow side-road,
making a `T` section with the main road.
The garage requires that the trucks come in order, for their parking to be fully accommodated.
But the trucks can come in any order to the office at the junction

owner - Sanjay
"""

def AreTrucksOrdered(seq):
    """check whether the garage have all the trucks in ordered manner.. """
    
    seq_list = ['1']                                                                       #first truck needs to be pass to garage      
    truck_counter = 1                                                                      # start loop from 2nd counter 
    side_road_trucks = list(seq[seq.index('1') + 1:])[::-1]                                # get the lined-up trucks on side road and using them as a STACK (side_road_trucks) 
    
    for truck_number in seq:        
        if truck_counter + 1 == int(truck_number):                                         #check 2nd, 3rd and so on... truck present in input sequence     
            seq_list.append(truck_number)
            if truck_number in side_road_trucks:  
                side_road_trucks.remove(truck_number)   
            truck_counter += 1             
            
        elif len(side_road_trucks) > 0 and truck_counter + 1 == int(side_road_trucks[-1]): # check if the first truck present in side road or in STACK
            seq_list.append(side_road_trucks[-1])
            side_road_trucks.remove(str(truck_counter + 1))                                # remove this entry as the truck already moved to garage
            if truck_number not in seq_list:  
                side_road_trucks.append(truck_number) 
            truck_counter += 1        
                
        else: 
            if truck_number not in (seq_list + side_road_trucks):           
                side_road_trucks.append(truck_number)                                      # park truck to Rode-side            
            
    return ''.join(seq_list + side_road_trucks[::-1]) == '123456'                          # Checking all trucks are lined up in the garage
       
     
if __name__ == '__main__':
    """main method """
    
    seq = str(input("Please Enter the lined-up order of the Trucks.. "))       
    if AreTrucksOrdered(seq):
        print 'YES!!! #true '
    else: print 'No!!! #false '
        
    
