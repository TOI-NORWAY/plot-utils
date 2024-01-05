"""TØI plot utils (tpu)."""


import logging

# Always use the module-level logger, so that it can be configured by the end user.
# Logging configuration should be done by the end user, not in the module.
logger = logging.getLogger(__name__)


def hello():
    """Hello world."""

    logger.info("Hello world!")

    print("Hello world!")


## set colorcycle to TØI-colors
from cycler import cycler
import matplotlib.pyplot as plt

toi_clrs = [
    "#65939D",
    "#D3741C",
    "#c5cc8e",
    "#ffe271",
    "#8bc9dd",
    "#336699",
    "#80217E",
    "#7d6a55",
    "#c7a0ca",
    "#a8cbd1",
]
plt.rcParams["axes.prop_cycle"] = cycler("color", toi_clrs)
# define color shortcuts for manual color setting
green_, orange_ = (
    "#65939D",
    "#D3741C",
)


def savefig(
    filename,
    fig,
    save_yn=0,
    path_="./figures/",
    ext_=[".png", ".pdf"],
):
    """
    Saves plots in various formats under the specified path with the specified filename.
    filename: str
    fig: matplotlib figure object
    save_yn: bool, 0 or 1
    path_: str
    ext_: list of strings

    """
    if save_yn:
        for e in ext_:
            fig.savefig(path_ + filename + e, bbox_inches="tight")
            print("saved " + filename + e)
    else:
        pass


def legend_cleaner(legend):
    """
    Remove underscores in legend title and labels.
    """
    # Get the current title, replace underscores with spaces and set it as the new title
    new_title = legend.get_title().get_text().replace("_", " ")
    legend.set_title(new_title)

    # Do the same for the legend labels
    new_labels = [t.get_text().replace("_", " ") for t in legend.texts]
    for t, l in zip(legend.texts, new_labels):
        t.set_text(l)


# similar to the legend_cleaner, but for axis tick labels:
def axis_tick_label_cleaner(ax):
    """
    Remove underscores in axis tick labels.
    """
    # Get the current tick labels, replace underscores with spaces and set it as the new tick labels
    new_ticklabels = [t.get_text().replace("_", " ") for t in ax.get_xticklabels()]
    ax.set_xticklabels(new_ticklabels)

    return ax


# similar to the legend_cleaner, but for axis labels:
def axis_label_cleaner(ax):
    """
    Remove underscores in axis labels.
    """
    # Get the current tick labels, replace underscores with spaces and set it as the new tick labels
    new_xlabel = ax.get_xlabel().replace("_", " ")
    new_ylabel = ax.get_ylabel().replace("_", " ")
    ax.set_xlabel(new_xlabel)
    ax.set_ylabel(new_ylabel)

    return ax
