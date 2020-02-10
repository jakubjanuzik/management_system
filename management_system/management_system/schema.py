import graphene

from projects.schema import Query as ProjectsQuery


class Query(ProjectsQuery):
    pass


schema = graphene.Schema(query=Query)
