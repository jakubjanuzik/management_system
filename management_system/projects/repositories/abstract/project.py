import abc


class ProjectRepository(abc.ABC):
    """An abstract repository class."""

    @abc.abstractmethod
    def get_project(self, name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_project(
        self, name, description, is_global=False, is_internal=False
    ):
        raise NotImplementedError
