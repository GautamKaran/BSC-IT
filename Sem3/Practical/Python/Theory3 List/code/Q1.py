"""
Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
****
*********
******* 
"""
def histogram(int_list):
    for num in int_list:
        print('*' * num)

# Example usage
histogram([4, 9, 7])
