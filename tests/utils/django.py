from test_app.models import Auth0User
import logging


logger = logging.getLogger(__name__)


def delete_all_django_users():
    logger.info("Attempting to delete all Django users.")
    user_list = list(Auth0User.objects.all())
    logger.info('Found {} existing django users.'.format(len(user_list)))
    for user in user_list:
        user.delete()
