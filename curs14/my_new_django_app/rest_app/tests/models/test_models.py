from django.test import TestCase

from rest_app.models import FancyCat

class FancyCatTest(TestCase):

    def setUp(self):
        FancyCat.objects.create(name='Oscar')
        FancyCat.objects.create(name='Max')

    def test_count_cats(self):
        self.assertEqual(FancyCat.objects.count(), 2)

    def test_create_new_cat(self):
        c = FancyCat.objects.create(name='Sam')
        self.assertEqual(FancyCat.objects.count(), 3)
        self.assertEqual(c.name, 'Sam')

    def test_edit_cat(self):
        c = FancyCat.objects.create(name='Alex')
        c.name = 'Bob'
        c.age = 3
        c.save()
        self.assertEqual(c.name, 'Bob')
        self.assertEqual(c.age, 3)
    
    def test_delete_cat(self):
        c = FancyCat.objects.get(id=1)
        c.delete()

        self.assertEqual(FancyCat.objects.count(), 1)