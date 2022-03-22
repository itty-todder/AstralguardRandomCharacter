import xml.etree.ElementTree as ET
from pathlib import Path

from CharacterGenerator.GeneratedItem import GeneratedItem

RACES_XML_NODE = "Races"
RACE_XML_NODE = "Race"
SUB_RACE_XML_NODE = "Subrace"

class GeneratorProvider:

    def __init__(self, generator_source):
        generator_source = Path(generator_source)
        if not generator_source.is_file():
            raise ValueError('Generator source file provided does not exist.')
        generator_xml_file_root = ET.parse(generator_source).getroot()
        self.__set_races(generator_xml_file_root)

    def __set_races(self, generator_xml_file_root):
        races_root_node = generator_xml_file_root.find(RACES_XML_NODE)
        races_nodes = races_root_node.findall(RACE_XML_NODE)
        self.races = []
        #TODO: Prettify(select only value)
        for race in races_nodes:
            sub_races_nodes = race.findall(SUB_RACE_XML_NODE)
            sub_races = []
            if sub_races_nodes is not None:
                for sub_race in sub_races_nodes:
                    sub_races.append(GeneratedItem(sub_race.get("Name")))
            self.races.append(GeneratedItem(race.get("Name"), sub_races))

