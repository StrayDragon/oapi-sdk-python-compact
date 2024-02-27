# Code generated by lark suite oapi sdk gen


from ....event.event import set_event_callback

from .model import *


class AwemeUserBindedAccountEventHandler:
    def __init__(self, callback):
        # type: (Callable[[Context, Config, AwemeUserBindedAccountEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, AwemeUserBindedAccountEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, AwemeUserBindedAccountEvent], Any]) -> None
        handler = AwemeUserBindedAccountEventHandler(callback)
        set_event_callback(
            conf,
            "aweme_ecosystem.aweme_user.binded_account_v1",
            handler.handle,
            clazz=AwemeUserBindedAccountEvent,
        )
