class ProjectSerializer:
    @staticmethod
    def serialize(project):
        return {
            "id": project.id,
            "name": project.name,
            "description": project.description,
            "is_global": project.is_global,
            "is_internal": project.is_internal,
            # TODO: When ClientSerializer exists
            # "client": ClientSerializer(project.client)
        }
