import click

from isotara import isotara_genealogy


MALE_COLOUR = "lightskyblue1"
FEMALE_COLOUR = "plum"


@click.group()
def cli():
    pass


@click.command()
def generate():
    """
    Generates an image file called genealogy.png which contains a family tree representation of
    the data found in isotara.py, specifically the isotara_genealogy array.
    """
    import pygraphviz as pgv

    G = pgv.AGraph(strict=False, directed=False)
    # The following has a bug where lines don't connect to center of nodes
    G.graph_attr['splines'] = 'ortho'
    G.graph_attr['rankdir'] = 'TB'
    G.graph_attr['overlap'] = 'True'
    G.graph_attr['concentrate'] = 'True'

    people_nodes = {}

    # Create all nodes
    for person in isotara_genealogy:
        G.add_node(person.get_name())
        people_nodes[person] = G.get_node(person.get_name())

    spousal_connectors = {}
    child_connectors = {}

    def get_child_connector(person_one, person_two):
        if (person_one.get_name(), person_two.get_name()) in child_connectors:
            return child_connectors[(person_one.get_name(), person_two.get_name())]
        elif (person_two.get_name(), person_one.get_name()) in child_connectors:
            return child_connectors[(person_two.get_name(), person_one.get_name())]
        else:
            return None

    def has_child_connector(person_one, person_two):
        return (person_one.get_name(), person_two.get_name()) in child_connectors \
            or (person_two.get_name(), person_one.get_name()) in child_connectors

    def get_spousal_connector(person_one, person_two):
        if (person_one.get_name(), person_two.get_name()) in spousal_connectors:
            return spousal_connectors[(person_one.get_name(), person_two.get_name())]
        elif (person_two.get_name(), person_one.get_name()) in spousal_connectors:
            return spousal_connectors[(person_two.get_name(), person_one.get_name())]
        else:
            return None

    def has_spousal_connector(person_one, person_two):
        return (person_one.get_name(), person_two.get_name()) in spousal_connectors \
            or (person_two.get_name(), person_one.get_name()) in spousal_connectors

    # Generate spousal edges
    for person in isotara_genealogy:
        spouse = person.get_spouse()
        if spouse is not None:
            # Create a point node to connect the spouses
            if not has_spousal_connector(person, spouse):
                spousal_node = f"spousal_node_{person.get_name()}_{spouse.get_name()}"
                G.add_node(spousal_node)
                spousal_node = G.get_node(spousal_node)
                spousal_connectors[(person.get_name(), spouse.get_name())] = spousal_node
                G.add_edge(person.get_name(), spousal_node)
                G.add_edge(spousal_node, spouse.get_name())
                # Specify that all three nodes mentioned here are in the same rank
                G.add_subgraph([person.get_name(), spousal_node, spouse.get_name()], rank="same")

    # Create all child edges
    for person in isotara_genealogy:
        parents = person.get_parents()
        if len(parents) == 0:
            continue
        elif len(parents) == 1:
            # TODO: Replace single-parent relationships with "unknown" parent instead
            G.add_edge(parents[0].get_name(), person.get_name())
        elif len(parents) == 2:
            if not has_child_connector(parents[0], parents[1]):
                spousal_connector = get_spousal_connector(parents[0], parents[1])
                child_connector = f"child_connector_{parents[0].get_name()}_{parents[1].get_name()}"
                G.add_node(child_connector)
                G.add_edge(spousal_connector, child_connector)
                child_connector = G.get_node(child_connector)
                child_connectors[(parents[0].get_name(), parents[1].get_name())] = child_connector
            else:
                child_connector = get_child_connector(parents[0], parents[1])
            G.add_edge(child_connector, person.get_name())
        else:
            raise ValueError(f"A person must have at most 2 parents, but {person} has {len(parents)} parents")

    # Get an array of arrays
    # Each element in the array is a list of people in the same generation
    generations = []
    for person in isotara_genealogy:
        generation = person.get_generation()
        if len(generations) <= generation:
            generations.append([])
        generations[generation].append(person)
    for generation in generations:
        G.add_subgraph(generation, rank="same")

    for _, child_connector in child_connectors.items():
        child_connector.attr['shape'] = 'point'
        child_connector.attr['width'] = 0
        child_connector.attr['height'] = 0

    for _, spousal_connector in spousal_connectors.items():
        spousal_connector.attr['shape'] = 'point'
        spousal_connector.attr['width'] = 0
        spousal_connector.attr['height'] = 0

    for person, node in people_nodes.items():
        node.attr['label'] = f"{person.get_name()}"
        node.attr['shape'] = 'box'
        node.attr['style'] = 'filled'
        if person.get_gender() == 'male':
            node.attr['color'] = MALE_COLOUR
            node.attr['fillcolor'] = MALE_COLOUR
        elif person.get_gender() == 'female':
            node.attr['color'] = FEMALE_COLOUR
            node.attr['fillcolor'] = FEMALE_COLOUR
        elif person.get_gender() == 'mtf':
            node.attr['color'] = MALE_COLOUR
            node.attr['fillcolor'] = FEMALE_COLOUR
        elif person.get_gender() == 'ftm':
            node.attr['color'] = FEMALE_COLOUR
            node.attr['fillcolor'] = MALE_COLOUR

    G.layout(prog="dot")
    G.draw("genealogy.png")

    print("Generated genealogy.png successfully.")


cli.add_command(generate)


if __name__ == "__main__":
    cli()