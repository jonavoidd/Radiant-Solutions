# The module containing the bills, profits, and sales

class Bills:
    def __init__(self, bills):
        self.bills = bills

    def get_bills(self):
        return self.bills

electricity = Bills(5000)
water = Bills(3000)


def profit(sales, cost):
    return round((sales - cost), 2)

def sale(sales):
    return sales