# Code generated by lark suite oapi sdk gen

from typing import List, Dict, Any
from ....utils.dt import to_json_decorator
import attr


@to_json_decorator
@attr.s
class AppTableFieldPropertyOption:
    name = attr.ib(type=str, default=None, metadata={"json": "name"})
    id = attr.ib(type=str, default=None, metadata={"json": "id"})


@to_json_decorator
@attr.s
class AppTableFieldProperty:
    options = attr.ib(
        type=List[AppTableFieldPropertyOption],
        default=None,
        metadata={"json": "options"},
    )
    formatter = attr.ib(type=str, default=None, metadata={"json": "formatter"})
    date_format = attr.ib(type=str, default=None, metadata={"json": "date_format"})
    time_format = attr.ib(type=str, default=None, metadata={"json": "time_format"})
    auto_fill = attr.ib(type=bool, default=None, metadata={"json": "auto_fill"})
    multiple = attr.ib(type=bool, default=None, metadata={"json": "multiple"})
    table_id = attr.ib(type=str, default=None, metadata={"json": "table_id"})
    view_id = attr.ib(type=str, default=None, metadata={"json": "view_id"})
    fields = attr.ib(type=List[str], default=None, metadata={"json": "fields"})


@to_json_decorator
@attr.s
class AppTableField:
    field_id = attr.ib(type=str, default=None, metadata={"json": "field_id"})
    field_name = attr.ib(type=str, default=None, metadata={"json": "field_name"})
    type = attr.ib(type=int, default=None, metadata={"json": "type"})
    property = attr.ib(type=AppTableFieldProperty, default=None, metadata={"json": "property"})


@to_json_decorator
@attr.s
class AppTable:
    table_id = attr.ib(type=str, default=None, metadata={"json": "table_id"})
    revision = attr.ib(type=int, default=None, metadata={"json": "revision"})
    name = attr.ib(type=str, default=None, metadata={"json": "name"})


@to_json_decorator
@attr.s
class DeleteRecord:
    deleted = attr.ib(type=bool, default=None, metadata={"json": "deleted"})
    record_id = attr.ib(type=str, default=None, metadata={"json": "record_id"})


@to_json_decorator
@attr.s
class Person:
    id = attr.ib(type=str, default=None, metadata={"json": "id"})
    name = attr.ib(type=str, default=None, metadata={"json": "name"})
    en_name = attr.ib(type=str, default=None, metadata={"json": "en_name"})
    email = attr.ib(type=str, default=None, metadata={"json": "email"})


@to_json_decorator
@attr.s
class App:
    app_token = attr.ib(type=str, default=None, metadata={"json": "app_token"})
    name = attr.ib(type=str, default=None, metadata={"json": "name"})
    revision = attr.ib(type=int, default=None, metadata={"json": "revision"})


@to_json_decorator
@attr.s
class AppTableRecord:
    record_id = attr.ib(type=str, default=None, metadata={"json": "record_id"})
    fields = attr.ib(type=Dict[str, Any], default=None, metadata={"json": "fields"})


@to_json_decorator
@attr.s
class AppTableView:
    view_id = attr.ib(type=str, default=None, metadata={"json": "view_id"})
    view_name = attr.ib(type=str, default=None, metadata={"json": "view_name"})
    view_type = attr.ib(type=str, default=None, metadata={"json": "view_type"})


@to_json_decorator
@attr.s
class Attachment:
    file_token = attr.ib(type=str, default=None, metadata={"json": "file_token"})
    name = attr.ib(type=str, default=None, metadata={"json": "name"})
    type = attr.ib(type=str, default=None, metadata={"json": "type"})
    size = attr.ib(type=int, default=None, metadata={"json": "size"})
    url = attr.ib(type=str, default=None, metadata={"json": "url"})
    tmp_url = attr.ib(type=str, default=None, metadata={"json": "tmp_url"})


@to_json_decorator
@attr.s
class ReqTable:
    name = attr.ib(type=str, default=None, metadata={"json": "name"})


@to_json_decorator
@attr.s
class Url:
    text = attr.ib(type=str, default=None, metadata={"json": "text"})
    link = attr.ib(type=str, default=None, metadata={"json": "link"})


@attr.s
class AppGetResult:
    app = attr.ib(type=App, default=None, metadata={"json": "app"})


