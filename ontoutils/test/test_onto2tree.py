from ontoutils.onto2tree import Onto2Tree

tree = Onto2Tree().generate_ontology_tree(ontology_file="http://purl.obolibrary.org/obo/cl/releases/2022-09-15/cl.owl",
                                          output_file="cl.txt")
print(tree)
