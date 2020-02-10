import graphene
import graphql

from projects.factories import ProductFactory
from projects.types import Product


class Query(graphene.ObjectType):
    product = graphene.Field(Product, name=graphene.String(required=True))

    def resolve_product(parent, info, name):
        product = ProductFactory.create().get(name=name)

        if product.get("error"):
            raise graphql.GraphQLError(product["error"])

        return product
