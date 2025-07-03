from conftest import build_images, remove_tmp_dir

from neuroplot.plot.single import GIF


def test_GIF():
    path = build_images()[0]
    gif_maker = GIF(axis=2, duration=5)
    gif_maker.create(path, path.parent / "test.gif")
    remove_tmp_dir()
