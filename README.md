# Domus Genoma

A declared home environment that can be reviewed, reproduced, and recovered.

Domus separates reusable configuration patterns from the private installation that
owns a person's machines, documents, runtime state, and credentials. This repository
publishes the reusable form: architecture, ownership rules, and small configuration
examples extracted from the original implementation.

The private operation remains in `4444J99/domus-genoma-private`, with its original
history, issues, and pull requests. Existing installations must use that private
repository as their source. This public repository is not a replacement source for
an existing installation.

## Explore

- [Architecture and ownership](docs/architecture.md)
- [Public/private boundary](docs/public-private-boundary.md)
- [Minimal chezmoi example](examples/chezmoi/README.md)
- [Extraction manifest](form-manifest.yaml)

The initial examples cover EditorConfig, XDG shell paths, modular zsh loading, and
history placement. Package provisioning, agent integrations, backup policy, and
machine-specific operations remain in the private implementation until separately
reviewed for extraction. This is a curated initial public edition.

## Verify

Run `python3 tools/check_public.py` to check the file allowlist and sample shell syntax.
The publication process also scans secrets and checks that public Git history is
disjoint from the private source. Every later extraction must repeat those checks.

## License

MIT; see [LICENSE](LICENSE). Exact source files retain the original license.
