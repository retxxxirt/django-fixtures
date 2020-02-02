import requests


def get_osm_data(place_id: int) -> dict:
    return requests.get(
        'https://nominatim.openstreetmap.org/details.php',
        params={'place_id': place_id, 'format': 'json'}
    ).json()
