import unittest
import transaction
import logging

from pyramid import testing

from .models import DBSession

logging.basicConfig(level = logging.INFO)
log = logging.getLogger(__name__)

class TestControllerHello(unittest.TestCase):

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

	def test_failed_request(self):
		from .controllers.hello.v1 import not_found_error
		request = testing.DummyRequest()
		result = not_found_error(request)
		self.assertEqual(result['error']['code'], 404)
		self.assertEqual(result['error']['message'], 'Ooops. Invalid request.')

	def test_list_users(self):
		from .controllers.hello.v1 import list_users
		request = testing.DummyRequest()
		result = list_users(request)
		self.assertEqual(result['count'], 1)
		self.assertEqual(result['data'][0]['name'], 'Manuel')

	def test_get_single_user(self):
		from .controllers.hello.v1 import view_user
		request = testing.DummyRequest()
		request.matchdict = {'user_id': '1'}
		result = view_user(request)
		self.assertEqual(result['id'], 1)
		self.assertEqual(result['name'], 'Manuel')

	def test_failed_get_single_user(self):
		from .controllers.hello.v1 import view_user
		request = testing.DummyRequest()
		request.matchdict = {'user_id': '10'}
		result = view_user(request)
		self.assertEqual(result['error']['code'], 404)
		self.assertEqual(result['error']['message'], 'User not found')

	def test_create_user(self):
		from .controllers.hello.v1 import create_user
		request = testing.DummyRequest()
		request.json = {'name' : 'New User'}
		result = create_user(request)
		log.info('tt: %s' % result)
		self.assertEqual(result['id'], 2)
		self.assertEqual(result['name'], 'New User')

	def test_failed_create_user(self):
		from .controllers.hello.v1 import create_user
		request = testing.DummyRequest()
		request.json = {'name' : 'New User'}
		result = create_user(request)
		request = testing.DummyRequest()
		request.json = {'name' : 'New User'}
		result = create_user(request)
		self.assertEqual(result['error']['code'], 500)
		self.assertEqual(result['error']['message'], 'Problem saving new User')


class TestModel(unittest.TestCase):

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

	def test_model_description(self):

		from .models import (
			User,
			)

		result = DBSession.query(
				User
			).filter(
				User.id == 1
			).first()

		self.assertEqual(str(result), "<User('Manuel')>")
