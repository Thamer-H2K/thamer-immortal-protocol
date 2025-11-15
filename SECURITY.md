# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Which versions are eligible for receiving such patches depends on the CVSS v3.0 Rating:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of Thamer Immortal Protocol seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### Please do NOT:
- Open a public GitHub issue for security vulnerabilities
- Discuss the vulnerability publicly until it has been addressed

### Please DO:
- Email your findings to **frankly.sa@gmail.com**
- Provide detailed information about the vulnerability
- Include steps to reproduce the issue if possible
- Allow us reasonable time to address the issue before public disclosure

### What to Include in Your Report:
- Type of vulnerability (e.g., SQL injection, XSS, authentication bypass)
- Full paths of source file(s) related to the vulnerability
- Location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

### Response Timeline:
- **Within 24 hours**: We will acknowledge receipt of your vulnerability report
- **Within 7 days**: We will provide a detailed response indicating next steps
- **Within 30 days**: We aim to release a fix for confirmed vulnerabilities

### Bug Bounty:
Currently, we do not offer a paid bug bounty program. However, we will publicly acknowledge security researchers who responsibly disclose vulnerabilities (with their permission).

## Security Features

### Encryption
- **Data at Rest**: AES-256-GCM encryption
- **Data in Transit**: TLS 1.3 with perfect forward secrecy
- **Key Management**: RSA-4096 for key exchange

### Authentication
- **Password Hashing**: Argon2id with secure parameters
- **Multi-Factor Authentication**: TOTP-based (RFC 6238)
- **JWT Tokens**: HS256 signing with short expiration
- **Session Management**: Secure session cookies with HttpOnly and SameSite flags

### Rate Limiting
- **API Rate Limits**: Token bucket algorithm
- **Login Attempts**: 5 attempts per 15 minutes
- **IP Blocking**: Automatic temporary blocking for suspicious activity

### Monitoring
- **Audit Logs**: Comprehensive logging of all security events
- **Intrusion Detection**: AI-powered anomaly detection
- **Real-time Alerts**: Immediate notification of critical security events

## Security Best Practices for Users

1. **Strong Passwords**: Use passwords with at least 12 characters including uppercase, lowercase, numbers, and symbols
2. **Enable MFA**: Always enable multi-factor authentication
3. **Keep Updated**: Regularly update to the latest version
4. **Secure Environment Variables**: Never commit `.env` files or expose secrets
5. **Review Access Logs**: Regularly check audit logs for suspicious activity
6. **Principle of Least Privilege**: Grant minimum necessary permissions to users
7. **Network Security**: Use firewalls and restrict access to necessary ports only

## Known Security Considerations

- This system is designed for **defensive security operations only**
- Ensure proper network segmentation and isolation
- Regular security audits are recommended
- Keep all dependencies up to date

## Security Updates

Security updates will be released as soon as possible after a vulnerability is confirmed. Users will be notified through:
- GitHub Security Advisories
- Release notes
- Email (for critical vulnerabilities)

## Contact

**Security Contact**: frankly.sa@gmail.com  
**Phone (Emergency)**: +966597778968  
**PGP Key**: Available upon request

---

**Thank you for helping keep Thamer Immortal Protocol and its users safe!**

© 2025 Thamer Aljadaan (CyberX) - Kingdom of Saudi Arabia 🇸🇦