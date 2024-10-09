import time

import pytest
from lark_oapi_compact.shortcut.sheets.models import CellPos, CellsRange, SheetRange

SPREADSHEET_TITLE = "Test Spreadsheet"
SHEET_TITLE = f"Testing Sheet {time.time()}"


@pytest.fixture
def testing_spreadsheet(sheets_shortcut, testing_folder_token):
    spreadsheet = sheets_shortcut.create_spreadsheet(testing_folder_token, SPREADSHEET_TITLE)
    yield spreadsheet


@pytest.fixture
def testing_sheet_id(sheets_shortcut, testing_spreadsheet):
    sheet_id = sheets_shortcut.create_sheet(
        testing_spreadsheet.spreadsheet_token,
        title=SHEET_TITLE,
    ).get(SHEET_TITLE, "")
    assert sheet_id, f"Failed to create sheet {SHEET_TITLE}"
    yield sheet_id
    sheets_shortcut.remove_sheet(testing_spreadsheet.spreadsheet_token, sheet_id)


def test_create_spreadsheet(testing_spreadsheet):
    assert testing_spreadsheet is not None
    assert testing_spreadsheet.title == SPREADSHEET_TITLE


def test_change_spreadsheet_permission(sheets_shortcut, testing_spreadsheet):
    sheets_shortcut.change_spreadsheet_permission(testing_spreadsheet.spreadsheet_token, "tenant_editable")


def test_get_spreadsheet_sheets(sheets_shortcut, testing_spreadsheet):
    sheets = sheets_shortcut.get_spreadsheet_sheets(testing_spreadsheet.spreadsheet_token)
    assert isinstance(sheets, list)
    assert len(sheets) > 0


def test_find_cell_locations_in_sheet(sheets_shortcut, testing_spreadsheet, testing_sheet_id):
    sheets_shortcut.batch_update_values(
        testing_spreadsheet.spreadsheet_token,
        testing_sheet_id,
        [(CellsRange(start_pos=CellPos(x="A", y=1), end_pos=CellPos(x="A", y=1)), [["test_value"]])],
    )
    result = sheets_shortcut.find_cell_locations_in_sheet(
        testing_spreadsheet.spreadsheet_token, testing_sheet_id, "test_value"
    )
    assert result is not None
    assert len(result.matched_cells) > 0


def test_recursive_find_cell_locations_in_sheet(sheets_shortcut, testing_spreadsheet, testing_sheet_id):
    sheets_shortcut.batch_update_values(
        testing_spreadsheet.spreadsheet_token,
        testing_sheet_id,
        [
            (
                CellsRange(start_pos=CellPos(x="A", y=1), end_pos=CellPos(x="A", y=3)),
                [["value1"], ["value2"], ["value3"]],
            )
        ],
    )
    result = sheets_shortcut.recursive_find_cell_locations_in_sheet(
        testing_spreadsheet.spreadsheet_token, testing_sheet_id, ["value1", "value2", "value3"]
    )
    assert result is not None


def test_batch_handle_sheets(sheets_shortcut, testing_spreadsheet):
    new_sheet = sheets_shortcut.create_sheet(testing_spreadsheet.spreadsheet_token, "New Sheet")
    assert len(new_sheet) > 0
    for sheet_id in new_sheet.values():
        sheets_shortcut.remove_sheet(testing_spreadsheet.spreadsheet_token, sheet_id)
    sheets = sheets_shortcut.get_spreadsheet_sheets(testing_spreadsheet.spreadsheet_token)
    assert all(sheet.title != "New Sheet" for sheet in sheets)


def test_merge_and_unmerge_cells(sheets_shortcut, testing_spreadsheet, testing_sheet_id):
    merge_range = CellsRange(start_pos=CellPos(x="A", y=1), end_pos=CellPos(x="B", y=2))
    sheets_shortcut.merge_cells(testing_spreadsheet.spreadsheet_token, testing_sheet_id, merge_range)

    sheet_range = SheetRange(sheet_id=testing_sheet_id, start_pos=CellPos(x="A", y=1), end_pos=CellPos(x="B", y=2))
    sheets_shortcut.unmerge_cells(testing_spreadsheet.spreadsheet_token, sheet_range)


def test_prepend_and_append_insert_values(sheets_shortcut, testing_spreadsheet, testing_sheet_id):
    values = [["prepend1"], ["prepend2"]]
    sheets_shortcut.prepend_insert_values(testing_spreadsheet.spreadsheet_token, testing_sheet_id, values=values)

    values = [["append1"], ["append2"]]
    sheets_shortcut.append_insert_values(testing_spreadsheet.spreadsheet_token, testing_sheet_id, values=values)

    result = sheets_shortcut.batch_read_values(
        testing_spreadsheet.spreadsheet_token,
        testing_sheet_id,
        [CellsRange(start_pos=CellPos(x="A", y=1), end_pos=CellPos(x="A", y=4))],
    )
    assert list(result.values())[0] == [["prepend1"], ["prepend2"], ["append1"], ["append2"]]


