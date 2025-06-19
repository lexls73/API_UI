import reflex as rx

config = rx.Config(
    app_name="API_UI",
    db_url="sqlite:///reflex.db",
    plugins=[rx.plugins.TailwindV3Plugin()],
)