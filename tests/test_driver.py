def test_get_self_root_folder_meta(driver_shortcut):
    result = driver_shortcut.get_self_root_folder_meta()
    assert result is not None


def test_get_folder_meta(driver_shortcut):
    folder_token = driver_shortcut.get_self_root_folder_meta().token
    result = driver_shortcut.get_folder_meta(folder_token)
    assert result is not None
