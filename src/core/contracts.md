# IRENX PRIME v0.2 — System Contract

A trade is eligible only when every upstream stage returns valid evidence.

## Decision contract

`REGIME → LIQUIDITY → REFLEXIVITY → OROCHI → VMAP → SIGNAL → RISK → EXECUTION`

Each stage may veto the decision. No downstream stage may bypass an upstream veto.

## Signal states

- `BUY`
- `SELL`
- `WAIT`
- `NO_TRADE`

`NO_TRADE` is the default state.

## Execution contract

Execution must receive a fully validated signal containing direction, entry/zone, stop loss, take profit, risk percentage, and evidence state. Execution must reject stale, incomplete, duplicated, or risk-invalid orders.

## Safety

Live execution remains disabled until backtest, walk-forward, paper-trading, risk regression, and manual production validation pass.
