# ontotree

Utility to write an ontology class hierarchy as a Newick tree.

## Usage

Clone this repository and then install package using **pip**: ```pip install .```

### Programmatic usage

Import package:

```Python
from ontotree.onto2tree import Onto2Tree
```

Generate a Newick tree representing the class hierarchy of the given ontology and get back an [ETE **Tree** object](https://github.com/etetoolkit/ete):

```Python
tree = Onto2Tree().generate_ontology_tree(ontology_file="http://purl.obolibrary.org/obo/cl/releases/2022-09-15/cl.owl")
```

Generate a tree, get the `Tree` object and save to the specified file:

```Python
tree = Onto2Tree().generate_ontology_tree(ontology_file="http://purl.obolibrary.org/obo/cl/releases/2022-09-15/cl.owl",
                                          output_file="cl.txt")
```

### Command-line usage

`python ontotree -ont ONTOLOGY -out OUTPUT [-R REASONING]` 

To display a help message do: ```python ontotree -h```

### Required arguments

`-ont ontology` Input ontology file path or URL.

`-out OUTPUT` Output file path.

### Optional arguments
`-r REASONING` Use reasoner to compute the ontology's inferred class hierarchy.