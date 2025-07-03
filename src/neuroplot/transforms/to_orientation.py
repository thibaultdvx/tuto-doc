from torchio.transforms import ToOrientation as BaseToOrientation


class ToOrientation(BaseToOrientation):
    def __init__(self, orientation: str = "RAS") -> None:
        assert (
            "R" in orientation or "L" in orientation
        ), "'orientation' must contain 'R' (Right) or 'L' (Left)"
        assert (
            "A" in orientation or "P" in orientation
        ), "'orientation' must contain 'A' (Anterior) or 'L' (Posterior)"
        assert (
            "S" in orientation or "I" in orientation
        ), "'orientation' must contain 'S' (Superior) or 'I' (Inferior)"
        assert len(orientation) == 3, "'orientation' must contain 3 letters"
        super().__init__(orientation=orientation)
