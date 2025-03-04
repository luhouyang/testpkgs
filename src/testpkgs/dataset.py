from importlib import resources


def get_flatland():
    """Get path to example "Flatland" [1]_ text file.

    Returns
    -------
    pathlib.PosixPath
        Path to file.

    References
    ----------
    .. [1] E. A. Abbott, "Flatland", Seeley & Co., 1884.
    """
    # with resources.path("testpkgs.data", "flatland.txt") as f:
    #     data_file_path = f
    data_file_path = resources.files("testpkgs.data") / "flatland.txt"
    return data_file_path
