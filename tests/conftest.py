import asyncio
import typing
from pathlib import Path

import nonebot
import pytest
from nonebug.app import App
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql.expression import delete


@pytest.fixture
async def app(nonebug_init: None, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    import nonebot

    config = nonebot.get_driver().config
    config.bison_config_path = str(tmp_path / "legacy_config")
    config.datastore_config_dir = str(tmp_path / "config")
    config.datastore_cache_dir = str(tmp_path / "cache")
    config.datastore_data_dir = str(tmp_path / "data")
    config.command_start = {""}
    config.superusers = {"10001"}
    config.log_level = "TRACE"
    config.bison_filter_log = False
    return App(monkeypatch)


@pytest.fixture
def dummy_user_subinfo(app: App):
    from nonebot_bison.types import User, UserSubInfo

    user = User(123, "group")
    return UserSubInfo(user=user, category_getter=lambda _: [], tag_getter=lambda _: [])


@pytest.fixture
async def db_migration(app: App):
    from nonebot_bison.config.db import upgrade_db
    from nonebot_bison.config.db_model import Subscribe, Target, User
    from nonebot_plugin_datastore.db import get_engine

    await upgrade_db()
    async with AsyncSession(get_engine()) as sess:
        await sess.execute(delete(User))
        await sess.execute(delete(Subscribe))
        await sess.execute(delete(Target))
        await sess.commit()
        await sess.close()
