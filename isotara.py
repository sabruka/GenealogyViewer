import sys

from person import Person

# TODO: Find a better way of populating this.
isotara_genealogy = []

# EAST-ARCADIA ROYAL FAMILY LINEAGE

androniki = Person(isotara_genealogy, "Androniki", "female")
dimitri_djemdor = Person(isotara_genealogy, "Dimitri Djemdor", "male")
renothi_djemdor = Person(isotara_genealogy, "Renothi Djemdor", "female")
renothi_djemdor.add_parents(androniki, dimitri_djemdor)

olive_natvig = Person(isotara_genealogy, "Olive Natvig", "female")
torgeir_colden = Person(isotara_genealogy, "Torgeir Colden", "male")
nosco_colden = Person(isotara_genealogy, "Nosco Colden", "male")
nosco_colden.add_parents(olive_natvig, torgeir_colden)

renothi_djemdor.add_spouse(nosco_colden)

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
georgia_anontelli.add_spouse(apos_djemdor)
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
