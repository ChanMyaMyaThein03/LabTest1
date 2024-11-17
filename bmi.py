def calculate_bmi(height, weight):
    print("Height:"+ height)     # print("Height", height)
    print("Weight:"+ weight)     # print("Weight", weight)

    W = float (weight)
    H = float (height)

    bmi = W * (H * H)

    if bmi < 18.5:
        print("Under Weight")
    elif bmi >= 18.5 and bmi <= 25.0:
        print ("Normal Weight")
    else:
        print ("Over Weight")
        
    return bmi

def calculate_bmi1(height,weight):
    print("Height"+str(height))
    print("Weight"+str(weight))


def main():
    print("Enter Height:")
    height = input()
    print("Enter Weight:")
    weight = input()

    result = calculate_bmi(height, weight)
    bmi = "{:.2f}".format(result)
    print("BMI =" + str(bmi) )


    
    calculate_bmi1(weight = 57, height = 1.73)  # if + use to concatenate for other data type: not str, it will show error

if __name__ == "__main__":
    main()
    
