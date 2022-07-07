'''
function to calculate bmi of a patient
'''
def calcBMI(weight,height):
    try:
        bmi=weight/(height*height)
    except:
        return "Wrong input"
    else:
        return bmi


'''
function to complement on the bmi of the patient
'''
def getComplement(bmi):
    comment=""
    # getting the comment for the bmi value given
    if bmi>0 and bmi<=18.5:
        comment="underweight😥.Seek medical attention🤕"
    elif bmi>18.5 and bmi<=24.9:
        comment="healthy😍😎.Keep it up😋💯"
    elif bmi>24.9 and bmi<=29.9:
        comment="overweight😰😰.Seek medical attention🤕"
    elif bmi>29.9:
        comment="Obese💩🥺.Seek medical attention🤕"

    return comment
    
'''
getting the input from the user
'''
print("\n\n")
weight=eval(input('Enter your weight(Kgs) : '))
height=eval(input('Enter your height(Metres) : '))

bmi=calcBMI(weight,height)
comment=getComplement(bmi)
print("\n\n")
'''
giving out response based on the values
'''
bmi="{:.2f}".format(bmi) # formatting the bmi to 2 decimal places
print(f'Your Bmi is {bmi} Kg/m2')
print(f'You are {comment}')
print("\n\n")

