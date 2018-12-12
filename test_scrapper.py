import unittest
import scrapper


class TestScrap(unittest.TestCase):

    # def test_add(self):
    #     self.assertEqual(t.add(10, 5), 15)
    #     self.assertEqual(t.add(-1, 1), 0)
    #     self.assertEqual(t.add(-1, -1), -2)

    def test_importTopMovies(self):
        try:
            scrapper.importTopMovies()
        except ValueError:
            self.fail("Code raised ValueError")


if __name__ == '__main__':
    unittest.main()
