# Project Backlog - ResearchDomain

This document is automatically synchronized with GitHub Issues. Last updated: 2026-01-01 21:44:39

## 📋 Master Issue List
Overview of all demands, their states and executors.

| # | Status | Title | Executor | Sprint | Milestone |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [# 1](https://github.com/The-Band-Solution/ResearchDomain/issues/1) | ✅ | Implement ResearchGroup Feature (Entities, Repositories, Controllers) | - | - | - |

---

## 📂 Workflow States

### 🟢 In Progress / Todo
_No issues in this state._

### ✅ Done / Released
- [#1](https://github.com/The-Band-Solution/ResearchDomain/issues/1) **Implement ResearchGroup Feature (Entities, Repositories, Controllers)**

---

## 📝 Detailed Backlog

### [CLOSED] [#1](https://github.com/The-Band-Solution/ResearchDomain/issues/1) Implement ResearchGroup Feature (Entities, Repositories, Controllers)
- **Executor**: -
- **Labels**: enhancement, feature
- **Milestone**: -

**Description**:
## Context
Implement the core entities for the `ResearchDomain` library as specified in the updated documentation.

## Requirements
- A `ResearchGroup` is a `Team`.
- A `ResearchGroup` must have at least one `Researcher`.
- A `ResearchGroup` is present in a `Campus`.
- A `Campus` is in a `University`.

## Proposed Changes
- Implement `University` (Organization), `Campus` (OrganizationalUnit), `ResearchGroup` (Team), and `Researcher` (Person).
- Implement specialized repository interfaces and SQLAlchemy strategies.
- Implement specialized controllers.

## References
Detailed in `docs/requirements.md`, `docs/sdd.md`, and `docs/specifications.md`.

---
