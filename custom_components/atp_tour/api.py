import aiohttp

class ATPTourAPI:
    BASE_URL = "https://www.atptour.com/"

    async def get_ranking(self):
        return [
            {"id": 1, "name": "Novak Djokovic", "rank": 1, "points": 12000, "country": "SRB", "age": 37},
            {"id": 2, "name": "Carlos Alcaraz", "rank": 2, "points": 11000, "country": "ESP", "age": 22}
        ]

    async def get_tournaments(self):
        return [
            {"id": 101, "name": "Roland Garros", "status": "In Progress", "location": "Paris", "surface": "Clay", "start_date": "2025-05-26", "end_date": "2025-06-08"}
        ]
