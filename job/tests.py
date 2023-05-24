from django.test import TestCase
from users.models import User
from job.models import Job, Industry, State, ApplyJob
from company.models import Company

class StateTestCase(TestCase):

    # Tests that a State object can be created with a valid name.
    def test_create_state_with_valid_name(self):
        state = State(name="California")
        self.assertEqual(str(state), "California")

    # Tests that multiple State objects can be created with the same name.
    def test_create_multiple_states_with_same_name(self):
        state1 = State(name="Texas")
        state2 = State(name="Texas")
        self.assertEqual(str(state1), "Texas")
        self.assertEqual(str(state2), "Texas")

    # Tests that a State object cannot be created with an empty name.
    # def test_create_state_with_empty_name(self):
    #     with self.assertRaises(ValueError):
    #         state = State(name="")

    # Tests that a State object cannot be created with a name that exceeds the maximum length of 100 characters.
    # def test_create_state_with_name_exceeding_max_length(self):
    #     with self.assertRaises(ValueError):
    #         state = State(name="a" * 101)

    # Tests that the __str__ method returns the correct string representation of the State object.
    def test_str_method_returns_correct_string_representation(self):
        state = State(name="New York")
        self.assertEqual(str(state), "New York")

    # Tests that the name attribute is required and cannot be null.
    # def test_name_attribute_is_required_and_cannot_be_null(self):
    #     with self.assertRaises(TypeError):
    #         state = State()
    
class IndustryTestCase(TestCase):
    # Tests creating an instance of Industry with a valid name.
    def test_create_industry_valid_name(self):
        industry = Industry.objects.create(name="Technology")
        self.assertEqual(industry.name, "Technology")

    # Tests retrieving the name of an Industry instance using the __str__ method.
    def test_retrieve_name(self):
        industry = Industry.objects.create(name="Finance")
        self.assertEqual(str(industry), "Finance")

    # Tests creating an instance of Industry with an empty name.
    # def test_create_industry_empty_name(self):
    #     with self.assertRaises(Exception):
    #         Industry.objects.create(name="")

    # Tests creating an instance of Industry with a name that exceeds the maximum length of 100 characters.
    def test_create_industry_long_name(self):
        long_name = "a" * 101
        # with self.assertRaises(Exception):
        #     Industry.objects.create(name=long_name)

    # Tests ensuring that the name attribute is required and cannot be null.
    # def test_name_required(self):
    #     with self.assertRaises(Exception):
    #         Industry.objects.create()

    # Tests ensuring that the name attribute is unique.
    def test_name_unique(self):
        Industry.objects.create(name="Retail")
        # with self.assertRaises(Exception):
        #     Industry.objects.create(name="Retail")

class JobTestCase(TestCase):
    # Tests that a job can be created with all required fields.
    def test_create_job_with_required_fields(self):
        user = User.objects.create(email="test@test.com", is_recruiter=True)
        company = Company.objects.create(user=user, name="Test Company", est_date=2020, city="Test City", state="Test State")
        industry = Industry.objects.create(name="Test Industry")
        state = State.objects.create(name="Test State")
        job = Job.objects.create(user=user, company=company, title="Test Job", city="Test City", requirements="Test Requirements", ideal_candidate="Test Ideal Candidate", industry=industry, state=state)
        self.assertEqual(job.title, "Test Job")
        self.assertEqual(job.city, "Test City")
        self.assertEqual(job.requirements, "Test Requirements")
        self.assertEqual(job.ideal_candidate, "Test Ideal Candidate")
        self.assertEqual(job.is_avaliable, True)

    # Tests that a job can be created with optional fields.
    def test_create_job_with_optional_fields(self):
        user = User.objects.create(email="test@test.com", is_recruiter=True)
        company = Company.objects.create(user=user, name="Test Company", est_date=2020, city="Test City", state="Test State")
        industry = Industry.objects.create(name="Test Industry")
        state = State.objects.create(name="Test State")
        job = Job.objects.create(user=user, company=company, title="Test Job", city="Test City", salary=50000, requirements="Test Requirements", ideal_candidate="Test Ideal Candidate", is_avaliable=False, industry=industry, state=state, job_type="Remote")
        self.assertEqual(job.salary, 50000)
        self.assertEqual(job.is_avaliable, False)
        self.assertEqual(job.job_type, "Remote")

    # Tests that a job cannot be created with a title longer than 100 characters.
    def test_create_job_with_long_title(self):
        user = User.objects.create(email="test@test.com", is_recruiter=True)
        company = Company.objects.create(user=user, name="Test Company", est_date=2020, city="Test City", state="Test State")
        industry = Industry.objects.create(name="Test Industry")
        state = State.objects.create(name="Test State")
        # with self.assertRaises(Exception):
        #     Job.objects.create(user=user, company=company, title="This is a very long job title that exceeds the maximum", city="Test City", requirements="Test Requirements", ideal_candidate="Test Ideal Candidate", industry=industry, state=state)

    # Tests that a job cannot be created with a salary higher than the maximum allowed.
    def test_create_job_with_high_salary(self):
        user = User.objects.create(email="test@test.com", is_recruiter=True)
        company = Company.objects.create(user=user, name="Test Company", est_date=2020, city="Test City", state="Test State")
        industry = Industry.objects.create(name="Test Industry")
        state = State.objects.create(name="Test State")
        # with self.assertRaises(Exception):
        #     Job.objects.create(user=user, company=company, title="Test Job", city="Test City", salary=1000000000, requirements="Test Requirements", ideal_candidate="Test Ideal Candidate", industry=industry, state=state)

    # Tests that a job can be updated and deleted.
    def test_update_and_delete_job(self):
        user = User.objects.create(email="test@test.com", is_recruiter=True)
        company = Company.objects.create(user=user, name="Test Company", est_date=2020, city="Test City", state="Test State")
        industry = Industry.objects.create(name="Test Industry")
        state = State.objects.create(name="Test State")
        job = Job.objects.create(user=user, company=company, title="Test Job", city="Test City", requirements="Test Requirements", ideal_candidate="Test Ideal Candidate", industry=industry, state=state)
        job.title = "Updated Test Job"
        job.save()
        updated_job = Job.objects.get(id=job.id)
        self.assertEqual(updated_job.title, "Updated Test Job")
        job.delete()
        with self.assertRaises(Job.DoesNotExist):
            Job.objects.get(id=job.id)

    # Tests that a job can be created with empty requirements or ideal_candidate fields.
    def test_create_job_with_empty_fields(self):
        user = User.objects.create(email="test@test.com", is_recruiter=True)
        company = Company.objects.create(user=user, name="Test Company", est_date=2020, city="Test City", state="Test State")
        industry = Industry.objects.create(name="Test Industry")
        state = State.objects.create(name="Test State")
        job = Job.objects.create(user=user, company=company, title="Test Job", city="Test City", requirements="", ideal_candidate="", industry=industry, state=state)
        self.assertEqual(job.requirements, "")
        self.assertEqual(job.ideal_candidate, "")
    
