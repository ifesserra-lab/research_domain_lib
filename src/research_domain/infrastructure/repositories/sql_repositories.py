from typing import List
from libbase.infrastructure.sql_repository import GenericSqlRepository
from eo_lib.infrastructure.database.postgres_client import PostgresClient
from research_domain.domain.repositories import (
    ResearcherRepositoryInterface,
    UniversityRepositoryInterface,
    CampusRepositoryInterface,
    ResearchGroupRepositoryInterface,
)
from research_domain.domain.entities import (
    Researcher,
    University,
    Campus,
    ResearchGroup,
    ResearcherInGroup,
)

class PostgresResearcherRepository(GenericSqlRepository[Researcher], ResearcherRepositoryInterface):
    def __init__(self):
        client = PostgresClient()
        super().__init__(client.get_session(), Researcher)

class PostgresUniversityRepository(GenericSqlRepository[University], UniversityRepositoryInterface):
    def __init__(self):
        client = PostgresClient()
        super().__init__(client.get_session(), University)

class PostgresCampusRepository(GenericSqlRepository[Campus], CampusRepositoryInterface):
    def __init__(self):
        client = PostgresClient()
        super().__init__(client.get_session(), Campus)

class PostgresResearchGroupRepository(GenericSqlRepository[ResearchGroup], ResearchGroupRepositoryInterface):
    def __init__(self):
        client = PostgresClient()
        super().__init__(client.get_session(), ResearchGroup)

    def add_member(self, member: ResearcherInGroup) -> ResearcherInGroup:
        try:
            self._session.add(member)
            self._session.commit()
            self._session.refresh(member)
            return member
        except Exception:
            self._session.rollback()
            raise

    def remove_member(self, member_id: int) -> bool:
        db_obj = self._session.query(ResearcherInGroup).filter_by(id=member_id).first()
        if db_obj:
            self._session.delete(db_obj)
            self._session.commit()
            return True
        return False

    def get_members(self, team_id: int) -> List[ResearcherInGroup]:
        return self._session.query(ResearcherInGroup).filter_by(team_id=team_id).all()
