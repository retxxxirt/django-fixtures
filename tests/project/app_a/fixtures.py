import json
from typing import List, Tuple

from django_fixtures import fixtures, dataset
from tests.project.app_a.models import OSMData
from tests.project.helpers import get_osm_data


class GeneratedNumbers(dataset.GeneratedDatasetMixin, fixtures.JSONFixture):
    def generate_dataset(self) -> list:
        return [number for number in range(100)]

    def process_dataset_entry(self, number: int) -> dict:
        return {'generated_number': number}


class OSMBasicData(fixtures.JSONFixture):
    dataset = [
        235471653, 235707734, 235744146, 235495355,
        235503051, 235594084, 235242069, 235508863
    ]

    def process_dataset_entry(self, place_id: int) -> dict:
        return get_osm_data(place_id)


class OSMFullData(fixtures.ModelFixture, dataset.TupleDatasetMixin):
    models, dataset = (OSMData,), [
        (235471653, 'Oh, say can you see by the dawn\'s early light', 'George Washington'),
        (235707734, 'Listen up! I\'m an American', 'John Alexander Macdonald'),
        (235744146, 'Allons enfants de la Patrie', 'Louis-Napoléon Bonaparte'),
        (235495355, 'Deutschland, Deutschland über alles', 'Friedrich Ebert'),
        (235503051, 'Fratelli d\'Italia', 'Enrico De Nicola'),
        (235594084, '¡Viva España!', 'Adolfo Suárez'),
        (235242069, 'Россия — священная наша держава', 'Boris Yeltsin'),
        (235508863, 'Ще не вмерла України, ні слава, ні воля', 'Leonid Kravchuk')
    ]

    def process_dataset_entry(self, place_id: int, anthem_beginning: str, first_president: str) -> OSMData:
        return OSMData(
            place_id=place_id, osm_data=json.dumps(get_osm_data(place_id)),
            anthem_beginning=anthem_beginning, first_president=first_president
        )


class OSMAdvancedData(fixtures.ModelFixture, dataset.DictDatasetMixin):
    models, dataset = (OSMData,), [
        {'place_id': 235471653, 'first_president': 'George Washington'},
        {'place_id': 235707734, 'first_president': 'John Alexander Macdonald'},
        {'place_id': 235744146, 'first_president': 'Louis-Napoléon Bonaparte'},
        {'place_id': 235495355, 'first_president': 'Friedrich Ebert'},
        {'place_id': 235503051, 'first_president': 'Enrico De Nicola'},
        {'place_id': 235594084, 'first_president': 'Adolfo Suárez'},
        {'place_id': 235242069, 'first_president': 'Boris Yeltsin'},
        {'place_id': 235508863, 'first_president': 'Leonid Kravchuk'}
    ]

    def process_dataset_entry(self, place_id: int, first_president: str) -> OSMData:
        return OSMData(place_id=place_id, osm_data=json.dumps(get_osm_data(place_id)), first_president=first_president)


class PresidentsData(fixtures.JSONFixture, dataset.GeneratedDatasetMixin):
    fixtures = ('app_a.OSMFullData',)

    def generate_dataset(self) -> List[int]:
        return [d['place_id'] for d in OSMData.objects.values('place_id').distinct()]

    def process_dataset_entry(self, place_id: int) -> Tuple[str, str]:
        osm_data = OSMData.objects.get(place_id=place_id)
        return json.loads(osm_data.osm_data)['localname'], osm_data.first_president
