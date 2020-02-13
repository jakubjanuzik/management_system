import graphene
import graphql
from common.exceptions import EntityCreationException
from projects.factory import ProjectFactory
from projects.types import ProjectType

REPOSITORY = ProjectFactory().get()


class CreateProjectMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(default_value="")
        is_internal = graphene.Boolean(default_value=False)
        is_global = graphene.Boolean(default_value=False)

    project = graphene.Field(ProjectType)

    def mutate(self, info, name, description, is_internal, is_global):
        try:
            project = REPOSITORY.create_project(
                name, description, is_internal, is_global
            )
        except EntityCreationException:
            raise graphql.GraphQLError("Could not create a project")

        return CreateProjectMutation(project=project)
