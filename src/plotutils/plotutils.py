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
