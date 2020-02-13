import graphene


class ProjectType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()
    is_global = graphene.Boolean()
    is_internal = graphene.Boolean()
    # TODO: Add Teams once get the type.
    # TODO: Add client once get the type.

    def resolve_id(parent, info):
        return parent.id

    def resolve_name(parent, info):
        return parent.name

    def resolve_description(parent, info):
        return parent.description

    def resolve_is_global(parent, info):
        return parent.is_global

    def resolve_is_internal(parent, info):
        return parent.is_internal
