import logging
import random
from time import sleep

from auth0.v3.exceptions import Auth0Error
from auth0.v3.management import Auth0
from django.conf import settings
from elizabeth import Personal
from retryz import retry

from django_auth0_user.auth0.api import AUTH0_TOKEN_CACHE, get_auth0, get_users_from_auth0, get_auth0_user

logger = logging.getLogger(__name__)


person = Personal('en')


@retry(wait=5, timeout=300, on_return=False)
def confirm_user_total(desired_total, auth0=None):
    if auth0 is None:
        auth0 = get_auth0()
    total_users = len(list(get_users_from_auth0(auth0)))
    return total_users == desired_total


def create_auth0_test_users(number_of_users, overrides=None, auth0=None):
    if auth0 is None:
        auth0 = get_auth0()
    auth0_users = []
    for i in range(number_of_users):
        gender = random.choice(['male', 'female'])
        test_user_details = {
            "connection": "Username-Password-Authentication",
            # "username": person.username(gender=gender),
            "password": person.password(length=8),
            "email": person.email(gender=gender, domains=['@example.com', ]),
            "email_verified": False,
            "verify_email": False,
            # "phone_number": person.telephone(mask="+############"),
            # "phone_verified": False,
            "user_metadata": {},
            "app_metadata": {},
        }
        if overrides is not None:
            test_user_details.update(overrides)
        user = auth0.users.create(body=test_user_details)
        logger.info("generated a new auth0 user: {}".format(user))
        # confirming user can be read
        retrieved_user = auth0.users.get(user['user_id'])
        auth0_users.append(retrieved_user)
        logger.info("Retrieved new auth0 user: {}".format(retrieved_user))


@retry(wait=5, timeout=300, on_return=False)
def create_and_confirm_auth0_test_users(desired_total, auth0=None):
    if auth0 is None:
        auth0 = get_auth0()
    current_user_total = len(list(get_users_from_auth0(auth0)))
    difference = desired_total - current_user_total
    if difference > 0:
        for i in range(difference):
            gender = random.choice(['male', 'female'])
            test_user_details = {
                "connection": "Username-Password-Authentication",
                # "username": person.username(gender=gender),
                "password": person.password(length=8),
                "email": person.email(gender=gender, domains=['@example.com', ]),
                "email_verified": False,
                "verify_email": False,
                # "phone_number": person.telephone(mask="+############"),
                # "phone_verified": False,
                "user_metadata": {},
                "app_metadata": {},
            }
            user = auth0.users.create(body=test_user_details)
            logger.info("generated a new auth0 user: {}".format(user))

    total_users = len(list(get_users_from_auth0(auth0)))
    return total_users == desired_total


def create_auth0_user(auth0=None, overrides=None):
    if auth0 is None:
        auth0 = get_auth0()
    gender = random.choice(['male', 'female'])
    test_user_details = {
        "connection": "Username-Password-Authentication",
        # "username": person.username(gender=gender),
        "password": person.password(length=8),
        "email": person.email(gender=gender, domains=['@example.com', ]),
        "email_verified": False,
        "verify_email": False,
        # "phone_number": person.telephone(mask="+############"),
        # "phone_verified": False,
        "user_metadata": {},
        "app_metadata": {},
    }
    if overrides is not None:
        test_user_details.update(overrides)
    user = auth0.users.create(body=test_user_details)
    logger.info("generated a new auth0 user: {}".format(user))


def create_ten_auth0_users():
    auth0 = Auth0(settings.AUTH0_USER_DOMAIN, AUTH0_TOKEN_CACHE.auth0_management_api_token)
    for i in range(10):
        create_auth0_user(auth0)


def delete_all_auth0_users():
    auth0 = Auth0(settings.AUTH0_USER_DOMAIN, AUTH0_TOKEN_CACHE.auth0_management_api_token)
    all_auth0_users = list(get_users_from_auth0(auth0))
    while len(list(get_users_from_auth0(auth0))) > 0:
        for user in all_auth0_users:
            auth0.users.delete(user['user_id'])

    check_empty = list(get_users_from_auth0(auth0))
    logger.info("{} users remain.".format(len(check_empty)))


