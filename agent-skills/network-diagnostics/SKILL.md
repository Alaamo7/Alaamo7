---
name: network-diagnostics
status: restored
description: Diagnose endpoint and small-network connectivity problems using layered TCP/IP troubleshooting, evidence collection, safe commands, hypothesis testing, and post-fix verification.
---

# Network Diagnostics Skill

Use a layered approach to network troubleshooting instead of random command execution.

## Core model

Work from the endpoint outward:

```text
Physical / Wi-Fi link
      ↓
NIC state
      ↓
IP configuration
      ↓
Gateway
      ↓
DHCP
      ↓
DNS
      ↓
Routing / firewall
      ↓
Target service/application
```

## Initial questions

Determine:

- One device or many?
- Wired, Wi-Fi, or both?
- Internet only or local resources too?
- Started after a change?
- Intermittent or constant?
- IP assigned automatically or statically?

## Evidence commands

Windows examples:

```powershell
ipconfig /all
Get-NetAdapter
Get-NetIPConfiguration
Get-DnsClientServerAddress
route print
arp -a
netstat -ano
nslookup example.com
ping <gateway>
tracert <target>
Test-NetConnection <host> -Port <port>
```

## Interpretation examples

These are diagnostic clues, not automatic conclusions:

- **169.254.x.x** → DHCP lease failure or unavailable DHCP path is plausible.
- Gateway unreachable with valid local IP → local link/VLAN/gateway/configuration issue is plausible.
- Gateway works and public IP works but hostname fails → DNS issue is plausible.
- DNS resolves and host responds but application port fails → firewall/service/application-layer issue is plausible.

Always confirm with additional evidence.

## DHCP checks

When DHCP is suspected:

- Confirm adapter is configured for DHCP.
- Check current lease information.
- Verify reachability/path to the DHCP service where possible.
- Use release/renew only when appropriate.

Example:

```cmd
ipconfig /release
ipconfig /renew
```

Do not repeatedly renew if the root cause is clearly link/VLAN/server-side.

## DNS checks

Compare:

- Configured DNS servers
- Direct IP connectivity
- `nslookup` results
- Application behavior

Flush cache only when cached resolution is a plausible cause:

```cmd
ipconfig /flushdns
```

## Wi-Fi checks

Inspect:

- SSID association
- Signal quality
- Frequency/band if relevant
- Authentication state
- DHCP result
- Adapter driver state
- Whether other devices on the same AP are affected

## Escalation output

```markdown
# Network Incident
- Scope:
- Connection type:
- Adapter state:
- IP/subnet:
- Gateway:
- DNS:
- DHCP state:
- Gateway test:
- DNS test:
- Route/port tests:
- Findings:
- Fix attempted:
- Result:
- Suspected next layer:
```

## Closure

After the change, test the actual user workflow—not only `ping`.

Verify local resources, DNS, target application/service, and stability when relevant.