class User:
    def __init__(self, name, email, password_hash, profile, nickname=None, position=None):
        self.name = name
        self.nickname = nickname
        self.email = email
        self.password_hash = password_hash
        self.profile = profile
        self.position = position
        self.team_id = None

class Team:
    def __init__(self, name, owner_id, code):
        self.name = name
        self.owner_id = owner_id
        self.code = code

class Game:
    def __init__(self, team_id, opponent, location, date_time):
        self.team_id = team_id
        self.opponent = opponent
        self.location = location
        self.date_time = date_time
        self.status = "scheduled"
        self.results = {
            "winner": None,
            "score": None,
            "mvp_votes": [],
            "goals": []
        }
