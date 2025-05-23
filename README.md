# Template for Reproducible Research Papers

[![Marimo](https://img.shields.io/badge/Launch-Marimo_notebook-hsl(168%2C61%25%2C28%25))](https://marimo.app/?src=https%3A%2F%2Fraw.githubusercontent.com%2Fklb2%2Freproducible-paper-python-template%2Frefs%2Fheads%2Fmaster%2FInteractive.py)
![GitHub](https://img.shields.io/github/license/klb2/reproducible-paper-python-template)
[![DOI](https://img.shields.io/badge/doi-10.1109/TWC.2022.3172760-informational)](https://doi.org/10.1109/TWC.2022.3172760)


```diff
! Update badge information/links
```

This repository provides a template for Python code that is accompanying a
research paper.
Most likely, this will be an implementation of an algorithm and/or simulation
results.

The code should be made publicly accessible in order to allow everybody to
reproduce the results presented in the paper.

You can use this template/fork it and use it as a starting point. You find a
basic structure in `main.py`, where only need to add your custom code.
This README also already contains all important information and you only need
to adjust the parts specific to your project.
The `run.sh` script should contain the exact commands that you used to generate
the results/plots in your paper. In particular, you should make sure to specify
all of the parameters.

The proposed structure of the README is
1. Information about the paper (title, authors, journal/conference, DOI, arXiv)
2. File list of all files that are provided in the repository (with short
   description)
3. Usage description. If you provide Jupyter notebooks this can also include a
   link to Binder.
4. Acknowledgements (funding information, ...)
5. License and Referencing (description of license and how to cite your work,
   e.g., the bibtex entry of your paper)

You can find some general ideas on the structure and required aspects of the
repository in [this blog
post](https://klb2.gitlab.io/writing/python/2021/12/20/reproducible-papers.html)
(independent of the used programming language).


## File List
The following files are provided in this repository:

- `run.sh`: Bash script that reproduces the figures presented in the paper.
- `util.py`: Python module that contains utility functions, e.g., for saving results.
```diff
- `main.py`: Python script that...
- ...
```

## Usage
### Running it online
The easiest way is to use the official [marimo](https://marimo.app/) playground
to run the notebook online. Simply navigate to [https://marimo.app/?src=https%3A%2F%2Fraw.githubusercontent.com%2Fklb2%2Freproducible-paper-python-template%2Frefs%2Fheads%2Fmaster%2FInteractive.py](https://marimo.app/?src=https%3A%2F%2Fraw.githubusercontent.com%2Fklb2%2Freproducible-paper-python-template%2Frefs%2Fheads%2Fmaster%2FInteractive.py)
```diff
! Add Marimo app link to notebook.
```
to run the notebooks in your browser without setting everything up locally.

### Local Installation
If you want to run it locally on your machine, Python3 and marimo are needed.
The present code was developed and tested with the following versions:
```diff
- Python 3.13
- numpy 2.2
- scipy 1.15
```

Make sure you have [Python3](https://www.python.org/downloads/) installed on
your computer.
You can then install the required packages by running
```bash
pip3 install -r requirements.txt
```
This will install all the needed packages which are listed in the requirements 
file.


Finally, you can run the Marimo notebooks with
```bash
marimo run Interactive.py
```

You can also recreate the figures from the paper by running
```bash
bash run.sh
```


## Acknowledgements
This research was supported by
```diff
! Add funding information
```


## License and Referencing
This program is licensed under the MIT license. If you in any way use this
code for research that results in publications, please cite our original
article listed above.

You can use the following BibTeX entry
```bibtex
@article{...,
  author = {...},
  title = {...},
  ...
}
```
```diff
! Add bibtex entry of the published paper
```
