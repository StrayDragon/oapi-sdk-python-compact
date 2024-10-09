import attr
from lark_oapi_compact.shortcut.utils import convert_model_to_dict, convert_remaintain_extra_model_to_dict, print_model


# 创建一个简单的 attr 类用于测试
@attr.s
class SimpleAttrModel:
    name = attr.ib(type=str)  # type: ignore
    age = attr.ib(type=int)  # type: ignore


# 创建一个模拟的 remaintain_extra 模型类
class MockRemaintainExtraModel:
    _types = {"name": str, "age": int}

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 创建一个嵌套的 remaintain_extra 模型类
class NestedMockRemaintainExtraModel:
    _types = {"info": MockRemaintainExtraModel, "extra": str}

    def __init__(self, info, extra):
        self.info = info
        self.extra = extra


# 添加一个空的 attr 模型测试
@attr.s
class EmptyAttrModel:
    pass


def test_convert_model_to_dict_empty_attr():
    model = EmptyAttrModel()
    result = convert_model_to_dict(model)
    assert result == {}


# 添加一个包含None值的 remaintain_extra 模型测试
class NoneValueRemaintainExtraModel:
    _types = {"name": str, "age": int}

    def __init__(self, name):
        self.name = name
        self.age = None


def test_convert_remaintain_extra_model_to_dict_none_value():
    model = NoneValueRemaintainExtraModel("Alice")
    result = convert_remaintain_extra_model_to_dict(model)
    assert result == {"name": "Alice", "age": None}


# 测试打印空模型
def test_print_empty_model(capsys):
    model = EmptyAttrModel()
    print_model(model)
    captured = capsys.readouterr()
    assert "EmptyAttrModel(" in captured.out
    assert ")" in captured.out


# 测试打印包含None值的模型
def test_print_model_with_none(capsys):
    model = NoneValueRemaintainExtraModel("Bob")
    print_model(model)
    captured = capsys.readouterr()
    assert "NoneValueRemaintainExtraModel(" in captured.out
    assert "name=Bob" in captured.out
    assert "age=None" in captured.out


def test_convert_model_to_dict_attr():
    model = SimpleAttrModel(name="Alice", age=30)  # type: ignore
    result = convert_model_to_dict(model)
    assert result == {"name": "Alice", "age": 30}


def test_convert_model_to_dict_remaintain_extra():
    model = MockRemaintainExtraModel("Bob", 25)
    result = convert_model_to_dict(model)
    assert result == {"name": "Bob", "age": 25}


def test_convert_model_to_dict_other():
    model = {"key": "value"}
    result = convert_model_to_dict(model)
    assert result is None


def test_convert_remaintain_extra_model_to_dict():
    model = MockRemaintainExtraModel("Charlie", 35)
    result = convert_remaintain_extra_model_to_dict(model)
    assert result == {"name": "Charlie", "age": 35}


def test_convert_remaintain_extra_model_to_dict_nested():
    inner_model = MockRemaintainExtraModel("David", 40)
    model = NestedMockRemaintainExtraModel(inner_model, "extra_info")
    result = convert_remaintain_extra_model_to_dict(model)
    assert result == {"info": {"name": "David", "age": 40}, "extra": "extra_info"}


def test_convert_remaintain_extra_model_to_dict_invalid():
    model = SimpleAttrModel(name="Eve", age=45)  # type: ignore
    result = convert_remaintain_extra_model_to_dict(model)
    assert result is None


def test_print_model_attr(capsys):
    model = SimpleAttrModel(name="Frank", age=50)  # type: ignore
    print_model(model)
    captured = capsys.readouterr()
    assert "SimpleAttrModel(" in captured.out
    assert "name=Frank" in captured.out
    assert "age=50" in captured.out


def test_print_model_remaintain_extra(capsys):
    model = MockRemaintainExtraModel("Grace", 55)
    print_model(model)
    captured = capsys.readouterr()
    assert "MockRemaintainExtraModel(" in captured.out
    assert "name=Grace" in captured.out
    assert "age=55" in captured.out


def test_print_model_other(capsys):
    model = ["item1", "item2"]
    print_model(model)
    captured = capsys.readouterr()
    assert str(model) in captured.out
