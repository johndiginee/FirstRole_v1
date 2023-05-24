from django.test import TestCase
from company.models import Company
from users.models import User

class CompanyTestCase(TestCase):

    # Tests that a Company object can be created with all attributes filled in correctly.
    def test_create_company_object(self):
        user = User.objects.create(email="test@test.com", is_recruiter=True)
        company = Company.objects.create(user=user, name="Test Company", est_date=2020, city="Test City", state="Test State")
        self.assertEqual(company.name, "Test Company")
        self.assertEqual(company.est_date, 2020)
        self.assertEqual(company.city, "Test City")
        self.assertEqual(company.state, "Test State")

    # Tests that the name attribute of a Company object can be accessed.
    def test_access_name_attribute(self):
        user = User.objects.create(email="test@test.com", is_recruiter=True)
        company = Company.objects.create(user=user, name="Test Company", est_date=2020, city="Test City", state="Test State")
        self.assertEqual(company.name, "Test Company")

    # # Tests that a Company object cannot be created with null or blank attributes.
    # def test_create_company_object_with_null_or_blank_attributes(self):
    #     user = User.objects.create(email="test@test.com", is_recruiter=True)
    #     with self.assertRaises(Exception):
    #         Company.objects.create(user=user, name=None, est_date=2020, city="Test City", state="Test State")
    #     with self.assertRaises(Exception):
    #         Company.objects.create(user=user, name="", est_date=2020, city="Test City", state="Test State")

    # Tests that a Company object cannot be created with an invalid establishment date (e.g. negative integer).
    def test_create_company_object_with_invalid_establishment_date(self):
        user = User.objects.create(email="test@test.com", is_recruiter=True)
        with self.assertRaises(Exception):
            Company.objects.create(user=user, name="Test Company", est_date=-2020, city="Test City", state="Test State")

    # Tests that a Company object can be updated and deleted.
    def test_update_and_delete_company_object(self):
        user = User.objects.create(email="test@test.com", is_recruiter=True)
        company = Company.objects.create(user=user, name="Test Company", est_date=2020, city="Test City", state="Test State")
        company.name = "New Test Company"
        company.save()
        self.assertEqual(company.name, "New Test Company")
        company.delete()
        with self.assertRaises(Company.DoesNotExist):
            Company.objects.get(user=user)

    # Tests that a Company object cannot be created without a corresponding User object.
    def test_create_company_object_without_corresponding_user_object(self):
        with self.assertRaises(Exception):
            Company.objects.create(name="Test Company", est_date=2020, city="Test City", state="Test State")