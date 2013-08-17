from hellopyramid.controllers.hello import v1


def includeme(config):

    config.add_route('users', '/hello')
    config.add_route('user', '/hello/{user_id}')

    config.scan()
