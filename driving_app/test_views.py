from django.test import TestCase
from django.urls import reverse
# my tests 

class HomeViewTestCase(TestCase):

    def test_home_url(self):
        self.response = self.client.get(reverse('index'))
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'index.html')

class AboutViewTestCase(TestCase):

    def test_about_url(self):
        self.response = self.client.get(reverse('about_page'))
        self.assertEqual(self.response.status_code, 405)
        self.assertTemplateUsed(self.response, 'about.html')

class CourseViewTestCase(TestCase):

    def test_course_url(self):
        self.response = self.client.get(reverse('course'))
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'course.html')

class ContactTestCase(TestCase):

    def test_contact_url(self):
        self.response = self.client.get(reverse('contact'))
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'contact.html')

