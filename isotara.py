import sys

from person import Person

# EAST-ARCADIA ROYAL FAMILY LINEAGE

androniki = Person("Androniki", "female")
dimitri_djemdor = Person("Dimitri Djemdor", "male")
renothi_djemdor = Person("Renothi Djemdor", "female")
renothi_djemdor.add_parents(androniki, dimitri_djemdor)

olive_natvig = Person("Olive Natvig", "female")
torgeir_colden = Person("Torgeir Colden", "male")
nosco_colden = Person("Nosco Colden", "male")
nosco_colden.add_parents(olive_natvig, torgeir_colden)

renothi_djemdor.add_spouse(nosco_colden)

isotara_genealogy = [
    androniki,
    dimitri_djemdor,
    renothi_djemdor,

    olive_natvig,
    torgeir_colden,
    nosco_colden,
]
