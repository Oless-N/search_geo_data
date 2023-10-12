def test_search_region(test_client):
    test_request_payload = {
        "region": "FR-22"
    }
    test_response_payload = {
        "result": [
            {
                "total_area": 12683.47436588409,
                "total_yield": 285663.4082793138,
                "avg_yield_per_ha": 22.52248871552806
            }
        ]
    }

    response = test_client.get("/api/v1/search_region",
                               json=test_request_payload)

    assert response.json() == test_response_payload

    assert response.status_code == 200


def test_search_quadrangle(test_client):
    test_request_payload = {
        "vertex1": {
            "lon": 4.612359,
            "lat": 45.934549
        },
        "vertex2": {
            "lon": 4.612359,
            "lat": 45.934494
        },
        "vertex3": {
            "lon": 4.612524,
            "lat": 45.934439
        },
        "vertex4": {
            "lon": 4.612688,
            "lat": 45.934494
        }
    }

    test_response_payload = {
        "result": [
            {
                "id": 9728101,
                "geometry": "0106000020E6100000010000000103000000010000000500000022A5D93C0E73124037C1374D9FF7464022A5D93C0E7312407427D87F9DF74640770FD07D39731240B08D78B29BF746404A9BAA7B647312407427D87F9DF7464022A5D93C0E73124037C1374D9FF74640",
                # noqa
                "area_ha": 0.01557290259904694,
                "crop": None,
                "history": "\"null\"",
                "productivity": None,
                "region": "FR-69",
                "score": None,
                "type": "MULTIPOLYGON"
            }
        ]
    }

    response = test_client.get(
        url="/api/v1/search_quadrangle",
        json=test_request_payload,
    )

    assert response.json() == test_response_payload

    assert response.status_code == 200


def test_search_nearby(test_client):
    test_request_payload = {
        "lon": 5.792218,
        "lat": 43.735445,
        "radius": 1000
    }
    test_response_payload = {
        "result": [
            {
                "id": 8911130,
                "geometry": "0106000020E6100000010000000103000000010000002C0000009DBCC804FC2A1740EC4FE27327DE454009336DFFCA2A1740021077F52ADE45408CBAD6DEA72A1740021077F52ADE4540A93121E6922A17407AA86DC328DE45400F4240BE842A1740F931E6AE25DE4540D105F52D732A1740DC80CF0F23DE4540EE7C3F355E2A17405419C6DD20DE4540AF40F4A44C2A1740AA0F24EF1CDE45401651137D3E2A1740A13193A817DE4540FF3F4E98302A17409753026212DE4540E82E89B3222A1740FA2B64AE0CDE45404F3FA88B142A17403271AB2006DE454010035DFB022A174029931ADA00DE45402D7AA702EE2917400DE2033BFEDD4540EE3D5C72DC29174020B58993FBDD4540554E7B4ACE29174075ABE7A4F7DD45403E3DB665C0291740D192C7D3F2DD4540A54DD53DB2291740C8B4368DEDDD4540A54DD53DB22917408F52094FE8DD4540554E7B4ACE291740799274CDE4DD4540D2C6116BF1291740799274CDE4DD4540B54FC763062A17409C340D8AE6DD45401CB7989F1B2A17408F52094FE8DD45403D7C9928422A17401DAB949EE9DD4540876C205D6C2A174017BA1281EADD45400F4240BE842A1740A5129ED0EBDD45404E7E8B4E962A1740336B2920EDDD454031074147AB2A1740C2C3B46FEEDD454070438CD7BC2A1740DE74CB0EF1DD4540AE7FD767CE2A1740CBA145B6F3DD454092088D60E32A1740828DEBDFF5DD4540D044D8F0F42A1740FD12F1D6F9DD45406A34B918032B174036751E15FFDD454003249A40112B17403F53AF5B04DE45401A355F251F2B1740E36BCF2C09DE4540B324404D2D2B17405EF1D4230DDE4540CA3505323B2B174075B169A510DE45406325E659492B17408B71FE2614DE45407A36AB3E572B1740A13193A817DE454014268C66652B1740B7F1272A1BDE45402A37514B732B17403868AF3E1EDE45405DBF60376C2B1740C0CFB87020DE4540CA3505323B2B1740DC80CF0F23DE45409DBCC804FC2A1740EC4FE27327DE4540",
                "area_ha": 1.727400983118033,
                "crop": None,
                "history": "\"null\"",
                "productivity": None,
                "region": "FR-83",
                "score": None,
                "type": "MULTIPOLYGON"
            }
        ]
    }

    response = test_client.get("/api/v1/search_region",
                               json=test_request_payload)

    assert response.json() == test_response_payload

    assert response.status_code == 200


def test_search_earch_geojson(test_client):
    test_request_payload = {
        "coordinates": [
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
    }
    test_response_payload = {
        "result": [
            {
                "id": 8462020,
                "geometry": "0106000020E610000001000000010300000001000000050000004FAC53E57BE608C095D233BDC4264840F415A4198BE608C030D978B0C526484094C2BCC799E608C095D233BDC4264840F415A4198BE608C0FBCBEEC9C32648404FAC53E57BE608C095D233BDC4264840",
                "area_ha": 0.001360266609652899,
                "crop": None,
                "history": "\"null\"",
                "productivity": None,
                "region": "FR-22",
                "score": None,
                "type": "MULTIPOLYGON"
            }
        ]
    }

    response = test_client.get("/api/v1/search_region",
                               json=test_request_payload)

    assert response.json() == test_response_payload

    assert response.status_code == 200
