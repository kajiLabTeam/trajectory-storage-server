# from abc import ABCMeta, abstractmethod
# from typing import Any

# from psycopg2.extensions import connection


# class RawDataRepositoryImpl(metaclass=ABCMeta):
#     @abstractmethod
#     def find_for_spot_id(
#         self,
#         s3: Any,
#         conn: connection,
#         spot_id: SpotAggregateId,
#         application: ApplicationAggregate,
#     ) -> RawDataAggregate:
#         pass

#     @abstractmethod
#     def save(
#         self,
#         s3: Any,
#         conn: connection,
#         spot_id: SpotAggregateId,
#         raw_data: RawDataAggregate,
#         application: ApplicationAggregate,
#     ) -> RawDataAggregate:
#         pass
