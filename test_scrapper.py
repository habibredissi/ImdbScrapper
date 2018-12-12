import unittest
import scrapper


class TestScrap(unittest.TestCase):

    def test_importTopMovies(self):
        try:
            scrapper.importTopMovies()
        except ValueError:
            self.fail("Code raised ValueError")


if __name__ == '__main__':
    unittest.main()
