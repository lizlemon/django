"""
Empty database backend for Django.

Django uses this if the database configuration is deliberately empty.
"""

from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.empty.features import DummyDatabaseFeatures

class DatabaseWrapper(BaseDatabaseWrapper):
    # Override the base class implementations with null
    # values. Check any of these to identify an empty connection
    # that is not an error
    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)
        self.features = DummyDatabaseFeatures(self)

    def is_usable(self):
        return False
