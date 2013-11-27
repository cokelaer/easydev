import pkg_resources


__all__ = ["get_dependencies"]

def get_dependencies(pkgname):
    try:
        res = pkg_resources.require(pkgname)
        res.sort()
        return res
    except:
        return []
