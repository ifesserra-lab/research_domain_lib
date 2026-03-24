import enum
from datetime import date
from typing import List, Optional

from eo_lib.domain.base import Base
from eo_lib.domain.entities import Initiative, Person, Role
from sqlalchemy import Boolean, Column, Date, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from research_domain.domain.mixins import SerializableMixin


class AdvisorshipType(enum.Enum):
    SCIENTIFIC_INITIATION = "Scientific Initiation"
    JUNIOR_SCIENTIFIC_INITIATION = "Junior Scientific Initiation"
    UNDERGRADUATE_THESIS = "Undergraduate Thesis"
    MASTER_THESIS = "Master Thesis"
    PHD_THESIS = "PhD Thesis"
    POST_DOCTORATE = "Post-Doctorate"


class AdvisorshipRole(enum.Enum):
    STUDENT = "Student"
    SUPERVISOR = "Supervisor"
    CO_SUPERVISOR = "Co-Supervisor"
    BOARD_MEMBER = "Board Member"


class AdvisorshipMember(Base, SerializableMixin):
    __tablename__ = "advisorship_members"

    id = Column(Integer, primary_key=True)
    advisorship_id = Column(Integer, ForeignKey("advisorships.id"), nullable=False)
    person_id = Column(Integer, ForeignKey("persons.id"), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=True)

    # We might want to store role name directly if Role entity is too heavy or specific
    # But for now assuming we link to a Role entity or store Enum as string?
    # The test uses Role(name=...), so we should probably link to Role or just store role name.
    # Given the test uses Role entity, let's assume we link to it OR we just support an internal role mapping.
    # Actually, simpler to just store the role name/enum if we don't have a Roles table widely used.
    # But usually a Roles table exists.
    # Let's assume we use a simplified approach for this specific domain if Role entity is external.
    # However, to pass the test `role=role_student` (which is a Role object), we should probably handle it.

    # Let's use a string column for role_name to be safe and simple, relying on the Enum.
    role_name = Column(String(50), nullable=False)

    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)

    person = relationship("Person")
    role = relationship("Role", foreign_keys=[role_id])
    advisorship = relationship("Advisorship", back_populates="members")


class Advisorship(Initiative, SerializableMixin):
    """
    Advisorship Model.

    A specialized Initiative that links a Student and a Supervisor (both represented as Person).
    An Advisorship has a team composed of a student, supervisor, and board members.
    Uses Joined Table Inheritance from initiatives.
    """

    __tablename__ = "advisorships"

    id = Column(Integer, ForeignKey("initiatives.id"), primary_key=True)
    fellowship_id = Column(Integer, ForeignKey("fellowships.id"), nullable=True)
    institution_id = Column(Integer, ForeignKey("organizations.id"), nullable=True)

    type = Column(Enum(AdvisorshipType), nullable=True)
    program = Column(String(500), nullable=True)
    defense_date = Column(Date, nullable=True)

    cancelled = Column(Boolean, default=False)
    cancellation_date = Column(Date, nullable=True)

    fellowship = relationship("Fellowship", foreign_keys=[fellowship_id])
    institution = relationship("Organization", foreign_keys=[institution_id])

    members = relationship(
        "AdvisorshipMember", back_populates="advisorship", cascade="all, delete-orphan"
    )

    @property
    def student(self) -> Optional[Person]:
        """Returns the person with Student role."""
        for member in self.members:
            if member.role_name == AdvisorshipRole.STUDENT.value:
                return member.person
        return None

    @property
    def supervisor(self) -> Optional[Person]:
        """Returns the person with Supervisor role."""
        for member in self.members:
            if member.role_name == AdvisorshipRole.SUPERVISOR.value:
                return member.person
        return None

    @property
    def board_members(self) -> List[Person]:
        """Returns list of persons with Board Member role."""
        return [
            m.person
            for m in self.members
            if m.role_name == AdvisorshipRole.BOARD_MEMBER.value
        ]

    @property
    def is_volunteer(self) -> bool:
        """Returns True if the advisorship is voluntary (no fellowship)."""
        return self.fellowship is None and self.fellowship_id is None

    def add_member(self, person: Person, role: Role, start_date: Optional[date] = None):
        """Adds a member to the advisorship."""
        member = AdvisorshipMember(
            person=person,
            role=role,
            role_id=role.id,
            role_name=role.name,
            start_date=start_date,
        )
        self.members.append(member)

    def __init__(
        self,
        name: str,
        fellowship_id: Optional[int] = None,
        institution_id: Optional[int] = None,
        type: Optional[AdvisorshipType] = None,
        program: Optional[str] = None,
        defense_date: Optional[date] = None,
        fellowship: Optional[object] = None,
        institution: Optional[object] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        cancelled: bool = False,
        cancellation_date: Optional[date] = None,
        description: Optional[str] = None,
        status: str = "active",
        id: Optional[int] = None,
        **kwargs,
    ):
        super().__init__(
            name=name,
            description=description,
            status=status,
            start_date=start_date,
            end_date=end_date,
            id=id,
            **kwargs,
        )
        self.fellowship_id = fellowship_id
        self.institution_id = institution_id
        self.type = type
        self.program = program
        self.defense_date = defense_date
        self.fellowship = fellowship
        self.institution = institution
        self.cancelled = cancelled
        self.cancellation_date = cancellation_date
