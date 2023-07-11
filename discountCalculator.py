# Discount calculator run only this file
while True:
    try:
        print('Enter product price : ')
        price = float(input())
        print('Quantity needed : ')
        quantity = int(input())
        print(' discount % : ')
        discount = float(input())
        discount_amount = price * (discount / 100)
        final_price = (price - discount_amount) * quantity
        print('discount amount per unit : ', discount_amount)
        print('the final price is :', final_price)
    except ValueError:
        print('Invalid input! Please enter numeric values.')
    except Exception as e:
        print('An error occurred:', str(e))
    finally:
        print('Please , do not forget to take your receipt ')
        print('Next customer ')
