from abc import ABCMeta, abstractmethod

from psycopg2.extensions import connection
from typing import Optional

class TrajectoryRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection, is_walking: bool, floor_id: str) -> str:
        pass

    @abstractmethod
    def find_for_id(self, conn: connection, trajectory_id: str) -> Optional[str]:
        pass

    @abstractmethod
    def update(self, conn: connection, is_walking: bool, trajectory_id: str) -> None:
        pass
