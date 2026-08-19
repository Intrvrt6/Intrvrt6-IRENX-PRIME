# IRENX PRIME

Private development repository for the IRENX trading-system architecture.

## Architecture

`REGIME → LIQUIDITY → REFLEXIVITY → OROCHI → VMAP → EXECUTION → RISK MANAGEMENT`

The system is selective by design. `NO TRADE` is a valid outcome when evidence is insufficient or risk constraints fail.

## Execution baseline

- Primary execution timeframe: M15
- Instrument baseline: XAUUSD
- Minimum target risk/reward baseline: 1:3
- VMAP is a confirmation/filter, not an independent trigger.
- No single indicator is allowed to open a trade by itself.

## Security baseline

- Repository is private.
- Secrets are never committed.
- `.env` and credential/key material are ignored by Git.
- `.env.example` contains placeholders only.
- GitHub Actions uses least-privilege `contents: read` for the Copilot setup workflow.
- Network allowlist guidance is documented under `config/network/`.

## Development rule

Strategy logic, execution logic, and risk management remain separated. Changes that affect execution or risk should be tested before production use.

This repository is a software/trading-system project and does not guarantee profitable trades or a specific win rate.
