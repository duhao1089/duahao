from test.booking import Booking
from test.customer import Customer
import allure
import pytest

from test.fight import Flight
from test.passenger import Passenger
from test.payment import Payment

data1=[{"name":1,"type":"123","year":1,"res":1.0},{"name":1,"type":"Regular","year":0,"res":1.0}]
data2=[{"flight":1,"utc_timestamp":1683744000.999,"res":"2023-05-10 18:40"},{"flight":1,"utc_timestamp":1612137600,"res":"2021-02-01 00:00"}]
data3=[{"flight_type":"domesti","tickets_count":1,"res":"Invalid flight type"},{"flight_type":"international","tickets_count":0,"res":"Invalid tickets count"},{"flight_type":"international","tickets_count":1.2,"res":"Invalid tickets count"}]
data4=[{"age":-1,"res":"年龄无效"}]
data5=[{"amount":1.1,"res":False},{"amount":0,"res":False}]

@allure.feature("customer")
class TestCase:
    @allure.story("Customer")
    @allure.description('反向:检查代码的错误处理机制能正常工作')
    @pytest.mark.parametrize("case",data1)
    def test_negative_customer(self,case):
        customer=Customer(case["name"],case["type"],case["year"])
        res=customer.customer_discount_calc()
        assert res==case["res"]

    @allure.story("Flight类测试")
    @allure.description('反向:检查代码的错误处理机制能正常工作')
    @pytest.mark.parametrize("case",data2)
    def test_negative_flight(self,case):
        flight=Flight(case["flight"],case["utc_timestamp"])
        res=flight.flight_time_convert()
        assert res==case["res"]

    @allure.story("Booking类测试")
    @allure.description('反向:检查代码的错误处理机制能正常工作')
    @pytest.mark.parametrize("case", data3)
    def test_negative_booking(self, case):  # 注意：方法名应改为test_negative_booking（符合反向测试命名规范）
        booking = Booking()
        with pytest.raises(ValueError) as exc_info:
            booking.booking_fee_calculate(case["flight_type"], case["tickets_count"])
        assert case["res"] in str(exc_info.value)  # 验证异常信息包含预期内容
    @allure.story("Passenger类测试")
    @allure.description('反向:检查代码的错误处理机制能正常工作')
    @pytest.mark.parametrize("case",data4)
    def test_positive_passenger(self,case):
        passenger=Passenger()
        res=passenger.passenger_age_validate(case["age"])
        assert res==case["res"]

    @allure.story("Payment类测试")
    @allure.description('反向:检查代码的错误处理机制能正常工作')
    @pytest.mark.parametrize("case",data5)
    def test_positive_payment(self,case):
        payment=Payment()
        res=payment.payment_amount_validate(case["amount"])
        assert res==case["res"]