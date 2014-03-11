import pkg_resources


__all__ = ["get_dependencies"]

def get_dependencies(pkgname):
    """Return dependencies of a package as a sorted list
    
    :param str pkgname: package name
    :return: list (empty list if no dependencies)
    """
    try:
        res = pkg_resources.require(pkgname)
        res = list(set(res))
        res.sort()
        return res
    except:
        return []
