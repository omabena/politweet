from .twitter import TwitterApi


def initialize_routes(api):
    api.add_resource(TwitterApi, '/')
