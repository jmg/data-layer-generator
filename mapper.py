"""
    Python data layer generator
    Author: Juan MAnuel Garcia <jmg.utn@gmail.com>
"""

class ObjectMapper(object):

    def __init__(self, entity):
        self.entity = entity

    def _get_pairs(self):
        return [(k,str(v)) for k,v in self.entity.__dict__.iteritems() if not k.startswith("_") and not k.startswith("__")]

    def _get_names(self):
        return [pair[0] for pair in self._get_pairs()]

    def _get_values(self):
        return [pair[1] for pair in self._get_pairs()]

    def _get_names_values(self):
        return self._get_names(), self._get_values()

    def insert(self):
        names, values = self._get_names_values()
        names = "%s" % ",".join(names)
        values = "'%s'" % "','".join(values)
        return "INSERT INTO %s(%s) VALUES (%s)" % (self.get_table(), names, values)

    def update(self, id):
        pairs = self._get_pairs()
        fields = ", ".join(["%s = '%s'" % (k,v) for k,v in pairs])
        return "UPDATE %s SET %s WHERE %s = '%s'" % (self.get_table(), fields, self.get_id(), id)

    def delete(self, id):
        return "DELETE FROM %s WHERE %s = %s" % (self.get_table(), self.get_id(), id)

    def get_all(self):
        names = ", ".join(self._get_names())
        return "SELECT %s FROM %s" % (names, self.get_table())

    def get_by_id(self, id):
        names = ", ".join(self._get_names())
        return "SELECT %s FROM %s WHERE %s = %s" % (names, self.get_table(), self.get_id(), id)

    #Overridables

    #You can Extend from this class and override the following methods in order to configurate
    #the table name and the id_name

    def get_table(self):
        return self.entity.__class__.__name__.lower()

    def get_id(self):
        return "id_%s" % self.entity.__class__.__name__.lower()
