class Booking:
    def __init__(self): self.fee_rate = {"domestic": 50, "international": 100} #fix_1
    def booking_fee_calculate(self, flight_type, tickets_count):
        if tickets_count <= 0:
            return 0
        if flight_type not in self.fee_rate:
            raise ValueError("Invalid tickets count")  #fix_2修复无效票数处理
        return self.fee_rate[flight_type] * tickets_count