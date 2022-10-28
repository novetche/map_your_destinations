import pytest
from map_from_database import get_locations_names, get_mapstyle_from_user, get_city_geodata

def test_get_locations_names():
    with pytest.raises(Exception):
        get_locations_names("Wrong token or wrong database ID")

def test_get_mapstyle_from_user():
    assert get_mapstyle_from_user("1") == "open-street-map"
    assert get_mapstyle_from_user("2") == "carto-positron"
    assert get_mapstyle_from_user("3") == "carto-darkmatter"
    assert get_mapstyle_from_user("4") == "stamen-terrain"
    assert get_mapstyle_from_user("5") == "stamen-toner"
    assert get_mapstyle_from_user("6") == "stamen-watercolor"

def test_get_city_geodata():
    assert get_city_geodata("Paris") == (48.8588897, 2.3200410217200766)
