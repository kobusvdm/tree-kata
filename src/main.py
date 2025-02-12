from dataclasses import dataclass
from typing import Optional

import click
import yaml


@dataclass
class TreeNode(dict):
    """
    A class representing a node in a binary tree.
    
    Each node has a value and two children (left and right).
    
    Attributes:
        value: The value of the node.
        left: The left child node.
        right: The right child node.
        
    Methods:
        from_dict: Construct a TreeNode object from a dictionary.
        __repr__: Return a string representation of the node for easier debugging.
    """
    
    value: str
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None
    
    @classmethod
    def from_dict(cls, data: dict) -> "TreeNode":
        """
        Construct a TreeNode object from a dictionary.

        :param data: Dictionary with keys 'value', 'left', 'right'.
        :return: A TreeNode object.
        """
        return cls(
            value=data["value"],
            left=cls.from_dict(data["left"]) if data["left"] is not None else None,
            right=cls.from_dict(data["right"]) if data["right"] is not None else None
        )

    def pre_order_traversal(self, depth: int = 0, visit: callable = click.echo) -> None:
        """
        Perform a pre-order traversal of the tree and print the nodes.

        :param depth: The depth of the current node in the tree.
        :param print_fn: The function used to print the node.
        """
        # Print the current node
        visit(f"{'  ' * depth}{self.value}")
        # Traverse the left subtree
        if self.left is not None:
            self.left.pre_order_traversal(depth + 1, visit)
        # Traverse the right subtree
        if self.right is not None:
            self.right.pre_order_traversal(depth + 1, visit)

    def in_order_traversal(self, depth: int = 0, visit: callable = click.echo) -> None:
        """
        Perform a pre-order traversal of the tree and print the nodes.

        :param depth: The depth of the current node in the tree.
        :param print_fn: The function used to print the node.
        """
        # Traverse the left subtree
        if self.left is not None:
            self.left.in_order_traversal(depth + 1, visit)
        # Print the current node
        visit(f"{'  ' * depth}{self.value}")
        # Traverse the right subtree
        if self.right is not None:
            self.right.in_order_traversal(depth + 1, visit)

    def post_order_traversal(self, depth: int = 0, visit: callable = click.echo) -> None:
        """
        Perform a pre-order traversal of the tree and print the nodes.

        :param depth: The depth of the current node in the tree.
        :param print_fn: The function used to print the node.
        """
        # Traverse the left subtree
        if self.left is not None:
            self.left.post_order_traversal(depth + 1, visit)
        # Traverse the right subtree
        if self.right is not None:
            self.right.post_order_traversal(depth + 1, visit)
        # Print the current node
        visit(f"{'  ' * depth}{self.value}")

    def __repr__(self) -> str:
        """
        Return a string representation of the node for easier debugging.
        """
        return (f"TreeNode(value={self.value!r}, "
                f"left={self.left!r}, "
                f"right={self.right!r})")

def load_tree_from_yaml(file_path: str) -> Optional[TreeNode]:
    """
    Load the tree from a YAML file and convert it into a TreeNode structure.

    :param file_path: Path to the YAML file containing the tree.
    :return: The root TreeNode of the constructed tree.
    """
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)

    # Convert the loaded dictionary into a bespoke TreeNode structure
    return TreeNode.from_dict(data)

@click.group()
def cli():
    """
    A command-line interface for loading and printing a YAML-based tree.
    """
    pass

@cli.command("pre-print")
@click.argument("file_path", type=click.Path(exists=True), default="src/tree.yaml")
def pre_print_tree_cmd(file_path: str) -> None:
    """
    Load a tree from YAML and print its structure in pre-order.
    """
    tree = load_tree_from_yaml(file_path)
    if tree is None:
        click.echo("No tree found in the given file.")
    else:
        click.echo(f"Current tree structure for file '{file_path}':")
        tree.pre_order_traversal()

@cli.command("in-print")
@click.argument("file_path", type=click.Path(exists=True), default="src/tree.yaml")
def in_print_tree_cmd(file_path: str) -> None:
    """
    Load a tree from YAML and print its structure in-order.
    """
    tree = load_tree_from_yaml(file_path)
    if tree is None:
        click.echo("No tree found in the given file.")
    else:
        click.echo(f"Current tree structure for file '{file_path}':")
        tree.in_order_traversal()

@cli.command("post-print")
@click.argument("file_path", type=click.Path(exists=True), default="src/tree.yaml")
def post_print_tree_cmd(file_path: str) -> None:
    """
    Load a tree from YAML and print its structure in post-order.
    """
    tree = load_tree_from_yaml(file_path)
    if tree is None:
        click.echo("No tree found in the given file.")
    else:
        click.echo(f"Current tree structure for file '{file_path}':")
        tree.post_order_traversal()

@cli.command("load-tree")
@click.argument("file_path", type=click.Path(exists=True), default="src/tree.yaml")
def load_tree_cmd(file_path: str) -> None:
    """
    Load a tree from YAML and print a confirmation.
    """
    tree = load_tree_from_yaml(file_path)
    if tree is None:
        click.echo("No tree found in the given file.")
    else:
        click.echo(f"Tree loaded successfully from {file_path}:")


if __name__ == "__main__":
    cli()