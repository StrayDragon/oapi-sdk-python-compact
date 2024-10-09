import os

import pytest
from lark_oapi_compact.shortcut.group_robot import FeishuGroupRobotShortCut


@pytest.fixture
def group_robot_shortcut():
    web_hook_url = os.environ.get("FEISHU_GROUP_ROBOT_WEBHOOK_URL", "")
    sign_secret = os.environ.get("FEISHU_GROUP_ROBOT_SIGN_SECRET", "")
    if not all([web_hook_url, sign_secret]):
        raise ValueError("FEISHU_GROUP_ROBOT_WEBHOOK_URL and FEISHU_GROUP_ROBOT_SIGN_SECRET must be set")
    return FeishuGroupRobotShortCut(
        web_hook_url=web_hook_url,
        sign_secret=sign_secret,
    )


def test_send_message(group_robot_shortcut):
    message_data = {"msg_type": "text", "content": {"text": "This is a test message"}}
    group_robot_shortcut.send_message(message_data)
    assert True
