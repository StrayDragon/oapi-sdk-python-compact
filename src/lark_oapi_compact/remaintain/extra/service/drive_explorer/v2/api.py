# Code generated by lark suite oapi sdk gen

from typing import *

from ....api import (
    Request as APIRequest,
    set_timeout,
    set_tenant_key,
    set_user_access_token,
    set_path_params,
    set_query_params,
)
from ....consts import (
    ACCESS_TOKEN_TYPE_TENANT,
    ACCESS_TOKEN_TYPE_USER,
)
from .model import *


class Service:
    def __init__(self, conf):
        # type: (Config) -> None
        self.conf = conf
        self.files = FileService(self)
        self.folders = FolderService(self)


class FileService:
    def __init__(self, service):
        # type: (Service) -> None
        self.service = service

    def copy(self, body, tenant_key=None, user_access_token=None, timeout=None):
        # type: (FileCopyReqBody, str, str, int) -> FileCopyReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        if user_access_token is not None:
            request_opts += [set_user_access_token(user_access_token)]

        return FileCopyReqCall(self, body, request_opts=request_opts)

    def create(self, body, tenant_key=None, user_access_token=None, timeout=None):
        # type: (FileCreateReqBody, str, str, int) -> FileCreateReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        if user_access_token is not None:
            request_opts += [set_user_access_token(user_access_token)]

        return FileCreateReqCall(self, body, request_opts=request_opts)

    def docs_delete(self, tenant_key=None, user_access_token=None, timeout=None):
        # type: (str, str, int) -> FileDocsDeleteReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        if user_access_token is not None:
            request_opts += [set_user_access_token(user_access_token)]

        return FileDocsDeleteReqCall(self, request_opts=request_opts)

    def spreadsheets_delete(self, tenant_key=None, user_access_token=None, timeout=None):
        # type: (str, str, int) -> FileSpreadsheetsDeleteReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        if user_access_token is not None:
            request_opts += [set_user_access_token(user_access_token)]

        return FileSpreadsheetsDeleteReqCall(self, request_opts=request_opts)


class FolderService:
    def __init__(self, service):
        # type: (Service) -> None
        self.service = service

    def children(self, tenant_key=None, user_access_token=None, timeout=None):
        # type: (str, str, int) -> FolderChildrenReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        if user_access_token is not None:
            request_opts += [set_user_access_token(user_access_token)]

        return FolderChildrenReqCall(self, request_opts=request_opts)

    def create(self, body, tenant_key=None, user_access_token=None, timeout=None):
        # type: (FolderCreateReqBody, str, str, int) -> FolderCreateReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        if user_access_token is not None:
            request_opts += [set_user_access_token(user_access_token)]

        return FolderCreateReqCall(self, body, request_opts=request_opts)

    def meta(self, tenant_key=None, user_access_token=None, timeout=None):
        # type: (str, str, int) -> FolderMetaReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        if user_access_token is not None:
            request_opts += [set_user_access_token(user_access_token)]

        return FolderMetaReqCall(self, request_opts=request_opts)

    def root_meta(self, tenant_key=None, user_access_token=None, timeout=None):
        # type: (str, str, int) -> FolderRootMetaReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        if user_access_token is not None:
            request_opts += [set_user_access_token(user_access_token)]

        return FolderRootMetaReqCall(self, request_opts=request_opts)


