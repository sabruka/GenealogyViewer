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
    G.graph_attr['splines'] = 'ortho'
    G.graph_attr['rankdir'] = 'TB'

    people_nodes = {}

    # Create all nodes
    for person in isotara_genealogy:
        G.add_node(person.get_name())
        people_nodes[person] = G.get_node(person.get_name())

    point_connectors = {}

    def get_connector(person_one, person_two):
        if (person_one.get_name(), person_two.get_name()) in point_connectors:
            return point_connectors[(person_one.get_name(), person_two.get_name())]
        elif (person_two.get_name(), person_one.get_name()) in point_connectors:
            return point_connectors[(person_two.get_name(), person_one.get_name())]
        else:
            return None

    def has_connector(person_one, person_two):
        return (person_one.get_name(), person_two.get_name()) in point_connectors \
            or (person_two.get_name(), person_one.get_name()) in point_connectors

    # Generate spousal edges
    for person in isotara_genealogy:
        spouse = person.get_spouse()
        if spouse is not None:
            # Create a point node to connect the spouses
            if not has_connector(person, spouse):
                point_node = f"point_{person.get_name()}_{spouse.get_name()}"
                G.add_node(point_node)
                point_node = G.get_node(point_node)
                point_connectors[(person.get_name(), spouse.get_name())] = point_node
                G.add_edge(person.get_name(), point_node)
                G.add_edge(point_node, spouse.get_name())
                # Specify that all three nodes mentioned here are in the same rank
                G.add_subgraph([person.get_name(), point_node, spouse.get_name()], rank="same")

    # Create all child edges
    for person in isotara_genealogy:
        parents = person.get_parents()
        if len(parents) == 0:
            continue
        elif len(parents) == 1:
            G.add_edge(parents[0].get_name(), person.get_name())
        elif len(parents) == 2:
            if not has_connector(parents[0], parents[1]):
                point_node = f"point_{parents[0].get_name()}_{parents[1].get_name()}"
                G.add_node(point_node)
                point_node = G.get_node(point_node)
                point_connectors[(parents[0].get_name(), parents[1].get_name())] = point_node
                G.add_edge(parents[0].get_name(), point_node)
                G.add_edge(point_node, parents[1].get_name())
                G.add_subgraph([parents[0].get_name(), point_node, parents[1].get_name()], rank="same")
            else:
                point_node = get_connector(parents[0], parents[1])
            G.add_edge(point_node, person.get_name(), dir="none")
        else:
            raise ValueError(f"A person must have at most 2 parents, but {person} has {len(parents)} parents")

    for _, point_node in point_connectors.items():
        point_node.attr['shape'] = 'point'
        point_node.attr['width'] = 0
        point_node.attr['height'] = 0

    for person, node in people_nodes.items():
        node.attr['label'] = person.get_name()
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