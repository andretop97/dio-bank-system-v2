def find_object_by_attribute(list_obj: list[object], attribute_key, value) -> object:
    for obj in list_obj:
        if getattr(obj, attribute_key) == value:
            return obj
    return None
