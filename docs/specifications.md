# specifications: ResearchDomain

## 1. Database Schema

### Table: `persons`
| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PK`, `AUTO` | Unique Identifier |
| `name` | `VARCHAR(100)` | `NOT NULL` | Full Name |

### Table: `research_groups`
| Column | Type | Constraints | Description |
| :--- | :--- | : :--- | :--- |
| `id` | `INTEGER` | `PK`, `AUTO` | Unique Identifier |
| `name` | `VARCHAR(100)` | `UNIQUE`, `NOT NULL` | Group Name |
| `campus_id` | `INTEGER` | `FK(campuses.id)` | Presence in Campus |

### Table: `team_members`
| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PK`, `AUTO` | Unique Identifier |
| `person_id` | `INTEGER` | `FK(persons.id)` | Link to Parent |
| `team_id` | `INTEGER` | `FK(research_groups.id)` | Link to Group |
| `role` | `VARCHAR(50)` | `NOT NULL` | Role (e.g., Researcher) |

### Table: `universities`
| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PK`, `AUTO` | Unique Identifier |
| `name` | `VARCHAR(100)` | `NOT NULL` | University Name |

### Table: `campuses`
| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PK`, `AUTO` | Unique Identifier |
| `name` | `VARCHAR(100)` | `NOT NULL` | Campus Name |
| `organization_id` | `INTEGER` | `FK(universities.id)` | Parent University |

## 2. API Specifications

### Class: `ResearcherController`
- `create_researcher(name: str, emails: list[str], identification_id: str, birthday: date) -> Researcher`
- `get_by_id(id: int) -> Researcher`

### Class: `ResearchGroupController`
- `create_research_group(name: str, campus_id: int, organization_id: int, description: str, short_name: str) -> ResearchGroup`
- `get_all() -> list[ResearchGroup]`

### Class: `UniversityController`
- `create_university(name: str, description: str, short_name: str) -> University`
- `get_all() -> list[University]`

### Class: `CampusController`
- `create_campus(name: str, organization_id: int, description: str, short_name: str) -> Campus`
- `get_all() -> list[Campus]`
