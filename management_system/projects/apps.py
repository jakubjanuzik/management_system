from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    name = "projects"

    def ready(self):
        """App loaded callback. Calls configure for dependency injection."""
        from projects.inject_config import configure

        configure()
