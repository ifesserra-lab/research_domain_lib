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
| `cnpq_url` | `VARCHAR(255)` | `NULLABLE` | CNPq Link |
| `site` | `VARCHAR(255)` | `NULLABLE` | Group Site |

### Table: `knowledge_areas`
| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PK`, `AUTO` | Unique Identifier |
| `name` | `VARCHAR(100)` | `UNIQUE`, `NOT NULL` | Area Name |

### Table: `group_knowledge_areas`
| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `group_id`| `INTEGER` | `FK(research_groups.id)`| Parent Group |
| `area_id`| `INTEGER` | `FK(knowledge_areas.id)` | Theme Link |

### Table: `roles`
| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PK`, `AUTO` | Unique Identifier |
| `name` | `VARCHAR(100)` | `UNIQUE`, `NOT NULL` | Role Name |
| `description`| `TEXT` | `NULLABLE` | Description |

### Table: `team_members`
| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PK`, `AUTO` | Unique Identifier |
| `person_id` | `INTEGER` | `FK(persons.id)` | Link to Parent |
| `team_id` | `INTEGER` | `FK(research_groups.id)` | Link to Group |
| `role_id` | `INTEGER` | `FK(roles.id)` | Participation Role |
| `start_date` | `DATE` | `NOT NULL` | Start of Membership/Leadership |
| `end_date` | `DATE` | `NULLABLE` | End of Membership/Leadership |

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
- `create_research_group(name: str, campus_id: int, organization_id: int, knowledge_area_ids: list[int], description: str, short_name: str, cnpq_url: str, site: str) -> ResearchGroup`
- `add_member(team_id: int, researcher_id: int, role_id: int, start_date: date, end_date: date = None) -> TeamMember`
- `add_leader(team_id: int, researcher_id: int, start_date: date, end_date: date = None) -> TeamMember`
- `get_leaders(team_id: int) -> list[TeamMember]`
- `get_all() -> list[ResearchGroup]`

### Class: `KnowledgeAreaController`
- `create_knowledge_area(name: str) -> KnowledgeArea`
- `get_all() -> list[KnowledgeArea]`

### Class: `UniversityController`
- `create_university(name: str, description: str, short_name: str) -> University`
- `get_all() -> list[University]`

### Class: `CampusController`
- `create_campus(name: str, organization_id: int, description: str, short_name: str) -> Campus`
- `get_all() -> list[Campus]`
