# Ansible Role: Get Certificate (arpanrec.nebula.get_certificate_ownca)

This role generates X.509 certificates signed by your own Certificate Authority (CA) for server and client authentication. It supports comprehensive certificate management with custom extensions, subject alternative names, and multiple output formats.

**Features:**

- Server and client certificate generation with custom CA
- Comprehensive certificate configuration (SAN, key usage, basic constraints)
- Multiple output formats (PEM, PKCS#12)
- Certificate chain and full-chain generation
- Configurable certificate validity periods
- Private key generation with customizable parameters
- File permission and ownership management
- Support for encrypted private keys
- Integration with organizational PKI infrastructure

Get Server or Client certificate.

## Variables

### CA Variables

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `get_certificate_ownca_rv_private_key_content` | `str` | `true` | - | Private Key as String of OWNCA. Mutually exclusive with `get_certificate_ownca_rv_private_key_path` |
| `get_certificate_ownca_rv_private_key_path` | `str` | `true` | - | Private Key path of OWNCA. Mutually exclusive with `get_certificate_ownca_rv_private_key_content` |
| `get_certificate_ownca_rv_private_key_password` | `str` | `false` | - | password if the ownca private key is encrypted. |
| `get_certificate_ownca_rv_certificate_content` | `str` | `true` | - | Certificate as String of OWNCA. Mutually exclusive with `get_certificate_ownca_rv_certificate_path` |
| `get_certificate_ownca_rv_certificate_path` | `str` | `true` | - | Certificate path of OWNCA. Mutually exclusive with `get_certificate_ownca_rv_certificate_content` |

### Private Key Variables

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `get_certificate_ownca_rv_getcert_private_key_content` | `str` | `true` | - | Private Key Content. Mutually exclusive with `get_certificate_ownca_rv_getcert_private_key_path` |
| `get_certificate_ownca_rv_getcert_private_key_path` | `str` | `true` | - | Private Key path. Mutually exclusive with `get_certificate_ownca_rv_getcert_private_key_content` |
| `get_certificate_ownca_rv_getcert_private_key_owner` | `str` | `false` | - | Private Key file owner, when `get_certificate_ownca_rv_getcert_private_key_path` is defined |
| `get_certificate_ownca_rv_getcert_private_key_group` | `str` | `false` | - | Private Key file owner group, when `get_certificate_ownca_rv_getcert_private_key_path` is defined |
| `get_certificate_ownca_rv_getcert_private_key_file_mode` | `str` | `false` | `0600` | Private Key file mode, when `get_certificate_ownca_rv_getcert_private_key_path` is defined |
| `get_certificate_ownca_rv_getcert_private_key_size` | `int` | `false` | - | Size of the private key |
| `get_certificate_ownca_rv_getcert_private_key_password` | `str` | `false` | - | password if the private key is encrypted. |

### Certificate Variables

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `get_certificate_ownca_rv_getcert_certificate_content` | `str` | `true` | - | Certificate as String. Mutually exclusive with `get_certificate_ownca_rv_getcert_certificate_path` |
| `get_certificate_ownca_rv_getcert_certificate_path` | `str` | `true` | - | Certificate path. Mutually exclusive with `get_certificate_ownca_rv_getcert_certificate_content` |
| `get_certificate_ownca_rv_getcert_certificate_file_mode` | `str` | `false` | `0600` | Private Key file mode, when `get_certificate_ownca_rv_getcert_certificate_path` is defined |
| `get_certificate_ownca_rv_getcert_certificate_owner` | `str` | `false` | - | Private Key file owner, when `get_certificate_ownca_rv_getcert_certificate_path` is defined |
| `get_certificate_ownca_rv_getcert_certificate_group` | `str` | `false` | - | Private Key file owner group, when `get_certificate_ownca_rv_getcert_certificate_path` is defined |
| `get_certificate_ownca_rv_getcert_validity_days` | `int` | `false` | `7` | Validity of certificate in days |

### CSR Config Variables

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `get_certificate_ownca_rv_getcert_key_usage` | `list[str]` | `false` | - | Key Usages, that can be found in the [OpenSSL documentation](https://www.openssl.org/docs/manmaster/man5/x509v3_config.html) |
| `get_certificate_ownca_rv_getcert_extended_key_usage` | `list[str]` | `false` | - | Extended Key Usages, that can be found in the [OpenSSL documentation](https://www.openssl.org/docs/manmaster/man5/x509v3_config.html) |
| `get_certificate_ownca_rv_getcert_subject_alt_name` | `list[str]` | `false` | - | Subject Alternative Name (SAN) extension to attach to the certificate signing request. Values must be prefixed by their options. (These are email, URI, DNS, RID, IP, dirName, otherName, and the ones specific to your CA). Note that if no SAN is specified, but a common name, the common name will be added as a SAN except if useCommonNameForSAN is set to false. More at [https://tools.ietf.org/html/rfc5280#section-4.2.1.6](https://tools.ietf.org/html/rfc5280#section-4.2.1.6). |
| `get_certificate_ownca_rv_getcert_subject` | `dict` | `false` | - | Key/value pairs that will be present in the subject name field of the certificate signing request. If you need to specify more than one value with the same key, use a list as value. Subject field option, such as `countryName`, `stateOrProvinceName`, `localityName`, `organizationName`, `organizationalUnitName`, `commonName`, or `emailAddress`. |
| `get_certificate_ownca_rv_getcert_basic_constraints` | `list[str]` | `false` | - | Indicates basic constraints, such as if the certificate is a CA. |

### Certificate Full Chain Variables

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `get_certificate_ownca_rv_getcert_certificatefullchain_path` | `str` | `false` | - | Certificate full chain path |
| `get_certificate_ownca_rv_getcert_certificatefullchain_file_mode` | `str` | `false` | `0600` | Private Key file mode, when `get_certificate_ownca_rv_getcert_certificatefullchain_path` is defined |
| `get_certificate_ownca_rv_getcert_certificatefullchain_owner` | `str` | `false` | - | Private Key file owner, when `get_certificate_ownca_rv_getcert_certificatefullchain_path` is defined |
| `get_certificate_ownca_rv_getcert_certificatefullchain_group` | `str` | `false` | - | Private Key file owner group, when `get_certificate_ownca_rv_getcert_certificatefullchain_path` is defined |

### PKCS12 Certificate Variables

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `get_certificate_ownca_rv_getcert_pkcs12_path` | `str` | `false` | - | Certificate pkcs12 path |
| `get_certificate_ownca_rv_getcert_pkcs12_password` | `str` | `false` | - | Certificate pkcs12 password |
| `get_certificate_ownca_rv_getcert_pkcs12_file_mode` | `str` | `false` | `0600` | Private Key file mode, when `get_certificate_ownca_rv_getcert_pkcs12_path` is defined |
| `get_certificate_ownca_rv_getcert_pkcs12_owner` | `str` | `false` | - | Private Key file owner, when `get_certificate_ownca_rv_getcert_pkcs12_path` is defined |
| `get_certificate_ownca_rv_getcert_pkcs12_group` | `str` | `false` | - | Private Key file owner group, when `get_certificate_ownca_rv_getcert_pkcs12_path` is defined |

## Example Certificate Role

```yaml
- name: Create Certificate
  ansible.builtin.import_role:
      name: arpanrec.nebula.get_certificate_ownca
  vars:
      get_certificate_ownca_rv_private_key_path: ownca_private_key.pem
      get_certificate_ownca_rv_certificate_path: ownca_certificate_path.pem
      get_certificate_ownca_rv_private_key_password: password
      get_certificate_ownca_rv_getcert_private_key_password: password
      get_certificate_ownca_rv_getcert_private_key_path: private_key.pem
      get_certificate_ownca_rv_getcert_certificate_path: certificate_path.pem
      get_certificate_ownca_rv_getcert_molecule_prepare_csr_path: ownca_csr.pem
      get_certificate_ownca_rv_getcert_certificatefullchain_path: certificate_chain_path.pem
      get_certificate_ownca_rv_getcert_key_usage:
          - digitalSignature
          - nonRepudiation
          - keyEncipherment
          - dataEncipherment
          - keyCertSign
          - cRLSign
      get_certificate_ownca_rv_getcert_extended_key_usage:
          - serverAuth
          - clientAuth
          - codeSigning
          - emailProtection
          - timeStamping
          - OCSPSigning
          - msCTLSign
      get_certificate_ownca_rv_getcert_subject_alt_name:
          - DNS:www.arpanrec.com
          - IP:172.0.0.1
      get_certificate_ownca_rv_getcert_subject:
          commonName: www.arpanrec.com
      get_certificate_ownca_rv_getcert_basic_constraints:
          - CA:TRUE
          - pathlen:0
      get_certificate_ownca_rv_getcert_private_key_file_mode: "0600"
```

## Testing Certificate Role

```bash
molecule test -s role.get_certificate_ownca.default
```
