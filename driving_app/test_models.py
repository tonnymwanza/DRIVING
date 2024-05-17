from django.test import TestCase

from . models import Appointment
# Create your tests here.

class AppointmentTestCase(TestCase):

    def setUp(self):
        self.appointment = Appointment.objects.create(
            name = 'mark', email = 'mark@gmail.com', course_type = 'driving', car_type = 'mark x', message = 'its good'
        )

    def test_appointment(self):
        self.assertEqual(self.appointment.name, 'mark')
        self.assertEqual(self.appointment.email, 'mark@gmail.com')
        self.assertEqual(self.appointment.course_type, 'driving')
        self.assertEqual(self.appointment.car_type, 'mark x')
        self.assertEqual(self.appointment.message, 'its good')