---
marp: true
theme: handout
paginate: false
---

# Alps quickstart — accounts, keys, access

Alps technical training · Swiss AI Initiative Annual Meeting 2026 · Module 1 · every claim below is documented at **docs.cscs.ch**

<div class="cols">
<div>

## 1. Three URLs

| | |
|---|---|
| `portal.cscs.ch` | the project: team, invitations, resources |
| `user-account.cscs.ch` | your account, MFA, SSH keys |
| `docs.cscs.ch` | everything else |

## 2. Roles in the portal

- **Project administrator** — the PI
- **Project manager** — the deputy PI
- **Project member** — everyone else

Administrators and managers invite people and assign roles.

Your **email address** identifies you: one address, one account. An account can belong to several projects and stays open while at least one of them is open. A project's end date stops its **compute**; the project stays active for another **90 days** for data retrieval, then it closes. Your account closes when the last of your projects does. A later invitation re-enables the same account.

## 3. Small and large projects

| | Small | Large |
|---|---|---|
| Budget | up to 32,000 GPUh | 500,000 GPUh and up |
| Duration | 6 months | 12 months |
| Review | rolling | two calls a year |
| Start | first day of next month | 1 January or 1 July |
| Storage | 1 TB, 1M inodes | state it in the proposal |

Apply at `swiss-ai.org/compute-grants` — `small-grants@swiss-ai.org`, `large-grants@swiss-ai.org`.

## 4. Inviting people

Single: **Invite Users** → email address → role.
Bulk: upload a CSV with these three columns.

```
Email,Role,Project
CragAlvarado@example.com,Project member,prj02
```

## 5. MFA is mandatory

Log in to any CSCS web application, enter the code emailed to you, scan the QR code with a TOTP app (Google Authenticator and FreeOTP are tested), confirm with the six-digit code.

> It is not possible to log in to CSCS systems using SSH without registering a device and creating certified SSH keys.

New accounts are usually opened within 48 hours.

</div>
<div>

## 6. Install cscs-key (once)

```
brew install eth-cscs/tap/cscs-key
cscs-key --version
```

No Homebrew? Download the release binary for your platform from `github.com/eth-cscs/cscs-key/releases` and put it on your `PATH`.

## 7. Generate a key pair (once, ever)

```
ssh-keygen -t ed25519 -f ~/.ssh/cscs-key
```

## 8. Sign it (every day)

```
cscs-key sign             # signs ~/.ssh/cscs-key
ssh-add -t 1d ~/.ssh/cscs-key
cscs-key list             # what is valid now
cscs-key revoke <serial>  # or --all
```

Keys are valid for **1 day** by default. You can create up to **5 keys per day**. Without the CLI: `user-account.cscs.ch` → SSH Keys → Sign Key.

## 9. ~/.ssh/config

```
Host ela
    HostName ela.cscs.ch
    User cscsusername
    IdentityFile ~/.ssh/cscs-key

Host clariden
    HostName clariden.alps.cscs.ch
    User cscsusername
    ProxyJump ela
    IdentityFile ~/.ssh/cscs-key
    IdentitiesOnly yes
```

Then `ssh clariden`. Add `-A` to forward your agent.

Bristen needs its **own** `Host` block, not a hostname swap: copy the `clariden` one and change the alias and `HostName` to `bristen` / `bristen.alps.cscs.ch`. The `ela` entry is shared. Clariden is where production runs go; Bristen is a test and development system, best effort.

## 10. Stuck

**service-desk@cscs.ch** · `docs.cscs.ch/access/ssh/`

</div>
</div>

<div class="wide">

## 11. Spending the budget

Every project is granted a compute credit in **GPU hours**. Consumption is **usage based** — you spend the credit as your jobs run — and you are expected to spend it roughly linearly, month by month.

| | |
|---|---|
| **Expected**, each month | your budget spread roughly linearly over the project |
| **Minimal**, each month | the expected amount minus a grace of **15% to 50%**, depending on budget size |
| Below the minimal | the credit between your usage and the minimal is **lost** |
| Between minimal and expected | the unused credit **rolls over** to the following months |
| Above the expected | no problem — you run at lower priority while you are ahead |
| Out of credit before the end | the `low` partition, capped at the equivalent of **two months** of your budget |
| End date | compute stops; the project stays active **90 more days** for data retrieval, then closes |

## 12. Tunnel to a service running on a compute node

```bash
ssh -N -J ${MYUSER}@ela.cscs.ch,${MYUSER}@${CLUSTER}.alps.cscs.ch -L ${PORT}:localhost:${PORT} ${MYUSER}@${NODE}
```

<p class="note">Sources: docs.cscs.ch/accounts/ · /accounts/account-create/ · /access/mfa/ · /access/ssh/ · /platforms/mlp/ · /clusters/clariden/ · /clusters/bristen/ · swiss-ai.org/compute-grants</p>

</div>
