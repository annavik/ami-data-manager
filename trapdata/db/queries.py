import sqlalchemy as sa

from .base import get_session
from trapdata.db import models


def count_species(db_path, monitoring_session):
    """
    Count number of species detected in a monitoring session.

    # @TODO try getting the largest example of each detected species
    # SQLAlchemy Query to GROUP BY and fetch MAX date
    query = db.select([
        USERS.c.email,
        USERS.c.first_name,
        USERS.c.last_name,
        db.func.max(USERS.c.created_on)
    ]).group_by(USERS.c.first_name, USERS.c.last_name)
    """

    with get_session(db_path) as sesh:
        return (
            sesh.query(
                # DetectedObject.binary_label,
                # DetectedObject.specific_label,
                sa.func.coalesce(
                    models.DetectedObject.specific_label,
                    models.DetectedObject.binary_label,
                ).label("label"),
                sa.func.count().label("count"),
            )
            .group_by("label")
            .order_by(sa.desc("count"))
            .filter_by(monitoring_session=monitoring_session)
            .all()
        )


def update_all_aggregates(directory):
    # Call the update_aggregates method of every model
    raise NotImplementedError

    with get_session(directory) as sesh:
        for ms in sesh.query(None).all():
            ms.update_aggregates()
        sesh.commit()
