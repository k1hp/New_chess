import unittest

# sys.path.append(os.path.join(os.getcwd(), "../chess_main"))
from chess_main.helpers import get_enemy_color


class TestHelpers(unittest.TestCase):
    def test_get_enemy_color(self):
        self.assertEqual(get_enemy_color("white"), "white")


if __name__ == "__main__":
    unittest.main()
