"""linear mapping is just a rule that maps input to output in a linear way.
For example, a linear mapping can be represented as:
y = mx + b
where m is the slope and b is the y-intercept.
This means that for every unit increase in x, y increases by m units.
This type of mapping is commonly used in various fields such as physics, economics, and computer science to model relationships between variables.
In computer science, linear mappings are often used in algorithms and data structures to efficiently transform data from one form to another.

"""

import numpy as np
def linear_mapping(input_array,slope,intercept):
    """
    This function applies a linear mapping to the input array.
    
    Parameters:
    input_array (numpy array): The input data to be transformed.
    slope (float): The slope of the linear mapping.
    intercept (float): The y-intercept of the linear mapping.
    
    Returns:
    numpy array: The transformed output data.
    """
    input_array=np.array(input_array)
    output_array= slope*input_array+ intercept
    
    return output_array

#example usage
if __name__=="__main__":
    input_data=[1,2,3,4,5]
    slope=2
    intercept=3
    output_data=linear_mapping(input_data,slope,intercept)
    print("Input Data: ",input_data)
    print("Output Data: ",output_data)