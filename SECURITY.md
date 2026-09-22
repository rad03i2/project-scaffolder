# Security Policy

## Reporting
Please report security concerns privately through GitHub's repository security reporting features when available. Do not include credentials or sensitive personal data in public issues.

## Security model
Project Scaffolder works only on local paths supplied by the user. It makes no network requests and executes no generated code. Project names are validated, output is constrained to a child directory of the selected destination, and existing managed files are not replaced unless `--force` is explicitly supplied.

Generated projects are foundations, not security guarantees. Review dependencies and deployment settings before production use.
