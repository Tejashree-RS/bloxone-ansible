#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: dns_record_info
short_description: Manage Record
description:
    - Manage Record
version_added: 2.0.0
author: Infoblox Inc. (@infobloxopen)
options:
    id:
        description:
            - ID of the object
        type: str
        required: false
    filters:
        description:
            - Filter dict to filter objects
        type: dict
        required: false
    filter_query:
        description:
            - Filter query to filter objects
        type: str
        required: false
    inherit:
        description:
            - Return inheritance information
        type: str
        required: false
        choices:
            - full
            - partial
            - none
        default: full
    tag_filters:
        description:
            - Filter dict to filter objects by tags
        type: dict
        required: false
    tag_filter_query:
        description:
            - Filter query to filter objects by tags
        type: str
        required: false

extends_documentation_fragment:
    - infoblox.bloxone.common
"""  # noqa: E501

EXAMPLES = r"""
  - name: Get DNS A Record information by ID
    infoblox.bloxone.a_record_info:
      id: "{{ a_record_id }}"

  - name: Get DNS A Record information by filters (e.g., name_in_zone)
    infoblox.bloxone.a_record_info:
      filters:
        name_in_zone: "example_a_record"
        type: "A"

  - name: Get DNS A Record information by raw filter query
    infoblox.bloxone.a_record_info:
      filter_query: "name_in_zone=='example_a_record' and type=='A'"

  - name: Get DNS A Record information by filters (zone)
    infoblox.bloxone.a_record_info:
      filters:
        zone: "example_zone_id"
        type: "A"

  - name: Get DNS A Record information by filter query for zone
    infoblox.bloxone.a_record_info:
      filter_query: "zone=='example_zone_id' and type=='A'"

  - name: Get DNS A Record information by filters (absolute_name_spec)
    infoblox.bloxone.a_record_info:
      filters:
        absolute_name_spec: "example_a_record.example.com"
        type: "A"

  - name: Get DNS A Record information by filter query for absolute_name_spec
    infoblox.bloxone.a_record_info:
      filter_query: "absolute_name_spec=='example_a_record.example.com' and type=='A'"

  - name: Get DNS A Record information by tag filters
    infoblox.bloxone.a_record_info:
      tag_filters:
        location: "site-1"
"""  # noqa: E501

RETURN = r"""
id:
    description:
        - ID of the Record object
    type: str
    returned: Always
