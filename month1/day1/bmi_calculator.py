"""
BMI Calculator 

A program that calculates Body Mass Index (BMI)
# using weight and height and classifies the result.

"""

def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculate BMI from weight (kg) and height (m).

    Parameters:
        weight (float): Weight in kilograms.
        height (float): Height in meters.

    Returns:
        float: Calculated BMI value.

    Raises:
        ValueError: If weight or height is less than or equal to zero.
    """
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive values.")

    return weight / (height ** 2)


def get_bmi_category(bmi: float) -> str:
    """
    Determine the BMI category.

    Parameters:
        bmi (float): Body Mass Index value.

    Returns:
        str: BMI category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


if __name__ == "__main__":
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError as error:
        print(f"Error: {error}")
