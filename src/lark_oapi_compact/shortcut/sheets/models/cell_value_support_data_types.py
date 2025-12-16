from __future__ import annotations

from enum import Enum

from ....compact import IS_V2, BaseModel, Field


class TextLink(BaseModel):
    type: str = "url"
    text: str
    link: str

    if not IS_V2:

        class Config:
            allow_population_by_field_name = True


class Formula(BaseModel):
    type: str = "formula"
    text: str

    if not IS_V2:

        class Config:
            allow_population_by_field_name = True


class MentionDocObjType(Enum):
    sheet = "sheet"
    doc = "doc"
    slide = "slide"
    bitable = "bitable"
    mindnote = "mindnote"


class MentionDoc(BaseModel):
    type: str = "mention"
    text_type: str = Field("fileToken", alias="textType")
    text: str
    obj_type: MentionDocObjType = Field(MentionDocObjType.doc, alias="objType")

    if not IS_V2:

        class Config:
            allow_population_by_field_name = True


class MentionUser(BaseModel):
    type: str = "mention"
    text: str
    text_type: str = Field("email", alias="textType")
    notify: bool = False
    grant_read_permission: bool = Field(False, alias="grantReadPermission")

    if not IS_V2:

        class Config:
            allow_population_by_field_name = True
