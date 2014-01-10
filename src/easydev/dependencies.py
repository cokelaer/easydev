import pkg_resources


__all__ = ["get_dependencies"]

def get_dependencies(pkgname):
    try:
        res = pkg_resources.require(pkgname)
        res = list(set(res))
        res.sort()
        return res
    except:
        return []
