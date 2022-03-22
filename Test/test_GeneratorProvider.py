import unittest

from CharacterGenerator.GeneratorProvider import GeneratorProvider


class TestGeneratorProvider(unittest.TestCase):
    def test_generator_loads_races(self):
        generator = GeneratorProvider(".\\TestFiles\\OnlyRaces.xml")
        self.assertEqual(1, len(generator.races), "Wrong number of races found, xml only contains 1")
        self.assertEqual(generator.races[0].value, "TestRace")

    def test_subraces_works(self):
        generator = GeneratorProvider(".\\TestFiles\\OnlyRaces.xml")
        self.assertEqual(generator.races[0].value, "TestRace")
        self.assertEqual(4, len(generator.races[0].subtypes), "Number of subraces is wrong")