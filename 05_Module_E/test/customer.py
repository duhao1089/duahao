


class Customer:
    def __init__(self, name, customer_type, years_member):
        self.name = name
        self.customer_type = customer_type # "VIP" or "Regular"
        self.years_member = years_member

    def customer_discount_calc(self):
        if self.customer_type == "VIP":   #fix_1
            discount = 0.9
        else:
            discount = 1.0
        if self.years_member > 10:
            discount = discount * 0.95
        if discount < 0.8:
            return 0.8
        else:
            return discount

