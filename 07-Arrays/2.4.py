# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
    ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
    ["Pancakes", "Sandwich", "Steak"],
    ["Smoothie", "Chicken Wrap", "Salmon"],
    ["Eggs", "Pasta", "Soup"],
    ["Toast", "Burrito", "Pizza"],
    ["Cereal", "Salad", "Fish Tacos"],
    ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Returns a week day name
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n-1]

# Returns a string with day meals (B,L,D) separated by comma
def day_meal_plan(meal_plan, day_number):
    meals = meal_plan[day_number]
    return meals[0] + ", " + meals[1] + ", " + meals[2]

# Prints weekly meal plan
print("WEEKLY MEAL PLAN")
print("(Breakfast, Lunch, Dinner)")
print("============================")

for day_index in range(7):
    print(weekday(day_index + 1) + ":",
          day_meal_plan(meal_plan, day_index))
