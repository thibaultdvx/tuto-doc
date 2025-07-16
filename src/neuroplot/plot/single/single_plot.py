from pathlib import Path
from typing import Callable, Sequence

import matplotlib.pyplot as plt
import numpy as np
import torchio as tio
from matplotlib.figure import Figure


class SinglePlot:
    """
    To plot a single neuroimage.

    2D slices will be plotted via the method :py:meth:`plot`. The user can choose which anatomical axes to plot,
    and which slice to plot along the axes.

    The title of the figure can be changed between plots using :py:meth:`set_title`.

    Parameters
    ----------
    axes : int | Sequence[int] | None, default=None
        The axis (or axes) to plot, among ``0`` (sagittal axis), ``1`` (coronal) or ``2`` (axial).
        Can be passed as a single axis, or a list of axes. If ``None``, the three axes will be plotted.
    slices : int | Sequence[int] | None, default=None
        The slice to plot for each axis. If ``None``, the middle slice will be plotted. Otherwise, the **number
        of slices passed must be equal to the number of plotted axes** (equal to :math:`3` if ``axes=None``).
    transforms : Sequence[Callable[[np.ndarray], np.ndarray]] | None, default=None
        Potential transforms to apply to the image before plotting.

        .. important::
            No matter the transforms passed, the image will first be reoriented to the :term:`RAS+` coordinate system.

    figsize : tuple[float, float] | None, default=None
        The size of the figure. See :py:func:`matplotlib.pyplot.figure` for more details.
    title : str | None, default=None
        A potential title for the figures that will be plotted.

    Raises
    ------
    AssertionError
        If the number of slices passed is not equal to the number of plotted axes.

    Examples
    --------

    .. code-block:: python

        from neuroplot.plot.single import SinglePlot
        from neuroplot.transforms import RescaleIntensity

        plotter = SinglePlot(axes=[0, 2], slices=[55, 167], transforms=[RescaleIntensity()])

    .. code-block:: python

        >>> plotter.set_title("A first image")
        >>> plotter.plot("data/example_1.nii.gz")

    .. code-block:: python

        >>> plotter.set_title("Another image")
        >>> plotter.plot("data/example_2.nii.gz")

    See Also
    --------
    :py:class:`neuroplot.plot.multiple.MultiplePlot`
        To plot multiple neuroimages in a grid of subplots.
    """

    def __init__(
        self,
        axes: int | Sequence[int] | None = None,
        slices: int | Sequence[int] | None = None,
        transforms: Sequence[Callable[[np.ndarray], np.ndarray]] | None = None,
        figsize: tuple[float, float] | None = None,
        title: str | None = None,
    ) -> None:
        self.axes, self.slices = self._check_axes_and_slices(axes, slices)
        if transforms is None:
            transforms = []
        transforms = [tio.ToCanonical()] + transforms
        self.transforms = tio.Compose(transforms)
        self.figsize = figsize
        self.title = title

    def set_title(self, title: str | None) -> None:
        """
        To change the title of the future plot.

        Parameters
        ----------
        title : Optional[str]
            The new title.
        """
        self.title = title

    def plot(
        self,
        img_path: str | Path,
        show: bool = True,
    ) -> Figure:
        """
        Builds a plot of an image.

        Parameters
        ----------
        img_path : Union[str, Path]
            The path to the image to plot.
        show : bool, default=True
            Whether to display the figure.

        Returns
        -------
        matplotlib.figure.Figure
            The figure with the desired 2D slices.

        Raises
        ------
        IndexError
            If a slice passed in ``slices`` is out of bounds in this image.
        """
        image = tio.ScalarImage(path=img_path)
        np_image = self.transforms(image).numpy().squeeze(0)

        slices = self._get_slice_indices(np_image)

        fig, plot_axes = plt.subplots(1, len(self.axes), figsize=self.figsize)
        if len(self.axes) == 1:
            plot_axes = [plot_axes]  # turn it into an iterable

        for ax, slc, plot_axis in zip(self.axes, slices, plot_axes):
            plot_axis.set_xlabel(f"axis={ax}, slice={slc}")
            plot_axis.imshow(self._get_slice(np_image, ax, slc), cmap="gray")

        if self.title:
            fig.suptitle(self.title)

        if show:
            plt.show()

        return fig

    @staticmethod
    def _check_axes_and_slices(
        axes: int | Sequence[int] | None,
        slices: int | Sequence[int] | None,
    ) -> tuple[Sequence[int], Sequence[int] | None]:
        """
        To check that 'axes' and 'slices' are consistent.
        """
        if axes is None:
            axes = [0, 1, 2]
        elif isinstance(axes, int):
            axes = [axes]

        if slices is None:
            n_slices = len(axes)
        elif isinstance(slices, int):
            n_slices = 1
            slices = [slices]
        else:
            n_slices = len(slices)

        assert (
            len(axes) == n_slices
        ), f"Got {len(axes)} elements for 'axes', but {n_slices} for 'slices'."

        return axes, slices

    def _get_slice_indices(
        self,
        image: np.ndarray,
    ) -> Sequence[int]:
        """
        Checks that the wanted slice is not out of bounds for this image.
        If ``slices`` was set to ``None``, computes the slice index.
        """
        spatial_shape = np.array(image.shape)

        if self.slices:
            slices = self.slices
        else:
            slices = spatial_shape // 2

        for ax, slc in zip(self.axes, slices):
            if slc >= spatial_shape[ax]:
                raise IndexError(f"Slice {slc} is out of bounds in axis {ax}.")

        return slices

    @staticmethod
    def _get_slice(image: np.ndarray, ax: int, slc: int) -> np.ndarray:
        """
        Gets the slice from the image.
        """
        indices = [slice(None)] * len(image.shape)
        indices[ax] = slc
        return image[tuple(indices)]
