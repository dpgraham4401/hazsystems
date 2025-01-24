# Create your tests here.

import pytest

from esystem.models import HazardousWasteSystem


@pytest.mark.django_db
class TestDummyClass:

    @pytest.fixture
    def string(self):
        return "hello"

    def test_dummy(self, string):
        assert string == "hello"

    def test_another_dummy(self, string):
        assert string == "hello"

    def test_create_model(self):
        system = HazardousWasteSystem.objects.create(name="Test System")
        assert isinstance(system, HazardousWasteSystem)