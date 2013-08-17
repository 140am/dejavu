import logging
from pyramid.view import view_config, notfound_view_config
from pyramid.response import Response

from sqlalchemy import exc

from hellopyramid import models

log = logging.getLogger(__name__)


@view_config(route_name='users', renderer='hello/list.jinja2', request_method='GET')
@view_config(route_name='users', renderer='json', request_method='GET', xhr=True)
def list_users(request):

    obj_list = models.DBSession.query(
            models.User
        ).all()

    user_list = []
    for obj in obj_list:
        user_list.append({
            'id' : obj.id,
            'name' : obj.name
        })

    return {
        'count' : len(user_list),
        'data' : user_list
    }

@view_config(route_name='users', renderer='json', request_method='POST')
def create_user(request):

    obj = models.User(
        name = request.json.get('name')
    )
    models.DBSession.add(obj)

    try:
        models.DBSession.flush()

    except exc.IntegrityError:
        return {'error' : {
            'message': 'Problem saving new User',
            'code': 500
        }}

    return {
        'id': obj.id,
        'name': obj.name
    }


@view_config(route_name='user', renderer='json', request_method='GET')
def view_user(request):

    obj = models.DBSession.query(
            models.User
        ).filter(
            models.User.id == request.matchdict.get('user_id')
        ).first()

    if not obj:
        return {'error' : {
            'message': 'User not found',
            'code': 404
        }}

    return {
        'id': obj.id,
        'name': obj.name
    }


@notfound_view_config(renderer='json')
def not_found_error(request):
        request.response.status = 404
        return {'error' : {
            'code' : 404,
            'message' : 'Ooops. Invalid request.'
        }}
