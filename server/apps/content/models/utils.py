import uuid


def get_upload_file_path(instance, filename: str) -> str:
    folder = f'{instance.__class__.__name__.lower()}s'
    return f'{folder}/{uuid.uuid4().hex}_{filename}'
