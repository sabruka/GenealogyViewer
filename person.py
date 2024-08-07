class Person:
    def __init__(self, genealogy: [], name: str, gender: str):
        genealogy.append(self)
        self.attr = {}
        self._name = name
        self._gender = gender
        self._parents = []
        self._children = []
        self._spouse = None
        self._generation = None

    def get_name(self):
        return self._name

    def get_gender(self):
        return self._gender

    def get_parents(self):
        return self._parents

    def has_parents(self):
        return len(self._parents) > 0

    def add_parent(self, parent):
        if parent in self._parents:
            return
        assert len(self._parents) < 2, "A person can have at most 2 parents"
        self._parents.append(parent)

    def set_spouse(self, spouse):
        if self._spouse is not None:
            return
        self._spouse = spouse
        spouse.set_spouse(self)

    def get_spouse(self):
        return self._spouse

    def add_parents(self, parent_one, parent_two):
        self.add_parent(parent_one)
        self.add_parent(parent_two)
        parent_one.set_spouse(parent_two)

    def get_generation(self):
        return self._generation

    def set_generation(self, generation):
        self._generation = generation
