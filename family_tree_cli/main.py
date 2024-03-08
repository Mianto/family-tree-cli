import typer
from typing import Tuple

app = typer.Typer()


@app.callback()
def callback():
    """
    A CLI tool for creating family tree
    """


@app.command("add-person")
def add_person(name: str):
    """
    Add a person to the family tree
    Usage: family-tree add Amit Dhakad
    """
    typer.echo("Adding Person {}", name)
    


@app.command("add-relationship")
def add_relationship_name(relation: str):
    """
    Add relationship name 
    Usage: family-tree add relationship father 
    """
    # typer.echo("Adding relationship {}", relation)


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
    
    # typer.echo("Adding relationship {} {} {}", name1, relationship, name2)



@app.command()
def count(relationships: Tuple[str, str, str]):
    """
    Query relationship
    Usage: family-tree count <relationship> of <name>
    """
    relation_name, of_var, name, = relationships
    if of_var.lower() != 'of':
        raise Exception('Not valid fourth Argument')

if __name__ == "__main__":
    app()