from dataclasses import asdict

from sqlalchemy import select

import uuid

from fast_zero.models import User


def test_create_user(session, mock_db_time):

    guid_test = uuid.uuid7()

    with mock_db_time(model=User) as time:
        new_user = User(
            username="alice",
            password="secret",
            email="test@test.com",
            guid=guid_test,
        )

        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == "alice"))

    assert asdict(user) == {
        "id": 1,
        "username": "alice",
        "password": "secret",
        "email": "test@test.com",
        "created_at": time,
        "guid": guid_test,
    }
