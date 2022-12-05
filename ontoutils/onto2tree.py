import logging
from ete3 import Tree
from owlready2 import get_ontology, sync_reasoner, Thing

logger = logging.getLogger('onto2tree')


class Onto2Tree:
    """Writes an ontology class hierarchy as a Newick tree"""

    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    def generate_ontology_tree(self, ontology_file, output_file="", use_reasoning=False):
        self._load_ontology(ontology_file, use_reasoning)
        logger.info("Creating ontology tree...")
        ontology_tree = Tree()
        self._add_children(ontology_tree, Thing)  # Start with ontology top class owl:Thing
        logger.info("...done")
        logger.debug(ontology_tree.get_ascii(attributes=["name", "iri"]))
        if output_file != "":
            ontology_tree.write(format=1, features=["iri"], outfile=output_file)  # Write tree to output file
        return ontology_tree

    def _add_children(self, root_node, ontology_term):
        for child_term in ontology_term.subclasses():
            child_node = root_node.add_child(name=child_term.label)
            child_node.add_features(iri=child_term.iri)
            self._add_children(child_node, child_term)

    def _load_ontology(self, ontology_path, use_reasoning):
        logger.info("Loading ontology...")
        ontology = get_ontology(ontology_path).load()
        logger.info("...done")
        if use_reasoning:
            logger.info("Reasoning over ontology...")
            with ontology:
                sync_reasoner()
            logger.info("...done")
        return ontology
