<<<<<<< Updated upstream
subtotal = float(input('Enter subtotal: '))
=======
from datetime import datetime, timedelta


subtotal = float(input('Enter subtotal: '))
todays_day = datetime.weekday(datetime.now())
if subtotal > 50 and (todays_day == 1 or todays_day == 2) :
    discount = 0.1 * subtotal
    print(f'discount amount: {discount:.2f}')
    subtotal = subtotal - discount
tax = 0.06 * subtotal
subtotal = tax + subtotal
print(f'sales tax amount: {tax:.2f}\n'
      f'total: {subtotal:.2f}')
>>>>>>> Stashed changes
