from ontoutils.onto2table import Onto2Table

df = Onto2Table.generate_ontology_table(ontology_file="http://purl.obolibrary.org/obo/cl/releases/2022-09-15/cl.owl",
                                        output_file="cl.csv",
                                        use_reasoning=True)
print(df.to_string())
