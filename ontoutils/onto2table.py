import pandas as pd
from text2term.term_collector import OntologyTermCollector


class Onto2Table:
    """Writes an ontology class hierarchy as a table"""

    @staticmethod
    def generate_table_from_file(ontology_file, output_file="", use_reasoning=False):
        collector = OntologyTermCollector()
        terms = collector.get_ontology_terms(ontology_iri=ontology_file,
                                             use_reasoning=use_reasoning,
                                             exclude_deprecated=True)
        return Onto2Table.generate_table_from_terms(terms, output_file=output_file)

    @staticmethod
    def generate_table_from_terms(ontology_terms, output_file=""):
        output = set()
        for term in ontology_terms:
            term_details = ontology_terms[term]
            parents = term_details.parents
            if len(parents) > 0:
                for parent in parents:
                    parent_label = parents[parent]
                    output.add((term, term_details.label, parent, parent_label))
            else:
                output.add((term, term_details.label, "http://www.w3.org/2002/07/owl#Thing", "owl:Thing"))
        output_df = pd.DataFrame(output, columns=['Term ID', 'Term Label', 'Parent ID', 'Parent Label'])
        if output_file != "":
            output_df.to_csv(output_file, index=False)
        return output_df
