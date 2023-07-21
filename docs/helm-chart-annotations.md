# Certification Annotations

- [Verifier added annotations](#verifier-added-annotations)
- [Annotations by profile](#annotations-by-profile)
  - [verifier-version](#verifier-version)
  - [profile](#profile)  
  - [chart-uri](#chart-uri)
  - [digests](#digests) 
  - [lastCertifiedTimestamp](#lastCertifiedTimestamp)  
  - [certifiedOpenShiftVersions](#certifiedOpenShiftVersions)
  - [testedOpenShiftVersion](#testedOpenShiftVersion)
  - [supportedOpenShiftVersions](#supportedOpenShiftVersions)
  - [webCatalogOnly](#webCatalogOnly)  
- [Provider annotations](#provider-annotations)
  - [charts.openshift.io/provider](#chartsopenshiftioprovider)
  - [charts.openshift.io/name](#chartsopenshiftioname)
  - [charts.openshift.io/supportURL](#chartsopenshiftiosupportURL)
  - [charts.openshift.io/archs](#chartsopenshiftioarchs)  


## Verifier added annotations


The my-chart-verifier tool adds annotations to a generated report.
Example:

```
metadata:
    tool:
        verifier-version: 1.10.0
        profile:
            VendorType: partner
            version: v1.1
        reportDigest: uint64:13041017788004879705    
        chart-uri: https://github.com/mmulholla/development/blob/master/charts/partners/test-org/psql-service/0.1.9/psql-service-0.1.9.tgz?raw=true
        digests:
            chart: sha256:94cbcb63531bc4457e7b0314f781070bbfe4affbdca98f67acadc381bf0f0b4f
            package: 4e9592ea31c0509bec308905289491b7056b78bdde2ab71a85c72be0901759b8
        lastCertifiedTimestamp: "2023-01-18T14:28:52.128965-05:00"
        testedOpenShiftVersion: "4.11"
        supportedOpenShiftVersions: '>=4.8'
        webCatalogOnly: false
 
```

The annotations added differ based on the profile version used.

## Annotations by profile

| Annotation                 | Profile Versions |
| -------------------------- |:-----------------
| [verifier-version](#verifier-version)                     | v1.0, v1.1
| [profile](#profile)                                       | v1.0, v1.1
| [chart-uri](#chart-uri)                                   | v1.0, v1.1
| [digests](#digests)                                       | v1.0, v1.1
| [lastCertifiedTimestamp](#lastCertifiedTimestamp)         | v1.0, v1.1
| [certifiedOpenShiftVersions](#certifiedOpenShiftVersions) | v1.0 
| [testedOpenShiftVersion](#testedOpenShiftVersion)         | v1.1
| [supportedOpenShiftVersions](#supportedOpenShiftVersions) | v1.1
| [webCatalogOnly](#webCatalogOnly) | not specific to a profile 

### verifier-version

The version of the my-chart-verifier which generated the report. 

### profile

This annotation includes the vendor type and version of the profile used to generate the report.

### chart-uri

The location of the chart specified to the my-chart-verifier. For report-only submissions, this must be the public url of the chart.

### digests

This annotation can include the following digests:
- digests.chart:
    - sha:256 value of the chart as calculated from the copy of the chart loaded into memory by the my-chart-verifier.  
    - When submitting a report, this value must match the value generated as part of the submission process.
- digest.package:
    - The sha value of the chart tarball if used to create the report.
    - Not included if chart source was used.
    
### lastCertifiedTimestamp

The time when the report was generated.

### certifiedOpenShiftVersions

- The version of OpenShift Container Platform (OCP) that the ```chart-testing``` check was performed on. If the role of the logged-in user prevents this annotation from being accessed, the value must be specified using the ```--openshift-version``` flag.
- If the ```certifiedOpenShiftVersions``` annotation is not set to a valid OpenShift version, the submission will fail.
- Renamed to the ```testedOpenShiftVersion``` annotation in the v1.1 profile version.

### testedOpenShiftVersion

- The version of OpenShift Container Platform (OCP) that the ```chart-testing``` check was performed on. If the role of the logged-in user prevents this annotation from being accessed, the value must be specified using the ```--openshift-version``` flag.
- If the ```testedOpenShiftVersion``` annotation is not set to a valid OpenShift version, the submission will fail.
- Renamed from ```certifiedOpenShiftVersions``` in profile version v1.1

### supportedOpenShiftVersions 

The OpenShift versions supported by the chart, based on the ```kubeVersion``` attribute in the ```chart.yaml``` file.

### webCatalogOnly

Used to control the distribution method of a certified chart:

- True: The chart is not published in the OpenShift Helm chart catalog when certified.
- False (default): The chart is published in the OpenShift Helm chart catalog when certified.

For more information, see: [Web Catalog Only.](helm-chart-submission.md#web-catalog-only)

## Provider annotations

The chart provider can also include annotations in `Chart.yaml`, which may be used when displaying the chart in the catalog, for example:

```
annotations:
   charts.openshift.io/archs: x86_64
   charts.openshift.io/name: PSQL RedHat Demo Chart
   charts.openshift.io/provider: RedHat
   charts.openshift.io/supportURL: https://github.com/dperaza4dustbit/helm-chart
```

### charts.openshift.io/provider

Name of chart provider (e.g., Red Hat), ready to be displayed in UI.

### charts.openshift.io/name

Human readable chart name, ready to be displayed in UI.
- This is mandatory with profile v1.1 (see: [has-kubeversion v1.1](helm-chart-troubleshooting.md#has-kubeversion-v11)) 

### charts.openshift.io/supportURL

Where users can find information about the chart provider's support.

### charts.openshift.io/archs

Comma separated list of supported architectures (e.g., x86_64, s390x, ...)

