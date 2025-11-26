# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
    [200, 50, 100],   # Week 1
    [180, 60, 110],   # Week 2
    [220, 55, 105],   # Week 3
    [210, 65, 95]     # Week 4
]

# totals per category
food_total = 0
transport_total = 0
utilities_total = 0

# totals per week
week_totals = [0, 0, 0, 0]

# total for month
month_total = 0

for i in range(len(monthly_expenses)):      # tygodnie
    week = monthly_expenses[i]
    food_total += week[0]
    transport_total += week[1]
    utilities_total += week[2]

    week_sum = week[0] + week[1] + week[2]
    week_totals[i] = week_sum
    month_total += week_sum

print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food_total)
print('Transport:', transport_total)
print('Utilities:', utilities_total)
print('Week 1:', week_totals[0])
print('Week 2:', week_totals[1])
print('Week 3:', week_totals[2])
print('Week 4:', week_totals[3])
print('----------------')
print('TOTAL:', month_total)
