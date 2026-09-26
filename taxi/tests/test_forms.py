from django.test import TestCase

from taxi.forms import (
    DriverCreationForm,
    CarSearchForm,
    DriverSearchForm,
    ManufacturerSearchForm
)
from taxi.models import Driver, Manufacturer, Car


class SearchFormTest(TestCase):
    def setUp(self):
        bmw = Manufacturer.objects.create(name="BMW", country="Germany")
        Car.objects.create(model="X5", manufacturer=bmw)
        Driver.objects.create(username="testadmin", password="test")

    def test_manufacturer_search(self):
        form = ManufacturerSearchForm(data={"name": "BMW"})
        self.assertTrue(form.is_valid())

    def test_driver_search(self):
        form = DriverSearchForm(data={"name": "test"})
        self.assertTrue(form.is_valid())

    def test_car_search(self):
        form = CarSearchForm(data={"name": "BMW"})
        self.assertTrue(form.is_valid())
