from django_fixtures.decorators import exclude_fixtures
from django_fixtures.unittests import FixturesTestCase


class FixturesUnittestsTestCase(FixturesTestCase):
    fixtures = ('app_a.GeneratedNumbers', 'app_a.OSMFullData')

    def test_count_of_numbers(self):
        self.assertEqual(len(self.fixtures.generated_numbers), 100)

    def test_count_of_objects(self):
        from tests.project.app_a.models import OSMData
        self.assertEqual(OSMData.objects.count(), 8)

    @exclude_fixtures('app_a.OSMFullData')
    def test_exclude_fixtures(self):
        from tests.project.app_a.models import OSMData
        self.assertEqual(OSMData.objects.count(), 0)
