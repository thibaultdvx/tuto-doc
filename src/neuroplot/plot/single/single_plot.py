from pathlib import Path
from typing import Callable, Optional, Sequence, Union

import matplotlib.pyplot as plt
import numpy as np
import torchio as tio
from matplotlib.figure import Figure


class SinglePlot:
    def __init__(
        self,
        axes: Optional[Union[int, Sequence[int]]] = None,
        slices: Optional[Union[int, Sequence[int]]] = None,
        transforms: Optional[Sequence[Callable[[np.ndarray], np.ndarray]]] = None,
        figsize: Optional[tuple[float, float]] = None,
        title: Optional[str] = None,
    ) -> None:
        self.axes, self.slices = self._check_axes_and_slices(axes, slices)
        self.transforms = tio.Compose(transforms) if transforms else lambda x: x
        self.figsize = figsize
        self.title = title

    def set_title(self, title: Optional[str]) -> None:
        self.title = title

    def plot(
        self,
        img_path: Union[str, Path],
        show: bool = True,
    ) -> Figure:
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
        axes: Optional[Union[int, Sequence[int]]],
        slices: Optional[Union[int, Sequence[int]]],
    ) -> tuple[Sequence[int], Optional[Sequence[int]]]:
        if axes is None:
            axes = [0, 1, 2]
        elif isinstance(axes, int):
            axes = [axes]

        if slices is None:
            n_slices = 3
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
        indices = [slice(None)] * len(image.shape)
        indices[ax] = slc
        return image[tuple(indices)]
