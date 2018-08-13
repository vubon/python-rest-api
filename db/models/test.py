from db.models.models import Model


class Person(Model):
    age: int = None
    height: float = None
    is_active: bool = True
    name: str


a = Person(age=28, name='Vubon')
print(a.name)
print(a.is_active)