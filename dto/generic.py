"""Base class for GigaChat API DTOs and it's methods."""

from typing import Any

from pydantic import BaseModel, ConfigDict


class GigaChatBaseModel(BaseModel):
    """Base class for GigaChat API DTOs."""

    model_config = ConfigDict(extra="forbid", use_enum_values=True)

    def model_dump(self, *, exclude_unset: bool = True, **kwargs) -> dict[str, Any]:
        """Generates a dictionary of the model data.

        Args:
            exclude_unset: whether to exclude unset fields from the dictionary.
            **kwargs: additional arguments to pass to the parent method.
        """
        return super().model_dump(exclude_unset=exclude_unset, **kwargs)
