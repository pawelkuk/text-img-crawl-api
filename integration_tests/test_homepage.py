from requests import get


pytest_plugins = ["docker_compose"]


def test_homepage_loads_readme(homepage: str):
    assert get(homepage).status_code == 200
