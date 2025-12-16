"""Test pydantic compatibility layer."""

import pytest

from lark_oapi_compact.compact import (
    BaseModel,
    CompatBase,
    compat_to_dict,
    compat_to_json,
    create_field,
)
from lark_oapi_compact.shortcut.sheets.models import CellPos, CellsRange
from lark_oapi_compact.shortcut.sheets.models.cell_value_support_data_types import (
    Formula,
    MentionDoc,
    MentionUser,
    TextLink,
)


def test_basic_model_creation():
    """Test basic model creation works."""

    class TestModel(BaseModel):
        name: str
        age: int = 25

    model = TestModel(name="test")
    assert model.name == "test"
    assert model.age == 25


def test_field_with_alias():
    """Test that field aliases work correctly."""

    class TestModel(BaseModel):
        internal_name: str = create_field(..., alias="external_name")

    # Test with alias
    model1 = TestModel(external_name="test")
    assert model1.internal_name == "test"

    # Test with field name (if supported by version)
    try:
        model2 = TestModel(internal_name="test2")
        assert model2.internal_name == "test2"
    except Exception:
        # Some versions might not allow this, which is fine
        pass


def test_cell_pos_model():
    """Test CellPos model works with compatibility layer."""
    pos = CellPos(x="A", y=1)
    assert pos.x == "A"
    assert pos.y == 1
    assert pos.to_param_range() == "A1"


def test_cell_pos_from_literal():
    """Test CellPos.from_literal method."""
    pos = CellPos.from_literal("B10")
    assert pos is not None
    assert pos.x == "B"
    assert pos.y == 10


def test_cells_range_model():
    """Test CellsRange model works with compatibility layer."""
    start = CellPos(x="A", y=1)
    end = CellPos(x="C", y=3)
    range_obj = CellsRange(start_pos=start, end_pos=end)
    assert range_obj.start_pos.x == "A"
    assert range_obj.end_pos.x == "C"
    assert range_obj.to_param_range_pos_part() == "A1:C3"


def test_text_link_model():
    """Test TextLink model with field compatibility."""
    link = TextLink(text="Example", link="https://example.com")
    assert link.text == "Example"
    assert link.link == "https://example.com"
    assert link.type == "url"


def test_formula_model():
    """Test Formula model."""
    formula = Formula(text="=SUM(A1:A10)")
    assert formula.text == "=SUM(A1:A10)"
    assert formula.type == "formula"


def test_mention_doc_model():
    """Test MentionDoc model with field aliases."""
    mention = MentionDoc(
        text="Document",
        obj_type="doc",
    )
    assert mention.text == "Document"
    # The alias should work
    assert mention.text_type == "fileToken"


def test_mention_user_model():
    """Test MentionUser model with field aliases."""
    # Test creating with alias (proper way in Pydantic v1)
    mention = MentionUser(text="user@example.com", **{"grantReadPermission": True})
    assert mention.text == "user@example.com"
    assert mention.grant_read_permission is True
    assert mention.text_type == "email"

    # Test default value
    mention2 = MentionUser(text="user2@example.com")
    assert mention2.grant_read_permission is False  # Default value


def test_model_serialization():
    """Test that model serialization works."""
    # Test with regular BaseModel (CellPos doesn't use CompatBase)
    pos = CellPos(x="A", y=1)

    # Test native Pydantic methods
    data = pos.model_dump() if hasattr(pos, "model_dump") else pos.dict()
    assert data["x"] == "A"
    assert data["y"] == 1

    # Test JSON export
    json_str = pos.model_dump_json() if hasattr(pos, "model_dump_json") else pos.json()
    assert "A" in json_str
    assert "1" in json_str

    # Test standalone compat functions
    compat_data = compat_to_dict(pos)
    assert compat_data["x"] == "A"
    assert compat_data["y"] == 1

    # Test JSON export with standalone function
    compat_json = compat_to_json(pos)
    assert "A" in compat_json
    assert "1" in compat_json

    # Test with CompatBase model
    class TestCompatModel(BaseModel, CompatBase):
        name: str
        age: int = 25

    compat_model = TestCompatModel(name="test")

    # Test compat methods (instance methods)
    compat_data = compat_model.compat_to_dict()
    assert compat_data["name"] == "test"
    assert compat_data["age"] == 25

    # Test JSON export
    compat_json = compat_model.compat_to_json()
    assert "test" in compat_json


def test_compat_methods():
    """Test new compat methods work correctly."""

    # Test with simple model that doesn't use CompatBase
    class TestModel(BaseModel):
        name: str
        age: int = 25

    model = TestModel(name="test")
    assert model.name == "test"
    assert model.age == 25

    # Test with CompatBase model
    class TestCompatModel(BaseModel, CompatBase):
        name: str
        age: int = 25

    compat_model = TestCompatModel(name="compat_test")
    assert compat_model.name == "compat_test"
    assert compat_model.age == 25

    # Test serialization methods
    data = compat_model.compat_to_dict()
    assert data["name"] == "compat_test"
    assert data["age"] == 25

    # Test parsing methods
    new_model = TestCompatModel.compat_from_dict({"name": "new_test", "age": 30})
    assert new_model.name == "new_test"
    assert new_model.age == 30

    # Test JSON methods
    json_str = compat_model.compat_to_json()
    assert "compat_test" in json_str

    # Parse from JSON
    json_model = TestCompatModel.compat_from_json(json_str)
    assert json_model.name == "compat_test"
    assert json_model.age == 25


def test_model_validation():
    """Test that model validation works."""
    # Valid data
    pos = CellPos(x="A", y=1)
    assert pos.x == "A"

    # Invalid data should raise appropriate error
    with pytest.raises((ValueError, TypeError)):
        CellPos(x="A", y="invalid")
