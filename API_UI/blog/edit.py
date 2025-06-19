import reflex as rx
from ..ui.base import base_page
#from . import forms

class EditExampleState(rx.State):
    title:str = "Helo World"
    content:str = "This is a blog post content."
    
    def handle_content_change(self,value):
        self.content = value
    
    def handle_submit(self, form_data: dict):
        print(form_data)

def blog_post_edit_form() -> rx.Component:
    return rx.form(
            rx.vstack(
                rx.hstack(
                    rx.input(
                        value=EditExampleState.title,
                        on_change=EditExampleState.set_title,
                        name="title",
                        placeholder="Title",
                        required=True,
                        type="text",
                        width="100%"
                    ),
                    width="100%"
                ),
                rx.text_area(
                    value=EditExampleState.content,
                    on_change=EditExampleState.handle_content_change,
                    name="content",
                    placeholder="Your content here...",
                    required=True,
                    width="100%",
                    height="50vh"
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=EditExampleState.handle_submit
        )

def blog_post_edit_page() -> rx.Component:
    my_form = blog_post_edit_form()
    my_child = rx.vstack(
            rx.heading("Edit Blog Post", size="9", text_align="center"),
            rx.desktop_only(
                rx.box(
                    my_form,
                    width="50vw"
                )
            ),
            rx.tablet_only(
                rx.box(
                    my_form,
                    width="75vw"
                )
            ),
            rx.mobile_only(
                rx.box(
                    my_form,
                    width="85vw"
                )
            ),
            spacing="5",
            align="center",
            min_height="90vh"
        )
    return base_page(my_child, hide_navbar=False)