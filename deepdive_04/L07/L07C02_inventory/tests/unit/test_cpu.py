""""Tests for CPU class"""

import pytest

from app.models import inventory


@pytest.fixture
def cpu_values():
    return {
        'name':'RYZEN Threadripper 2990WX',
        'manufacturer':'AMD',
        'total':10,
        'allocated':3,
        'cores':32,
        'socket':'sTR4',
        'power_watts':250
    }


@pytest.fixture
def cpu(cpu_values):
    return inventory.CPU(**cpu_values)


def test_create_cpu(cpu,cpu_values):
    for attr_name in cpu_values:
        assert getattr(cpu,attr_name) == cpu_values.get(attr_name)

@pytest.mark.parametrize(
    'cores,exception',[(10.5,TypeError),(-1,ValueError),(0,ValueError)]
)
def test_create_invalid_cores(cores,exception,cpu_values):
    cpu_values['cores'] = cores
    with pytest.raises(exception):
        inventory.CPU(**cpu_values)