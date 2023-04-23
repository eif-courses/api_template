from typing import Optional

from sqlmodel import SQLModel, Field


class Document(SQLModel, table=True):
    # Auto Increment ID that's why is optional
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    title: str = Field()
    url: str = Field()
