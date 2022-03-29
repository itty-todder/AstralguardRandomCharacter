from CharacterGenerator.GeneratorProvider import GeneratorProvider

if __name__ == "__main__":
    generator = GeneratorProvider(r".\GeneratorGeneral.xml")
    (generated_class, generated_subclass), (race, subrace) = generator.generate_astral_guard()

    print("Class:", generated_class.value)
    print("\tSubclass:", generated_subclass.value)
    print("Race:", race.value)
    if subrace:
        print("\tSubrace:", subrace.value)