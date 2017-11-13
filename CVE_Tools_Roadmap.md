# CVE Tools Roadmap
This document is meant to organize discussion about CVE support tools.

Considering a possible move to one standard and required JSON format/schema, CVE should provide supportive tool and documentation. Humans should not have to edit JSON by hand.

Need to ask CNAs (and other requesters) what they like/want/need.

Tools need to fit together/cover needed uses.

## Existing/Emerging Tools
These are not necessarily organized to fit/cover needed uses, we haven't yet evaluated uses/requirements.

1. Online CVE submission form: <https://cveform.mitre.org/>

2. JSON validation script: <https://github.com/CVEProject/automation-working-group/tree/master/tools>

3. Convert CNA assignment information in CSV or flat file format to JSON: <https://github.com/CVEProject/automation-working-group/blob/master/tools/cna-assignment-info-to-json.pl>

4. Local Node.js application to enter a CVE record (currently only allows one reference and one product?): <https://github.com/CVEProject/automation-working-group/blob/master/tools/mitre-cna-assignment-info.js>

5. Vulnogram is a tool for creating, editing, validating, previewing CVE information in CVE JSON format, and for generating advisories.
   * Standalone browser based application: https://vulnogram.github.io/
   * Node.js server application: https://github.com/Vulnogram/Vulnogram

## Potential/Desired Tools
Understanding that requirements solcitation has not happened yet.

1. A local web browser/html/javascript form/application that allows a user to fill out a CVE record and produces a JSON file. Validate JSON. Validate field data within reason. Provide help/guidance/pointers.

2. Python (or other language) library to more easily create CVE JSON?
