from conftest import build_images

from neuroplot.plot.single import GIF


def test_GIF(tmp_path):
    path = build_images(tmp_path)[0]
    gif_maker = GIF(axis=2, duration=5)
    gif_maker.create(path, path.parent / "test.gif")
