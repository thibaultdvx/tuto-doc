from conftest import build_images
from torchio import Crop, RescaleIntensity

from neuroplot.plot.multiple import MultiplePlot


def test_SinglePlot(tmp_path):
    paths = build_images(tmp_path, n=2)
    img_dict = {"A": paths[0], "B": paths[1]}
    gif_maker = MultiplePlot(
        axes=[0, 1],
        slices=[2, 3],
        transforms=[RescaleIntensity(), Crop(cropping=1)],
        figsize=(5, 5),
        title="ABC",
    )
    gif_maker.plot(**img_dict, show=False)
    gif_maker = MultiplePlot(axes=[0, 1, 2])
    gif_maker.plot(**img_dict, show=False)
    gif_maker.plot(**{"A": paths[0]}, show=False)
    gif_maker = MultiplePlot(axes=1, slices=3)
    gif_maker.plot(**img_dict, show=False)
    gif_maker.plot(**{"A": paths[0]}, show=False)
    gif_maker = MultiplePlot(slices=[3, 4, 5])
    gif_maker.plot(**img_dict, show=False)
