import pytest
from python_algerian_mobile_phone_number.AlgerianMobilePhoneNumber import AlgerianMobilePhoneNumber

def test_instantiation():
    numbers = ['0550000000','00213660000000','+213770000000']
    for number in numbers:
        instance = AlgerianMobilePhoneNumber(number)
        assert instance.number == number

def test_stringRepresentation():
    numbers = ['0550000000','00213660000000','+213770000000']
    for number in numbers:
        instance = AlgerianMobilePhoneNumber(number)
        assert instance.__str__() == number

def test_isMobilis():
    numbers = ['0660000000','00213660000000','+213660000000']
    for number in numbers:
        instance = AlgerianMobilePhoneNumber(number)
        assert  instance.isMobilis() == True 

def test_isDjezzy():
    numbers = ['0770000000','00213770000000','+213770000000']
    for number in numbers:
        instance = AlgerianMobilePhoneNumber(number)
        assert  instance.isDjezzy() == True 

def test_isOoredoo():
    numbers = ['0550000000','00213550000000','+213550000000']
    for number in numbers:
        instance = AlgerianMobilePhoneNumber(number)
        assert  instance.isOoredoo() == True 

def test_equalsTo():
    numbers = ['0550000000','00213550000000','+213550000000']
    other = AlgerianMobilePhoneNumber('0550000000')
    for number in numbers:
        instance = AlgerianMobilePhoneNumber(number) 
        assert instance.equalsTo(other)

def test_changeNumber():
    numbers = ['0550000000','00213660000000','+213770000000']
    for number in numbers:
        instance = AlgerianMobilePhoneNumber(number)
        assert instance.changeNumber('0798000000') == '0798000000'

def test_convertToInternational():
    numbers = ['0550000000','00213660000000','+213770000000']
    number_00213 = ['00213550000000','00213660000000','00213770000000']
    number_plus_213 = ['+213550000000','+213660000000','+213770000000']
    for index, number in enumerate(numbers):
        instance = AlgerianMobilePhoneNumber(number)
        assert instance.convertToInternational('00') == number_00213[index] 
    for index, number in enumerate(numbers):
        instance = AlgerianMobilePhoneNumber(number)
        assert instance.convertToInternational('+') == number_plus_213[index] 

def test_convertToLocal():
    numbers = ['0550000000','00213660000000','+213770000000']
    number_local = ['0550000000','0660000000','0770000000']
    for index, number in enumerate(numbers):
        instance = AlgerianMobilePhoneNumber(number)
        assert instance.convertToLocal() == number_local[index] 
