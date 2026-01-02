# Project Backlog - ResearchDomain

This document is automatically synchronized with GitHub Issues. Last updated: 2026-01-01 21:35:00

## 📋 Master Issue List
Overview of all demands, their states and executors.

| # | Status | Title | Executor | Sprint | Milestone |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [#2](https://github.com/The-Band-Solution/ResearchDomain/pull/2) | ✅ | Feature: Implement ResearchGroup Feature (Entities, Repositories, Controllers) | @paulossjunior | Sprint 1 | v0.1.0 |

---

## 📂 Workflow States

### 🟢 In Progress / Todo
_No issues in this state._

### ✅ Done / Released
- [#2](https://github.com/The-Band-Solution/ResearchDomain/pull/2) **Feature: Implement ResearchGroup Feature** (Executor: @paulossjunior)
    - **PR**: [#2](https://github.com/The-Band-Solution/ResearchDomain/pull/2)
    - **SHA**: `39f41ee`

---

## 🏃 Sprints (Interactions)
Organized by execution cycles.

### 🗓️ Sprint 1 (2026-01-01 - 2026-01-15)
- ✅ [#2](https://github.com/The-Band-Solution/ResearchDomain/pull/2) Feature: Implement ResearchGroup Feature

---

## 🎯 Delivery Marks (Milestones)

### 🏁 v0.1.0 - Initial Core Implementation
- ✅ [#2](https://github.com/The-Band-Solution/ResearchDomain/pull/2) Feature: Implement ResearchGroup Feature

---

## 📝 Detailed Backlog

### [OPEN] [#1](https://github.com/The-Band-Solution/ResearchDomain/issues/1) Feature: Implement ResearchGroup Feature
- **Executor**: @paulossjunior
- **Labels**: `enhancement`, `feature`
- **Milestone**: v0.1.0

**Description**:
## Context
Implement the core entities for the `ResearchDomain` library as specified in the updated documentation.

## Requirements
- A `ResearchGroup` is a `Team`.
- A `ResearchGroup` must have at least one `Researcher`.
- A `ResearchGroup` is present in a `Campus`.
- A `Campus` is in a `University`.

## Proposed Changes
- Implement `University`, `Campus`, `ResearchGroup`, and `Researcher`.
- Implement specialized repository interfaces and SQLAlchemy strategies.
- Implement specialized controllers and services.
