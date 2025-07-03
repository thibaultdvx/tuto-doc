from pathlib import Path
from typing import Union

import matplotlib.pyplot as plt
import torchio as tio
from matplotlib.figure import Figure
import numpy as np
from ..single import SinglePlot


class MultiplePlot(SinglePlot):
    def plot(    # pylint: disable=arguments-differ
        self,
        show: bool = True,
        **kwargs: Union[str, Path],
    ) -> Figure:
        images: dict[str, tio.ScalarImage] = {
            name: self.transforms(tio.ScalarImage(path=path)).numpy().squeeze(0)
            for name, path in kwargs.items()
        }

        fig, plot_axes = plt.subplots(len(images), len(self.axes), figsize=self.figsize)
        if len(images) == 1:
            plot_axes = np.expand_dims(plot_axes, axis=0)
        if len(self.axes) == 1:
            plot_axes = np.expand_dims(plot_axes, axis=1)

        for i, (name, image) in enumerate(images.items()):
            slice_indices = self._get_slice_indices(image)

            for j, (ax, slc) in enumerate(zip(self.axes, slice_indices)):
                if j == 0:
                    plot_axes[i, j].set_ylabel(name)
                plot_axes[i, j].set_xlabel(f"axis={ax}, slice={slc}")
                plot_axes[i, j].imshow(self._get_slice(image, ax, slc))

        if self.title:
            fig.suptitle(self.title)

        if show:
            plt.show()

        return fig
