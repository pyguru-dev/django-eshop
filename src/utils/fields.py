from typing import Any
from django.db import models


class UppercaseCharField(models.CharField):
    
    def from_db_value(self, value, *args, **kwargs):
        return self.to_python(value)
    
    def to_python(self, value: Any) -> Any:
        val = super().to_python(value)
        if isinstance(val, str):
            return val.upper()
        return val
