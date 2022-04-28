import logging
from ete3 import Tree
from owlready2 import get_ontology, sync_reasoner, Thing

logger = logging.getLogger('ontotree')


class OntoTree:

    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    def convert_ontology(self, ontology_file_path, output_file_path, use_reasoning=False):
        ontology_tree = self.get_ontology_tree(ontology_file_path, use_reasoning)
        logger.debug(ontology_tree.get_ascii(attributes=["name", "iri"]))
        ontology_tree.write(format=1, features=["iri"], outfile=output_file_path)  # Write tree to Newick format file

    def get_ontology_tree(self, ontology_file_path, use_reasoning):
        self.load_ontology(ontology_file_path, use_reasoning)
        logger.info("Creating ontology tree...")
        ontology_tree = Tree()
        self.add_children(ontology_tree, Thing)  # Start with ontology top class owl:Thing
        logger.info("...done")
        return ontology_tree

    def add_children(self, root_node, ontology_term):
        for child_term in ontology_term.subclasses():
            child_node = root_node.add_child(name=child_term.label)
            child_node.add_features(iri=child_term.iri)
            self.add_children(child_node, child_term)

    def load_ontology(self, ontology_path, use_reasoning):
        logger.info("Loading ontology...")
        ontology = get_ontology(ontology_path).load()
        logger.info("...done")
        if use_reasoning:
            logger.info("Reasoning over ontology...")
            with ontology:
                sync_reasoner()
            logger.info("...done")
        return ontology
