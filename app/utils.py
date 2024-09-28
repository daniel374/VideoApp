import os


def clean_extension(file_name):
    name_without_ext, _ = os.path.splitext(file_name)
    return name_without_ext