objects:
    description:
        - Record object
    type: list
    elements: dict
    returned: Always
    contains:
        absolute_name_spec:
            description:
                - "Synthetic field, used to determine I(zone) and/or I(name_in_zone) field for records."
            type: str
            returned: Always
        absolute_zone_name:
            description:
                - "The absolute domain name of the zone where this record belongs."
            type: str
            returned: Always
        comment:
            description:
                - "The description for the DNS resource record. May contain 0 to 1024 characters. Can include UTF-8."
            type: str
            returned: Always
        created_at:
            description:
                - "The timestamp when the object has been created."
            type: str
            returned: Always
        delegation:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        disabled:
            description:
                - "Indicates if the DNS resource record is disabled. A disabled object is effectively non-existent when generating configuration."
                - "Defaults to I(false)."
            type: bool
            returned: Always
        dns_absolute_name_spec:
            description:
                - "The DNS protocol textual representation of I(absolute_name_spec)."
            type: str
            returned: Always
        dns_absolute_zone_name:
            description:
                - "The DNS protocol textual representation of the absolute domain name of the zone where this record belongs."
            type: str
            returned: Always
        dns_name_in_zone:
            description:
                - "The DNS protocol textual representation of the relative owner name for the DNS zone."
            type: str
            returned: Always
        dns_rdata:
            description:
                - "The DNS protocol textual representation of the DNS resource record data."
            type: str
            returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        inheritance_sources:
            description:
                - "The inheritance configuration."
            type: dict
            returned: Always
            contains:
                ttl:
                    description: ""
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "The inheritance setting for a field."
                                - "Valid values are:"
                                - "* I(inherit): Use the inherited value."
                                - "* I(override): Use the value set in the object."
                                - "Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "The human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "The inherited value."
                            type: int
                            returned: Always
        ipam_host:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        name_in_zone:
            description:
                - "The relative owner name to the zone origin. Must be specified for creating the DNS resource record and is read only for other operations."
            type: str
            returned: Always
        options:
            description:
                - "The DNS resource record type-specific non-protocol options."
                - "Valid value for I(A) (Address) and I(AAAA) (IPv6 Address) records:"
                - "Option     | Description -----------|----------------------------------------- create_ptr | A boolean flag which can be set to I(true) for POST operation to automatically create the corresponding PTR record. check_rmz  | A boolean flag which can be set to I(true) for POST operation to check the existence of reverse zone for creating the corresponding PTR record. Only applicable if the I(create_ptr) option is set to I(true)."
                - "Valid value for I(PTR) (Pointer) records:"
                - "Option     | Description -----------|---------------------------------------- address    | For GET operation it contains the IPv4 or IPv6 address represented by the PTR record.<br><br>For POST and PATCH operations it can be used to create/update a PTR record based on the IP address it represents. In this case, in addition to the I(address) in the options field, need to specify the I(view) field. |"
            type: dict
            returned: Always
        provider_metadata:
            description:
                - "external DNS provider metadata."
            type: dict
            returned: Always
        rdata:
            description:
                - "The DNS resource record data in JSON format. Certain DNS resource record-specific subfields are required for creating the DNS resource record."
                - "Subfields for I(A) (Address) record:"
                - "Subfield | Description                           |Required ---------|---------------------------------------|-------- address  | The IPv4 address of the host.<br><br> | Yes"
                - "Subfields for I(AAAA) (IPv6 Address) record:"
                - "Subfield | Description                           | Required ---------|---------------------------------------|--------- address  | The IPv6 address of the host.<br><br> | Yes"
                - "Subfields for I(CAA) (Certification Authority Authorization) record:"
                - "Subfield | Description                           | Required ---------|---------------------------------------|--------- flags    | An unsigned 8-bit integer which specifies the CAA record flags. RFC 6844 defines one (highest) bit in flag octet, remaining bits are deferred for future use. This bit is referenced as I(Critical). When the bit is set (flag value == 128), issuers must not issue certificates in case CAA records contain unknown property tags.<br><br>Defaults to 0.<br><br> | No tag      | The CAA record property tag string which indicates the type of CAA record. The following property tags are defined by RFC 6844:<ul><li>I(issue): Used to explicitly authorize CA to issue certificates for the domain in which the property is published.</li><li>I(issuewild): Used to explicitly authorize a single CA to issue wildcard certificates for the domain in which the property is published.</li><li>I(iodef): Used to specify an email address or URL to report invalid certificate requests or issuers' certificate policy violations.</li></ul>Note: I(issuewild) type takes precedence over I(issue).<br><br> | Yes value    | A string which contains the CAA record property value.<br><br>Specifies the CA who is authorized to issue a certificate for the domain if the CAA record property tag is I(issue) or I(issuewild).<br><br> Specifies the URL/email address to report CAA policy violation for the domain if the CAA record property tag is I(iodef).<br><br> | Yes"
                - "Subfields for I(CNAME) (Canonical Name) record:"
                - "Subfield | Description                           | Required ---------|---------------------------------------|--------- cname    | A domain name which specifies the canonical or primary name for the owner. The owner name is an alias. Can be empty.<br><br> | Yes"
                - "Subfields for I(DNAME) (Delegation Name) record:"
                - "Subfield | Description                           | Required ---------|---------------------------------------|--------- target   | The target domain name to which the zone will be mapped. Can be empty.<br><br> | Yes"
                - "Subfields for I(DHCID) (DHCP Identifier) record:"
                - "Subfield | Description                           | Required ---------|---------------------------------------|--------- dhcid    | The Base64 encoded string which contains DHCP client information.<br><br> | Yes"
                - "Subfields for I(MX) (Mail Exchanger) record:"
                - "Subfield   | Description                       | Required -----------|-----------------------------------|--------- exchange   | A domain name which specifies a host willing to act as a mail exchange for the owner name.<br><br> | Yes preference | An unsigned 16-bit integer which specifies the preference given to this RR among others at the same owner. Lower values are preferred. The range of the value is 0 to 65535. <br><br> | Yes"
                - "Subfields for I(NAPTR) (Naming Authority Pointer) record:"
                - "Subfield    | Description                         | Required ------------|-------------------------------------|--------- flags       | A character string containing flags to control aspects of the rewriting and interpretation of the fields in the DNS resource record. The flags that are currently used are: <ul><li> B(U): Indicates that the output maps to a URI (Uniform Record Identifier). </li><li> B(S): Indicates that the output is a domain name that has at least one SRV record. The DNS client must then send a query for the SRV record of the resulting domain name. </li><li> B(A): Indicates that the output is a domain name that has at least one A or AAAA record. The DNS client must then send a query for the A or AAAA record of the resulting domain name. </li><li> B(P): Indicates that the protocol specified in the I(services) field defines the next step or phase. </li></ul> | No order       | A 16-bit unsigned integer specifying the order in which the NAPTR records must be processed. Low numbers are processed before high numbers, and once a NAPTR is found whose rule \"matches\" the target, the client must not consider any NAPTRs with a higher value for order (except as noted below for the \"flags\" field. The range of the value is 0 to 65535. <br><br> | Yes preference  |A 16-bit unsigned integer that specifies the order in which NAPTR records with equal \"order\" values should be processed, low numbers being processed before high numbers. This is similar to the preference field in an MX record, and is used so domain administrators can direct clients towards more capable hosts or lighter weight protocols. A client may look at records with higher preference values if it has a good reason to do so such as not understanding the preferred protocol or service. The range of the value is 0 to 65535.<br><br> | Yes regexp      | A string containing a substitution expression that is applied to the original string held by the client in order to construct the next domain name to lookup.<br><br>Defaults to none.<br><br> | No replacement | The next name to query for NAPTR, SRV, or address records depending on the value of the I(flags) field. This can be an absolute or relative domain name. Can be empty.<br><br> | Yes services | Specifies the service(s) available down this rewrite path. It may also specify the particular protocol that is used to talk with a service. A protocol must be specified if the flags field states that the NAPTR is terminal. If a protocol is specified, but the flags field does not state that the NAPTR is terminal, the next lookup must be for a NAPTR. The client may choose not to perform the next lookup if the protocol is unknown, but that behavior must not be relied upon.<br><br>The service field may take any of the values below (using the Augmented BNF of RFC 2234):<br><br>service_field = [ [protocol] *(\"+\" rs)]<br>protocol = ALPHA * 31 ALPHANUM<br>rs = ALPHA * 31 ALPHANUM<br><br>The protocol and rs fields are limited to 32 characters and must start with an alphabetic character.<br><br> For example, an optional protocol specification followed by 0 or more resolution services. Each resolution service is indicated by an initial '+' character.<br><br> Note that the empty string is also a valid service field.  This will typically be seen at the beginning of a series of rules, when it is impossible to know what services and protocols will be offered by a particular service.<br><br> The actual format of the service request and response will be determined by the resolution protocol. Protocols need not offer all services. The labels for service requests shall be formed from the set of characters [A-Z0-9]. The case of the alphabetic characters is not significant.<br><br> | Yes"
                - "Subfields for I(NS) (Name Server) record:"
                - "Subfield | Description                         | Required ---------|-------------------------------------|--------- dname    | A domain-name which specifies a host which should be authoritative for the specified class and domain. Can be absolute or relative domain name and include UTF-8. <br><br> | Yes"
                - "Subfields for I(PTR) (Pointer) record:"
                - "Subfield | Description                         | Required ---------|-------------------------------------|--------- dname    | A domain name which points to some location in the domain name space. Can be absolute or relative domain name and include UTF-8. <br><br> | Yes"
                - "Subfields for I(SOA) (Start of Authority) record:"
                - "Subfield     | Description                         | Required ------------ |-------------------------------------|--------- expire       | The time interval in seconds after which zone data will expire and secondary server stops answering requests for the zone.<br><br> | No mname        | The domain name for the master server for the zone. Can be absolute or relative domain name.<br><br> | Yes negative_ttl | The time interval in seconds for which name servers can cache negative responses for zone. <br><br>Defaults to 900 seconds (15 minutes).<br><br> | No refresh      | The time interval in seconds that specifies how often secondary servers need to send a message to the primary server for a zone to check that their data is current, and retrieve fresh data if it is not.<br><br>Defaults to 10800 seconds (3 hours).<br><br> | No retry        | The time interval in seconds for which the secondary server will wait before attempting to recontact the primary server after a connection failure occurs.<br><br>Defaults to 3600 seconds (1 hour).<br><br> | No rname        | The domain name which specifies the mailbox of the person responsible for this zone. <br><br> | No serial       | An unsigned 32-bit integer that specifies the serial number of the zone. Used to indicate that zone data was updated, so the secondary name server can initiate zone transfer. The range of the value is 0 to 4294967295. <br><br> | No"
                - "Subfields for I(SRV) (Service) record:"
                - "Subfield | Description                         | Required ---------|-------------------------------------|--------- port     | An unsigned 16-bit integer which specifies the port on this target host of this service. The range of the value is 0 to 65535. This is often as specified in Assigned Numbers but need not be.<br><br> | Yes priority | An unsigned 16-bit integer which specifies the priority of this target host. The range of the value is 0 to 65535. A client must attempt to contact the target host with the lowest-numbered priority it can reach. Target hosts with the same priority should be tried in an order defined by the I(weight) field.<br><br>| Yes target   | The domain name of the target host. There must be one or more address records for this name, the name must not be an alias (in the sense of RFC 1034 or RFC 2181).<br><br>A target of \".\" means that the service is decidedly not available at this domain. | Yes weight   | An unsigned 16-bit integer which specifies a relative weight for entries with the same priority. The range of the value is 0 to 65535. Larger weights should be given a proportionately higher probability of being selected. Domain administrators should use weight 0 when there isn't any server selection to do, to make the RR easier to read for humans (less noisy). In the presence of records containing weights greater than 0, records with weight 0 should have a very small chance of being selected.<br><br>In the absence of a protocol whose specification calls for the use of other weighting information, a client arranges the SRV RRs of the same priority in the order in which target hosts, specified by the SRV RRs, will be contacted.<br><br>Defaults to 0.<br><br>| No"
                - "Subfields for I(TXT) (Text) record:"
                - "Subfield | Description                         | Required ---------|-------------------------------------|--------- text     | The semantics of the text depends on the domain where it is found.<br><br> | No"
                - "Generic record can be used to represent any DNS resource record not listed above. Subfields for a generic record consist of a list of struct subfields, each having the following sub-subfields: Sub-subfield | Description                        | Required -------------|------------------------------------|--------- type         | Following types are supported:<ul><li>I(8BIT): Unsigned 8-bit integer. </li><li> I(16BIT): Unsigned 16-bit integer. </li><li> I(32BIT): Unsigned 32-bit integer. </li><li> I(IPV6): IPv6 address. For example, \"abcd:123::abcd\". </li><li> I(IPV4): IPv4 address. For example, \"1.1.1.1\". </li><li> I(DomainName): Domain name (absolute or relative). </li><li> I(TEXT): ASCII text. </li><li> I(BASE64): Base64 encoded binary data. </li><li> I(HEX): Hex encoded binary data. </li><li>I(PRESENTATION): Presentation is a standard textual form of record data, as shown in a standard master zone file. <br><br> For example, an IPSEC RDATA could be specified using the PRESENTATION type field whose value is \"10 1 2 192.0.2.38 AQNRU3mG7TVTO2BkR47usntb102uFJtugbo6BSGvgqt4AQ==\", instead of a sequence of the following subfields: <ul><li> 8BIT: value=10 </li><li> 8BIT: value=1 </li><li> 8BIT: value=2 </li><li> IPV4: value=\"192.0.2.38\" </li><li> BASE64 (without I(length_kind) sub-subfield): value=\"AQNRU3mG7TVTO2BkR47usntb102uFJtugbo6BSGvgqt4AQ==\" </li></ul></li></ul>If type is I(PRESENTATION), only one struct subfield can be specified. <br><br> | Yes length_kind  | A string indicating the size in bits of a sub-subfield that is prepended to the value and encodes the length of the value. Valid values are:<ul><li>I(8): If I(type) is I(ASCII) or I(BASE64). </li><li>I(16): If I(type) is I(HEX).</li></ul>Defaults to none. <br><br>| Only required for some types. value        | A string representing the value for the sub-subfield | Yes"
            type: dict
            returned: Always
        source:
            description:
                - "Source indicator                    | Description ------------------------------------|-------------------------------- I(STATIC)                            |  Record was created manually by API call to I(dns/record). Valid for all record types except I(SOA). I(SYSTEM)                            |  Record was created automatically based on name server assignment. Valid for I(SOA), I(NS), I(A), I(AAAA), and I(PTR) record types. I(DYNAMIC)                           |  Record was created dynamically by performing dynamic update. Valid for all record types except I(SOA). I(DELEGATED)                         |  Record was created automatically based on delegation servers assignment. Always extends the I(SYSTEM) bit. Valid for I(NS), I(A), I(AAAA), and I(PTR) record types. I(DTC)                               |  Record was created automatically based on the DTC configuration. Always extends the I(SYSTEM) bit. Valid only for I(IBMETA) record type with I(LBDN) subtype. I(STATIC), I(SYSTEM)                  |  Record was created manually by API call but it is obfuscated by record generated based on name server assignment. I(DYNAMIC), I(SYSTEM)                 |  Record was created dynamically by DDNS but it is obfuscated by record generated based on name server assignment. I(DELEGATED), I(SYSTEM)               |  Record was created automatically based on delegation servers assignment. I(SYSTEM) will always accompany I(DELEGATED). I(DTC), I(SYSTEM)                     |  Record was created automatically based on the DTC configuration. I(SYSTEM) will always accompany I(DTC). I(STATIC), I(SYSTEM), I(DELEGATED)     |  Record was created manually by API call but it is obfuscated by record generated based on name server assignment as a result of creating a delegation. I(DYNAMIC), I(SYSTEM), I(DELEGATED)    |  Record was created dynamically by DDNS but it is obfuscated by record generated based on name server assignment as a result of creating a delegation."
            type: list
            returned: Always
        subtype:
            description:
                - "The DNS resource record subtype specified in the textual mnemonic format. Valid only in case I(type) is I(IBMETA)."
                - "Value | Numeric Type | Description ------|--------------|--------------------------------------------- | 0            | Default value LBDN  | 1            | LBDN record"
            type: str
            returned: Always
        tags:
            description:
                - "The tags for the DNS resource record in JSON format."
            type: dict
            returned: Always
        ttl:
            description:
                - "The record time to live value in seconds. The range of this value is 0 to 2147483647."
                - "Defaults to TTL value from the SOA record of the zone."
            type: int
            returned: Always
        type:
            description:
                - "The DNS resource record type specified in the textual mnemonic format or in the \"TYPEnnn\" format where \"nnn\" indicates the numeric type value."
                - "Value  | Numeric Type | Description -------|--------------|--------------------------------------------- A      | 1            | Address record AAAA   | 28           | IPv6 Address record CAA    | 257          | Certification Authority Authorization record CNAME  | 5            | Canonical Name record DNAME  | 39           | Delegation Name record DHCID  | 49           | DHCP Identifier record MX     | 15           | Mail Exchanger record NAPTR  | 35           | Naming Authority Pointer record NS     | 2            | Name Server record PTR    | 12           | Pointer record SOA    | 6            | Start of Authority record SRV    | 33           | Service record TXT    | 16           | Text record IBMETA | 65536        | Infoblox meta records, not valid for DNS protocol (read-only)"
            type: str
            returned: Always
        updated_at:
            description:
                - "The timestamp when the object has been updated. Equals to I(created_at) if not updated after creation."
            type: str
            returned: Always
        view:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        view_name:
            description:
                - "The display name of the DNS view that contains the parent zone of the DNS resource record."
            type: str
            returned: Always
        zone:
            description:
                - "The resource identifier."
            type: str
            returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from bloxone_client import ApiException, NotFoundException
    from dns_data import RecordApi
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class RecordInfoModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(RecordInfoModule, self).__init__(*args, **kwargs)
        self._existing = None
        self._limit = 1000

    def find_by_id(self):
        try:
            resp = RecordApi(self.client).read(self.params["id"], inherit="full")
            return [resp.result]
        except NotFoundException as e:
            return None

    def find(self):
        if self.params["id"] is not None:
            return self.find_by_id()

        filter_str = None
        if self.params["filters"] is not None:
            filter_str = " and ".join([f"{k}=='{v}'" for k, v in self.params["filters"].items()])
        elif self.params["filter_query"] is not None:
            filter_str = self.params["filter_query"]

        tag_filter_str = None
        if self.params["tag_filters"] is not None:
            tag_filter_str = " and ".join([f"{k}=='{v}'" for k, v in self.params["tag_filters"].items()])
        elif self.params["tag_filter_query"] is not None:
            tag_filter_str = self.params["tag_filter_query"]

        all_results = []
        offset = 0

        while True:
            try:
                resp = RecordApi(self.client).list(
                    offset=offset, limit=self._limit, filter=filter_str, tfilter=tag_filter_str, inherit="full"
                )
                all_results.extend(resp.results)

                if len(resp.results) < self._limit:
                    break
                offset += self._limit

            except ApiException as e:
                self.fail_json(msg=f"Failed to execute command: {e.status} {e.reason} {e.body}")

        return all_results

    def run_command(self):
        result = dict(objects=[])

        if self.check_mode:
            self.exit_json(**result)

        find_results = self.find()

        all_results = []
        for r in find_results:
            all_results.append(r.model_dump(by_alias=True, exclude_none=True))

        result["objects"] = all_results
        self.exit_json(**result)


def main():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        id=dict(type="str", required=False),
        filters=dict(type="dict", required=False),
        filter_query=dict(type="str", required=False),
        inherit=dict(type="str", required=False, choices=["full", "partial", "none"], default="full"),
        tag_filters=dict(type="dict", required=False),
        tag_filter_query=dict(type="str", required=False),
    )

    module = RecordInfoModule(
        argument_spec=module_args,
        supports_check_mode=True,
        mutually_exclusive=[
            ["id", "filters", "filter_query"],
            ["id", "tag_filters", "tag_filter_query"],
        ],
    )
    module.run_command()


if __name__ == "__main__":
    main()
