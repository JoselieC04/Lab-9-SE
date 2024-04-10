def encoder(password):
    # the variable should accept a string
    encode = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        # Shifting up by 3 numbers,
        # Wraps back around when needed
        encode += encoded_digit
    return encode


while True:
    # program start up menu
    print("Menu")
    print("---------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

    # variable based off of user input
    userChoice = input("Please enter an option:")
    if userChoice == "1":
        # should encode the password
        userEncode = input("Please enter your password to encode:")
        # the variable should hold to what the function returns
        encodedPassword = encoder(userEncode)
        print("Your password has been encoded and stored!")
        print()
    elif userChoice == "2":
        # Decode the encoded password
        # meant for my partner
        print("The encoded password is", encodedPassword, "and the original password is", userEncode)
        print()
    elif userChoice == "3":
        break
    else:
        print("Please choose a valid option")
