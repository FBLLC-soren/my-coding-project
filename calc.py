# A simple procurement savings calculator
original_price = 1000
negotiated_price = 850

savings = original_price - negotiated_price
percentage = (savings / original_price) * 100

print(f"Original: ${original_price}")
print(f"Negotiated: ${negotiated_price}")
print(f"You saved: ${savings} ({percentage}%)")
