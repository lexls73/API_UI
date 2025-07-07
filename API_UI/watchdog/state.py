import os
import reflex as rx
from datetime import datetime
from geopy.geocoders import Nominatim
from bigfinite_api_client.api_simul import api
from .. import utils

class WatchdogState(rx.State):
    """Define el estado del formulario."""
    environment: str = ""
    mode:str = ""
    agent_id:str = ""
    file_name:str = ""
    agent_name = ""
    description: str = "Created by Watchdog UI"
    triggering_type: str = ""
    custom_tags: str = ""
    isa_tags: str = ""
    profiles:str = ""
    city_country: str = "Barcelona, Spain"
    is_submitting: bool = False
    data_getting: bool = False
    
    @staticmethod
    def get_agent(env: str, agent_id: str):

        os.environ["AIZON_ENVIRONMENT"] = env
        PATH = "DATA/WATCHDOG/"
        url = f"/agents/{agent_id}"
        res = api(url, "GET")

        utils.common_utils.save_json(PATH,agent_id, res["json"])
        utils.common_utils.save_json(PATH,f"{agent_id}_trigger", res["json"]["triggers"])
    
    @staticmethod
    def create_agent(
        env: str,
        file_name: str,
        agent_id: str,
        agent_name: str,
        agent_description: str,
        triggering_type: str = "value",
        custom_tags: list = [],
        isa_tags: list = [],
        city_country: str = "Barcelona, Spain",
        profiles: list = ["admin"],
    ):

        os.environ["AIZON_ENVIRONMENT"] = env
        geolocator = Nominatim(user_agent="geoapi")
        location = geolocator.geocode(city_country)
        geolocation = {"lat": location.latitude, "lng": location.longitude}

        listened_Entities = utils.common_utils.load_json("entities")

        for listened_Entity in listened_Entities.values():

            url = "elements"
            entity_type = listened_Entity["type"]
            entity_id = listened_Entity["id"]

            url = utils.common_utils.set_type(entity_type)

            body = {
                "active": True,
                "code": entity_id,
                "customTags": custom_tags,
                "dataType": "JSON",
                "description": f"Script created {entity_id}",
                "geolocation": geolocation,
                "id": entity_id,
                "uom": {
                    "description": "na",
                    "magnitude": "na",
                    "name": "na",
                    "uom": "na",
                },
            }

            api(url, "POST", body)

        triggers = utils.common_utils.load_json(f"{file_name}_trigger")
        frequency = "0 */2 * * *"

        for v in triggers.values():
            if v["action"]["actionType"] == "newValue":
                triggers_entity_id_type = v["action"]["beID"]

                aux = triggers_entity_id_type.split(";")

                url = utils.common_utils.set_type(aux[1])

                body = {
                    "active": True,
                    "code": aux[0],
                    "customTags": custom_tags,
                    "dataType": "JSON",
                    "description": f"Script created {aux[0]}",
                    "geolocation": geolocation,
                    "id": aux[0],
                    "uom": {
                        "description": "na",
                        "magnitude": "na",
                        "name": "na",
                        "uom": "na",
                    },
                }

                api(url, "POST", body)

        url = "/agents"

        body = {
            "id": agent_id,
            "code": agent_name,
            "expiration": "2030-12-31",
            "description": agent_description,
            "customTags": custom_tags,
            "isaTags": isa_tags,
            "active": True,
            "triggers": [],
            "geolocation": geolocation,
            "triggeringType": triggering_type,
            "profiles": profiles,
        }

        for k, v in triggers.items():
            body["triggers"].append(v)

        if triggering_type == "cron":
            body["cron"] = frequency
        else:
            body["listenedEntities"] = []

            for listened_Entity in listened_Entities.values():
                body["listenedEntities"].append(listened_Entity)

        api(url, "POST", body)

    def reset_fields(self):
        self.environment = ""
        self.mode
        self.agent_id = ""
        self.file_name = ""
        self.agent_name = ""
        self.description = "Created by Watchdog UI" 
        self.triggering_type = ""
        self.custom_tags = ""
        self.isa_tags = ""
        self.profiles = ""
        self.city_country = "Barcelona, Spain"
        self.is_submitting = False
        self.data_getting = False
        yield

    def handle_submit(self, form_data: dict):
        # 1. Mostrar el spinner
        self.is_submitting = True
        """Maneja el envío del formulario."""
        self.environment = form_data.get("env", "").strip()
        self.mode = form_data.get("mode", "").strip()
        self.agent_id = form_data.get("agent_id", "").strip()
        self.file_name = form_data.get("file_name", "").strip()
        self.agent_name = form_data.get("agent_name", "").strip()
        self.description = form_data.get("description", "Created by Watchdog UI").strip()
        self.triggering_type = form_data.get("triggering_type", "").strip()
        self.custom_tags = form_data.get("custom_tags", "").strip()
        self.isa_tags = form_data.get("isa_tags", "").strip()
        self.profiles = form_data.get("profiles", "").strip()
        self.city_country = form_data.get("city_country", "Barcelona, Spain").strip()
        yield

        if self.mode == "get":

            self.get_agent(self.environment,self.agent_id)
            self.data_getting = True

        elif self.mode == "create":

            if cs := '':
                cs = self.custom_tags.split(',')
            else:
                cs = []
            if self.isa_tags != '':
                pr = self.profiles.split(',')
            else:
                pr = []
            if self.isa_tags != '':
                isa = self.isa_tags.split(',')
            else:
                isa = []

            self.create_agent(
                env=self.environment,
                file_name=self.file_name,
                agent_id=self.agent_id,
                agent_name=self.agent_name,
                agent_description=self.description,
                triggering_type=self.triggering_type,
                custom_tags=cs,
                isa_tags=isa,
                city_country=self.city_country,
                profiles=pr,
            )
            yield

        self.is_submitting = False
        yield