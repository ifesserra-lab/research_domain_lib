# Software Design Description (SDD)

## 1. Solution Architecture

### 1.1 Architectural Pattern
The system follows a **Strict Layered Architecture** emphasizing separation of concerns, testability, and flexibility. It integrates **MVC (Model-View-Controller)** principles with **Domain-Driven Design (DDD)** tactical patterns.

| Layer | Component | Responsibility |
|-------|-----------|----------------|
| **Presentation** | **Controllers** | Acts as a Facade/Entry Point. Handles user input, delegates to Services, and formats responses (DTOs/Entities). |
| **Business Logic** | **Services** | Encapsulates domain business rules. Orchestrates data flow between Controllers and Repositories. |
| **Data Access** | **Repositories** | Abstracts the storage mechanism. Provides a clean interface for Domain operations (CRUD+L). implemented using the **Generic Repository Pattern**. |
| **Persistence** | **Strategies** | Concrete implementations of storage: `SQLAlchemy`, `JSON File`, or `In-Memory`. Selected via **Strategy Pattern**. |
| **Domain** | **Unified Models** | **DRY Principle**: Entities serve as both Domain Objects and ORM Mappings (SQLAlchemy Declarative). |

### 1.2 Design Patterns
- **Strategy Pattern**: Used to switch between Database, JSON, and Memory storage at runtime via Configuration.
- **Generic Repository**: Defines generic `add`, `get`, `update`, `delete`, `list` operations in an abstract base class to eliminate boilerplate.
- **Factory Pattern**: `ServiceFactory` handles dependency injection, wiring Services with the correct Repository Strategy.
- **Singleton Pattern**: The `PostgresClient` ensures a single global database connection pool.

## 2. Data Design (IEEE 1016)

### 2.1 Mini-World Scenario
The system models a research environment within Universities.
- A **University** (Organization) is the top-level entity.
- A **Campus** (Organizational Unit) is a branch of a University.
- A **Research Group** (Team) is a collective of individuals conducting research, presence in a specific **Campus**.
- A **Researcher** (Person) is an individual belonging to one or more Research Groups.
- A **TeamMember** (Researcher in ResearchGroup) represents the association of a Researcher to a Research Group.

### 2.2 Data Dictionary

#### 2.2.1 Researcher (Person)
| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| `id` | Integer | PK, Auto-Inc | Unique internal identifier for the researcher. |
| `name` | String | Not Null | The full legal name of the researcher. |
| `identification_id` | String | Unique | Personal identification card / tax ID. |
| `birthday` | Date | Optional | The date of birth. |

#### 2.2.2 PersonEmail
| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| `id` | Integer | PK, Auto-Inc | Unique identifier for the email record. |
| `person_id` | Integer | FK (Person) | Reference to the Person owner. |
| `email` | String | Unique, Not Null | The email address. |

#### 2.2.2 Research Group (Team)
| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| `id` | Integer | PK, Auto-Inc | Unique internal identifier for the group. |
| `name` | String | Unique, Not Null | The official name of the research group. |
| `description`| Text | Optional | A detailed description of the group's purpose. |

#### 2.2.3 Researcher in Group (TeamMember)
| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| `id` | Integer | PK, Auto-Inc | Unique identifier for the membership record. |
| `person_id` | Integer | FK (Person) | Reference to the Researcher. |
| `team_id` | Integer | FK (Team) | Reference to the Research Group. |
| `role` | String | Default "member" | The functional role of the researcher within this specific group. |
| `start_date` | Date | Default NOW | Date when the researcher joined the group. |
| `end_date` | Date | Nullable | Date when the researcher left the group. Open interval if null. |

#### 2.2.4 InitiativeType
| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| `id` | Integer | PK, Auto-Inc | Unique identifier. |
| `name` | String | Unique, Not Null | The type name (e.g., "Research", "Development"). |
| `description` | Text | Optional | Description of the type. |

#### 2.2.5 Initiative
| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| `id` | Integer | PK, Auto-Inc | Unique internal identifier for the project. |
| `name` | String | Unique, Not Null | The code name or label of the initiative. |
| `description` | Text | Optional | Detailed description. |
| `start_date` | Date | Optional | Projected start date. |
| `end_date` | Date | Optional | Projected end date. |
| `status` | String | Default "active" | Valid values: active, completed, archived. |
| `initiative_type_id` | Integer | FK (InitiativeType) | The type of the initiative. |

#### 2.2.6 Organization
| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| `id` | Integer | PK, Auto-Inc | Unique identifier. |
| `name` | String | Not Null | Entity name. |
| `description` | Text | Optional | - |
| `short_name` | String | Unique, Optional | Acronym or slug. |

#### 2.2.7 OrganizationalUnit
| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| `id` | Integer | PK, Auto-Inc | Unique identifier. |
| `name` | String | Not Null | Unit name. |
| `organization_id` | Integer | FK (Organization) | Parent organization. |
| `parent_id` | Integer | FK (Unit), Nullable | Hierarchical parent. |
| `description` | Text | Optional | - |
| `short_name` | String | Optional | - |

#### 2.2.5 Implementation Strategy
The entities are implemented using **SQLAlchemy Declarative Models** inheriting from a shared `Base`. This provides a direct mapping between the classes described above and the underlying Relational Database Schema, ensuring the DRY principle is respected.

## 3. Class Diagrams

### 3.1 Domain Model Class Diagram
This diagram illustrates the core entities and their relationships within the domain layer.

```mermaid
classDiagram
    %% Entities
    class Researcher {
        +int id
        +str name
        +list[PersonEmail] emails
    }

    class ResearchGroup {
        +int id
        +str name
        +int campus_id
        +list[ResearcherInGroup] members
    }

    class ResearcherInGroup {
        +int id
        +int person_id
        +int team_id
        +str role
    }
    
    class University {
        +int id
        +str name
        +str short_name
    }

    class Campus {
        +int id
        +int organization_id
        +str name
    }

    %% Relationships
    Researcher "1" --> "N" ResearcherInGroup : Belongs to
    ResearchGroup "1" --> "N" ResearcherInGroup : Contains
    University "1" --> "N" Campus : Contains
    ResearchGroup "N" --> "1" Campus : Present in
```

### 3.2 Architecture Class Diagram
This diagram showcases the strict layered architecture, highlighting the flow from Controllers to Services and finally to Repositories.

```mermaid
classDiagram
    %% Layers
    namespace Presentation {
        class PersonController
        class TeamController
        class InitiativeController
    }
    
    namespace Business_Logic {
        class PersonService
        class TeamService
        class InitiativeService
    }
    
    namespace Data_Access {
        class PersonRepository
        class TeamRepository
        class InitiativeRepository
        class InitiativeTypeRepository
    }
    
    namespace Domain {
        class Person
        class Team
        class Initiative
        class InitiativeType
        class Organization
        class OrganizationalUnit
    }

    %% Dependencies
    PersonController --|> PersonService : uses
    TeamController --|> TeamService : uses
    InitiativeController --|> InitiativeService : uses
    
    PersonService --|> PersonRepository : uses
    TeamService --|> TeamRepository : uses
    InitiativeService --|> InitiativeRepository : uses
    InitiativeService --|> InitiativeTypeRepository : uses

    %% Entities flow through all layers
    PersonController ..> Person : handles
    PersonService ..> Person : processes
    PersonRepository ..> Person : persists

    TeamController ..> Team : handles
    TeamService ..> Team : processes
    TeamRepository ..> Team : persists
    TeamRepository ..> Person : manages membership

    InitiativeController ..> Initiative : handles
    InitiativeService ..> Initiative : processes
    InitiativeRepository ..> Initiative : persists
    InitiativeRepository ..> Team : manages assignment
```

### 3.3 Package Model Diagram
The following diagram illustrates the dependencies between the logical packages (folders) of the library. It clearly shows the **One-Way Dependency Rule**: Outer layers depend on inner layers, and the Domain remains the independent core.

```mermaid
classDiagram
    direction TB
    
    namespace eo_lib_controllers {
        class Controllers ["eo_lib.controllers"]
    }
    
    namespace eo_lib_services {
        class Services ["eo_lib.services"]
    }
    
    namespace eo_lib_domain {
        class Domain ["eo_lib.domain"]
    }
    
    namespace eo_lib_infrastructure {
        class Infrastructure ["eo_lib.infrastructure"]
    }
    
    namespace eo_lib_root {
        class Factories ["eo_lib.factories"]
        class Config ["eo_lib.config"]
    }

    Controllers ..> Services : orchestrates
    Controllers ..> Domain : uses entities
    Controllers ..> Factories : uses for DB-independent init
    
    Services ..> Domain : implements business logic using
    
    Infrastructure ..> Domain : implements repository interfaces
    Infrastructure ..> Config : reads settings
    
    Factories ..> Services : wires
    Factories ..> Infrastructure : selects strategy
    Factories ..> Config : reads storage type
```

## 4. Sequence Diagram: Add Member to Team

```mermaid
sequenceDiagram
    autonumber
    actor Client
    participant Controller as TeamController
    participant Service as TeamService
    participant TeamRepo as PostgresTeamRepo
    participant DB as PostgreSQL

    Client->>Controller: add_member(team_id, person_id, role)
    Controller->>Service: add_member(team_id, person_id, role)
    
    Service->>TeamRepo: add_member(TeamMember)
    TeamRepo->>DB: INSERT INTO team_members ...
    DB-->>TeamRepo: Success
    TeamRepo-->>Service: TeamMember(id=...)
    
    Service-->>Controller: TeamMemberDTO
    Controller-->>Client: TeamMemberDTO
```
