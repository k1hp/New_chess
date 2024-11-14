import pytest
from chess_main.field import Field
from chess_main.figures import place_all_figures


@pytest.fixture
def get_start_field():
    field = Field()
    field.create_new_field()
    place_all_figures(field)
    return field
