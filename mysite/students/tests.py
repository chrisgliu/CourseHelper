from django.test import Client, TestCase

from .models import Student, Enrolled, Major, Year, Semester, Course
from django.urls import reverse
# Create your tests here.

class StudentsTestCase(TestCase):
    def testaboutPage(self):
        c = Client()
        response = c.get(reverse("about"))
        self.assertEqual(response.status_code, 404)
    
    def testcreditPage(self):
        c = Client()
        response = c.get(reverse("credit"))
        self.assertEqual(response.status_code, 404)
    
    def testschedulePage(self):
        c = Client()
        response = c.get(reverse("schedule"))
        self.assertEqual(response.status_code, 404)
    def testsignUpPage(self):
        c = Client()
        response = c.get(reverse("signUp"))
        self.assertEqual(response.status_code, 404)
    def testsignInPage(self):
        c = Client()
        response = c.get(reverse("signIn"))
        self.assertEqual(response.status_code, 404)
