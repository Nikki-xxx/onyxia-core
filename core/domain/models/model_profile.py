from __future__ import annotations


class ModelProfile:
    """
    Información pública de una modelo dentro de Onyxia.
    """

    def __init__(
        self,
        display_name: str,
        country: str,
        age: int | None = None,
        bio: str | None = None,
    ):
        self.display_name = display_name
        self.country = country
        self.age = age
        self.bio = bio

    def update_bio(self, bio: str):
        self.bio = bio