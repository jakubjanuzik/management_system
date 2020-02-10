class ProjectRepo(object):
    def __init__(self, db_repo):
        self.db_repo = db_repo
        # self.cache_repo = cache_repo

    def get_project(self, name):
        # project = self.cache_repo.get_project(reference)

        # if project is None:
        project = self.db_repo.get_project(name)
        # self.cache_repo.save_project(project)

        return project
