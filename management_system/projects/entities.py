class Team:
    def __init__(self, name, users, description):
        self._name = name
        self._users = users
        self._description = description

    @property
    def users(self):
        return self._users

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description


class Role:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


class Project:
    def __init__(
        self,
        id,
        name,
        description,
        teams,
        is_global,
        is_internal,
        client=None,
    ):
        self._id = id
        self._name = name
        self._description = description
        self._teams = teams
        # TODO: Add when Client has it's architecture
        self._is_global = is_global
        self._is_internal = is_internal
        self._client = client

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def teams(self):
        return self._teams

    @property
    def client(self):
        return self._client

    @property
    def is_global(self):
        return self._is_global

    @property
    def is_internal(self):
        return self._is_internal

    @property
    def id(self):
        return self._id
