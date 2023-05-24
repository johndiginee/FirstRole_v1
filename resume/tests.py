from django.test import TestCase
from resume.models import Resume
from users.models import User

class ResumeTestCase(TestCase):
    # Tests that a Resume object can be created with all required fields filled in.
    def test_create_resume_with_required_fields(self):
        user = User.objects.create(email='test@test.com', is_applicant=True)
        resume = Resume.objects.create(user=user, first_name='John', surname='Doe', job_title='Software Engineer')
        self.assertEqual(resume.user, user)
        self.assertEqual(resume.first_name, 'John')
        self.assertEqual(resume.surname, 'Doe')
        self.assertEqual(resume.job_title, 'Software Engineer')

    # Tests that a Resume object can be updated with new information.
    def test_update_resume(self):
        user = User.objects.create(email='test@test.com', is_applicant=True)
        resume = Resume.objects.create(user=user, first_name='John', surname='Doe', job_title='Software Engineer')
        resume.first_name = 'Jane'
        resume.surname = 'Smith'
        resume.job_title = 'Web Developer'
        resume.save()
        self.assertEqual(resume.first_name, 'Jane')
        self.assertEqual(resume.surname, 'Smith')
        self.assertEqual(resume.job_title, 'Web Developer')

    # Tests that a Resume object can be created with no optional fields filled in.
    def test_create_resume_with_no_optional_fields(self):
        user = User.objects.create(email='test@test.com', is_applicant=True)
        resume = Resume.objects.create(user=user)
        self.assertEqual(resume.user, user)

    # Tests that a Resume object can be created with a very long name or location.
    def test_create_resume_with_long_name_or_location(self):
        user = User.objects.create(email='test@test.com', is_applicant=True)
        long_name = 'a' * 101
        long_location = 'b' * 101
        resume = Resume.objects.create(user=user, first_name=long_name, surname=long_name, location=long_location)
        self.assertEqual(resume.user, user)
        self.assertEqual(resume.first_name, long_name)
        self.assertEqual(resume.surname, long_name)
        self.assertEqual(resume.location, long_location)

    # Tests that a Resume object can be deleted.
    def test_delete_resume(self):
        user = User.objects.create(email='test@test.com', is_applicant=True)
        resume = Resume.objects.create(user=user, first_name='John', surname='Doe', job_title='Software Engineer')
        resume.delete()
        self.assertFalse(Resume.objects.filter(user=user).exists())

    # Tests that a very large file can be uploaded to the upload_resume field.
    # def test_upload_large_file_to_upload_resume(self):
    #     user = User.objects.create(email='test@test.com', is_applicant=True)
    #     with open('large_file.pdf', 'wb') as f:
    #         f.write(b'a' * 1024 * 1024 * 10) # 10 MB file
    #     with open('large_file.pdf', 'rb') as f:
    #         resume = Resume.objects.create(user=user, upload_resume=f)
    #         self.assertEqual(resume.user, user)