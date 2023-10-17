from functools import lru_cache

from pandas import DataFrame, ExcelFile


class TechnicalDataFileProcessor:
    def __init__(self) -> None:
        ...

    def __del__(self):
        ...

    @lru_cache
    def excel_from_bytes(self, io: bytes) -> ExcelFile:
        ...

    @lru_cache
    def get_dataframe(self) -> DataFrame:
        ...
