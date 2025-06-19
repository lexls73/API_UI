import reflex as rx
import reflex_local_auth

class NavigationState(rx.State):
    """State class for managing navigation in the app."""
    current_route = "/"

    def set_route(self, route: str):
        """Set the current route."""
        self.current_route = route
        return rx.redirect(route)
    
    def get_current_route(self) -> str:
        """Get the current route."""
        return self.current_route