# Security Policy

## Supported Versions

We currently support the following versions with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of text2svg3d seriously. If you discover a security vulnerability, please follow these steps:

### 1. **Do Not** Open a Public Issue

Please do not report security vulnerabilities through public GitHub issues.

### 2. Report Privately

Send an email to: **security@text2svg3d.example.com** (or create a private security advisory on GitHub)

Include the following information:
- Description of the vulnerability
- Steps to reproduce the issue
- Potential impact
- Suggested fix (if any)

### 3. Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days
- **Fix Timeline**: Depends on severity
  - Critical: Within 7 days
  - High: Within 30 days
  - Medium/Low: Next minor release

### 4. Disclosure Policy

- We will coordinate disclosure with you
- We will credit you in the security advisory (unless you prefer to remain anonymous)
- We will release a security advisory after the fix is deployed

## Security Best Practices

When using text2svg3d:

### Input Validation
- Always validate user input before passing to the library
- Use size limits (0.1-1000mm) as documented
- Sanitize file paths to prevent path traversal

### File Operations
- Ensure output directories have appropriate permissions
- Be cautious when processing fonts from untrusted sources
- Validate SVG output before sending to 3D printers

### Dependencies
- Keep dependencies up to date
- Use Dependabot to monitor for vulnerabilities
- Review dependency changes before updating

## Known Security Considerations

### Font Files
- text2svg3d processes TrueType/OpenType font files
- Maliciously crafted font files could potentially exploit vulnerabilities in:
  - FreeType library (mitigated: we use latest version)
  - fontTools library (mitigated: we use latest version)
- **Recommendation**: Only use fonts from trusted sources

### SVG Generation
- Generated SVG files are designed for 3D printing, not web display
- SVG files can contain JavaScript in web contexts (not applicable here)
- **Recommendation**: Sanitize SVG files if displaying in web browsers

### Cache Files
- Font cache stored in `~/.cache/text2svg3d/` with restricted permissions (0o700)
- Theme preferences stored in `~/.config/text2svg3d/` with user-only access
- **No sensitive data** is stored in cache files

## Security Measures Implemented

✅ **Input Validation**
- All user inputs are validated with strict type checking
- Size ranges enforced (0.1-1000mm)
- Path validation prevents directory traversal

✅ **Exception Handling**
- Specific exception types (no bare except)
- No information leakage in error messages
- Proper logging with appropriate levels

✅ **File Permissions**
- Cache directories created with mode 0o700 (user-only)
- No world-readable sensitive files

✅ **Dependency Management**
- Minimal dependencies (3 core libraries)
- All dependencies actively maintained
- Automated security scanning with Bandit

✅ **Code Quality**
- Static analysis with flake8, mypy
- Security scanning with bandit in CI/CD
- Pre-commit hooks for code quality

✅ **No Code Execution**
- No eval(), exec(), or __import__ of user input
- No shell command execution with user input
- No pickle deserialization of untrusted data

## Security Scanning

We use the following tools for security:

- **Bandit**: Python security linter
- **Dependabot**: Automated dependency updates
- **GitHub Security Advisories**: Vulnerability notifications
- **CodeQL** (planned): Advanced code analysis

## Acknowledgments

We would like to thank the following individuals for responsibly disclosing security issues:

_(No security issues reported yet)_

## Contact

For security concerns, contact:
- **Email**: security@text2svg3d.example.com
- **GitHub**: Create a private security advisory

---

Last Updated: 2025-11-05
