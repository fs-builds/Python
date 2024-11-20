print("Welcome to Back to Work! Your BMR, TDEE, calorie intake, and macros will be calculated to help you on your fitness journey.")

weight = int(input("How much do you weigh? (lbs):\n"))
height = int(input("How tall are you? (in):\n"))
age = int(input("How old are you?\n"))
gender = input("M or F?\n")
activity = (input("Activity level? (light, moderate, active):\n")).lower()
goal = input("What's your fitness goal? (cutting, maintaining, bulking):\n").lower()
BMR_Men = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)
BMR_Women = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)

TDEE = 0
Calorie_Intake = 0
Protein_Calories = 0
Carbs_Calories = 0
Fat_Calories = 0

# based on gender and activity
if gender == "M":
    print(f"Your basal metabolic rate (BMR) is {BMR_Men} calories per day.")
    if activity == "light":
        TDEE = BMR_Men * 1.2
    elif activity == "moderate":
        TDEE = BMR_Men * 1.55
    elif activity == "active":
        TDEE = BMR_Men * 1.725
    else:
        print("Invalid. Please enter light, moderate, or active.")
        exit()


elif gender == "F":
    print(f"Your basal metabolic rate (BMR) is {BMR_Women} calories per day.")
    if activity == "light":
        TDEE = BMR_Women * 1.2
    elif activity == "moderate":
        TDEE = BMR_Women * 1.55
    elif activity == "active":
        TDEE = BMR_Women * 1.725
    else:
        print("Invalid. Please enter light, moderate, or active.")
        exit()
else:
    print("Invalid. Please enter M or F")
    exit()


#
if goal == "cutting":
    Calorie_Intake = TDEE - 500

    Protein_Calories = Calorie_Intake * (40/100)
    Carbs_Calories = Calorie_Intake * (40/100)
    Fat_Calories = Calorie_Intake * (20/100)

elif goal == "maintaining":
    Calorie_Intake = TDEE
    Protein_Calories = Calorie_Intake * (30 / 100)
    Carbs_Calories = Calorie_Intake * (40 / 100)
    Fat_Calories = Calorie_Intake * (30 / 100)
elif goal == "bulking":
    Calorie_Intake = TDEE + 500
    Protein_Calories = Calorie_Intake * (25 / 100)
    Carbs_Calories = Calorie_Intake * (50 / 100)
    Fat_Calories = Calorie_Intake * (25 / 100)
else:
    print("Invalid. Please enter cutting, maintaining, or bulking.")
    exit()

# Calculating for macros
Protein_Grams = Protein_Calories / 4
Carbs_Grams = Carbs_Calories / 4
Fat_Grams = Fat_Calories / 9

# Results
print(f"Your Total Daily Energy Expenditure (TDEE): {TDEE} calories/day.\nYour calorie intake: {Calorie_Intake} calories/day.\nProtein: {Protein_Grams} grams.\nCarbohydrates: {Carbs_Grams} grams.\nFats: {Fat_Grams} grams.")
print("Hope you have a great fitness journey!")















