from abc import ABC, abstractmethod
from contextlib import suppress
from dataclasses import dataclass
from typing import Any


@dataclass
class SyncContext:
    customer: dict[str, Any]
    config: dict[str, Any]


@dataclass
class RecordTransformation(ABC):
    @abstractmethod
    def transform(self, record: dict[str, Any], context: SyncContext) -> dict[str, Any]:
        pass


@dataclass
class AddFieldsRecordTransformation(RecordTransformation):
    fields: dict[str, Any]

    def transform(self, record: dict[str, Any], context: SyncContext) -> dict[str, Any]:
        for field_name, field_value in self.fields.items():
            if callable(field_value):
                with suppress(KeyError):
                    record[field_name] = field_value(context)
            else:
                record[field_name] = field_value

        return record
