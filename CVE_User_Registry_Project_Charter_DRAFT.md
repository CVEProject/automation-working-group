# Project Charter

## Project Name:  CVE User Registry Requirements Elicitation

## Project Lead:  Kurt Seifried kseifried@cloudsecurityalliance.org

## Project URL: https://github.com/CVEProject/CVE-User-Registry

## Overview:
The CVE User Registry (originally referred to as the CNA registry, but scoping has changed) requirements elicitation project is a collaborative effort to gather, 
analyze, and document the user stories and requirements for a searchable CVE User (both CNA's, data publishers and additional entities such as projects receiving CVEs) registry. 
The proposed registry would contain information needed to support key CVE workflows, enable automation, and enhance coordination between CNAs, publishers and other stakeholders.

## Objectives:
- Provide unique identifiers for CNAs and Publishers (e.g. NVD)
- Create, assign, register, and manage CNA / Publisher and Project namespaces
- Store information about each CNA and Publisher that the CNA/Publisher itself would maintain such as: 
  - GitHub users authorized to submit pull requests
  - CNA scope designations
  - Official names for organizations/products as declared by vendor
  - Public keys
  - Points-of-contacts
- Establish rules governing changes to stored CVE data provided by the CNA/Publisher/etc.
- Provide underlying components for authentication and authorization.

## Proposed Activities:
- Document workflows
- Develop user stories that describe the:
  - Capabilities to be provided by the service
  - Resources required and dependencies that exist
  - Assumptions/Constraints
  - Acceptance criteria
- Document the business, user, functional, security and performance requirements for the proposed capabilities.