def test_batch_update_and_read_values(sheets_shortcut, testing_spreadsheet, testing_sheet_id):
    update_range = CellsRange(start_pos=CellPos(x="A", y=1), end_pos=CellPos(x="B", y=2))
    values = [["A1", "B1"], ["A2", "B2"]]
    sheets_shortcut.batch_update_values(
        testing_spreadsheet.spreadsheet_token, testing_sheet_id, [(update_range, values)]
    )

    read_result = sheets_shortcut.batch_read_values(
        testing_spreadsheet.spreadsheet_token, testing_sheet_id, [update_range]
    )
    assert list(read_result.values())[0] == values


def test_update_formula_value_cell(sheets_shortcut, testing_spreadsheet, testing_sheet_id):
    formula = "=SUM(A1:A2)"
    result_cell = CellPos(x="B", y=3)
    sheets_shortcut.update_formula_value_cell(
        testing_spreadsheet.spreadsheet_token, testing_sheet_id, formula, result_cell
    )
    read_result = sheets_shortcut.batch_read_values(
        testing_spreadsheet.spreadsheet_token,
        testing_sheet_id,
        [CellsRange(start_pos=result_cell, end_pos=result_cell)],
        value_render_option="Formula",
    )
    assert list(read_result.values())[0] == [[formula]]


def test_update_formula_value_cell_using_sum_of_cell_range(sheets_shortcut, testing_spreadsheet, testing_sheet_id):
    target_range = CellsRange(start_pos=CellPos(x="A", y=1), end_pos=CellPos(x="A", y=2))
    result_cell = CellPos(x="B", y=3)
    sheets_shortcut.update_formula_value_cell_using_sum_of_cell_range(
        testing_spreadsheet.spreadsheet_token, testing_sheet_id, target_range, result_cell
    )
    read_result = sheets_shortcut.batch_read_values(
        testing_spreadsheet.spreadsheet_token,
        testing_sheet_id,
        [CellsRange(start_pos=result_cell, end_pos=result_cell)],
        value_render_option="Formula",
    )
    assert list(read_result.values())[0] == [["=SUM(A1:A2)"]]


def test_insert_and_delete_dimension(sheets_shortcut, testing_spreadsheet, testing_sheet_id):
    sheets_shortcut.insert_dimension(testing_spreadsheet.spreadsheet_token, testing_sheet_id, "ROWS", 0, 1)
    sheets_shortcut.delete_dimension(testing_spreadsheet.spreadsheet_token, testing_sheet_id, "ROWS", 1, 2)


def test_truncate_and_replace_sheet(sheets_shortcut, testing_spreadsheet, testing_sheet_id):
    sheets_shortcut.truncate_sheet(testing_spreadsheet.spreadsheet_token, testing_sheet_id)

    new_values = [["new1"], ["new2"]]
    sheets_shortcut.replace_sheet_by_values(testing_spreadsheet.spreadsheet_token, testing_sheet_id, new_values)

    read_result = sheets_shortcut.batch_read_values(
        testing_spreadsheet.spreadsheet_token,
        testing_sheet_id,
        [CellsRange(start_pos=CellPos(x="A", y=1), end_pos=CellPos(x="A", y=2))],
    )
    assert list(read_result.values())[0] == new_values


def test_insert_image_to_cell(sheets_shortcut, testing_spreadsheet, testing_sheet_id):
    cell_pos = CellPos(x="A", y=1)
    # 5x5的纯黑色图片
    # fmt: off
    image_byte_array = [137, 80, 78, 71, 13, 10, 26, 10, 0, 0, 0, 13, 73, 72, 68, 82, 0, 0, 0, 5, 0, 0, 0, 5, 8, 2, 0, 0, 0, 2, 13, 177, 178, 0, 0, 0, 12, 73, 68, 65, 84, 120, 156, 99, 96, 160, 46, 0, 0, 0, 80, 0, 1, 243, 48, 247, 42, 0, 0, 0, 0, 73, 69, 78, 68, 174, 66, 96, 130]  # noqa: E501
    # fmt: on
    sheets_shortcut.insert_image_to_cell(
        testing_spreadsheet.spreadsheet_token, testing_sheet_id, cell_pos, image_byte_array, "test_image.png"
    )
    assert True
