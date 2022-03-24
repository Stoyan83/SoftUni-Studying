square_meters_landscaping = float(input())
square_meter_price = 7.61

sum = square_meters_landscaping * square_meter_price
discount = sum * 0.18
total_sum = sum - discount

print(f"The final price is: {total_sum} lv.")
print(f"The discount is: {discount} lv.")
