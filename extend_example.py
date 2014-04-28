from mapper import ObjectMapper

class Person(object):

    def __init__(self):

        self.name = 'john'
        self.age = 22

        #this properties are ignored
        self._some_information = 'Not saved in table'
        self.__other_stuff = 'Also ignored'


class PersonMapper(ObjectMapper):
    """
        This class overrides get_table and get_id methods to
        customize the ObjectMapper according to the tables I have.

        Usage demo and tests

        >>> p = Person()
        >>> m = PersonMapper(p)

        >>> m.insert()
        ("INSERT INTO people(age,name) VALUES ('?','?')", '22', 'john')

        >>> m.get_by_id(id=1)
        ('SELECT age, name FROM people WHERE id_people = ?', 1)

        >>> m.get_all()
        'SELECT age, name FROM people'

        >>> m.delete(id=1)
        ('DELETE FROM people WHERE id_people = ?', 1)

        >>> m.update(id=1)
        ("UPDATE people SET age = '?', name = '?' WHERE id_people = ?", '22', 'john', 1)
    """

    def get_table(self):
        """
            Returns the table name
        """

        return "people"

    def get_id(self):
        """
            Returns the id field name
        """

        return "id_people"


if __name__ == '__main__':

    import doctest
    doctest.testmod()
