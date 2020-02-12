import inject
from projects.repositories.abstract.project import ProjectRepository


class ProjectFactory:
    """
    Project factory that uses dependency injection.
    Usually it would have been done in the class that requires
    ProjectRepository but since GraphQL resolvers are static methods it's not
    possible.
    """

    repository = inject.attr(ProjectRepository)

    def get(self):
        return self.repository