@attr.s
class AppTableListResult:
    has_more = attr.ib(type=bool, default=None, metadata={"json": "has_more"})
    page_token = attr.ib(type=str, default=None, metadata={"json": "page_token"})
    total = attr.ib(type=int, default=None, metadata={"json": "total"})
    items = attr.ib(type=List[AppTable], default=None, metadata={"json": "items"})


@to_json_decorator
@attr.s
class AppTableBatchCreateReqBody:
    tables = attr.ib(type=List[ReqTable], default=None, metadata={"json": "tables"})


@attr.s
class AppTableBatchCreateResult:
    table_ids = attr.ib(type=List[str], default=None, metadata={"json": "table_ids"})


@to_json_decorator
@attr.s
class AppTableCreateReqBody:
    table = attr.ib(type=ReqTable, default=None, metadata={"json": "table"})


@attr.s
class AppTableCreateResult:
    table_id = attr.ib(type=str, default=None, metadata={"json": "table_id"})


@to_json_decorator
@attr.s
class AppTableBatchDeleteReqBody:
    table_ids = attr.ib(type=List[str], default=None, metadata={"json": "table_ids"})


@attr.s
class AppTableFieldListResult:
    has_more = attr.ib(type=bool, default=None, metadata={"json": "has_more"})
    page_token = attr.ib(type=str, default=None, metadata={"json": "page_token"})
    total = attr.ib(type=int, default=None, metadata={"json": "total"})
    items = attr.ib(type=List[AppTableField], default=None, metadata={"json": "items"})


@attr.s
class AppTableFieldCreateResult:
    field = attr.ib(type=AppTableField, default=None, metadata={"json": "field"})


@attr.s
class AppTableFieldDeleteResult:
    field_id = attr.ib(type=str, default=None, metadata={"json": "field_id"})
    deleted = attr.ib(type=bool, default=None, metadata={"json": "deleted"})


@attr.s
class AppTableFieldUpdateResult:
    field = attr.ib(type=AppTableField, default=None, metadata={"json": "field"})


@to_json_decorator
@attr.s
class AppTableRecordBatchDeleteReqBody:
    records = attr.ib(type=List[str], default=None, metadata={"json": "records"})


@attr.s
class AppTableRecordBatchDeleteResult:
    records = attr.ib(type=List[DeleteRecord], default=None, metadata={"json": "records"})


@to_json_decorator
@attr.s
class AppTableRecordBatchCreateReqBody:
    records = attr.ib(type=List[AppTableRecord], default=None, metadata={"json": "records"})


@attr.s
class AppTableRecordBatchCreateResult:
    records = attr.ib(type=List[AppTableRecord], default=None, metadata={"json": "records"})


@attr.s
class AppTableRecordGetResult:
    record = attr.ib(type=AppTableRecord, default=None, metadata={"json": "record"})


@attr.s
class AppTableRecordUpdateResult:
    record = attr.ib(type=AppTableRecord, default=None, metadata={"json": "record"})


@attr.s
class AppTableRecordListResult:
    has_more = attr.ib(type=bool, default=None, metadata={"json": "has_more"})
    page_token = attr.ib(type=str, default=None, metadata={"json": "page_token"})
    total = attr.ib(type=int, default=None, metadata={"json": "total"})
    items = attr.ib(type=List[AppTableRecord], default=None, metadata={"json": "items"})


@to_json_decorator
@attr.s
class AppTableRecordBatchUpdateReqBody:
    records = attr.ib(type=List[AppTableRecord], default=None, metadata={"json": "records"})


@attr.s
class AppTableRecordBatchUpdateResult:
    records = attr.ib(type=List[AppTableRecord], default=None, metadata={"json": "records"})


@attr.s
class AppTableRecordCreateResult:
    record = attr.ib(type=AppTableRecord, default=None, metadata={"json": "record"})


@attr.s
class AppTableViewCreateResult:
    app_table_view = attr.ib(type=AppTableView, default=None, metadata={"json": "app.table.view"})


@attr.s
class AppTableViewListResult:
    items = attr.ib(type=List[AppTableView], default=None, metadata={"json": "items"})
    page_token = attr.ib(type=str, default=None, metadata={"json": "page_token"})
    has_more = attr.ib(type=bool, default=None, metadata={"json": "has_more"})
    total = attr.ib(type=int, default=None, metadata={"json": "total"})
