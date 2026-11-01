# Agentic Research Network

An open, **candidate research and product model** for funding AI-assisted research, evaluating contributions, and connecting accepted work to Product value. It is a model and simulation package, not an operating token network or a claim of validated research, assessment quality, sales, or returns.

The complete proposal lives in [model v1](docs/proposals/agentic-research-network/2026-10-29/model-v1/README.md). It includes candidate definitions, artifact schemas and records, novelty and contribution criteria, W/U/F token economics, sponsor participation, governance, cash-loop simulations, and the [Engineer Assessment Product 001 example](docs/proposals/agentic-research-network/2026-10-29/model-v1/product-001-ea/README.md). The example adds an optional engineer lead marketplace, direct engineer reward E, web/API/SDK distribution, and W-funded search visibility. All are proposals.

## Work on the model

Use Python 3 and install the one validation dependency:

```sh
python3 -m pip install -r requirements.txt
python3 docs/proposals/agentic-research-network/2026-10-29/model-v1/validate.py
python3 -m unittest discover -q -s docs/proposals/agentic-research-network/2026-10-29/model-v1/economics -p 'test_*.py'
python3 -m unittest discover -q -s docs/proposals/agentic-research-network/2026-10-29/model-v1/product-001-ea -p 'test_*.py'
```

The validator checks internal references, candidate status, selected source hashes, and stored synthetic results. Passing checks does not make a policy operative or establish an empirical result. See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution boundaries.

## Public example and dependencies

The [EA source snapshot](examples/engineer-assessment/README.md) contains the 88 selected files used by Product 001's crosswalk. One participant-purpose document was redacted to remove controller and approver identifiers before publication. It contains no participant records. The snapshot is intentionally narrower than the separate EA workspace; some links inside those source documents point to files outside this slice. Product 001's manifest pins the public snapshot's exact bytes.

The [Lab schema snapshot](authority/README.md) contains only the 17 existing artifact schemas needed by this package's validator. It is a dependency snapshot, not a new Lab authority. The original Lab checkout and other local projects are outside this repository.

## Status

No task offers, accepted research runs or findings, token issue, sponsor funding, engineer lead sales, employer access, stablecoin payments, or Product decisions are represented as real events here. Contributions should preserve that distinction.
