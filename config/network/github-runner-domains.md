# GitHub Actions / Runner Network Baseline

Use this document as a network allowlist reference for IRENX runners. GitHub's current documentation is authoritative; review it before changing firewall rules because domains can change.

## Core HTTPS access

- github.com
- api.github.com
- *.actions.githubusercontent.com
- codeload.github.com
- results-receiver.actions.githubusercontent.com
- *.blob.core.windows.net
- objects.githubusercontent.com
- github-releases.githubusercontent.com
- github-registry-files.githubusercontent.com

## Git LFS

- github-cloud.githubusercontent.com
- github-cloud.s3.amazonaws.com

## Security rules

1. Prefer outbound HTTPS/443 only.
2. Do not hard-code credentials, PATs, runner tokens, broker secrets, or API keys in this repository.
3. Store sensitive values in GitHub Actions Secrets/Variables or the appropriate external secret manager.
4. Keep the workflow permission scope minimal; this project uses `contents: read` for Copilot setup.
5. Treat this file as documentation, not as a guarantee that the list is exhaustive. Verify against GitHub's official self-hosted runner documentation before production firewall changes.
