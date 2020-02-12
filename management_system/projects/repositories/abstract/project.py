import abc


class ProjectRepository(abc.ABC):
    """An abstract repository class."""

    @abc.abstractmethod
    def get_project(self, name):
        raise NotImplementedError
