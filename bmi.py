def bmi(Height, Weight):
    return Weight / (Height ** 2)

def Cal_Bmi(Bmi):
    if Bmi < 18.5:
        return "You are Underweight."
    elif Bmi < 25:
        return "You are perfect!"
    elif Bmi < 30:
        return "You are Overweight"
    else:
        return "You have Obesity"

def main():
    Height = float(input("Enter your height in mtr: "))
    Weight = float(input("Enter your weight in kg: "))
    Bmi = bmi(Height, Weight)
    category = Cal_Bmi(Bmi)
    
    print(f"Your BMI is: {Bmi:.2f}")
    print(f"Your BMI category is: {category}")

if __name__ == "__main__":
    main()
