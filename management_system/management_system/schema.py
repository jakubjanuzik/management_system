import graphene
from projects.schema import Mutation as ProjectMutation
from projects.schema import Query as ProjectsQuery


class Query(ProjectsQuery):
    pass


class Mutation(ProjectMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
