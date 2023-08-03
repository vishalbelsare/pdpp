- [`pdpp`](#pdpp)
  - [Installation Prerequisites](#installation-prerequisites)
  - [Installation](#installation)
  - [Example](#example)
  - [Usage from the Command Line](#usage-from-the-command-line)


# `pdpp`

`pdpp` is a command-line interface for facilitating the creation and maintainance of transparent and reproducible data workflows. `pdpp` adheres to principles espoused by Patrick Ball in his manifesto on ['Principled Data Processing'](https://www.youtube.com/watch?v=ZSunU9GQdcI). `pdpp` can be used to create 'tasks', populate task directories with the requisite subdirectories, link together tasks' inputs and outputs, and executing the pipeline using the `doit` [suite of automation tools](https://pydoit.org/). 

`pdpp` is also capable of producing rich visualizaitons of the data processing workflows it creates:



Every project that comforms with Patrick Ball's ['Principled Data Processing'](https://www.youtube.com/watch?v=ZSunU9GQdcI) guidelines uses the 'task' as the quantum of a workflow. Each task in a workflow takes the form of a directory that houses a discrete data operation, such as extracting records from plaintext documents and storing the results as a `.csv` file. Ideally, each task should be simple and conceptually unified enough that a short 3- or 4-word description is enough to convey what the task accomplishes.^[In practical terms, this implies that PDP-compliant projects tend to use many more distinct script files to perform what would normally be accomplished in the space of a single, longer script.] 

Each task directory contains at minimum three subdirectories:

1. `input`, which contains all of the task's local data dependencies
2. `output`, which contains all of the task's local data outputs (also referred to as 'targets')
3. `src`, which all of the task's source code^[Which, ideally, would be contained within a single script file.]

The `pdpp` package adds two additional constraints to Patrick Ball's original formulation of PDP: 

1. All local data files needed by the workflow but which are not generated by any of the workflow's tasks must be included in the `_import_` directory, which `pdpp` places at the same directory level as the overall workflow during project initialization.
2. All local data files produced by the workflow as project outputs must be routed into the `_export_` directory, which `pdpp` places at the same directory level as the overall workflow during project initialization.

These additional constraints disambiguate the input and output of the overall workflow, which permits `pdpp` workflows to be easily stacked or embedded within one another. 


## Installation Prerequisites

Aside from an up-to-date installation of `python` and `pip` (installation instructions for which can be found [here](https://wiki.python.org/moin/BeginnersGuide/Download)), the `pdpp` package depends on `graphviz`, which must be installed before attempting to install `pykrusch`. Installation instructions for `graphviz` can be found at the [GraphViz installation instructions page.](https://pygraphviz.github.io/documentation/stable/install.html#windows-install)


## Installation

To install `pykrusch`, use `pip`:

```bash
pip install pdpp
```


## Example

The first step when using `pdpp` is to initialize a new project directory, which must be empty. To initialize a new project directory, use the following command:

```bash
pdpp init
```

Doing so should produce a directory tree similar to this one:

![](img/init.png)

For the purposes of this example, a `.csv` file containing some toy data has been added to the `_import_` directory. 

At this point, we're ready to add our first task to the project. To do this, we'll use the `new` command:

```bash
pdpp new
```

Upon executing the command, `pdpp` will request a name for the new task. We'll call it 'task_1'. After supplying the name, `pdpp` will display an interactive menu which allows users to specify which other tasks in the project contain files that 'task_1' will depend upon. 

![](img/task_1_task_dep.png)

At the moment, this isn't a very decision to make, as there's only one other task in the project that can files can be imported from. Select it (using spacebar) and press the enter/return key. `pdpp` will then display a nested list of all the files available to be nominated as a dependency of 'task_1':

![](img/task_1_file_dep.png)

Select 'example_data.csv' and press enter. `pdpp` will inform you that your new task has been created. At this point, the project's tree diagram should appear similar to this:

![](img/tree_2.png)

The tree diagram shows that 'task_1' exists, that its input directory contains `example_data.csv` (which is hard linked to the `example_data.csv` file in `_import_`, meaning that any changes to one will be reflected in the other). 



## Usage from the Command Line

