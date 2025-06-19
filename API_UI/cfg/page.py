import reflex as rx
import reflex_local_auth
from ..ui.base import base_page
from . import form, BigfiniteCfgState

def render_cfg_item(item):
    return rx.box(
        rx.text(f"[{item[0]}]"),
        rx.text(f"user: {item[1].get('user', '')}"),
        rx.text(f"customer: {item[1].get('customer', '')}"),
        rx.text(f"password: {item[1].get('password', '')}"),
        padding="2",
        border="1px solid #ccc",
        margin="2"
    )

@reflex_local_auth.require_login
def cfg_page():
    my_child = rx.vstack(
        rx.heading(f"Edit file: {BigfiniteCfgState.cfg_path}"),
        rx.vstack(
            rx.cond(
                BigfiniteCfgState.is_loading,
                rx.spinner(color="blue", size="3"),
                rx.fragment(),
            )
        ),
        #rx.button("Load Config", on_click=BigfiniteCfgState.load_config),
        rx.cond(
                BigfiniteCfgState.load_ok,
                rx.fragment(),
                rx.button("Load Config", on_click=BigfiniteCfgState.load_config),
            ),
        rx.cond(
                BigfiniteCfgState.load_ok,
                rx.text("Config Loaded"),
                rx.text("Click for Config Load"),
            ),
        form.cfg_edit_form(),
        spacing="5",
        justify="center",
        align="center",
        min_height="80vh",
        id="my_child"
    )
    
    return base_page(my_child, hide_navbar=False)