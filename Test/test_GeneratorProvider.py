import unittest

from CharacterGenerator.GeneratorProvider import GeneratorProvider



class TestGeneratorProvider(unittest.TestCase):
    def test_generator_loads_races(self):
        generator = GeneratorProvider(".\\TestFiles\\OnlyRaces.xml")
        races = generator._GeneratorProvider__races
        self.assertEqual(1, len(races), "Wrong number of races found, xml only contains 1")
        self.assertEqual(races[0].value, "TestRace")

    def test_generate_loads_subraces(self):
        generator = GeneratorProvider(".\\TestFiles\\OnlyRaces.xml")
        races = generator._GeneratorProvider__races
        self.assertEqual(races[0].value, "TestRace")
        self.assertEqual(4, len(races[0].subtypes), "Number of subraces is wrong")

    def test_generator_loads_classes(self):
        generator = GeneratorProvider(".\\TestFiles\\OnlyClass.xml")
        classes = generator._GeneratorProvider__classes
        self.assertEqual(1, len(classes), "Wrong number of classes found, xml only contains 1")
        self.assertEqual(classes[0].value, "TestClass")

    def test_generate_loads_subraces(self):
        generator = GeneratorProvider(".\\TestFiles\\OnlyClass.xml")
        classes = generator._GeneratorProvider__classes
        self.assertEqual(classes[0].value, "TestClass")
        self.assertEqual(5, len(classes[0].subtypes), "Number of subraces is wrong")