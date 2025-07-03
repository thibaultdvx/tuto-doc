from pathlib import Path

import numpy as np
import torchio as tio


def build_images(tmp_dir, n: int = 1) -> list[Path]:
    tmp_dir.mkdir(exist_ok=True)
    paths = []
    for k in range(n):
        image = tio.ScalarImage(tensor=np.random.randn(1, 8, 9, 10))
        path = (tmp_dir / f"test_{k}").with_suffix(".nii.gz")
        image.save(path)
        paths.append(path)

    return paths
