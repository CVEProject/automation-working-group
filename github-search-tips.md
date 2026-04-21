# Searching the CVE Program on GitHub

*A guide to using GitHub search across the [CVEProject](https://github.com/CVEProject) organization to find CVE Records, program rules, policy documents, API information, and community discussions.*

---

## How It Works

The CVE Program publishes its data, rules, policies, schema, tooling, and community discussions across 25+ public repositories at [github.com/CVEProject](https://github.com/CVEProject). GitHub's code search is a powerful complement to the search on [cve.org](https://cve.org), especially for:

- **Deep content searches** across all JSON fields in 280,000+ CVE Records (credits, references, CVSS scores, assigner, etc.)
- **Cross-repo searches** that find a term across CVE Records, CNA Rules, policy docs, and working group notes simultaneously
- **Path filtering** to restrict results by year, CVE ID range, or file type
- **Issue & discussion searches** that surface years of institutional knowledge about API behavior, schema decisions, and program governance

---

## Organization-Wide Search

Search the **entire CVEProject org** at once with:

```
org:CVEProject "search terms"
```

This is the single most powerful technique — it searches all repos simultaneously. Examples:

```
org:CVEProject "disputed"                       # Records, policy, rules, FAQ, schema, WG notes
org:CVEProject "4.2.1"                          # A specific CNA Rule number across all repos
org:CVEProject "Independently Fixable"          # A glossary term across all program materials
org:CVEProject "unsupported-when-assigned"      # EOL tag usage across records and policy
org:CVEProject "Council of Roots"               # Governance term across all repos
org:CVEProject "Vulnrichment" OR "vulnrichment" # ADP effort across all repos
```

> **Tip:** All terms are `AND`ed by default. Use `OR` for alternatives. Use `"quotes"` for exact phrases.

---

## Repository Guide

### CVE Records — [cvelistV5](https://github.com/CVEProject/cvelistV5)

The authoritative CVE List. Every published CVE Record in JSON 5.0 format, organized as `cves/{year}/{Nxxx}/CVE-{year}-{N}.json`.

**Direct navigation** — if you know the CVE ID:
```
https://github.com/CVEProject/cvelistV5/blob/main/cves/2024/3xxx/CVE-2024-3094.json
```

**Searching records:**

```
repo:CVEProject/cvelistV5 "Apache HTTP Server"                        # By product
repo:CVEProject/cvelistV5 "CWE-79"                                    # By CWE
repo:CVEProject/cvelistV5 "baseScore" "9.8"                           # By CVSS score
repo:CVEProject/cvelistV5 "assignerShortName" "github"                # By assigning CNA
repo:CVEProject/cvelistV5 "credits" "Jane Doe"                        # By researcher credit
repo:CVEProject/cvelistV5 "tagExtension" "disputed"                   # Disputed records
repo:CVEProject/cvelistV5 "exclusively-hosted-service"                # Hosted service tag
repo:CVEProject/cvelistV5 path:cves/2025 "SQL injection"              # Scoped to a year
repo:CVEProject/cvelistV5 path:cves/2024/1xxx "privilege escalation"  # Scoped to an ID range
repo:CVEProject/cvelistV5 path:cves/2025 "REJECTED"                   # Rejected records
repo:CVEProject/cvelistV5 "github.com/advisories"                     # By reference domain
repo:CVEProject/cvelistV5 "GHSA-xxxx-xxxx-xxxx"                       # By GHSA ID
```

**Tip:** Include JSON field names alongside values (e.g., `"vendorName" "Cisco"`) to reduce false positives.

**Bulk downloads** are available via [GitHub Releases](https://github.com/CVEProject/cvelistV5/releases).

---

### CNA Rules, FAQ, Glossary & Board Data — [cve-website](https://github.com/CVEProject/cve-website)

Source for [cve.org](https://cve.org). Contains the CNA Operational Rules, FAQ, Glossary, Board member list, and partner organization types — all as **structured JSON**, making them highly searchable. Branch: `dev`.

**CNA Rules** (`cnaRules.json`) — the operational rulebook for all 460+ CNAs:

```
repo:CVEProject/cve-website "MUST" path:cnaRules.json                 # All mandatory rules
repo:CVEProject/cve-website "SHOULD NOT" path:cnaRules.json           # Not-recommended guidance
repo:CVEProject/cve-website "Scope" path:cnaRules.json                # Scope-related rules
repo:CVEProject/cve-website "72 hours" path:cnaRules.json             # Publishing timelines
repo:CVEProject/cve-website "dispute" path:cnaRules.json              # Dispute-related rules
repo:CVEProject/cve-website "End-of-Life" path:cnaRules.json          # EOL product rules
repo:CVEProject/cve-website "exclusively-hosted-service" path:cnaRules.json  # Hosted service rules
```

**FAQ** (`faqs.json`):

```
repo:CVEProject/cve-website "DISPUTED" path:faqs.json
repo:CVEProject/cve-website "CNA-LR" path:faqs.json
repo:CVEProject/cve-website "RESERVED" path:faqs.json
```

**Glossary** (`glossaryEntries.json`), **Board members** (`currentBoardMembersList.json`), **Partner org types** (`partnersRolesOrgTypes.json`):

```
repo:CVEProject/cve-website path:glossaryEntries.json "Independently Fixable"
repo:CVEProject/cve-website path:currentBoardMembersList.json
repo:CVEProject/cve-website path:partnersRolesOrgTypes.json
```

---

### Program Policy Documents — [cve-documents](https://github.com/CVEProject/cve-documents)

Official CVE Program policy documents in Markdown: **Board Charter** (v3.5.0), **Dispute Policy** (v2.0.0), and **Inactive CNA Policy** (v1.2.0).

```
repo:CVEProject/cve-documents "MUST" path:*.md                        # All mandatory requirements
repo:CVEProject/cve-documents "voting" path:CVE_Board_Charter         # Board voting rules
repo:CVEProject/cve-documents "quorum" path:CVE_Board_Charter         # Quorum requirements
repo:CVEProject/cve-documents "Executive Session" path:CVE_Board_Charter
repo:CVEProject/cve-documents "Adjudicator" path:CVE_Dispute          # Dispute adjudication
repo:CVEProject/cve-documents "five business days" path:CVE_Dispute   # Dispute timelines
repo:CVEProject/cve-documents "revoked" path:CVE_Inactive             # CNA removal process
repo:CVEProject/cve-documents "six-month" path:CVE_Inactive           # Inactivity threshold
```

---

### CVE Services API — [cve-services](https://github.com/CVEProject/cve-services)

Source code for the CVE Services API. The most valuable content here is in the **170+ open issues**, which contain years of institutional knowledge about API behavior, bugs, and edge cases.

```
repo:CVEProject/cve-services "rate limit"
repo:CVEProject/cve-services "validation error"
repo:CVEProject/cve-services "rejected" label:bug
repo:CVEProject/cve-services "bulk" OR "batch"
repo:CVEProject/cve-services "transfer"
```

API documentation lives in the companion repo [cve-services-doc](https://github.com/CVEProject/cve-services-doc).

---

### CVE Record Format & Schema — [cve-schema](https://github.com/CVEProject/cve-schema)

The CVE JSON 5.0 schema definition. 110 open issues track proposals and debates about the record format.

```
repo:CVEProject/cve-schema "tagExtension" path:schema
repo:CVEProject/cve-schema "adp" path:schema
repo:CVEProject/cve-schema "metrics" path:schema
repo:CVEProject/cve-schema "required" is:issue                        # Schema change proposals
```

---

## Local Clone & API Techniques

For exhaustive queries beyond GitHub's ~1,000 result cap, clone locally:

```bash
git clone --depth 1 https://github.com/CVEProject/cvelistV5.git
```

**ripgrep:**
```bash
rg "remote code execution" cves/2025/ -l
rg '"baseScore": 10.0' cves/ -l
```

**jq** (structured queries):
```bash
find cves/2024 -name "*.json" -exec sh -c '
  jq -e ".containers.cna.metrics[]?.cvssV3_1?.baseScore // empty | select(. >= 9.0)" "$1" >/dev/null 2>&1 && echo "$1"
' _ {} \;
```

**GitHub API** (30 search requests/min authenticated):
```bash
curl -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  "https://api.github.com/search/code?q=repo:CVEProject/cvelistV5+%22CWE-89%22+path:cves/2024"
```

---

## Tips

1. **Use quotes** for exact phrases: `"use after free"`.
2. **Scope to a year** when searching cvelistV5: `path:cves/2025` dramatically reduces noise.
3. **Include JSON field names** alongside values to reduce false positives.
4. **Use `org:CVEProject`** for cross-cutting questions that span records, rules, and policy.
5. **Search issues too** — cve-services (170+) and cve-schema (110+) issues contain institutional knowledge not found in any documentation.
6. **cvelistV5 updates ~hourly** — `git pull` regularly if working locally.
7. **Use the CVE Services API** for structured queries by field (state, date ranges, assigner): [cveawg.mitre.org/api-docs](https://cveawg.mitre.org/api-docs/). The search on [cve.org](https://cve.org) complements GitHub search well, especially for date-based queries and wildcards.

---

## Additional Resources

| Resource | URL |
|---|---|
| CVE Program | [cve.org](https://www.cve.org/) |
| CVEProject GitHub Org | [github.com/CVEProject](https://github.com/CVEProject) |
| CVE Services API Docs | [cveawg.mitre.org/api-docs](https://cveawg.mitre.org/api-docs/) |
| CVE Record Format Schema | [cveproject.github.io/cve-schema](https://cveproject.github.io/cve-schema/) |
| GitHub Code Search Docs | [docs.github.com/en/search-github/github-code-search](https://docs.github.com/en/search-github/github-code-search) |
| List of CVE Partners | [cve.org/PartnerInformation/ListofPartners](https://www.cve.org/PartnerInformation/ListofPartners) |
| CVE Terms of Use | [cve.org/Legal/TermsOfUse](https://www.cve.org/Legal/TermsOfUse) |

---

*GitHub search is a complement to the official CVE Services API and the search on cve.org. For authoritative CVE Record data and programmatic integration, always reference the official CVE Services.*
