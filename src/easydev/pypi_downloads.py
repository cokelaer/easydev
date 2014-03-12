



def plot_pypi_downloads(package):
    """pLot number of downloads versus time


    .. plot::
        :include-source:

        >>> from easydev import pypi_downloads
        >>> df = pypi_downloads.plot_pypi_downloads("easydev")

        
    .. warnings:: requires pandas and vanity packages
    """
    import vanity
    releases = list(vanity.package_releases([package]))[0][1]
    downloads = []
    times = []
    data = list(vanity.release_data([package]))
    for i in range(0, len(releases)):
        if len(data[i][0]):
            dt = data[i][0][0]['upload_time']
            download = data[i][0][0]['downloads']
            tt = dt.timetuple()
            times.append([tt[0], tt[1], tt[2]])
            downloads.append(download)
    import pandas as pd
    import datetime
    df = pd.Series(downloads, [datetime.datetime(*x) for x in times],
            name=package)
    df = df.sort_index()
    df.cumsum().plot(marker="o")
    return df
