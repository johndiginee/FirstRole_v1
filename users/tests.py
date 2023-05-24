from django.test import TestCase
from users.models import User

class UserTestCase(TestCase):
    # Tests that a user can be created with a valid email and default values for all other attributes.
    def test_create_user_with_valid_email_and_default_values(self):
        user = User.objects.create(email='test@example.com')
        self.assertEqual(user.email, 'test@example.com')
        self.assertFalse(user.is_recruiter)
        self.assertFalse(user.is_applicant)
        self.assertFalse(user.has_resume)
        self.assertFalse(user.has_company)

    # Tests that a user can be created with a valid email and one or more attributes set to True.
    def test_create_user_with_valid_email_and_setting_attributes_to_true(self):
        user = User.objects.create(email='test@example.com', is_recruiter=True, has_resume=True)
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.is_recruiter)
        self.assertFalse(user.is_applicant)
        self.assertTrue(user.has_resume)
        self.assertFalse(user.has_company)

    # # Tests that a user cannot be created with an empty email.
    # def test_create_user_with_empty_email(self):
    #     with self.assertRaises(ValueError):
    #         User.objects.create(email='')

    # Tests that a user cannot be created with an email that already exists in the database.
    def test_create_user_with_existing_email(self):
        User.objects.create(email='test@example.com')
        with self.assertRaises(Exception):
            User.objects.create(email='test@example.com')

    # Tests that a user can be created with all attributes set to False.
    def test_create_user_with_all_attributes_set_to_false(self):
        user = User.objects.create(email='test@example.com', is_recruiter=False, is_applicant=False, has_resume=False, has_company=False)
        self.assertEqual(user.email, 'test@example.com')
        self.assertFalse(user.is_recruiter)
        self.assertFalse(user.is_applicant)
        self.assertFalse(user.has_resume)
        self.assertFalse(user.has_company)

    # Tests that a user can be authenticated using email and password.
    def test_user_authentication(self):
        user = User.objects.create(email='test@example.com')
        user.set_password('password')
        user.save()
        authenticated_user = User.objects.get(email='test@example.com')
        self.assertTrue(authenticated_user.check_password('password'))