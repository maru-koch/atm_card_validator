import logging


logging.basicConfig(filename='cardValidator.log', level=logging.INFO)


def cardValidator(card_number):

    """
        A function to validate a credit or debit card. 
        param card_number(str): The card number to validate
        return validity: the card brand/Maker
        - validation is implemented using a closure
    """
    #2. calculating the checksum 
    def isValid(digits):
        if not digits: 
            return False
        sum_of_numbers, even_numbers = 0, digits[-2::-2]  
        try:
            for number in even_numbers: 
                number = int(number) * 2
                if number > 9: 
                    digit_1, digit_2 = divmod(number, 10)
                    sum_of_numbers += (digit_1 + digit_2)
                else: 
                    sum_of_numbers += number
            sum_of_numbers += sum([int(odd) for odd in digits[-1::-2]])
        except ValueError as err:
            logging.error("Card not supported: ", str(err), exc_info=True)
        finally:
            return True if sum_of_numbers % 10 == 0 else False

    #3. checking for card length and starting digits    
    valid = isValid(card_number)
    total_digits = len(card_number)
    if valid:
        if total_digits == 15 and card_number[:2] in ['34', '37']: return 'Amex'
        elif total_digits == 16 and card_number[:2] in ['51', '52', '53', '54', '55']: return "MASTERCARD"
        elif total_digits == 13 or 16 and card_number.startswith('4'): return "Visa"
    return "INVALID"

#1: accepting user input
# cardNumber = input('\n\tEnter your Credit/Debit card number: ')
# print(cardValidator(cardNumber))

# NOTE: I noticed certain class of mastercard begins with 22 e.g 2222420000001113. these were not validated in this program 



print(cardValidator("4003600000000014"))