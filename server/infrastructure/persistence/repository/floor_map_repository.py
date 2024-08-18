from typing import Optional

from psycopg2.extensions import connection
from ulid import ULID

from server.domain.repository_impl.floor_repository_impl import (
    FloorMapImageRepositoryImpl,
    FloorMapRepositoryImpl,
)


class FloorMapRepository(FloorMapRepositoryImpl):
    def save(self, conn: connection) -> None:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute("INSERT INTO floor_maps (id) VALUES (%s)", (str(ulid)))


class FloorMapImageRepository(FloorMapImageRepositoryImpl):
    def save(self, conn: connection, floor_map_id: str, floor_map_image: bytes) -> str:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute(
                    "INSERT INTO floor_map_images (id, floor_map_id) VALUES (%s, %s, %s) RETURNING id",
                    (str(ulid), floor_map_id, floor_map_image),
                )

                result = cursor.fetchone()
                if result is not None:
                    floor_map_image_id = result[0]
                else:
                    raise ValueError("Failed to save floor map image")

                return floor_map_image_id

    def find_for_floor_map_id(
        self, conn: connection, floor_map_id: str
    ) -> Optional[str]:
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id FROM floor_map_images WHERE floor_map_id = %s",
                    (floor_map_id,),
                )

                # TODO : 画像の取得処理を追加する
                result = cursor.fetchone()
                if result is not None:
                    floor_map_image_id = result[0]
                else:
                    return None

                return floor_map_image_id
