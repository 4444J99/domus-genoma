# Minimal chezmoi layout

These files are a small source-layout example, not an installer for an existing
Domus host. Review them in an isolated destination before incorporating individual
files into your own chezmoi source.

- `dot_editorconfig` maps to `.editorconfig`.
- `dot_zshenv` defines XDG locations and zsh's configuration directory.
- `dot_config/zsh/dot_zshrc` loads numbered configuration modules.
- `00-init.zsh` initializes a startup timer and leaves the filesystem root.
- `01-history.zsh` places history under the XDG state directory.

The entrypoint supports additional numbered modules. Its retained upstream comments
describe the wider private installation; only the files listed above ship here.

The example has no identity values, credential lookups, package installs or
apply-time scripts. The module syntax is checked by the public verifier. A host
installation must separately test its actual shell and consumers.
