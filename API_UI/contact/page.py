import reflex as rx
from ..ui.base import base_page
from . import form, state, model

def contact_entry_list_item(contact: model.ConctacEntryModel):
    return rx.box(
        rx.heading(contact.first_name + " " + contact.last_name, size="4"),
        rx.text(contact.message),
        padding="2"
    )

#def foreach_callback(text):
#    return rx.box(rx.text(text))

def contact_page_list() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Contact Entries", size="5", text_align="center"),
            #rx.foreach(
            #    ["abc","abc","cde"],
            #    foreach_callback
            #),
            rx.foreach(
                state.ContactState.entries,
                contact_entry_list_item
            ),
            spacing="5",
            align="center",
            min_height="85vh",
        )
    )

def contact_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("Contact Us", size="9", text_align="center"),
            rx.cond(state.ContactState.did_submit,state.ContactState.thank_you,""),
            rx.desktop_only(
                rx.box(
                    form.contact_form(),
                    width="50vw"
                )
            ),
            rx.tablet_only(
                rx.box(
                    form.contact_form(),
                    width="75vw"
                )
            ),
            rx.mobile_only(
                rx.box(
                    form.contact_form(),
                    width="85vw"
                )
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id="my_child"
        )
    return base_page(my_child, hide_navbar=False)