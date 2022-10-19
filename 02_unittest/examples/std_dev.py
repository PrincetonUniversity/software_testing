"""
    Compuate the average of values in the list.
    Raise ValueError if there any illegal values in the list.
"""
import math

def mean(list):
    sum = 0
    for i in range(0, len(list)):
        sum = sum + list[i]
    result = sum/len(list)
    return result

"""
    Compute the standard deviation of the list of numbers.
    Raise Value error if there are any illegal values in the list.
"""
def standard_deviation(list):
    deviation = 0
    m = mean(list)
    for i in range(0, len(list)):
        deviation = deviation + (list[i] - m)**2
    result = math.sqrt(deviation/len(list))
    return result

