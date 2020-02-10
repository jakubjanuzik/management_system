from projects.interactors import GetProjectInteractor
from projects.providers import ProjectProvider
from projects.repositories import ProjectDatabaseRepo
from projects.unit_repositories import ProjectRepo
from projects.views import ProjectView


class ProjectDatabaseRepoFactory:
    @staticmethod
    def get():
        return ProjectDatabaseRepo()


class ProjectRepoFactory:
    @staticmethod
    def get():
        db_repo = ProjectDatabaseRepoFactory.get()
        return ProjectRepo(db_repo)


class GetProjectInteractorFactory:
    @staticmethod
    def get():
        project_repo = ProjectRepoFactory.get()
        return GetProjectInteractor(project_repo)


class ProductViewFactory:
    @staticmethod
    def create():
        get_product_interactor = GetProjectInteractorFactory.get()
        return ProjectView(get_product_interactor)


class ProductFactory:
    @staticmethod
    def create():
        product_interactor = GetProjectInteractorFactory.get()
        return ProjectProvider(product_interactor)
