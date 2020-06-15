'''
@author Mohammed amine BOURAS <mohamine19@gmail.com>
@link    https://github.com/mohamine18/python_algerian_mobile_phone_number
@license http://www.opensource.org/licenses/mit-license.php MIT (see the LICENSE file)
'''
import re

class AlgerianMobilePhoneNumber:
    
    def __init__(self, number):
        '''
        __init__ reserved method is called each time an object is created from the class in order to initialize the attributes.
        Initialization steps:
        1- foramtting the number by removing the spaces and dashes (-)
        2- check the number if is a valid or not (if invalid! raise an Exception is raised)
        3- create instance of the class AlgerianMobilePhoneNumber
        '''
        pattern = r"\s|-+"
        number = re.sub(pattern, "", str(number))
        pattern = r"^(00213|\+213|0)(5|6|7)[0-9]{8}"
        result = re.match(pattern, str(number))
        if result is not None:
            self._number = str(number)
        else:
            raise Exception('Phone number is invalid!')
    
    def __str__(self):
        '''
        __str__ The string representation of the class instace number
        '''
        return str(self._number)

    def isMobilis(self):
        '''
        check if it is a Mobilis phone number
        '''
        pattern = r"^(00213|\+213|0)(6)[0-9]{8}"
        result = re.match(pattern, self._number)
        return True if result is not None else False

    def isDjezzy(self):
        '''
        check if it is a Djezzy phone number
        '''
        pattern = r"^(00213|\+213|0)(7)[0-9]{8}"
        result = re.match(pattern, self._number)
        return True if result is not None else False
        
    def isOoredoo(self):
        '''
        check if it is an Ooredoo phone number
        '''
        pattern = r"^(00213|\+213|0)(5)[0-9]{8}"
        result = re.match(pattern, self._number)
        return True if result is not None else False

    def __number_without_prefix(self):
        '''
        Private method to get a number without indicatives.
        This method is used to compare the phone numbers 
        '''
        pattern_without_prefix = r"(5|6|7)[0-9]{8}"
        match = re.search(pattern_without_prefix, self._number)
        return self._number[match.start():]
    
    def equalsTo(self, other):
        '''
        Check if two given algerian phone numbers are equal or not
        '''
        return self.__number_without_prefix() == other.__number_without_prefix()
    
    def changeNumber(self, newnumber):
        '''
        Change the phone number value is a safe way to avoid assigning mistakes
        Also must be used with the convertors when changing number format  
        '''
        replace = AlgerianMobilePhoneNumber(newnumber)
        self._number = replace.__str__()
        return self._number

    def convertToInternational(self, prefix='00'):
        '''
        A method to convert a valid mobile phone number to an international one
        Returns a new value without overwrite the instance value
        '''
        if prefix == '00' or prefix == '+':
            pattern = r"^(00213|\+213|0)"
            newnumber = re.sub(pattern, f'{prefix}213', self._number)
            return newnumber
        else:
            raise Exception("Prefix Invalid!")

    def convertToLocal(self):
        '''
        A method to convert a valid mobile phone number to a local one
        Returns a new value without overwrite the instance value
        '''
        pattern = r"^(00213|\+213|0)"
        newnumber = re.sub(pattern, '0', self._number)
        return newnumber

    #TODO: add locallines detectors