from django.test import TestCase
from .models import Leader

# Create your tests here.


class LeaderTestCase(TestCase):
    def setUp(self):
        Leader.objects.create(name='SimpleName', text='SimpleText', owner_id='1', leader_status='P')
        Leader.objects.create(name='SimpleName2', text='SimpleText2', owner_id='2', leader_status='S')

    def testdatabase(self):
        first_name = Leader.objects.get(name='SimpleName')
        second_name = Leader.objects.get(name='SimpleName2')

        self.assertEqual(first_name.text, 'SimpleText')
        self.assertEqual(second_name.text, 'SimpleText2')

