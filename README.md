# Python Data Access Layer Generator

----------------------------------------------------------------------

If you are bored to write the data access layer from scratch for every table in your database and you don’t want include more dependencies in your proyect (like SQLAlquemy, Elixir, Django-ORM, SQLObjects) here’s the solution!

This piece of code is a Data Layer SQL Generator for your Data Table Objects (DTOs). It provides the SQL statments to the basic operations in the database.

**It’s very simple to use:**

```python

from mapper import ObjectMapper

class Person(object):

    def __init__(self):

        self.name = 'john'
        self.age = 22

        #this properties are ignored
        self._some_information = 'Not saved in table'
        self.__other_stuff = 'Also ignored'

p = Person()
m = ObjectMapper(p)

>>> m.insert()
"INSERT INTO person(age,name) VALUES ('22','john')"
>>> m.update(id=1)
"UPDATE person SET age = '22', name = 'john' WHERE id_person = '1'"
>>> m.delete(id=1)
"DELETE FROM person WHERE id_person = 1"
>>> m.get_all()
"SELECT age, name FROM person"
>>> m.get_by_id(id=1)
"SELECT age, name FROM person WHERE id_person = 1"

```

And forget about writting the repetitive SQL Layer for your tables!
