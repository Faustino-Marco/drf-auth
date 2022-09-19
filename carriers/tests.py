from django.test import TestCase
from .models import Carrier
from django.contrib.auth import get_user_model

# Create your tests here.
class CarrierTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username="testuser1", password="pass")
        testuser1.save()

        test_carrier = Carrier.objects.create(name="rake", owner="testuser1", description="Better than shovels")
        test_carrier.save()
    
    def test_carriers_model(self):
        carrier = Carrier.objects.get(id=1)
        actual_owner = str(carrier.owner)
        actual_name = str(carrier.name)
        actual_description = str(carrier.description)
        self.assertEqual(actual_owner, "joe")
        self.assertEqual(actual_name, "truck")
        self.assertEqual(actual_description, "Hauling TP for WalMart.")