from conftest import build_images
from torchio import Crop, RescaleIntensity

from neuroplot.plot.single import SinglePlot


def test_SinglePlot(tmp_path):
    path = build_images(tmp_path)[0]
    gif_maker = SinglePlot(
        axes=[0, 1],
        slices=[2, 3],
        transforms=[RescaleIntensity(), Crop(cropping=1)],
        figsize=(5, 5),
        title="ABC",
    )
    gif_maker.plot(path, show=False)
    gif_maker = SinglePlot(axes=[0, 1, 2])
    gif_maker.plot(path, show=False)
    gif_maker = SinglePlot(axes=1, slices=3)
    gif_maker.plot(path, show=False)
    gif_maker = SinglePlot(slices=[3, 4, 5])
    gif_maker.plot(path, show=False)
