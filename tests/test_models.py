#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_django-db-auth0-user
------------

Tests for `django-db-auth0-user` models module.
"""
# TODO: Remove Auth0User model & create an example custom user model. Everyone should have their own custom user model.
import logging


logger = logging.getLogger(__name__)


# @pytest.mark.django_db
# @pytest.mark.usefixtures('one_user')
# class TestOneAuth0User(TransactionTestCase):
#     def test_count_one_auth0_user(self):
#         assert Auth0User.objects.count(auth0_db_refresh=True) == 1

    # def test_all_on_one_auth0_user(self):
    #     auth0 = get_auth0()
    #     auth0_users = list(get_users_from_auth0(auth0))
    #     all_users = list(Auth0User.objects.all())
    #     for remote_user in auth0_users:
    #         """For every user in Auth0, check we find them in the list of all users in the DB."""
    #         assert any([remote_user['user_id'] == db_user.auth0_user_id for db_user in all_users])

    # def test_get_one_auth0_user(self):
    #     auth0 = get_auth0()
    #     auth0_users = get_users_from_auth0(auth0)
    #     auth0_user = list(auth0_users)[0]
    #     auth0_user_id = auth0_user['user_id']
    #     user = Auth0User.objects.get(auth0_user_id=auth0_user_id, auth0_db_refresh=True)
    #     assert auth0_user_id == user.auth0_user_id

    # @pytest.mark.xfail()
    # def test_get_one_auth0_user_that_doesnt_exist_should_fail(self):
    #     auth0 = get_auth0()
    #     auth0_users = get_users_from_auth0(auth0)
    #     auth0_user = list(auth0_users)[0]
    #     auth0_user_id = auth0_user['user_id'] + '_not_going_to_work'
    #     with pytest.raises(Auth0User.DoesNotExist):
    #         user = Auth0User.objects.get(auth0_user_id=auth0_user_id, auth0_db_refresh=True)
    #         # assert auth0_user_id == user.auth0_user_id

    # def test_filter_exists_on_one_auth0_user(self):
    #     auth0 = get_auth0()
    #     auth0_users = get_users_from_auth0(auth0)
    #     auth0_user = list(auth0_users)[0]
    #     auth0_user_id = auth0_user['user_id']
    #     assert Auth0User.objects.filter(auth0_user_id=auth0_user_id).exists(auth0_db_refresh=True) is True

    # @pytest.mark.xfail(raises=AssertionError)
    # def test_filter_exists_on_one_auth0_user_that_doesnt_exist_should_fail(self):
    #     auth0 = get_auth0()
    #     auth0_users = get_users_from_auth0(auth0)
    #     auth0_user = list(auth0_users)[0]
    #     auth0_user_id = auth0_user['user_id'] + '_not_going_to_work'
    #     assert Auth0User.objects.filter(auth0_user_id=auth0_user_id).exists() is False


# @pytest.mark.django_db
# @pytest.mark.usefixtures('five_users')
# class TestFiveAuth0Users(TransactionTestCase):
#     def test_count_five_auth0_users(self):
#         assert Auth0User.objects.count() == 5
#
#     def test_all_on_five_auth0_users(self):
#         auth0 = get_auth0()
#         auth0_users = list(get_users_from_auth0(auth0))
#         all_users = list(Auth0User.objects.all())
#         for remote_user in auth0_users:
#             """For every user in Auth0, check we find them in the list of all users in the DB."""
#             assert any([remote_user['user_id'] == db_user.auth0_user_id for db_user in all_users])


# @pytest.mark.django_db
# @pytest.mark.usefixtures('ten_users')
# class TestTenAuth0Users(TransactionTestCase):
#     def test_count_ten_auth0_users(self):
#         assert Auth0User.objects.count() == 10


# @pytest.mark.django_db
# @pytest.mark.usefixtures('with_33_auth0_users')
# class TestThirtyThreeAuth0Users(TransactionTestCase):
#     def test_count_thirty_three_auth0_users(self):
#         assert Auth0User.objects.count() == 33


# @pytest.mark.django_db
# @pytest.mark.usefixtures('with_100_auth0_users')
# class TestOneHundredAuth0Users(TransactionTestCase):
#     def test_count_one_hundred_auth0_users(self):
#         assert Auth0User.objects.count() == 100


# @pytest.mark.django_db
# class TestDjangoDBAuth0User:
#     def test_count_ten_auth0_users(delete_all_auth0_users, delete_all_django_users, create_ten_users_for_auth0_test):
#         assert Auth0User.objects.count() == 10
#
#     def test_count_one_auth0_user(delete_all_auth0_users, delete_all_django_users, create_one_user_for_auth0_test):
#         assert Auth0User.objects.count() == 1
#
#     def test_count_one_hundred_auth0_users(delete_all_auth0_users, delete_all_django_users, create_one_hundred_users_for_auth0_test):
#         assert Auth0User.objects.count() == 100
#
#     @pytest.mark.xfail
#     def test_create_auth0_user_should_fail(self):
#         new_user = Auth0User()
#         new_user.save()

# user_data = {
#         'app_metadata': {},
#         'clientID': 'dHnrsr87JWuA92kc8vV0VC5MCSfrTcUC',
#         'created_at': '2017-08-29T06:31:41.567Z',
#         'email': 'user1@example.com',
#         'email_verified': False,
#         'identities': [{'connection': 'Username-Password-Authentication',
#                  'isSocial': False,
#                  'provider': 'auth0',
#                  'user_id': '59a50a4dfb030d7b2bf0cde7'}],
#         'name': 'user1@example.com',
#         'nickname': 'user1',
#         'picture': 'https://s.gravatar.com/avatar/111d68d06e2d317b5a59c2c6c5bad808?s=480&r=pg&d=https%3A%2F%2Fcdn.auth0.com%2Favatars%2Fus.png',
#         'sub': 'auth0|59a50a4dfb030d7b2bf0cde7',
#         'updated_at': '2017-08-29T08:15:25.378Z',
#         'user_id': 'auth0|59a50a4dfb030d7b2bf0cde7',
#         'user_metadata': {}
#     }
#

# @pytest.mark.django_db
# def test_save_auth0_user():
#     user = Auth0User(**{Auth0User.USERNAME_FIELD: user_data['user_id'], Auth0User.EMAIL_FIELD: user_data['email']})
#     user.save()
#     assert user.is_active
