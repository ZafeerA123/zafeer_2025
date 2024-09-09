import sys
from typing import Union

# Define types for mean function
Number = Union[int, float]  # Number can be either int or float type
Numbers = list[Number] # Numbers is a list of Number types
Scores = Union[Number, Numbers] # Scores can be single or multiple 

def mean(scores: Scores, method: int = 1) -> float:
    """
    Calculate the mean of a list of scores.
    
    Average and Average2 are hidden functions performing the mean algorithm.

    If a single score is provided in scores, it is returned as the mean.
    If a list of scores is provided, the average is calculated and returned.
    """

    def average(scores): 
        """Calculate the average of a list of scores using a Python for loop."""
        sum = 0
        len = 0
        for score in scores:
            if isinstance(score, Number):
                sum += score
                len += 1
            else:
                print("Bad data: " + str(score))
                return None  # Return None if bad data is found
        return sum / len if len > 0 else None

    def average2(scores):
        """Calculate the average of a list of scores using the built-in sum() function."""
        return sum(scores) / len(scores)

    if isinstance(scores, list):
        result = None
        if method == 1:
            result = average(scores)
        else:
            result = average2(scores)
        
        if result is None:
            return "Error: Bad data encountered"
        return round(result, 2)
    
    return scores

# Test the function with valid and invalid data
print(mean([100, 90, 85.5]))  # Should return a valid mean
print(mean([100, "NaN", 90]))  # Should print an error message
