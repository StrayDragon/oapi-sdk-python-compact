import pytest

from lark_oapi_compact.shortcut.message import FeishuMessageShortcut


@pytest.fixture
def message_shortcut(feishu_settings):
    return FeishuMessageShortcut(feishu_settings)


@pytest.mark.skip(reason="TODO: Not total implemented!")
def test_send_group_robot_message(message_shortcut):
    body = {"msg_type": "text", "content": {"text": "This is a test message"}}
    result = message_shortcut.send_group_robot_message(body)
    assert result is not None
