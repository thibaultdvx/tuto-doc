from pathlib import Path

import numpy as np
import torchio as tio
import shutil

TMP_DIR = Path(__file__).parent / "tmp"


def build_images(n: int = 1) -> list[Path]:
    TMP_DIR.mkdir(exist_ok=True)
    paths = []
    for k in range(n):
        image = tio.ScalarImage(tensor=np.random.randn(1, 8, 9, 10))
        path = (TMP_DIR / f"test_{k}").with_suffix(".nii.gz")
        image.save(path)
        paths.append(path)

    return paths


def remove_tmp_dir() -> None:
    if TMP_DIR.exists():
        shutil.rmtree(TMP_DIR)
