import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import importlib.util

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "adk", "hospital_consultant", "context.py"))
spec = importlib.util.spec_from_file_location("context", module_path)
context = importlib.util.module_from_spec(spec)
spec.loader.exec_module(context)
JsonFileContextStore = context.JsonFileContextStore


def test_json_file_context_store(tmp_path):
    path = tmp_path / "ctx.json"
    store = JsonFileContextStore(str(path))
    store.set_company_context("c1", {"foo": "bar"})
    store.add_user_message("c1", "u1", "hello")

    # Reload and verify persistence
    store2 = JsonFileContextStore(str(path))
    assert store2.get_company_context("c1") == {"foo": "bar"}
    assert store2.get_user_history("c1", "u1") == ["hello"]
