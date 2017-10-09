

def get_username(strategy, details, backend, user=None, *args, **kwargs):
    if not user:
        username = None
        auth0_user_id_as_username = backend.AUTH0_USER_ID_IS_DJANGO_USERNAME
        if auth0_user_id_as_username:
            # This assumes the 'uid' has been populated earlier in the pipeline.
            # If this stops working, using backend.id_token['user_id'] instead should fix this.
            username = kwargs.get('uid')
        if username is not None:
            # We don't bother checking if this is unique, because we are assuming that
            # 'social_core.pipeline.user.get_username' is in the social auth pipeline and will check for us.
            return {'username': username}
    return None
