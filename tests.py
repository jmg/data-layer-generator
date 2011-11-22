import unittest
from mapper import ObjectMapper

class Person(object):

    def __init__(self):

        self.name = 'john'
        self.age = 22

        #this properties are ignored
        self._some_information = 'Not saved in table'
        self.__other_stuff = 'Also ignored'


class TestMapper(unittest.TestCase):
    
    def test_sql(self):
        
        p = Person()
        m = ObjectMapper(p)
        
        self.assertEquals(m.insert(), "INSERT INTO person(age,name) VALUES ('22','john')")        
        self.assertEquals(m.get_by_id(id=1), "SELECT age, name FROM person WHERE id_person = 1")        
        self.assertEquals(m.get_all(), "SELECT age, name FROM person")        
        self.assertEquals(m.delete(id=1), "DELETE FROM person WHERE id_person = 1")        
        self.assertEquals(m.update(id=1), "UPDATE person SET age = '22', name = 'john' WHERE id_person = '1'")


unittest.main()