class FileCopyReqCall:
    def __init__(self, service, body, request_opts=None):
        # type: (FileService, FileCopyReqBody, List[Any]) -> None

        self.service = service
        self.body = body
        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_fileToken(self, file_token):
        # type: (str) -> FileCopyReqCall
        self.path_params["fileToken"] = file_token
        return self

    def do(self):
        # type: () -> APIResponse[Type[FileCopyResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/drive/explorer/v2/file/copy/files/:fileToken",
            "POST",
            [ACCESS_TOKEN_TYPE_TENANT, ACCESS_TOKEN_TYPE_USER],
            self.body,
            output_class=FileCopyResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class FileCreateReqCall:
    def __init__(self, service, body, request_opts=None):
        # type: (FileService, FileCreateReqBody, List[Any]) -> None

        self.service = service
        self.body = body
        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_folderToken(self, folder_token):
        # type: (str) -> FileCreateReqCall
        self.path_params["folderToken"] = folder_token
        return self

    def do(self):
        # type: () -> APIResponse[Type[FileCreateResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/drive/explorer/v2/file/:folderToken",
            "POST",
            [ACCESS_TOKEN_TYPE_TENANT, ACCESS_TOKEN_TYPE_USER],
            self.body,
            output_class=FileCreateResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class FileDocsDeleteReqCall:
    def __init__(self, service, request_opts=None):
        # type: (FileService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_docToken(self, doc_token):
        # type: (str) -> FileDocsDeleteReqCall
        self.path_params["docToken"] = doc_token
        return self

    def do(self):
        # type: () -> APIResponse[Type[FileDocsDeleteResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/drive/explorer/v2/file/docs/:docToken",
            "DELETE",
            [ACCESS_TOKEN_TYPE_TENANT, ACCESS_TOKEN_TYPE_USER],
            None,
            output_class=FileDocsDeleteResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class FileSpreadsheetsDeleteReqCall:
    def __init__(self, service, request_opts=None):
        # type: (FileService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_spreadsheetToken(self, spreadsheet_token):
        # type: (str) -> FileSpreadsheetsDeleteReqCall
        self.path_params["spreadsheetToken"] = spreadsheet_token
        return self

    def do(self):
        # type: () -> APIResponse[Type[FileSpreadsheetsDeleteResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/drive/explorer/v2/file/spreadsheets/:spreadsheetToken",
            "DELETE",
            [ACCESS_TOKEN_TYPE_TENANT, ACCESS_TOKEN_TYPE_USER],
            None,
            output_class=FileSpreadsheetsDeleteResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class FolderChildrenReqCall:
    def __init__(self, service, request_opts=None):
        # type: (FolderService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]
        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_folderToken(self, folder_token):
        # type: (str) -> FolderChildrenReqCall
        self.path_params["folderToken"] = folder_token
        return self

    def set_types(self, types):
        # type: (List[str]) -> FolderChildrenReqCall
        self.query_params["types"] = types
        return self

    def do(self):
        # type: () -> APIResponse[Type[FolderChildrenResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/drive/explorer/v2/folder/:folderToken/children",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT, ACCESS_TOKEN_TYPE_USER],
            None,
            output_class=FolderChildrenResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class FolderCreateReqCall:
    def __init__(self, service, body, request_opts=None):
        # type: (FolderService, FolderCreateReqBody, List[Any]) -> None

        self.service = service
        self.body = body
        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_folderToken(self, folder_token):
        # type: (str) -> FolderCreateReqCall
        self.path_params["folderToken"] = folder_token
        return self

    def do(self):
        # type: () -> APIResponse[Type[FolderCreateResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/drive/explorer/v2/folder/:folderToken",
            "POST",
            [ACCESS_TOKEN_TYPE_TENANT, ACCESS_TOKEN_TYPE_USER],
            self.body,
            output_class=FolderCreateResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class FolderMetaReqCall:
    def __init__(self, service, request_opts=None):
        # type: (FolderService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_folderToken(self, folder_token):
        # type: (str) -> FolderMetaReqCall
        self.path_params["folderToken"] = folder_token
        return self

    def do(self):
        # type: () -> APIResponse[Type[FolderMetaResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/drive/explorer/v2/folder/:folderToken/meta",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT, ACCESS_TOKEN_TYPE_USER],
            None,
            output_class=FolderMetaResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class FolderRootMetaReqCall:
    def __init__(self, service, request_opts=None):
        # type: (FolderService, List[Any]) -> None

        self.service = service

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def do(self):
        # type: () -> APIResponse[Type[FolderRootMetaResult]]
        root_service = self.service.service

        conf = root_service.conf
        req = APIRequest(
            "/open-apis/drive/explorer/v2/root_folder/meta",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT, ACCESS_TOKEN_TYPE_USER],
            None,
            output_class=FolderRootMetaResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp
