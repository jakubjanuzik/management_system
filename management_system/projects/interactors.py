class GetProjectInteractor:
    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, name):
        self.name = name
        return self

    def execute(self):
        return self.project_repo.get_project(name=self.name)
