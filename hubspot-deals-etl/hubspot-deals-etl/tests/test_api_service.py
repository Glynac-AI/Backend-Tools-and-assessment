import os

from services.api_service import APIService


def test_get_deals_returns_results():
    token = os.getenv("HUBSPOT_TOKEN")

    if not token:
        raise AssertionError("HUBSPOT_TOKEN is not set")

    service = APIService()

    response = service.get_deals(
        access_token=token,
        limit=1,
    )

    assert isinstance(response, dict)
    assert "results" in response
    assert isinstance(response["results"], list)


def test_get_deals_result_has_id():
    token = os.getenv("HUBSPOT_TOKEN")

    if not token:
        raise AssertionError("HUBSPOT_TOKEN is not set")

    service = APIService()

    response = service.get_deals(
        access_token=token,
        limit=1,
    )

    results = response.get("results", [])

    assert len(results) >= 1
    assert "id" in results[0]