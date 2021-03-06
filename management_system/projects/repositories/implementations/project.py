from common.exceptions import EntityCreationException, EntityDoesNotExist
from django.db import IntegrityError
from projects.entities import Project as ProjectEntity
from projects.models import Project
from projects.repositories.abstract.project import ProjectRepository


class DatabaseProjectRepository(ProjectRepository):
    """Repository to get data from the database."""

    def get_project(self, name):
        """
        Calls DjangoORM and returns project from database with given name.
        """
        try:
            orm_project = Project.objects.get(name=name)
        except Project.DoesNotExist:
            raise EntityDoesNotExist()

        return self._decode_orm_project(orm_project)

    def _decode_orm_project(self, orm_project):
        """Decodes orm object into entity."""
        return ProjectEntity(
            name=orm_project.name,
            description=orm_project.description,
            teams=orm_project.teams,
            is_global=orm_project.is_global,
            is_internal=orm_project.is_internal,
            id=orm_project.pk,
            # client=orm_project.client,
        )

    def create_project(
        self, name, description="", is_global=False, is_internal=False
    ):
        """Calls DjangoORM to create and return project from database."""
        # TODO: add teams support

        try:
            orm_project = Project.objects.create(
                name=name,
                description=description,
                is_global=is_global,
                is_internal=is_internal,
            )
        except IntegrityError:
            raise EntityCreationException()

        return self._decode_orm_project(orm_project)
