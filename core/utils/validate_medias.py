def validate_medias(object) -> bool:
    '''Validate if object has one or many medias.'''
    if object.media.all().count() <= 1:
        return False

    return True
