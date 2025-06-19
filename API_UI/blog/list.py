import reflex as rx
from ..ui.base import base_page
from . import state, model
from .. import navigation

def blog_post_detail_link(child:rx.Component, post: model.BlogPostModel):
    
    if post is None:
        return rx.fragment(child)
    
    post_id = post.id
    
    if post_id is None:
        return rx.fragment(child)
    
    root_path = navigation.routes.BLOG_POSTS_ROUTE
    post_detail_url = f"{root_path}/{post_id}"
    
    return rx.link(
            child,
            href=post_detail_url
        )
    
def blog_post_list_item(post: model.BlogPostModel):
    return rx.box(
        blog_post_detail_link(
            rx.heading(post.title),
            post
        ),
        padding="2"
    )

def blog_post_page_list() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Blog Post", size="5", text_align="center"),
            rx.button(
                "Add New Post",
                on_click=navigation.NavigationState.set_route(navigation.routes.BLOG_ADD_POST_ROUTE),
                size="3",
            ),
            rx.foreach(
                state.BlogPostState.posts,
                blog_post_list_item
            ),
            spacing="5",
            align="center",
            min_height="85vh",
        )
    )
