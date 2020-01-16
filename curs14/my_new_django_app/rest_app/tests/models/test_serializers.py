from django.test import TestCase
from django.utils import timezone
from freezegun import freeze_time
import pytz


from rest_app.serializers import FancyCatSerializer
from rest_app.models import FancyCat

class FancyCatSerializerTest(TestCase):
    @freeze_time()
    def setUp(self):
        timezone.activate(pytz.timezone('UTC'))
        self.now = timezone.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        FancyCat.objects.create(
            name='Alex',
            age=2,
            is_active=False,
            description='Fluffy cat'
            )
    
    def test_serializer(self):
        cat = FancyCat.objects.get(id=1)
        serializer = FancyCatSerializer(cat)

        self.assertEqual(serializer.data, {
            'id': 1,
            'name': 'Alex',
            # 'age': 2,
            # 'is_active': False,
            # 'description': 'Fluffy cat',
            # 'date_added': self.now
        })

    