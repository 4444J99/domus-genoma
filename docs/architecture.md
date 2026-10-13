# Architecture

Domus treats configuration as source. Chezmoi renders that source into the home
directory; applications retain ownership of their own mutable state.

| Layer | Owns |
| --- | --- |
| Configuration source | Templates, desired settings, ownership declarations |
| Private installation | Machine identities, personal choices, operational records |
| Credential provider | Secret values and authenticated delivery |
| Applications | Sessions, databases, caches, trust decisions and native state |
| Verification | Render checks, installed-file comparison and functional probes |

An update first checks the proposed source, renders the affected configuration,
and validates the result. Apply only the affected owned files, then check the
installed result and the consumer that loads it. Mixed-ownership files require
targeted modification that retains application-owned fields.

Recovery retains the preceding accepted configuration and records the failed
revision and phase. An application health check is separate from a file checksum:
the latter establishes the bytes installed, while the former establishes that the
consumer can use them.

Public examples demonstrate configuration layout. They do not activate scheduled
jobs, install packages, access credential stores, or change an existing private
installation. The complete host implementation stays in the private operation.
