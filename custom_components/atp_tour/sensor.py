from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN
from .api import ATPTourAPI

async def async_setup_platform(hass, config, add_entities, discovery_info=None):
    api = ATPTourAPI()
    ranking = await api.get_ranking()
    tournaments = await api.get_tournaments()

    sensors = []

    for player in ranking[:10]:
        sensors.append(ATPRankingSensor(player))

    for tournament in tournaments:
        sensors.append(ATPTournamentSensor(tournament))

    add_entities(sensors, True)

class ATPRankingSensor(SensorEntity):
    def __init__(self, player):
        self._attr_name = f"{player['name']} (ATP Rank)"
        self._attr_unique_id = f"atp_rank_{player['id']}"
        self._state = player['rank']
        self._player = player

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return {
            "points": self._player['points'],
            "country": self._player['country'],
            "age": self._player['age']
        }

class ATPTournamentSensor(SensorEntity):
    def __init__(self, tournament):
        self._attr_name = f"{tournament['name']} (Tournament)"
        self._attr_unique_id = f"atp_tour_{tournament['id']}"
        self._state = tournament['status']
        self._tournament = tournament

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return {
            "location": self._tournament['location'],
            "surface": self._tournament['surface'],
            "start_date": self._tournament['start_date'],
            "end_date": self._tournament['end_date'],
            "winner": self._tournament.get('winner')
        }
