#method 1
price_per_item = 111.33
quantity = 3
subtotal = price_per_item * quantity
discount_rate = 0.10
discount_amount = subtotal * discount_rate
final_total = subtotal - discount_amount
print(f"Subtotal: Rs{subtotal:.2f}")
print(f"Discount Amount: Rs{discount_amount:.2f}")
print(f"Final Total: Rs{final_total:.2f}")

hotel_charge = 1200.88
number_of_nights = 7
discount_rate = 0.18
subtotal = hotel_charge * number_of_nights
discount_amount = subtotal * discount_rate
final_total = subtotal - discount_amount
print(f"Subtotal: Rs{subtotal:.2f}")
print(f"Discount Amount: Rs{discount_amount:.2f}")
print(f"Final Total: Rs{final_total:.2f}")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
sum_of_numbers = a + b
print(f"The sum of {a} and {b} is: {sum_of_numbers}")

sub = a - b
print(f"The difference between {a} and {b} is: {sub}")

mul = a * b
print(f"The product of {a} and {b} is: {mul}")

div = a / b
print(f"The quotient of {a} and {b} is: {div:.2f}")


print(2**3**2)



