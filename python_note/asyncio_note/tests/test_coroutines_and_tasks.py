import pytest
from python_note.asyncio_note.coroutines_and_tasks_2 import do_work


@pytest.mark.asyncio
async def test_do_work(capsys):
    result = await do_work("test task", 0.1)
    captured = capsys.readouterr()
    assert "test task started" in captured.out
    assert "test task done" in captured.out
    assert result == 1
