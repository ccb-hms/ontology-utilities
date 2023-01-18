import argparse
from onto2tree import Onto2Tree
from onto2table import Onto2Table


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Utilities to write an ontology class hierarchy as a Newick tree or as a table")
    parser.add_argument("-ont", "--ontology", required=True, type=str, help="Input ontology file path or URL")
    parser.add_argument("-out", "--output", required=True, type=str, help="Output file path")
    parser.add_argument("-r", "--reasoning", required=False, default=False, action="store_true",
                        help="Use reasoner to compute the ontology's inferred class hierarchy")
    parser.add_argument("-f", "--format", required=False, default="tree", type=str,
                        help="Specify whether to convert the ontology's class hierarchy to Newick tree or table format")
    arguments = parser.parse_args()
    return arguments.ontology, arguments.output, arguments.reasoning, arguments.format


# TODO consider making the edge/relationship type parameterizable (to go beyond IS-A (SubClass) relationships)
if __name__ == "__main__":
    ontology, output_file, use_reasoning, output_format = get_arguments()
    if output_format == "tree":
        Onto2Tree().generate_ontology_tree(ontology_file=ontology,
                                           output_file=output_file,
                                           use_reasoning=use_reasoning)
    elif output_format == "table":
        Onto2Table.generate_table_from_file(ontology_file=ontology,
                                            output_file=output_file,
                                            use_reasoning=use_reasoning)
    else:
        raise RuntimeError("Unsupported output format: " + output_format)
