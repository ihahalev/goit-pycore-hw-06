from collections import UserDict
import re
from customErrors import ShortName, PhoneValidationError
from wrappers import input_error

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name: str):
        super().__init__(name)
        self.check_name(name)
        self.value = name.strip()

    def edit_name(self, new_name: str):
        self.check_name(new_name)
        self.value = new_name.strip()

    def check_name(_, name: str):
        if (len(name.strip())<2):
            raise ShortName("Name should be at least 2 chars")

class Phone(Field):
    def __init__(self, phone: str):
        super().__init__(phone)
        self.validate_phone(phone)
        self.value = phone

    def edit_phone(self, new_phone: str):
        self.validate_phone(new_phone)
        self.value = new_phone

    def validate_phone(_, phone: str):
        pattern = r"^\d{10}$"
        check = re.search(pattern, phone.strip())
        if not check:
            raise PhoneValidationError("Phone should be 10 digits")

class Record:
    @input_error
    def __init__(self, name):
        self.name = Name(name)
        self.phones: list[Phone] = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    @input_error
    def add_phone(self, phone_number: str):
        #validation check
        new_phone = Phone(phone_number)
        if not [phone for phone in self.phones if phone.value == new_phone.value]:
            self.phones.append(new_phone)

    @input_error
    def find_phone(self, phone_number):
        #validation check
        checked_phone = Phone(phone_number)
        return [phone for phone in self.phones if phone.value == checked_phone.value][0]

    @input_error
    def edit_phone(self, old_phone, new_phone):
        found_phone = self.find_phone(old_phone)
        #validation check
        change_phone = Phone(new_phone)
        found_phone.edit_phone(change_phone.value)

class AddressBook(UserDict):
    def add_record(self, rec:Record):
        if rec.name.value in self.data:
            print("name already exist")
        else:
            self.data[rec.name.value] = rec
    def find(self, name:str):
        found = self.data.get(name)
        if found:
            return found
        else:
            print("name doesn't exist")
    def delete(self, name:str):
        found = self.data.get(name)
        if found:
            return self.data.pop(name)
        else:
            print("name doesn't exist")

book = AddressBook()

John = Record("John")
print(John)
John.add_phone("1234567890")
print(John)
John.add_phone("5555555555")
print(John)
John.edit_phone("1234567890", "1112223333")
print(John)
book.add_record(John)
print(book)
book.delete(John.name.value)
print(book)

ia = Record("J")
ia = Record("ia")
print(ia)
ia.add_phone("1234567890")
print(ia)
ia.add_phone("555555555")
print(ia)
ia.add_phone("55555555588")
print(ia)
ia.edit_phone("1234567890", "111222333")
print(ia)
book.add_record(ia)
print(book)
book.delete(ia.name.value)
print(book)