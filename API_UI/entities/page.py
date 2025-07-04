import reflex as rx
import reflex_local_auth
from ..ui.base import base_page
from . import form

# def contact_entry_list_item(contact: model.ConctacEntryModel):
#     return rx.box(
#         rx.heading(contact.first_name + " " + contact.last_name, size="4"),
#         rx.text(contact.message),
#         padding="2"
#     )

# def foreach_callback(text):
#     return rx.box(rx.text(text))

# def contact_page_list() -> rx.Component:
#     return base_page(
#         rx.vstack(
#             rx.heading("Contact Entries", size="5", text_align="center"),
#             rx.foreach(
#                 ["abc","abc","cde"],
#                 foreach_callback
#             ),
#             # rx.foreach(
#             #     state.ContactState.entries,
#             #     contact_entry_list_item
#             # ),
#             spacing="5",
#             align="center",
#             min_height="85vh",
#         )
#     )

@reflex_local_auth.require_login
def abm_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("Entities CRUD Form", size="9", text_align="center"),
            rx.desktop_only(
                rx.box(
                    form.form_component(),
                    padding="20px",
                    max_width="600px",
                )
            ),
            rx.tablet_only(
                rx.box(
                    form.form_component(),
                    width="75vw"
                )
            ),
            rx.mobile_only(
                rx.box(
                    form.form_component(),
                    width="85vw"
                )
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="80vh",
            id="my_child"
        )
    return base_page(my_child)