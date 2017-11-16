def fahrenheit_to_celsius(temp):
    '''
        Input:
            temp (float) - temp in fahrenheit
            
        Returns:
            temp (float) - temp in celsius
    '''
    celsius = (32.0 - temp)*(5.0/9)

    return celsius

def celsius_to_fahrenheit(temp):
    '''
    Input:
    temp (float) - temp in fahrenheit
    
    Returns:
    temp (float) - temp in celsius
    '''

    fahrenheit = 32.0 + temp*9.0/5

    return fahrenheit
