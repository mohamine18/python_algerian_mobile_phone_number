# Python Algerian mobile phone number package

This package provides several methods to deal with Algerian phone numbers.

The aim of this package is to create a python community in Algeria and provide all possible libraries to make python frameworks and projects such as Django or Flask adapted to Algerian market and easy to use.

Inspired by the [PHP Package](https://github.com/cherifGsoul/php-algerian-mobile-phone-number) authored by Mohamed Cherif Bouchelaghem.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Python Algerian mobile phone number package.
```
pip install python-algerian-mobile-phone-number
```

## Usage:

### Instantiation:
Create an instance of the class AlgerianMobilePhoneNumber and pass the phone number value as an attribute

- Import
```python 
from python_algerian_mobile_phone_number import AlgerianMobilePhoneNumber
```

```python 
phoneNumber = AlgerianMobilePhoneNumber('0770000000')
```

Or:

```python 
phoneNumber = AlgerianMobilePhoneNumber('07 70 00 00 00')
```

Or:

```python 
phoneNumber = AlgerianMobilePhoneNumber('07-70-00-00-00')
```

> __NOTE__: For now only space and hyphens "-" separated numbers are accepted.

>__NOTE__: International phone indicative such 00213 or +213 are accepted.


### API:

#### str

To get the string representation of the instance use the built in function __str\__:

```python
phoneNumber.__str__() #'0770000000'
```

#### equalsTo

To compare two phone numbers:
```python
other = AlgerianMobilePhoneNumber('0770000000')
phoneNumber.equalsTo(other) #True
```

#### isMobilis, isDjezzy and isOoredoo

To check the mobile phone number provider including Mobilis, Djezzy and Ooredoo

```python
phoneNumber = AlgerianMobilePhoneNumber('0770000000')
phoneNumber.isMobilis() #False
phoneNumber.isDjezzy()  #True
phoneNumber.isOoredoo() #False
```

#### changeNumber

To change the phone number of an instance:
```python
phoneNumber = AlgerianMobilePhoneNumber('0770000000')
phoneNumber.changeNumber('0798000000') #'0798000000'
```

#### convertToInternational

The method takes one parameter named prefix -- values only '00' and '+'
```python
phoneNumber = AlgerianMobilePhoneNumber('0770000000')
phoneNumber.convertToInternational()     #'00213770000000'
phoneNumber.convertToInternational('00') #'00213770000000'
phoneNumber.convertToInternational('+')  #'+213770000000'
```

#### convertToLocal

The method convert the internaltionl number to local one. Accepts both '00213' and '+213'
```python
phoneNumber = AlgerianMobilePhoneNumber('00213770000000')
phoneNumber.convertToLocal() #'0770000000'
```
>__NOTE__: convertToInternational and convertToLocal does not change the number instance so you can assign it to a variable. If you want to change the class instance use changeNumber instead to avoid mistakes.

## Contribution
Contributions are welcome to give the best of this package.

- Clone the repo:

```shell
$ git clone git@github.com:mohamine18/python_algerian_mobile_phone_number.git
```
- Enter the cloned repository directory.


### Testing:
- Install pytest:

```shell
$ pip install pytest
```
- Run test.py script for unit testing:

```shell
$ pytest test.py
```

## License

[MIT License](LICENSE).
