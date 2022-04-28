# ontotree

Utility to write an ontology class hierarchy as a Newick tree.

## Usage

Install package using **pip**: ```pip install .```

Execute the tool as follows:

`python ontotree -ont ONTOLOGY -out OUTPUT [-R REASONING]` 

To display a help message do: ```python ontotree -h```

### Required arguments

`-ont ontology` Input ontology file path or URL.

`-out OUTPUT` Output file path.

### Optional arguments
`-r REASONING` Use reasoner to compute the ontology's inferred class hierarchy.