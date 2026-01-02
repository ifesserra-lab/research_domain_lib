from typing import List, Dict, Optional, TypeVar, Any
from libbase.infrastructure.memory_repository import GenericMemoryRepository
from eo_lib.domain.entities import TeamMember, Role
from research_domain.domain.repositories import (
    ResearcherRepositoryInterface,
    UniversityRepositoryInterface,
    CampusRepositoryInterface,
    ResearchGroupRepositoryInterface,
    KnowledgeAreaRepositoryInterface,
    RoleRepositoryInterface,
)
from research_domain.domain.entities import Researcher, University, Campus, ResearchGroup, KnowledgeArea

class BaseInMemoryRepository(GenericMemoryRepository):
    def __init__(self):
        super().__init__()
        self._id_counter = 1

    def add(self, entity: Any) -> Any:
        if not hasattr(entity, 'id') or not entity.id:
            entity.id = self._id_counter
            self._id_counter += 1
        super().add(entity)
        return entity

class InMemoryResearcherRepository(BaseInMemoryRepository, ResearcherRepositoryInterface):
    pass

class InMemoryUniversityRepository(BaseInMemoryRepository, UniversityRepositoryInterface):
    pass

class InMemoryCampusRepository(BaseInMemoryRepository, CampusRepositoryInterface):
    pass

class InMemoryResearchGroupRepository(BaseInMemoryRepository, ResearchGroupRepositoryInterface):
    def __init__(self):
        super().__init__()
        self._members: Dict[int, TeamMember] = {}
        self._member_id_counter = 1

    def add_member(self, member: TeamMember) -> TeamMember:
        if not member.id:
            member.id = self._member_id_counter
            self._member_id_counter += 1
        self._members[member.id] = member
        return member

    def remove_member(self, member_id: int) -> bool:
        if member_id in self._members:
            del self._members[member_id]
            return True
        return False

    def get_members(self, team_id: int) -> List[TeamMember]:
        return [m for m in self._members.values() if m.team_id == team_id]

class InMemoryKnowledgeAreaRepository(BaseInMemoryRepository, KnowledgeAreaRepositoryInterface):
    pass

class InMemoryRoleRepository(BaseInMemoryRepository, RoleRepositoryInterface):
    pass
