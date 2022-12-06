# ontoutils

Utilities to write an ontology class hierarchy as a Newick tree or as a table.

## Usage

Clone this repository and then install package using **pip**: ```pip install .```

### Programmatic usage

Import package:

```Python
from ontoutils.onto2tree import Onto2Tree
```

Generate a Newick tree representing the class hierarchy of the given ontology and get back an [ETE **Tree** object](https://github.com/etetoolkit/ete):

```Python
tree = Onto2Tree().generate_ontology_tree(ontology_file="http://purl.obolibrary.org/obo/cl/releases/2022-09-15/cl.owl")
```

Generate a `Tree` object representing the ontology's inferred class hierarchy and save to the specified file:

```Python
tree = Onto2Tree().generate_ontology_tree(ontology_file="http://purl.obolibrary.org/obo/cl/releases/2022-09-15/cl.owl",
                                          output_file="cl.txt",
                                          use_reasoning=True)
```

Generate a table representing the inferred class hierarchy of the given ontology and get back a data frame:

```Python
from ontoutils.onto2table import Onto2Table

df = Onto2Table.generate_ontology_table(ontology_file="http://purl.obolibrary.org/obo/cl/releases/2022-09-15/cl.owl",
                                        output_file="cl.csv",
                                        use_reasoning=True)
```

### Command-line usage

`python ontoutils -ont ONTOLOGY -out OUTPUT [-R REASONING]` 

To display a help message do: ```python ontoutils -h```

### Required arguments

`-ont ontology` Input ontology file path or URL.

`-out OUTPUT` Output file path.

### Optional arguments
`-r REASONING` Use reasoner to compute the ontology's inferred class hierarchy.