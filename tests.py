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

    def setUp(self):

        p = Person()
        self.m = ObjectMapper(p)

    def test_insert(self):
        self.assertEquals(self.m.insert(), ("INSERT INTO person(age,name) VALUES ('?','?')", '22', 'john'))

    def test_get_by_id(self):
        self.assertEquals(self.m.get_by_id(id=1), ('SELECT age, name FROM person WHERE id_person = ?', 1))

    def test_select_all(self):
        self.assertEquals(self.m.get_all(), "SELECT age, name FROM person")

    def test_delete(self):
        self.assertEquals(self.m.delete(id=1), ('DELETE FROM person WHERE id_person = ?', 1))

    def test_update(self):
        self.assertEquals(self.m.update(id=1), ("UPDATE person SET age = '?', name = '?' WHERE id_person = ?", '22', 'john', 1))


unittest.main()
