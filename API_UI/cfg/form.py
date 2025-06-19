import reflex as rx
from ..auth.state import SessionState
from . import BigfiniteCfgState

def cfg_edit_form():
    user_info_obj = SessionState.authenticated_user_info
    username_via_user_obj = rx.cond(
        user_info_obj & user_info_obj.user,
        user_info_obj.user.username,
        "My Account"
    )
    return rx.form(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.cond(
                        BigfiniteCfgState.is_loading,
                        rx.spinner(color="blue", size="3"),
                        rx.fragment(),
                    )
                ),
                rx.select(
                    items=BigfiniteCfgState.config_data.keys().to(list),
                    value=BigfiniteCfgState.section,
                    on_change=BigfiniteCfgState.set_section,
                    name="section",
                    placeholder="Select section",
                    required=True,
                    width="150px"
                ),
                rx.input(
                    value=f"{username_via_user_obj}",
                    on_change=BigfiniteCfgState.set_user,
                    name="user",
                    #placeholder="User",
                    required=True,
                    read_only=True,
                    width="150px"
                ),
                rx.input(
                    value=BigfiniteCfgState.customer,
                    on_change=BigfiniteCfgState.set_customer,
                    name="customer",
                    placeholder="Customer",
                    required=True,
                    read_only=True,
                    width="150px"
                ),
                rx.input(
                    value=BigfiniteCfgState.password,
                    on_change=BigfiniteCfgState.set_password,
                    name="password",
                    placeholder="Enter Password",
                    required=True,
                    type="password",
                    width="150px"
                ),
                rx.button("Save", type="submit", width="150px"),
            ),
        ),
        on_submit=BigfiniteCfgState.save_section,
        reset_on_submit=True,
        width="90%",
        max_width="900px", # Por ejemplo, no más de 900px de ancho
        align="center"
    )