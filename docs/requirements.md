# Requirements: ResearchDomain

## 1. Functional Requirements (FR)

### FR-01: Person Management (Researchers)
- **FR-01-A**: The system must allow creating a Researcher (Person) with `name` and zero or more `emails`.
- **FR-01-B**: The system must allow retrieving a Researcher by ID.

### FR-02: Team Management (Research Groups)
- **FR-02-A**: The system must allow creating a ResearchGroup (Team).
- **FR-02-B**: The system must allow adding a Researcher to a ResearchGroup.
- **FR-02-C**: A ResearchGroup must have at least one Researcher.
- **FR-02-D**: ResearchGroup must be associated with a Campus.

### FR-03: Organization Management (Universities)
- **FR-03-A**: The system must allow creating a University (Organization).

### FR-04: Organizational Unit Management (Campuses)
- **FR-04-A**: The system must allow creating a Campus (OrganizationalUnit) within a University.
- **FR-04-B**: A Campus must belong to a University.

## 2. Non-Functional Requirements (NFR)

### NFR-01: Architecture
- **NFR-01-A**: The system must strictly follow MVC + Service + Repository layers, using `libbase` as core.
- **NFR-01-B**: The Domain layer must have no dependencies on the Infrastructure layer (DIP).

### NFR-02: Quality
- **NFR-02-A**: All public methods must be type-hinted.
- **NFR-02-B**: Data validation using Pydantic.

## 3. Constraints
- Must use PostgreSQL.
- Must use SQLAlchemy.
- Must inherit/use patterns from `libbase`.
