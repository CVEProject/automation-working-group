# CVE Record Validation Rules

This document outlines the validation rules applied to the CVE Record schema as defined in the [CVE Record Format](https://github.com/CVEProject/cve-schema/blob/main/schema/docs/CVE_Record_Format_bundled.json) and those applied by the CVE Services System. 

## Validation Rules

### 1. CVE Metadata
- **Field**: `cveMetadata`
    - **Required**: Yes
    - **Validation**:
        - Must include `cveId`, `assignerOrgId`, `assignerShortName`, and `dateUpdated`.
        - `cveId` must follow the CVE ID format (e.g., `CVE-YYYY-NNNNN`).

### 2. Containers
- **Field**: `containers`
    - **Required**: Yes
    - **Validation**:
        - Must include a `cna` container.
        - Additional containers must conform to their respective schemas.

### 3. CNA Container
- **Field**: `containers.cna`
    - **Required**: Yes
    - **Validation**:
        - Must include `providerMetadata`, `descriptions`, and `affected`.
        - `providerMetadata` must include `orgId`, `shortName`, and `dateUpdated`.
        - `descriptions` must be an array with at least one entry, each containing `lang` and `value`.
        - `affected` must be an array with valid product and version information.

### 4. Problem Type
- **Field**: `containers.cna.problemTypes`
    - **Required**: No
    - **Validation**:
        - If present, must be an array with valid `descriptions`.
        - Each description must include `lang` and `value`.

### 5. References
- **Field**: `containers.cna.references`
    - **Required**: No
    - **Validation**:
        - If present, must be an array with valid `url` entries.
        - Each reference may include `name` and `tags`.

### 6. Affected Products
- **Field**: `containers.cna.affected`
    - **Required**: Yes
    - **Validation**:
        - Must include `vendor`, `product`, and `versions`.
        - `versions` must include valid `version` and optional `status` or `lessThan`.

### 7. Credits
- **Field**: `containers.cna.credits`
    - **Required**: No
    - **Validation**:
        - If present, must be an array with valid `lang` and `value` fields.

### 8. Metrics
- **Field**: `containers.cna.metrics`
    - **Required**: No
    - **Validation**:
        - If present, must conform to the CVSS schema.

### 9. Timeline
- **Field**: `containers.cna.timeline`
    - **Required**: No
    - **Validation**:
        - If present, must be an array with valid `lang`, `value`, and `time`.

### 10. Acknowledgments
- **Field**: `containers.cna.acknowledgments`
    - **Required**: No
    - **Validation**:
        - If present, must include `names` and optional `organizations` or `summary`.

### 11. Data Format
- **Field**: Entire Document
    - **Validation**:
        - Must be a valid JSON document.
        - Must conform to the CVE Record schema.

### 12. CVE Services Validation Rules
- **Field**: `DatePublic`
    - **Validation**:
        - Must not be more than 24 hours in the future.

- **Field**: `Descriptions`
    - **Validation**:
        - Must have at least one English-language description.
        - Must include at least one description with at least one non-whitespace character.
     
-  **Field**: `containers.cna.affected.packageURL`
      - **Validation**:
          - If present, must be a syntactically valid PackageURL, adhering to the PackageURL schema.
          - If present, must not contain the version component of a PackageURL.
            
- **Field**: `containers.cna.timeline.time`
    - **Validation**:
        - Prevents timestamps from having invalid timezone offsets. i.e. "2026-01-01T00:00:00.123456+25:00"
  
