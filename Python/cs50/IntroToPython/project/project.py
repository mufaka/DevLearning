import os 
from rich.console import Group
from rich.tree import Tree 
from rich.panel import Panel
from rich import print 
from edi_parser import EdiParser 

def main():
    #file_name = os.path.join("edi_samples", "270-generic-request-dependent.edi")
    file_name = os.path.join("edi_samples", "837P-COB-claim-from-billing-provider-to-payer-a.edi") 
    #file_name = os.path.join("edi_samples", "999-response-to-3-837s.edi")

    parser = EdiParser()
    document = parser.parse_file(file_name)

    for transaction_set in document.transaction_sets:
        debug_node(transaction_set)

def debug_node(transaction_set):
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
