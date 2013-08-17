import unittest
import transaction
import logging

from pyramid import testing

from .models import DBSession

logging.basicConfig(level = logging.INFO)
log = logging.getLogger(__name__)

class TestMyView(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        from .models import (
            Base,
            User,
            )
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            model = User(name='Manuel')
            DBSession.add(model)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_list_users(self):
        from .controllers.hello.v1 import list_users
        request = testing.DummyRequest()
        result = list_users(request)
        self.assertEqual(result['count'], 1)
        self.assertEqual(result['data'][0]['name'], 'Manuel')
