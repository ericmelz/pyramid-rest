from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_chameleon')
        register_routes(config)
    return config.make_wsgi_app()


def register_routes(config):
    config.include('.routes')
    config.add_static_view('static', 'static', cache_max_age=1)
    config.scan()
