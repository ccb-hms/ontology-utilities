from ontoutils.onto2table import Onto2Table

df = Onto2Table.generate_table_from_file(ontology_file="http://purl.obolibrary.org/obo/hp/releases/2022-06-11/hp.owl",
                                         output_file="hpo.csv",
                                         use_reasoning=False)
print(df.to_string())

# when using reasoning it may be necessary to increase the max Java heap space
# that the reasoner (provided by owlready) can use, which can be done like so:
# import owlready2
# owlready2.reasoning.JAVA_MEMORY = 16000
