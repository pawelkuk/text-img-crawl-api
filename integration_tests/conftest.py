import pytest
from urllib3.util.retry import Retry
from requests import Session
from requests.adapters import HTTPAdapter


@pytest.fixture(name='homepage')
def fixture_homepage(function_scoped_container_getter) -> str:
    """Waits for the app to come online, then returns the URL to a homepage."""
    service = function_scoped_container_getter.get('read-websites-api') \
        .network_info[0]
    base_url = f"http://{service.hostname}:{service.host_port}"
    retry = Retry(
        total=8,
        backoff_factor=0.1,
        status_forcelist=[500, 502, 503, 504],
    )
    session = Session()
    session.mount('http://', HTTPAdapter(max_retries=retry))

    assert session.get(base_url).status_code == 200
    return base_url
