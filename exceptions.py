class InvalidAgeException(Exception):
    "Raised when the age is less than 18"
    pass

number = 18

try:
    input_num  = int(input("Enter your age"))
    if ( input_num < number):
        raise InvalidAgeException
    else:
        print("Eligble to vote")

except InvalidAgeException:
    print ("Exception occured : less than 18")

