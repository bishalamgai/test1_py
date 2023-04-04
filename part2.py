
RED = "red"
BLUE = "blue"
YELLOW = "yellow"


color1 = input("Enter the first primary colour: ")
color2 = input("Enter the second primary colour: ")


if color1 != RED and color1 != BLUE and color1 != YELLOW:
    print("Error: Invalid Color1")
elif color2 != RED and color2 != BLUE and color2 != YELLOW:
    print("Error: Invalid Color2")
elif color1 == color2:
    print("Error: The two colors you entered are same")
else:
   
    if color1 == RED:
        if color2 == BLUE:
            print("PURPLE")
        else:
            print("ORANGE")
    elif color1 == BLUE:
        if color2 == RED:
            print("PURPLE")
        else:
            print("GREEN")
    else: 
        if color2 == RED:
            print("ORANGE")
        else:
            print("GREEN")
