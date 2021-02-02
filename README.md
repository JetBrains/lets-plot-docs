# Lets-Plot documentation site

This repository contains sources for building and publishing the [Lets-Plot](https://github.com/JetBrains/lets-plot) project documentation site using [Sphinx](https://www.sphinx-doc.org) and
[GitHub Pages](https://pages.github.com).

## Build and publish documentation site

All commands should be run from the repository root.

1. Create conda environment `lets-plot-docs` from file environment.yml:

    ```bash
    conda env create -f ./environment.yml
    ```

    If you have this environment already, update it:

    ```bash
    conda env update --name lets-plot-docs -f environment.yml --prune
    ```

2. Activate this environment:

    ```bash
    conda activate lets-plot-docs
    ```

3. Only for Windows users, run:

    ```bash
    conda install m2w64-toolchain
    ```

4. Install Lets-Plot Python package:

    ```bash
    pip install lets-plot
    ```
 
5. Build documentation (HTML):  

    ```bash
    sphinx-build -b html ./source ./docs
    ```

6. Check docs/index.html in your browser.

7. Commit and push new changes. 

