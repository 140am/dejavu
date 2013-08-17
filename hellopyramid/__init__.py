from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns the Pyramid WSGI application.
    """
    # Create the Pyramid Configurator.
    config = Configurator(settings=settings)

    # http://docs.pylonsproject.org/projects/pyramid_exclog/dev/api.html#pyramid_exclog.includeme
    config.include('pyramid_exclog')
    # https://pylonsproject.org/projects/pyramid_tm/dev/api.html#pyramid_tm.includeme
    config.include('pyramid_tm')
    # https://docs.pylonsproject.org/projects/pyramid_jinja2/dev/api.html#pyramid_jinja2.includeme
    config.include('pyramid_jinja2')

    # Initialize sqlalchemy database engine
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    # view handler
    config.include('hellopyramid.controllers.hello')

    # jinja2 configuration
    config.add_jinja2_search_path("hellopyramid:templates")

    # static content route
    config.add_static_view('static', 'static', cache_max_age=3600)

    return config.make_wsgi_app()
