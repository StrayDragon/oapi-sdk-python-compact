import os

import pytest
from lark_oapi_compact.shortcut.compact import FeishuOpenAPICompactSettings
from lark_oapi_compact.shortcut.driver import FeishuDriverShortcut
from lark_oapi_compact.shortcut.sheets import FeishuSheetsShortcut


@pytest.fixture(scope="session")
def feishu_settings():
    app_id = os.environ.get("FEISHU_APP_ID", "")
    app_secret = os.environ.get("FEISHU_APP_SECRET", "")
    if not app_id or not app_secret:
        raise ValueError("FEISHU_APP_ID and FEISHU_APP_SECRET must be set")
    return FeishuOpenAPICompactSettings(
        app_id=app_id,
        app_secret=app_secret,
        name="Test Feishu OAPI App",
    )


@pytest.fixture(scope="session")
def driver_shortcut(feishu_settings):
    return FeishuDriverShortcut(feishu_settings)


@pytest.fixture(scope="session")
def sheets_shortcut(feishu_settings):
    return FeishuSheetsShortcut(feishu_settings)


@pytest.fixture
def testing_folder_token(driver_shortcut):
    folder_meta = driver_shortcut.get_self_root_folder_meta()
    return folder_meta.token
