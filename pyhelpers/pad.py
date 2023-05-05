# function that takes in a number and pads it with zeros to a certain length and returns it as a string

def pad(number, length):
    # convert number to string
    number = str(number)
    # get the length of the number
    number_length = len(number)
    # get the amount of zeros we need to pad
    zeros_to_pad = length - number_length
    # pad the number with zeros
    padded_number = "0" * zeros_to_pad + number
    # return the padded number
    return padded_number