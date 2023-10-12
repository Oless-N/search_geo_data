from unittest import mock

import pytest
import requests
import json

base_url = 'http://localhost:8989/api/v1/'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}


def test_search_multipolygon():
    test_response_payload = {
        'result': [
            {
                'id': 8462020,
                'geometry': mock.ANY,
                'area_ha': 0.001360266609652899,
                'crop': mock.ANY,
                'history': "\"null\"",
                'productivity': mock.ANY,
                'region': 'FR-22',
                'score': mock.ANY,
                'type': 'MULTIPOLYGON'
            }
        ]
    }

    url = f'{base_url}search_multipolygon'

    payload = json.dumps({
        'coordinates': [
            [
                -3.1125408,
                48.3028787
            ],
            [
                -3.1125695,
                48.3029075
            ],
            [
                -3.1125983,
                48.3028787
            ],
            [
                -3.1125695,
                48.30285
            ],
            [
                -3.1125408,
                48.3028787
            ]
        ]
    })

    response = requests.request(
        'GET',
        url,
        headers=headers,
        data=payload)

    assert response.json() == test_response_payload

    assert response.status_code == 200


def test_search_nearby():
    test_response_payload = {'result': [
        {
            'id': 8911130,
            'geometry': mock.ANY,
            'area_ha': 1.727400983118033,
            'crop': mock.ANY,
            'history': "\"null\"",
            'productivity': mock.ANY,
            'region': 'FR-83',
            'score': mock.ANY,
            'type': 'MULTIPOLYGON'
        }
    ]
    }

    url = f'{base_url}search_nearby'

    payload = json.dumps({
        'lon': 5.792218,
        'lat': 43.735445,
        'radius': 1000
    })

    response = requests.request(
        'GET',
        url,
        headers=headers,
        data=payload)

    assert response.json() == test_response_payload

    assert response.status_code == 200


def test_search_region():
    test_response_payload = {
        'result': [
            {
                'total_area': pytest.approx(12683.47436588409, abs=1e-6),
                'total_yield': pytest.approx(285663.4082793138, abs=1e-6),
                'avg_yield_per_ha': pytest.approx(22.52248871552806, abs=1e-6)
            }
        ]
    }

    url = f'{base_url}search_region'

    payload = json.dumps({
        'region': 'FR-22'
    })

    response = requests.request(
        'GET',
        url,
        headers=headers,
        data=payload)

    assert response.json() == test_response_payload

    assert response.status_code == 200


def test_search_quadrangle():
    test_response_payload = {
        'result': [
            {
                'id': 9728101,
                'geometry': mock.ANY,
                'area_ha': 0.01557290259904694,
                'crop': mock.ANY,
                'history': mock.ANY,
                'productivity': mock.ANY,
                'region': 'FR-69',
                'score': mock.ANY,
                'type': 'MULTIPOLYGON'
            }
        ]
    }

    url = f'{base_url}search_quadrangle'

    payload = json.dumps({
        'vertex1': {
            'lon': 4.612359,
            'lat': 45.934549
        },
        'vertex2': {
            'lon': 4.612359,
            'lat': 45.934494
        },
        'vertex3': {
            'lon': 4.612524,
            'lat': 45.934439
        },
        'vertex4': {
            'lon': 4.612688,
            'lat': 45.934494
        }
    }
    )

    response = requests.request(
        'GET',
        url,
        headers=headers,
        data=payload,
    )

    assert response.json() == test_response_payload

    assert response.status_code == 200
