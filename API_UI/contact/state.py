import asyncio
import reflex as rx
from typing import List
from sqlmodel import select
from .model import ConctacEntryModel

class ContactState(rx.State):
    form_data: dict = {}
    entries: List['ConctacEntryModel'] = []
    did_submit: bool = False
    
    @rx.var
    def thank_you(self) -> str:
        first_name = self.form_data.get("first_name", "")
        return f"Thank you {first_name}".strip() + "!"
        
    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        #print(form_data)
        self.form_data = form_data
        data = form_data.copy()
        for k,v in data.items():
            if v == "" or v is None:
                continue
            
            data[k] = v
            
            # Strip whitespace from all fields
        with rx.session() as session:
            db_entry = ConctacEntryModel(
                **data  # Unpack the form data into the model
            )
            session.add(db_entry)
            session.commit()
            self.did_submit = True
            yield
            
        await asyncio.sleep(2)  # Simulate a delay for processing
        self.did_submit = False
        yield

    def list_entries(self):
        """List all contact entries."""
        with rx.session() as session:
            entries = session.exec(
                select(ConctacEntryModel)
            ).all()
            self.entries = entries
