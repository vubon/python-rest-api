from db.tests.models import Model


class Person(Model):
    name = ''
    age = ''


a = Person(name="vubon", age=28)
