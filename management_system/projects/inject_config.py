"""Configuration for dependency injection using python-inject."""

import inject
from projects.repositories.abstract.project import ProjectRepository
from projects.repositories.implementations.project import (
    DatabaseProjectRepository,
)

BIND_INSTANCES = {
    ProjectRepository: DatabaseProjectRepository(),
}


def inject_config(binder):
    """Callback used to configure the dependency injection bindings."""
    for cls, instance in BIND_INSTANCES.items():
        binder.bind(cls, instance)


def configure():
    """Configuration entrypoint."""
    inject.configure_once(inject_config)
