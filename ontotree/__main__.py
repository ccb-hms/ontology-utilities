import argparse
from onto2tree import Onto2Tree


def get_arguments():
    parser = argparse.ArgumentParser(description="Utility to write an ontology class hierarchy as a Newick tree.")
    parser.add_argument("-ont", "--ontology", required=True, type=str, help="Input ontology file path or URL")
    parser.add_argument("-out", "--output", required=True, type=str, help="Output file path")
    parser.add_argument("-r", "--reasoning", required=False, default=False, action="store_true",
                        help="Use reasoner to compute the ontology's inferred class hierarchy")
    arguments = parser.parse_args()
    return arguments.ontology, arguments.output, arguments.reasoning


if __name__ == "__main__":
    ontology, output_file, use_reasoning = get_arguments()
    Onto2Tree().generate_ontology_tree(ontology_file=ontology, output_file=output_file, use_reasoning=use_reasoning)
    # TODO consider making the edge/relationship type parameterizable (to go beyond IS-A (SubClass) relationships)