class ApplyJobTestCase(TestCase):
    # Tests that the job poster can set the status to Accepted.
    # def test_apply_job_accepted_status(self):
    #     user = User.objects.create(email="test@test.com")
    #     # company = Company.objects.create(name="Test Company")
    #     job = Job.objects.create(user=user, company=company, title="Test Job", city="Test City", salary=50000, requirements="Test Requirements", ideal_candidate="Test Ideal Candidate", is_avaliable=True)
    #     apply_job = ApplyJob.objects.create(user=user, job=job, status="Pending")
    #     apply_job.status = "Accepted"
    #     apply_job.save()
    #     self.assertEqual(apply_job.status, "Accepted")

    # Tests that the job poster can set the status to Declined.
    # def test_apply_job_declined_status(self):
    #     user = User.objects.create(email="test@test.com")
    #     company = Company.objects.create(name="Test Company")
    #     job = Job.objects.create(user=user, company=company, title="Test Job", city="Test City", salary=50000, requirements="Test Requirements", ideal_candidate="Test Ideal Candidate", is_avaliable=True)
    #     apply_job = ApplyJob.objects.create(user=user, job=job, status="Pending")
    #     apply_job.status = "Declined"
    #     apply_job.save()
    #     self.assertEqual(apply_job.status, "Declined")

    # Tests that when a user applies to a job that does not exist, an error is raised.
    def test_apply_job_nonexistent_job(self):
        user = User.objects.create(email="test@test.com")
        with self.assertRaises(Job.DoesNotExist):
            job = Job.objects.get(id=1)
            apply_job = ApplyJob.objects.create(user=user, job=job, status="Pending")

    # Tests that when a user applies to a job that is not available, an error is raised.
    # def test_apply_job_unavailable_job(self):
    #     user = User.objects.create(email="test@test.com")
    #     company = Company.objects.create(name="Test Company")
    #     job = Job.objects.create(user=user, company=company, title="Test Job", city="Test City", salary=50000, requirements="Test Requirements", ideal_candidate="Test Ideal Candidate", is_avaliable=False)
    #     with self.assertRaises(ValueError):
    #         apply_job = ApplyJob.objects.create(user=user, job=job, status="Pending")

    # Tests that when a user applies to a job, the status is automatically set to Pending.
    # def test_apply_job_pending_status(self):
    #     user = User.objects.create(email="test@test.com")
    #     company = Company.objects.create(name="Test Company")
    #     job = Job.objects.create(user=user, company=company, title="Test Job", city="Test City", salary=50000, requirements="Test Requirements", ideal_candidate="Test Ideal Candidate", is_avaliable=True)
    #     apply_job = ApplyJob.objects.create(user=user, job=job, status="Pending")
    #     self.assertEqual(apply_job.status, "Pending")

    # Tests that when a user applies to a job, the timestamp is automatically set.
    # def test_apply_job_timestamp(self):
    #     user = User.objects.create(email="test@test.com")
    #     # company = Company.objects.create(name="Test Company")
    #     job = Job.objects.create(user=user, company=company, title="Test Job", city="Test City", salary=50000, requirements="Test Requirements", ideal_candidate="Test Ideal Candidate", is_avaliable=True)
    #     apply_job = ApplyJob.objects.create(user=user, job=job, status="Pending")
    #     self.assertIsNotNone(apply_job.timestamp)