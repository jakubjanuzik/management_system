from projects.repositories import ProjectDatabaseRepo
from projects.unit_repositories import ProjectRepo
from projects.interactors import GetProjectInteractor
from projects.views import ProjectView


class ProjectDatabaseRepoFactory(object):
    @staticmethod
    def get():
        return ProjectDatabaseRepo()


class ProjectRepoFactory(object):
    @staticmethod
    def get():
        db_repo = ProjectDatabaseRepoFactory.get()
        return ProjectRepo(db_repo)


class GetProjectInteractorFactory(object):
    @staticmethod
    def get():
        project_repo = ProjectRepoFactory.get()
        return GetProjectInteractor(project_repo)


class ProductViewFactory(object):
    @staticmethod
    def create():
        get_product_interactor = GetProjectInteractorFactory.get()
        return ProjectView(get_product_interactor)
