from pathlib import Path
from typing import Union

import torchio as tio


class GIF:
    def __init__(self, axis: int, duration: float) -> None:
        assert axis in {0, 1, 2}, "'axis' must be 0, 1 or 2."
        assert duration > 0, "'duration' must be a positive float (in second)."
        self.axis = axis
        self.duration = duration
        self.reorient = tio.ToCanonical()

    def create(self, img_path: Union[str, Path], gif_path: Union[str, Path]) -> None:
        image = self.reorient(tio.ScalarImage(path=img_path))
        image.to_gif(axis=self.axis, duration=self.duration, output_path=gif_path)
