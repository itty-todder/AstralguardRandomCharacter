import unittest

from CharacterGenerator.GeneratorProvider import GeneratorProvider


class TestGeneratorProvider(unittest.TestCase):
    def test_generator_loads_races(self):
        generator = GeneratorProvider(".\\TestFiles\\OnlyRaces.xml")
        self.assertEqual(len(generator.races), 1, "More then 1 race found, xml only contains 1")
        self.assertEqual(generator.races[0].value, "TestRace")
