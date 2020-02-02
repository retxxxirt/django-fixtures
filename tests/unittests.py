from django_fixtures.unittests import FixturesTestCase


class FixturesUnittestsTestCase(FixturesTestCase):
    fixtures = ('app_a.GeneratedNumbers', 'app_a.OSMFullData')

    def test_count_of_numbers(self):
        self.assertEqual(len(self.fixtures_data['app_a.GeneratedNumbers']), 100)

    def test_count_of_objects(self):
        from tests.project.app_a.models import OSMData
        self.assertEqual(OSMData.objects.using(self.database).count(), 8)
