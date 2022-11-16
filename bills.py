# The module containing all the bills

class Bills:
    def __init__(self, bills):
        self.bills = bills

    def get_bills(self):
        return self.bills

electricity = Bills(5000)
water = Bills(3000)
