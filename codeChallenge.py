#Library for hash
import hashlib


def challenge(start_string):
    #Use the ASCII values of each character in the string and generate a list of these values.
    #ord(char) for the ASCII value. 
    ascii_values = [ord(char) for char in start_string]

    #Multiply each value in the list by the number of characters in the string.
    multiplied_values = [i*len(start_string) for i in ascii_values]

    #Find the sum of all numbers in the resulting list.
    sum_from_list = sum(multiplied_values)

    #Use this sum to generate a SHA256 hash.
    sha256_hash = hashlib.sha256(str(sum_from_list).encode()).hexdigest()

    #Return the answer
    return sha256_hash

start_string = "CitricSheep"
hexadecimal_string = challenge(start_string)
print("Hexadecimal String:", hexadecimal_string)

