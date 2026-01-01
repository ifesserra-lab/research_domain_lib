# How to Use This Template

This repository serves as a starting point for creating new strictly architectural Python CRUD libraries.

## 1. Instantiate the Repository

-   Click "Use this template" on GitHub to create a new repository.
-   Clone your new repository.

## 2. Rename the Package

-   Data: Rename the directory `src/lib_template` to your library name (e.g., `src/my_awesome_lib`).
-   Configuration: Open `pyproject.toml` and update:
    -   `name = "my-awesome-lib"`
    -   `packages = ["src/my_awesome_lib"]`

## 3. Core Dependencies

**CRITICAL**: This template depends on `libbase`. Do not remove it from `pyproject.toml` unless you are refactoring the entire architectural base.

```toml
dependencies = [
    ...
    "libbase @ git+https://github.com/The-Band-Solution/libbase.git@v0.1.0",
]
```

## 4. Develop Your Library

1.  **Domain**: Add entities in `domain/entities` and repository interfaces in `domain/repositories`.
2.  **Infrastructure**: Implement your repositories in `infrastructure/repositories` (Memory, Postgres, JSON).
3.  **Services**: Create services in `services/` extending `BaseService`.
4.  **Wiring**: Update `factories.py` to return your specific implementations.
