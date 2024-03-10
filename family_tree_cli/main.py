import typer
from typing import Tuple

from family_tree_cli.service import PersonService

app = typer.Typer()
personService = PersonService()


@app.callback()
def callback():
    """
    A CLI tool for creating family tree
    """


@app.command("add-person")
def add_person(name: str):
    """
    Add a person to the family tree
    Usage: family-tree add "Amit Dhakad"
    """
    personService.add_person(name.lower())


@app.command("add-relationship")
def add_relationship_name(relation: str):
    """
    Add relationship name 
    Usage: family-tree add relationship father 
    """
    personService.add_relationship(relation.lower())


@app.command("connect")
def connect_people_using_relationship(relationships: Tuple[str, str, str, str, str]):
    """
    Connect two people using relationship
    Usage: family-tree connect <name> as <relationship> of <name>
    """
    name1, as_var, relationship, of_var, name2 = relationships
    if as_var.lower() != 'as':
        raise Exception('Not valid second argument')
    if of_var.lower() != 'of':
        raise Exception('Not valid fourth Argument')

    personService.connect_person_relationship(
        name1.lower(), name2.lower(), relationship.lower())


@app.command()
def count(relationships: Tuple[str, str, str]):
    """
    Query relationship
    Usage: family-tree count <relationship> of <name>
    """
    relation_name, of_var, name, = relationships
    if of_var.lower() != 'of':
        raise Exception('Not valid second Argument')
    print(personService.find_count_in_relation(relation_name.lower(), name.lower()))
    

@app.command()
def father(father_name: Tuple[str, str]):
    """
    Query relationship
    Usage: family-tree count <relationship> of <name>
    """
    of_var, name = father_name
    if of_var.lower() != 'of':
        raise Exception('Not valid second Argument')
    print(personService.find_relative('father', name.lower()))


if __name__ == "__main__":
    app()
