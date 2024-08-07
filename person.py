class Person:
    def __init__(self, name: str, gender: str):
        self.attr = {}
        self._name = name
        self._gender = gender
        self._parents = []
        self._children = []
        self._spouse = None

    def get_name(self):
        return self._name

    def get_gender(self):
        return self._gender

    def get_parents(self):
        return self._parents

    def add_parent(self, parent):
        if parent in self._parents:
            return
        assert len(self._parents) < 2, "A person can have at most 2 parents"
        self._parents.append(parent)

    def add_spouse(self, spouse):
        if self._spouse is not None:
            return
        self._spouse = spouse
        spouse.add_spouse(self)

    def get_spouse(self):
        return self._spouse

    def add_parents(self, parent_one, parent_two):
        self.add_parent(parent_one)
        self.add_parent(parent_two)

    def __str__(self):
        return self._name
