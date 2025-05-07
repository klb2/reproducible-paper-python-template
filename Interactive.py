import marimo

__generated_with = "0.13.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    # Paper Title

    _Authors:_ Author One (Affiliation), Author Two (Affiliation)


    This notebook is part of the publication "Paper Title" (Publication information, [doi:XXX](https://doi.org/)).
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Heading...

    Add some text and explanations. You can use $\LaTeX$ commands, such as $\alpha$ or equations $$\int_{0}^{1} f(x) \mathrm{d} x = \pi$$


    Also Marimo allows having interactive elements, such as sliders to manipulate parameters.
    """
    )
    return


@app.cell
def _(slider_noise_level):
    slider_noise_level
    return


@app.cell
def _(noise_level, np, plt, x):
    _fig, _axs = plt.subplots()

    y = np.sin(x) + noise_level * np.random.randn(len(x))
    _axs.plot(x, y)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Code

    In the following, we have necessary imports and code.
    As Marimo builds a dependency tree of the cells, they can be in any order.
    Therefore, we can keep the messy parts at the end of the notebook.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ### Parameter Definitions

    In this section, we define (global) parameters and interactive sliders.
    """
    )
    return


@app.cell
def _(np):
    num_samples = 100
    x = np.linspace(0, 10, num_samples)
    return (x,)


@app.cell
def _(mo):
    slider_noise_level = mo.ui.slider(0, 1, 0.1)
    return (slider_noise_level,)


@app.cell
def _(slider_noise_level):
    noise_level = slider_noise_level.value
    return (noise_level,)


@app.cell
def _(mo):
    mo.md(r"""### Function Definitions""")
    return


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.md(r"""### Imports""")
    return


@app.cell
def _():
    import marimo as mo

    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt


if __name__ == "__main__":
    app.run()
