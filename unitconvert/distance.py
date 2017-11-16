def miles_to_kilometers(distance):
    '''
        PARAMETERS
        ---------
        distance : (float)
                    distance in miles
                    
        RETURNS
        ---------
        distance : (float)
                    distance in kilometers
    '''

    km = distance*1.61

    return km

def kilometers_to_miles(distance):
    '''
        PARAMETERS
        ---------
        distance : (float)
        	    distance in kilometers
        
        RETURNS
        ---------
        distance : (float)
        	    distance in miles
        '''
    
    miles = distance/1.61
    
    return miles
