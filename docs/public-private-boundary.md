# Public and private ownership

The public repository starts with fresh Git history. Its root manifest lists every
admitted file. It receives only reviewed reusable material, never a full private
tree copy or a merge from private history.

The private repository retains the complete existing operation and history,
including personal documents, agent memories, internal plans, machine configuration,
client work, and credential routing. Live secret values continue to belong to the
credential provider. A repository's private visibility does not authorize adding
plaintext credentials.

Publication is explicit: select files from a fixed private revision, review their
whole contents and dependencies, adapt examples where needed, record provenance,
scan the resulting tree and history, and publish from the separate public root.
An automated secret scan supplements that review; it cannot decide whether prose
or identifiers are appropriate to publish.

The public repository name must never be used as a push target for the private
checkout. Before reusing the original name, update private remotes and active
bootstrap references. Keep the local source directory stable to preserve running
applications and worktree paths.
