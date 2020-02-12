import graphene
import graphql
from common.exceptions import EntityDoesNotExist
from projects.factory import ProjectFactory
from projects.types import Product

REPOSITORY = ProjectFactory().get()


class Query(graphene.ObjectType):
    product = graphene.Field(Product, name=graphene.String(required=True))

    def resolve_product(parent, info, name):
        try:
            product = REPOSITORY.get_project(name=name)
        except EntityDoesNotExist:
            raise graphql.GraphQLError("Product does not exist!")

        return product
