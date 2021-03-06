def has_privilege(method=None, resource=None, *args, **kwargs) -> bool:
    """Check if user with Administrator role can access a particular resource.
    """
    return __resources.get(resource, lambda *arg: False)(
        method, *args, **kwargs
    )


def __location_access(method=None, *args, **kwargs):
    return True


def __employee_access(method=None, *args, **kwargs):
    return True


__resources = {
    "location": __location_access,
    "employee": __employee_access
}
