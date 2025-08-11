from test.customer import Customer
from test.fight import Flight
from test.booking import Booking
from test.passenger import Passenger
from test.payment import Payment
import allure
import pytest

data1=[{"name":1,"type":"VIP","year":1,"res":0.9},{"name":1,"type":"Regular","year":1,"res":1.0},{"name":1,"type":"VIP","year":11,"res":0.855}]
data2=[{"flight":1,"utc_timestamp":1672531200,"res":"2023-01-01 00:00"},{"flight":1,"utc_timestamp":1683744000,"res":"2023-05-10 18:40"}]
data3=[{"flight_type":"domestic","tickets_count":1,"res":50},{"flight_type":"international","tickets_count":2,"res":200}]
data4=[{"age":1,"res":"infant"},{"age":2,"res":"child"},{"age":13,"res":"adult"}]
data5=[{"amount":1,"res":True}]

@allure.feature("project测单元试")
class TestCase:
    @allure.story("Customer类测试")
    @allure.description('正向:检查程序输出结果正确')
    @pytest.mark.parametrize("case",data1)
    def test_positive_customer(self,case):
        customer=Customer(case["name"],case["type"],case["year"])
        res=customer.customer_discount_calc()
        assert res==case["res"]

    @allure.story("Flight类测试")
    @allure.description('正向:检查程序输出结果正确')
    @pytest.mark.parametrize("case",data2)
    def test_positive_flight(self,case):
        flight=Flight(case["flight"],case["utc_timestamp"])
        res=flight.flight_time_convert()
        assert res==case["res"]

    @allure.story("Booking类测试")
    @allure.description('正向:检查程序输出结果正确')
    @pytest.mark.parametrize("case",data3)
    def test_positive_booking(self,case):
        booking=Booking()
        res=booking.booking_fee_calculate(case["flight_type"],case["tickets_count"])
        assert res==case["res"]

    @allure.story("Passenger类测试")
    @allure.description('正向:检查程序输出结果正确')
    @pytest.mark.parametrize("case",data4)
    def test_positive_passenger(self,case):
        passenger=Passenger()
        res=passenger.passenger_age_validate(case["age"])
        assert res==case["res"]

    @allure.story("Payment类测试")
    @allure.description('正向:检查程序输出结果正确')
    @pytest.mark.parametrize("case",data5)
    def test_positive_payment(self,case):
        payment=Payment()
        res=payment.payment_amount_validate(case["amount"])
        assert res==case["res"]



