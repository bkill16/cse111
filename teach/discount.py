from datetime import datetime

current_date_and_time = datetime.now()

day_of_week = current_date_and_time.weekday()

subtotal = float(input("\nPlease enter the subtotal: "))

if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
    discount = subtotal * 0.10
    print(f"Discount Amount: ${discount:.2f}")
    
    new_subtotal = subtotal - discount
    sales_tax = new_subtotal * 0.06
    total = new_subtotal + sales_tax

else:
    sales_tax = subtotal * 0.06
    total = subtotal + sales_tax

print(f"Sales Tax Amount: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}\n")