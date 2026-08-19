# IRENX Self-Hosted Runner

## Required label

`irenx-prime`

The GitHub Actions health workflow targets:

```yaml
runs-on: [self-hosted, irenx-prime]
```

## Auto-start

Register the runner on the Linux host and configure it as a service using GitHub's official runner service configuration. Do not commit the runner registration token or `.runner` credentials to this repository.

## Health check

`.github/workflows/irenx-runner-health.yml` runs every 15 minutes and can also be triggered manually. It verifies that a runner with the `irenx-prime` label is available and reports runner identity and a basic heartbeat.

## Android access

Android is treated as the remote control/client. The runner itself should run on a supported Linux host, VPS, Windows, or macOS environment rather than relying on Android/Termux as an officially supported GitHub runner platform.

## Security

- Never commit registration tokens, PATs, SSH private keys, or cloud credentials.
- Keep the runner host dedicated and patched.
- Use least-privilege repository permissions.
- Do not expose the runner's local service directly to the public internet.
