# Daily Calorie Tracker
# This program allows users to log their meals and calories, and provides insights on their daily intake.
#--- Task 1: Welcome Message ---
print("===================================")
print(" Welcome to the Daily Calorie Tracker ")
print("===================================")
print("This program helps you log meals, track calories,")
print("and check if you are within your daily limit.\n")

# --- Task 2: Input & Data Collection ---
meals = []       # to store meal names
calories = []    # to store calorie values

num_meals = int(input("How many meals do you want to log today? "))

for i in range(num_meals):
    meal = input("Enter the name of meal " + str(i+1) + ": ")
    cal = int(input("Enter calories for " + meal + ": "))
    meals.append(meal)
    calories.append(cal)

# --- Task 3: Calculations ---
total_calories = sum(calories)
average_calories = total_calories / len(calories)

daily_limit = int(input("\nEnter your daily calorie limit: "))

# --- Task 4: Limit Warning ---
if total_calories > daily_limit:
    status = "WARNING: You exceeded your daily limit!"
else:
    status = "Good job! You are within your daily limit."

# --- Task 5: Neatly Formatted Output ---
print("\nYour Calorie Report")
print("---------------------------")
print("Meal\t\tCalories")
print("---------------------------")
for i in range(len(meals)):
    print(meals[i], "\t\t", calories[i])
print("---------------------------")
print("Total:\t\t", total_calories)
print("Average:\t", round(average_calories, 2))
print(status)
print("---------------------------")

