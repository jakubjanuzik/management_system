from http import HTTPStatus
from common.exceptions import EntityDoesNotExist
from projects.serializers import ProjectSerializer


class ProjectView(object):
    def __init__(self, get_project_interactor):
        self.get_project_interactor = get_project_interactor

    def get(self, name):
        try:
            project = self.get_project_interactor.set_params(
                name=name
            ).execute()
        except EntityDoesNotExist:
            body = {"error": "Project does not exist!"}
            status = HTTPStatus.NOT_FOUND
        else:
            body = ProjectSerializer.serialize(project)
            status = HTTPStatus.OK

        return body, status
