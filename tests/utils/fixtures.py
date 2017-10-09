from tests.utils.auth0 import delete_all_auth0_users as delete_all_auth0_users_via_api
from tests.utils.auth0 import create_auth0_test_users
from tests.utils.auth0 import create_and_confirm_auth0_test_users
from tests.utils.auth0 import delete_all_auth0_users_with_confirmation
from tests.utils.auth0 import create_multiple_auth0_users_and_confirm
from tests.utils.auth0 import pause_and_confirm_total_auth0_users
from tests.utils.django import delete_all_django_users
from test_app.models import Auth0User
import pytest
import logging


logger = logging.getLogger(__name__)


DELAY = 15


@pytest.fixture(scope="class")
def one_auth0_user(request):
    """
    Pytest fixture providing one Auth0 user for testing.

    Create a new user in Auth0 and add it to the class of our requesting test case class at runtime.
    This is a little different than most PyTest fixtures because are working around the fact that
    we are using SeleniumTestCase for some tests, which as a subclass of TestCase cannot use normal
    PyTest fixture based parametrization.

    :param request:
    :return:
    """
    users = create_multiple_auth0_users_and_confirm(1)
    request.cls.user = users[0]


@pytest.fixture(scope='function')
def delete_all_auth0_users():
    logger.info('Deleting all auth0 users.')
    delete_all_auth0_users_via_api()
    yield
    logger.info('Deleting all auth0 users.')
    delete_all_auth0_users_via_api()


@pytest.fixture(scope='function')
def delete_all_django_users():
    logger.info('Deleting Django User objects.')
    Auth0User.objects.all().delete()
    yield
    logger.info('Deleting Django User objects.')
    Auth0User.objects.all().delete()


@pytest.fixture(scope='function')
def cleanup_django_and_auth0():
    logger.info('Deleting all auth0 users.')
    delete_all_auth0_users_via_api()
    logger.info('Deleting Django User objects.')
    Auth0User.objects.all().delete()
    yield
    logger.info('Deleting Django User objects.')
    Auth0User.objects.all().delete()
    logger.info('Deleting all auth0 users.')
    delete_all_auth0_users_via_api()


@pytest.fixture(scope='function')
def one_user():
    number_of_users = 1
    logger.info('Start of one_user() fixture.')
    logger.info('Deleting all auth0 users.')
    delete_all_auth0_users_with_confirmation()
    logger.info('Deleting Django User objects.')
    Auth0User.objects.all().delete()
    create_multiple_auth0_users_and_confirm(number_of_users)
    pause_and_confirm_total_auth0_users(DELAY, number_of_users)
    yield
    logger.info('Deleting Django User objects.')
    Auth0User.objects.all().delete()
    logger.info('Deleting all auth0 users.')
    delete_all_auth0_users_with_confirmation()
    logger.info('End of one_user() fixture.')


@pytest.fixture(scope='function')
def five_users():
    number_of_users = 5
    logger.info('Start of five_users() fixture.')
    logger.info('Deleting all auth0 users.')
    delete_all_auth0_users_with_confirmation()
    logger.info('Deleting Django User objects.')
    Auth0User.objects.all().delete()
    create_multiple_auth0_users_and_confirm(number_of_users)
    pause_and_confirm_total_auth0_users(DELAY, number_of_users)
    yield
    logger.info('Deleting Django User objects.')
    Auth0User.objects.all().delete()
    logger.info('Deleting all auth0 users.')
    delete_all_auth0_users_with_confirmation()
    logger.info('End of five_users() fixture.')


@pytest.fixture(scope='function')
def ten_users():
    number_of_users = 10
    logger.info('Start of ten_users() fixture.')
    logger.info('Deleting all auth0 users.')
    delete_all_auth0_users_with_confirmation()
    logger.info('Deleting Django User objects.')
    Auth0User.objects.all().delete()
    create_multiple_auth0_users_and_confirm(number_of_users)
    pause_and_confirm_total_auth0_users(DELAY, number_of_users)
    yield
    logger.info('Deleting Django User objects.')
    Auth0User.objects.all().delete()
    logger.info('Deleting all auth0 users.')
    delete_all_auth0_users_with_confirmation()
    logger.info('End of ten_users() fixture.')


@pytest.fixture(scope='function')
def with_33_auth0_users():
    number_of_users = 33
    logger.info('Start of ten_users() fixture.')
    logger.info('Deleting all auth0 users.')
    delete_all_auth0_users_with_confirmation()
    logger.info('Deleting Django User objects.')
    Auth0User.objects.all().delete()
    create_multiple_auth0_users_and_confirm(number_of_users)
    pause_and_confirm_total_auth0_users(DELAY, number_of_users)
    yield
    logger.info('Deleting Django User objects.')
    Auth0User.objects.all().delete()
    logger.info('Deleting all auth0 users.')
    delete_all_auth0_users_with_confirmation()
    logger.info('End of ten_users() fixture.')


@pytest.fixture(scope='function')
def with_100_auth0_users():
    number_of_users = 100
    logger.info('Start of ten_users() fixture.')
    logger.info('Deleting all auth0 users.')
    delete_all_auth0_users_with_confirmation()
    logger.info('Deleting Django User objects.')
    Auth0User.objects.all().delete()
    create_multiple_auth0_users_and_confirm(number_of_users)
    pause_and_confirm_total_auth0_users(DELAY, number_of_users)
    yield
    logger.info('Deleting Django User objects.')
    Auth0User.objects.all().delete()
    logger.info('Deleting all auth0 users.')
    delete_all_auth0_users_with_confirmation()
    logger.info('End of ten_users() fixture.')
