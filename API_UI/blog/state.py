from typing import Optional, List
import reflex as rx

from sqlmodel import select

from .model import BlogPostModel

class BlogPostState(rx.State):
    """State class for managing blog posts."""
    
    posts: List['BlogPostModel'] = []
    post: Optional[BlogPostModel] = None
    
    @rx.var
    def blog_post_id(self) -> Optional[int]:
        return self.router.page.params.get("blog_id",None)
    
    def add_posts(self, form_data:dict):
        with rx.session() as session:
            post = BlogPostModel(**form_data)
            #print("adding", post)
            session.add(post)
            session.commit()
            session.refresh(post)
            #print("added", post)
            self.post = post
    
    def load_posts(self):
        with rx.session() as session:
            """Load all blog posts from the database."""
            posts = session.exec(
                select(BlogPostModel)
            ).all()
            self.posts = posts
    
    def load_post_detail(self):
        with rx.session() as session:
            """Load all blog posts from the database."""
            if self.blog_post_id == "":
                self.post = None
                return
            result = session.exec(
                select(BlogPostModel).where(BlogPostModel.id == self.blog_post_id
            ).one_or_none())
            self.posts = result

class BlogAddPostFormState(BlogPostState):
    form_data: dict = {}
    
    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        self.add_posts(form_data)