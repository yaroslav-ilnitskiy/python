import json


class Student(object):
    __name: str
    __year: int
    __gender: str
    __phone: str

    def __init__(self, name: str):
        self.__name = name

    def set_name(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_year(self, year: int):
        self.__year = year

    def get_year(self) -> int:
        return self.__year

    def set_gender(self, gender: str):
        self.__gender = gender

    def get_gender(self) -> str:
        return self.__gender

    def set_phone(self, phone: str):
        self.__phone = phone

    def get_phone(self) -> str:
        return self.__phone

    def serialize(self) -> str:
        return json.dumps({
            "name": self.get_name(),
            "year": self.get_year(),
            "gender": self.get_gender(),
            "phone": self.get_phone(),
        })

    @staticmethod
    def unserialize(data):
        student = Student(data["name"])

        student.set_year(data["year"])
        student.set_gender(data["gender"])
        student.set_phone(data["phone"])

        return student

    def output(self):
        print(
            f'Name: {self.get_name()} Phone: {self.get_phone()} Year {self.get_year()}'
            f' gender {self.get_gender()}'
        )
