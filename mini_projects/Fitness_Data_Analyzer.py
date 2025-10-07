def calculate_bmi(weight, height):
    """Calculate the Body Mass Index (BMI)."""
    bmi = weight / (height ** 2)
    return bmi


def calculate_calories_burned(duration):
    """Calculate the estimated number of calories burned during exercise."""
    calories = 5 * duration
    return calories


def filter_overweight_people(people_data):
    """Filter overweight people based on BMI."""
    overweight_people = []
    for person in people_data:
        if person["bmi"] >= 25:
            overweight_people.append(person)
    return overweight_people


def filter_underweight_people(people_data):
    """Filter underweight people based on BMI"""
    underweight_people = []
    for person in people_data:
        if person["bmi"] < 18.5:
            underweight_people.append(person)
    return underweight_people

# Main program
people_data = []

print("Enter fitness data for each person (Enter a blank name to finish):")
while True:
    """Collecting information about people(height, weight, exercise duration) in people_data list"""
    name = input("Enter person's name: ").strip()
    if not name:
        break
    weight = float(input("Enter person's weight in kilograms: "))
    height = float(input("Enter person's height in meters: "))
    duration = float(input("Enter exercise duration in minutes: "))
    person = {'name': name, 'weight': weight, 'height': height, 'duration': duration, 'bmi': calculate_bmi(weight, height)}
    people_data.append(person)

print("\nFitness Analysis:")
""" Displaying fitness analysis of all people in people_data list"""
for index, person in enumerate(people_data):
    calories_burned = calculate_calories_burned(person['duration'])
    print(f"{person['name']}: BMI = {person['bmi']:.2f}, Calories burned = {calories_burned:.2f}")

overweight_people = filter_overweight_people(people_data)
""" Displaying data of overweight people if available"""
if overweight_people:
    print("\nOverweight People:")
    for person in overweight_people:
        print(f"{person['name']}: BMI = {person['bmi']:.2f}")
underweight_people = filter_underweight_people(people_data)
"""Displaying data of underweight people if available"""
if underweight_people:
    print("\nUnderweight People:")
    for person in underweight_people:
        print(f"{person['name']}: BMI = {person['bmi']:.2f}")