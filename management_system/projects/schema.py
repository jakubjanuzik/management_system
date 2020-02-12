import graphene
import graphql
from common.exceptions import EntityDoesNotExist
from projects.factory import ProjectFactory
from projects.types import Project

REPOSITORY = ProjectFactory().get()


class Query(graphene.ObjectType):
    project = graphene.Field(Project, name=graphene.String(required=True))

    def resolve_project(parent, info, name):
        try:
            project = REPOSITORY.get_project(name=name)
        except EntityDoesNotExist:
            raise graphql.GraphQLError("Project does not exist!")

        return project
