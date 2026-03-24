# ResearchDomain

`research_domain` is a Python library for modeling and managing academic research data with a layered architecture built around domain entities, services, controllers, and repository strategies.

It is designed for scenarios such as:

- managing researchers, universities, campuses, and research groups
- registering advisorships, fellowships, academic education, articles, and other research production
- switching between in-memory repositories for local work and SQL-backed repositories for persistence

## Highlights

- Clear architectural layers: `domain`, `services`, `controllers`, and `infrastructure`
- Rich academic domain model on top of `eo_lib` and `libbase`
- `memory` strategy for tests and local development
- PostgreSQL strategy for persistent environments
- Public API centered on specialized controllers

## Requirements

- Python 3.10+
- PostgreSQL only when using `STORAGE_TYPE=postgres` or `STORAGE_TYPE=db`

## Installation

### Development install

```bash
git clone https://github.com/The-Band-Solution/ResearchDomain.git
cd ResearchDomain
python3 -m venv .venv
. .venv/bin/activate
pip install -e .[dev]
```

The project depends on:

- `eo_lib`
- `libbase`

Both are declared in [`pyproject.toml`](/home/paulossjunior/projects/ResearchDomain/pyproject.toml).

### Package metadata

- Package name: `research_domain`
- Current version: `0.14.1`

## Configuration

The project reads configuration from environment variables and supports `.env` via `python-dotenv`.

Example:

```env
# Repository strategy
STORAGE_TYPE=memory

# Used only for postgres/db strategies
DATABASE_URL=postgresql://user:password@localhost:5432/research_db
```

### Storage strategies

- `memory`: recommended for tests, examples, and local exploration
- `postgres` or `db`: uses SQL repositories backed by PostgreSQL

In `memory` mode, repositories are now shared across controllers/services created by the factory, so entities created in one controller are visible to related flows in another controller during the same process.

## Public API

The package root lazily exposes the main controllers, entities, and services. Typical imports look like this:

```python
from research_domain import (
    ResearcherController,
    ResearchGroupController,
    UniversityController,
    CampusController,
    ArticleController,
    AdvisorshipController,
)
```

Available controllers include:

- `ResearcherController`
- `UniversityController`
- `CampusController`
- `ResearchGroupController`
- `KnowledgeAreaController`
- `RoleController`
- `AdvisorshipController`
- `FellowshipController`
- `AcademicEducationController`
- `ArticleController`
- `EducationTypeController`
- `ProductionTypeController`
- `ResearchProductionController`

## Quick Start

### Create a researcher

```python
from research_domain import ResearcherController

researchers = ResearcherController()

joyce = researchers.create_researcher(
    name="Dr. Joyce",
    emails=["joyce@ufsc.br", "joyce.academic@gmail.com"],
    resume="Researcher in applied AI.",
)

print(joyce.id, joyce.name)
```

### Create a university and campus

```python
from research_domain import CampusController, UniversityController

universities = UniversityController()
campuses = CampusController()

ufsc = universities.create_university(
    name="Federal University of Santa Catarina",
    short_name="UFSC",
)

florianopolis = campuses.create_campus(
    name="Florianopolis Campus",
    organization_id=ufsc.id,
)
```

### Create a research group

```python
from research_domain import ResearchGroupController

groups = ResearchGroupController()

ai_lab = groups.create_research_group(
    name="Artificial Intelligence Laboratory",
    campus_id=florianopolis.id,
    organization_id=ufsc.id,
    short_name="LIA",
)
```

### Create an article linked to an existing researcher

```python
from research_domain import ArticleController, ArticleType

articles = ArticleController()

paper = articles.create_article(
    title="Knowledge Graphs in Research Management",
    year=2026,
    type=ArticleType.JOURNAL,
    author_ids=[joyce.id],
    doi="10.1000/example",
)
```

### Create and cancel an advisorship

```python
from datetime import date

from research_domain import AdvisorshipController

advisorships = AdvisorshipController()

advisorship = advisorships.create_advisorship(
    name="Scientific Initiation 2026",
    student_id=joyce.id,
    start_date=date(2026, 1, 1),
)

advisorships.cancel_advisorship(advisorship.id, date(2026, 6, 1))
```

## Running Tests

Run the test suite with:

```bash
pytest
```

If your environment has the project dependencies installed outside the active interpreter, you may need to provide `PYTHONPATH` explicitly:

```bash
PYTHONPATH=src python -m pytest
```

## Repository Layout

```text
src/research_domain/
  controllers/     Public-facing application API
  domain/          Entities, mixins, repository contracts
  infrastructure/  Memory and SQL repository implementations
  services/        Use-case and orchestration layer
```

## Documentation

- [Documentation Index](/home/paulossjunior/projects/ResearchDomain/docs/README.md)
- [Requirements](/home/paulossjunior/projects/ResearchDomain/docs/requirements.md)
- [Specifications](/home/paulossjunior/projects/ResearchDomain/docs/specifications.md)
- [Software Design Description](/home/paulossjunior/projects/ResearchDomain/docs/sdd.md)
- [Implementation Plan](/home/paulossjunior/projects/ResearchDomain/docs/implementation_plan.md)
- [Backlog](/home/paulossjunior/projects/ResearchDomain/docs/backlog.md)
