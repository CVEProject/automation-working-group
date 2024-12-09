*The goal of this document is to create a proposal for an archiving solution of references linked in published CVE records.*

**Why?**

- [CVE Reference Investigations](https://docs.google.com/presentation/d/1jO7y1WHAUTWZwUl4tP3ZRJT0gvG6KxQklUvsXoM6NF4/edit#slide=id.g2793d2f3e58_2_50)
  - Link rot (30% of CVE records have at least one dead link)
  - Potential for malicious takeover of invalid domains referenced in CVE records
  - Reliance on archive.org for archival

**High-level requirements discussion:**

- Is there a subset of references that we want to archive, or should this effort cover all references?
  - AWG (Dec 3,2024): there is no distinction between references to determine which should vs shouldn't be archived; we should archive them all
- Do we want to archive references in ADP records as well?
  - AWG (Dec 3,2024): we should archive ADP references too (especially secretariat's container that contains primary references)
- How often should references be re-archived beyond the first archival?
  - AWG (Dec 3,2024): we should re-archive at intervals; 0, 3, 10, 90?
  - Do we need to store older versions? How many?
    - AWG (Dec 3,2024): three latest versions? Build with the expectation of having multiple versions; MVP is having one archived reference. The goal is to always have at least one archived reference to prevent dead links. If we're snapshotting multiple times, we should keep previous versions.
- How fast do we need to archive a reference once it appears in a record?
  - AWG (Dec 3,2024): at submission, ideally
- Do we need to archive a full page, or just the text of a page?
  - If the full page, does it need to store all of the assets of the pages (HTML/JS/CSS) so that it can be rendered on its own once archived?
  - AWG (Dec 3,2024): multiple formats if possible: preferably one user-acessible format (image/pdf via headless browser) and one machine-readable (HTML/WARC)
- How should the references be retrievable?
  - Do we need a viewer of the archived references, or just provide them in their raw form and allow users to download them?
  - AWG (Dec 3,2024): user story: I have an existing (dead) URL, show me the archived version of it.
  - AWG (Dec 3,2024): user story: I have a CVE ID, show me all of its archived references.
  - AWG (Dec 3,2024): no need for generic search of all references

**Questions**

_Dec 3,2024_:
- Do we replace dead links with their archived versions?
  - AWG: leave the original link and indicate that it may be invalid and provide a way to resolve it to its archived version
- Should a CVE record instead be improved to contain enough information to not heavily depend on references?
  - AWG: it may be impractical to house all data that is currently placed in referenced content in the CVE record itself
  - AWG: are there common data patterns that appear in references but not in CVE record? CVE record often contains summarized versions of metadata about the vulnerability.
- Are there legal considerations for serving archived content?
  - AWG: Kris to double-check with Alec
- Should archived content be limited to CNAs to prevent bulk download by the public?
  - AWG: bulk download of all archived content could be added in a later version, not in MVP
  - AWG: estimated based on local experiments 3TB of archived data for the entired CVE data set

**Architectural Approaches**

- archivebox vs <something_else>
  - ask Tod to demo archivebox

**Proposed solution**

- (answer questions above before coming up with solutions)