def delete_auth0_user_and_confirm(user, auth0=None):
    if auth0 is None:
        auth0 = get_auth0()

    user_id = user['user_id']
    deletion_response = auth0.users.delete(user_id)
    logger.info("Deletion Response: {}".format(deletion_response))

    @retry(wait=5, timeout=300, on_return=False)
    def confirm(target_user_id):
        try:
            query_response = auth0.users.get(target_user_id)
            logger.info("Found User: {}".format(query_response))
        except Auth0Error as err:
            if str(err) == "404: The user does not exist.":
                logger.info("Response: {}".format(err))
                return True
        return False

    confirm(user_id)


# @retry(wait=1, timeout=30, on_return=False)
def delete_all_auth0_users_with_confirmation():
    logger.info("Attempting to delete all auth0 users, with confirmation.")
    auth0 = get_auth0()
    all_auth0_users = list(get_users_from_auth0(auth0))
    for user in all_auth0_users:
        delete_auth0_user_and_confirm(user, auth0=auth0)
        logger.info("Deleted: {}".format(user['user_id']))
    total_users = len(list(get_users_from_auth0(auth0)))
    logger.info("{} users remain.".format(total_users))
    return total_users == 0


def create_auth0_user_and_confirm(auth0=None):
    if auth0 is None:
        auth0 = get_auth0()

    gender = random.choice(['male', 'female'])
    test_user_details = {
        "connection": "Username-Password-Authentication",
        # "username": person.username(gender=gender),
        "password": person.password(length=8),
        "email": person.email(gender=gender, domains=['@example.com', ]),
        "email_verified": False,
        "verify_email": False,
        # "phone_number": person.telephone(mask="+############"),
        # "phone_verified": False,
        "user_metadata": {},
        "app_metadata": {},
    }
    user = auth0.users.create(body=test_user_details)
    logger.info("generated a new auth0 user: {}".format(user))

    @retry(wait=5, timeout=300, on_return=False)
    def confirm(target_user_id):
        try:
            query_response = auth0.users.get(target_user_id)
            logger.info("Found User: {}".format(query_response))
            return True
        except Auth0Error as err:
            logger.info("Response: {}".format(err))
            return False

    confirm(user['user_id'])


def create_multiple_auth0_users_and_confirm(number_of_users_to_create, auth0=None):
    logger.info("Attempting to create {} auth0 users, with confirmation.".format(number_of_users_to_create))
    if auth0 is None:
        auth0 = get_auth0()

    user_list = []
    for i in range(number_of_users_to_create):
        gender = random.choice(['male', 'female'])
        test_user_details = {
            "connection": "Username-Password-Authentication",
            # "username": person.username(gender=gender),
            "password": person.password(length=8),
            "email": person.email(gender=gender, domains=['@example.com', ]),
            "email_verified": False,
            "verify_email": False,
            # "phone_number": person.telephone(mask="+############"),
            # "phone_verified": False,
            "user_metadata": {},
            "app_metadata": {},
        }
        user = auth0.users.create(body=test_user_details)
        logger.info("generated a new auth0 user: {}".format(user))
        user_list.append({**test_user_details, **user})

    # TODO: Pass in a list of users and query to check they are all in auth0, retry until they are all in auth0.
    @retry(wait=5, timeout=300, on_return=False)
    def confirm(_user_list):
        _user_ids = [_x['user_id'] for _x in _user_list]
        _retrieved_user_list = []
        _retrieved_user_ids = []
        for _user in _user_list:
            _auth0_user = get_auth0_user(_user['user_id'])
            _retrieved_user_ids.append(_auth0_user['user_id'])
            _retrieved_user_list.append(_auth0_user)

        if set(_user_ids) == set(_retrieved_user_ids):
            logger.info("Found all new users users. {}".format(_user_ids))
            return True
        return False

    confirm(user_list)
    return user_list


def pause_and_confirm_total_auth0_users(pause_duration, desired_total_users, auth0=None):
    if auth0 is None:
        auth0 = get_auth0()
    logger.info('Pausing for {} seconds'.format(pause_duration))
    sleep(pause_duration)
    logger.info('Confirming {} Auth0 users'.format(desired_total_users))

    @retry(wait=1, timeout=60, on_return=False)
    def confirm(desired_total):
        number_of_users = len(list(get_users_from_auth0(auth0)))
        logger.info("Found {} users.".format(number_of_users))
        if number_of_users == desired_total:
            return True
        return False

    confirm(desired_total_users)

