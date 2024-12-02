*The goal of this document is to create a proposal for an archiving solution of references linked in published CVE records.*

**Why?**

- [CVE Reference Investigations](https://docs.google.com/presentation/d/1jO7y1WHAUTWZwUl4tP3ZRJT0gvG6KxQklUvsXoM6NF4/edit#slide=id.g2793d2f3e58_2_50)
  - Link rot (30% of CVE records have at least one dead link)
  - Potential for malicious takeover of invalid domains referenced in CVE records
  - Reliance on archive.org for archival

**High-level requirements discussion:**

- Do we need to archive a full page, or just the text of a page?
  - If the full page, does it need to store all of the assets of the pages (HTML/JS/CSS) so that it can be rendered on its own once archived?
- How often should references be re-archived beyond the first archival?
  - Do we need to store older versions? How many?
- How fast do we need to archive a reference once it appears in a record?
- How should the references be retrievable?
  - Do we need a viewer of the archived references, or just provide them in their raw form and allow users to download them?
- Is there a subset of references that we want to archive, or should this effort cover all references?
- Do we want to archive references in ADP records as well?

**Proposed solutions**

- (answer questions above before coming up with solutions)
