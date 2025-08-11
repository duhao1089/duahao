class Passenger:
    def passenger_age_validate(self, age):
        if age < 2:  #fix_1
            return "infant"
        elif age <= 12:
            return "child"
        else:
            return "adult"