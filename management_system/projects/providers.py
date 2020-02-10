from common.exceptions import EntityDoesNotExist
from projects.serializers import ProjectSerializer


class ProjectProvider:
    def __init__(self, get_project_interactor):
        self.get_project_interactor = get_project_interactor

    def get(self, name):
        try:
            project = self.get_project_interactor.set_params(
                name=name
            ).execute()
        except EntityDoesNotExist:
            body = {"error": "Product does not exist!"}
        else:
            body = ProjectSerializer.serialize(project)

        return body
