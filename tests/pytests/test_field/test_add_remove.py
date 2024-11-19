from dataclasses import dataclass

import pytest

from chess_main.field import remove_figure, add_figure_ways, remove_figure_ways, Field
from tests.pytests.conftest import second_figures_placement
from copy import deepcopy


@pytest.mark.skip(reason="нет смысла писать тест, потому что полностью покрыта")
def test_add_figure(): ...


@pytest.mark.parametrize("horizontal, vertical", [(5, 6), (4, 3), (3, 1)])
def test_remove_figure(horizontal, vertical, second_figures_placement):
    start_figure = second_figures_placement[vertical][horizontal][1]
    remove_figure(start_figure, second_figures_placement)
    end_figure = second_figures_placement[vertical][horizontal][1]
    assert start_figure != end_figure


@dataclass
class TestFigureWays:
    horizontal: int
    vertical: int
    current_field: Field

    @property
    def parameters(self):
        return self.horizontal, self.vertical, self.current_field

    # def test_add_figure_ways(self):
    #     self.start_field = deepcopy(self.current_field)
    #     add_figure_ways(*self.parameters)
    #     end_field = self.current_field
    #     assert self.start_field != end_field
    #
    # def test_remove_figure_ways(self):
    #     remove_figure_ways(*self.parameters)
    #     end_field = self.current_field
    #     self.start_field.print_field()
    #     end_field.print_field()
    #     assert all(
    #         map(
    #             lambda item: str(item[0]) == str(item[1]),
    #             zip(self.start_field, end_field),
    #         )
    #     )

    def test_add_figure_ways(self):
        self.start_field = deepcopy(self.current_field)
        add_figure_ways(*self.parameters)
        end_field = self.current_field
        assert self.start_field != end_field

    def test_remove_figure_ways(self):
        self.start_field = deepcopy(self.current_field)
        remove_figure_ways(*self.parameters)
        end_field = self.current_field
        assert self.start_field != end_field


@pytest.mark.development
@pytest.mark.parametrize("horizontal, vertical", [(5, 6), (4, 3), (3, 1)])
def test_figure_ways(horizontal, vertical, second_figures_placement):
    tester = TestFigureWays(horizontal, vertical, second_figures_placement)
    tester.test_add_figure_ways()
    tester.test_remove_figure_ways()
