class Payment:
    def payment_amount_validate(self, amount):
        if amount > 0 and isinstance(amount, int):  #fix_1
            return True
        else:
            return False