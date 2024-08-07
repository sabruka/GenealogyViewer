import sys

from person import Person

# TODO: Find a better way of populating this.
isotara_genealogy = []

# EAST-ARCADIA ROYAL FAMILY LINEAGE

unknown_grandmother = Person(isotara_genealogy, "Unknown Regal Grandmother", "female")
unknown_grandfather = Person(isotara_genealogy, "Unknown Regal Grandfather", "male")
unknown_regal_mother = Person(isotara_genealogy, "Unknown Regal Mother", "female")
unknwon_regal_aunt = Person(isotara_genealogy, "Unknown Regal Aunt", "female")

androniki = Person(isotara_genealogy, "Androniki", "female")
dimitri_djemdor = Person(isotara_genealogy, "Dimitri Djemdor", "male")
renothi_djemdor = Person(isotara_genealogy, "Renothi Djemdor", "female")
renothi_djemdor.add_parents(androniki, dimitri_djemdor)

olive_natvig = Person(isotara_genealogy, "Olive Natvig", "female")
torgeir_colden = Person(isotara_genealogy, "Torgeir Colden", "male")
nosco_colden = Person(isotara_genealogy, "Nosco Colden", "male")
nosco_colden.add_parents(olive_natvig, torgeir_colden)

renothi_djemdor.set_spouse(nosco_colden)

henri_tolgeir_colden_djemdor = Person(isotara_genealogy, "Henri Tolgeir Colden-Djemdor", "male")
henri_tolgeir_colden_djemdor.add_parents(renothi_djemdor, nosco_colden)
teresa_of_sourdorel = Person(isotara_genealogy, "Teresa of Sourdorel", "female")

anna_colden = Person(isotara_genealogy, "Anna Colden", "female")
anna_colden.add_parents(henri_tolgeir_colden_djemdor, teresa_of_sourdorel)
tassia_colden_djemdor = Person(isotara_genealogy, "Tassia Colden-Djemdor", "female")
tassia_colden_djemdor.add_parents(henri_tolgeir_colden_djemdor, teresa_of_sourdorel)
apos_djemdor = Person(isotara_genealogy, "Apos Djemdor", "male")
apos_djemdor.add_parents(henri_tolgeir_colden_djemdor, teresa_of_sourdorel)
georgia_anontelli = Person(isotara_genealogy, "Georgia Anontelli", "female")
georgia_anontelli.set_spouse(apos_djemdor)
gianni_djemdor = Person(isotara_genealogy, "Gianni Djemdor", "male")
gianni_djemdor.add_parents(georgia_anontelli, apos_djemdor)
mihalis_kaneas = Person(isotara_genealogy, "Mihalis Kaneas", "male")
efimia_djemdor = Person(isotara_genealogy, "Efimia Djemdor", "female")
efimia_djemdor.add_parents(mihalis_kaneas, gianni_djemdor)

apos_colden = Person(isotara_genealogy, "Apos Colden", "male")
ismini_colden = Person(isotara_genealogy, "Ismini Colden", "mtf")
ismini_colden.add_parents(anna_colden, apos_colden)
petraki_colden = Person(isotara_genealogy, "Petra Colden", "male")
petraki_colden.add_parents(anna_colden, apos_colden)


def calculate_generation(isotara_genealogy):
    to_calculate = [person for person in isotara_genealogy if person.get_generation() is None]
    while len(to_calculate) > 0:
        for person in to_calculate:
            # Set generation based on the following rules:
            # 1. If a person has no parents and no spouse, set their generation to 0.
            # 2. If a person has a spouse and the spouse's generation is known, set the person's generation to the spouse's generation.
            # 3. If a person has parents and all of their parents' generations are known, set the person's generation to the maximum of their parents' generations plus 1.
            # 4. If a person has no spouse and

            if not person.has_parents() and (person.get_spouse() is None or not person.get_spouse().has_parents()):
                person.set_generation(0)
                to_calculate.remove(person)
            elif person.get_spouse() is not None and person.get_spouse().get_generation() is not None:
                person.set_generation(person.get_spouse().get_generation())
                to_calculate.remove(person)
            elif person.has_parents() and all(parent.get_generation() is not None for parent in person.get_parents()):
                person.set_generation(max(parent.get_generation() for parent in person.get_parents()) + 1)
                to_calculate.remove(person)


calculate_generation(isotara_genealogy)
