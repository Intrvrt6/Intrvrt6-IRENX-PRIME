from pathlib import Path


ROOT = Path(__file__).parents[1]
CONFIG = (ROOT / "config" / "irenx-v0.2.yml").read_text()
CONTRACT = (ROOT / "src" / "core" / "contracts.md").read_text()


def test_core_pipeline_is_ordered():
    expected = [
        "REGIME",
        "LIQUIDITY",
        "REFLEXIVITY",
        "OROCHI",
        "VMAP",
        "SIGNAL",
        "RISK",
        "EXECUTION",
    ]
    assert all(item in CONFIG for item in expected)


def test_safe_defaults():
    assert "no_trade_is_valid: true" in CONFIG
    assert "single_indicator_trigger: false" in CONFIG
    assert "vmap_independent_trigger: false" in CONFIG
    assert "risk_veto: true" in CONFIG
    assert "live: false" in CONFIG


def test_promotion_requires_validation():
    for requirement in (
        "require_backtest: true",
        "require_walk_forward: true",
        "require_paper_validation: true",
        "require_risk_validation: true",
        "require_manual_live_approval: true",
    ):
        assert requirement in CONFIG


def test_contract_keeps_no_trade_default():
    assert "`NO_TRADE` is the default state." in CONTRACT
