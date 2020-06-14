# Python Algerian mobile phone number package

This package provides several methods to deal with Algerian phone numbers.
It can be used in your projects or to integrate it into your favorite python frameworks such as Django or Flask.

Inspired by the [PHP Package](https://github.com/cherifGsoul/php-algerian-mobile-phone-number) authored by Mohamed Cherif Bouchelaghem.
## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Python Algerian mobile phone number package.
```
pip install python_algerian_mobile_phone_number
```

## Usage:

### Instantiation:

The class doesn't have a public constructor, it has a named constructor instead in order to preseve its invariants:

```python 
import pythonAlgerianMobilePhoneNumber;

$phoneNumber = AlgerianMobilePhoneNumber::fromString('0699000000');
```

Or:

```php
use Cherif\AlgerianMobilePhoneNumber\AlgerianMobilePhoneNumber;

$phoneNumber = AlgerianMobilePhoneNumber::fromString('06 99 00 00 00');
```

Or:

```php
use Cherif\AlgerianMobilePhoneNumber\AlgerianMobilePhoneNumber;

$phoneNumber = AlgerianMobilePhoneNumber::fromString('06-99-00-00-00'); //
```

The value object class accepts international phone indicative, 00213 or +213, too.

> __NOTE__: For now only space and dash "-" separated numbers are accepted.


### API:

#### asString

To get the string value of the object:

```php
$phoneNumber->asString(); // -> '0699000000'
```

#### equals

For comparaison check:
```php
$other = AlgerianMobilePhoneNumber::fromString('0699000000');
$phoneNumber->equals($other); // -> true
```

#### isMobilis, isDjezzy and isOoredoo

To know if the object respresents a Mobilis, Djezzy or Ooredoo phone number

```php
$phoneNumber = AlgerianMobilePhoneNumber::fromString('0699000000');
$phoneNumber->isMobilis(); // -> true
$phoneNumber->isDjezzy(); // -> false
$phoneNumber->isOoredoo(); // -> false
```

#### withNumber

```php
use Cherif\AlgerianMobilePhoneNumber\AlgerianMobilePhoneNumber;

$phoneNumber = AlgerianMobilePhoneNumber::fromString('06-99-00-00-00');
$phoneNumber->withNumber('07-99-00-00-00'); // Will return a new instance that represents the new number
```


#### __toString
Casts the value object to string:
```php
$phoneNumber = AlgerianMobilePhoneNumber::fromString('0699000000');
(string)$phoneNumber; // -> '0699000000'
```

## Contribution
Contributions are welcome to make this library better.

- Clone the repo:

```shell
$ git clone git@github.com:cherifGsoul/php-algerian-mobile-phone-number.git
```

and enter to the cloned repository directory.

- Install dependencies:

```shell
$ composer install
```

### Testing:
Run composer script for testing:

```shell
$ composer test
```

## License

[MIT License](LICENSE).