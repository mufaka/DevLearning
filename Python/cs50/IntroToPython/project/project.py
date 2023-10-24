import argparse
from rich.console import Group
from rich.tree import Tree 
from rich.panel import Panel
from rich import print 
from edi_parser import EdiParser 

def main():
    parser = argparse.ArgumentParser(
        prog='EDI Viewer',
        description='Displays EDI in a structure defined by the implementation specification.')
    
    parser.add_argument("filename")
    args = parser.parse_args()

    parser = EdiParser()
    document = parser.parse_file(args.filename)

    for transaction_set in document.transaction_sets:
        show_tree(transaction_set)

def show_tree(transaction_set):
    tree = Tree(transaction_set.name, hide_root=True)
    populate_tree(transaction_set, tree)
    print(tree)

def populate_tree(edi_node, tree):
    if hasattr(edi_node, "raw_edi"):
        panel = Panel.fit(f"[italic]{edi_node.raw_edi.replace(':', '-')}", border_style="red")
        branch = tree.add(Group(edi_node.name, panel))
    elif hasattr(edi_node, "sub_elements"):
        for element in edi_node.sub_elements:
            values = ' '.join(element.values)
            branch = tree.add(f"[bold white]{edi_node.name}: [/bold white]{values}")
    else:
        branch = tree.add(f"[bold blue]{edi_node.name}", guide_style="blue")

    for child_node in edi_node.children:
        populate_tree(child_node, branch)

if __name__ == "__main__":
    main()
