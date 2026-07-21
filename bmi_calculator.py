def calculate_bmi(weight, height):
    """
    Calculate BMI from weight (kg) and height (m).

    Parameters:
        weight (float): Weight in kilograms.
        height (float): Height in meters.

    Returns:
        tuple[float, str]: BMI value and category.
    """
    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            return bmi, "Underweight"
        elif 18.5 <= bmi < 25:
            return bmi, "Normal weight"
        elif 25 <= bmi < 30:
            return bmi, "Overweight"
        else:
            return bmi, "Obese"
    else:
        raise ValueError("Weight and height must be positive values.")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi, category = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")
print(f"Category: {category}")