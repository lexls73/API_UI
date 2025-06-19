import reflex as rx
from . import state

def blog_post_add_form() -> rx.Component:
    return rx.form(
            rx.vstack(
                rx.hstack(
                    rx.input(
                        name="title",
                        placeholder="Title",
                        required=True,
                        type="text",
                        width="100%"
                    ),
                    width="100%"
                ),
                rx.text_area(
                    name="content",
                    placeholder="Your content here...",
                    required=True,
                    width="100%",
                    height="50vh"
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=state.BlogAddPostFormState.handle_submit,
            reset_on_submit=True,
        )