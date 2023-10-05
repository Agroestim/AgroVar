from datetime import datetime
from typing import IO, Any

from django.core.files.base import File
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible


@deconstructible
class GridFS(Storage):
    """
    A MongoDB Grid File System Stroage implementation.

    TODO: Definir el sistema de almacenamiento para los ficheros
    GridFS.
    """

    def __init__(self) -> None:
        ...

    def open(self, name: str, mode: str = ...) -> File:
        return super().open(name, mode)

    def save(
        self, name: str | None, content: IO[Any], max_length: int | None = ...
    ) -> str:
        return super().save(name, content, max_length)

    def get_valid_name(self, name: str) -> str:
        return super().get_valid_name(name)

    def get_alternative_name(self, file_root: str, file_ext: str):
        ...

    def get_available_name(self, name: str, max_length: int | None = ...) -> str:
        return super().get_available_name(name, max_length)

    def generate_filename(self, filename: str) -> str:
        return super().generate_filename(filename)

    def path(self, name: str) -> str:
        return super().path(name)

    def delete(self, name: str) -> None:
        return super().delete(name)

    def exists(self, name: str) -> bool:
        return super().exists(name)

    def size(self, name: str) -> int:
        return super().size(name)

    def url(self, name: str | None) -> str:
        return super().url(name)

    def get_created_time(self, name: str) -> datetime:
        return super().get_created_time(name)

    def get_modified_time(self, name: str) -> datetime:
        return super().get_modified_time(name)
