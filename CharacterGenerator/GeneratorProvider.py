import xml.etree.ElementTree as ET
from pathlib import Path
import random

from CharacterGenerator.GeneratedItem import GeneratedItem

RACES_XML_NODE = "Races"
RACE_XML_NODE = "Race"
SUB_RACE_XML_NODE = "Subrace"

CLASSES_XML_NODE = "Classes"
CLASS_XML_NODE = "Class"
SUB_CLASS_XML_NODE = "Subclass"


class GeneratorProvider:
    def __init__(self, generator_source):
        generator_source = Path(generator_source)
        if not generator_source.is_file():
            raise ValueError('Generator source file provided does not exist.')
        generator_xml_file_root = ET.parse(generator_source).getroot()
        self.__set_races(generator_xml_file_root)
        self.__set_classes(generator_xml_file_root)

    def generate_astral_guard(self):
        race, subrace = self.get_random_race()
        generated_class, generated_subclass = self.get_random_class()

        return (generated_class, generated_subclass), (race, subrace)

    def get_random_race(self):
        random_race = random.choice(self.__races)
        random_sub_race = None

        if random_race.subtypes:
            random_sub_race = random.choice(random_race.subtypes)

        return random_race, random_sub_race

    def get_random_class(self):
        random_class = random.choice(self.__classes)
        random_sub_class = None

        if random_class.subtypes:
            random_sub_class = random.choice(random_class.subtypes)

        return random_class, random_sub_class

    def __set_races(self, generator_xml_file_root):
        races_root_node = generator_xml_file_root.find(RACES_XML_NODE)
        self.__races = GeneratorProvider.__get_generated_items(races_root_node, RACE_XML_NODE, SUB_RACE_XML_NODE)

    def __set_classes(self, generator_xml_file_root):
        classes_root_node = generator_xml_file_root.find(CLASSES_XML_NODE)
        self.__classes = GeneratorProvider.__get_generated_items(classes_root_node, CLASS_XML_NODE, SUB_CLASS_XML_NODE)

    @staticmethod
    def __get_generated_items(generated_root_xml_node, type_name, sub_type_name):
        if generated_root_xml_node is None:
            print("Node does not exist.")
            return []
        nodes = generated_root_xml_node.findall(type_name)
        items = []
        for item_node in nodes:
            generated_item = GeneratorProvider.__generate_item_from_xml_node(item_node, sub_type_name)
            items.append(generated_item)

        return items

    @staticmethod
    def __generate_item_from_xml_node(xml_node, sub_item_node):
        sub_items_nodes = xml_node.findall(sub_item_node)
        sub_items = []
        if sub_items_nodes is not None:
            for sub_race in sub_items_nodes:
                sub_items.append(GeneratedItem(sub_race.get("Name")))
        return GeneratedItem(xml_node.get("Name"), sub_items)
