## Architecture

This tool inspects a Helm
chart URI (`file://`, `https?://`, etc)
and returns either a *positive* result indicating the Helm chart has passed all checks, or a *negative* result indicating
which checks have failed and remedial actions.

The application is separated in two pieces: a command line interface and a library. This is handy because the command
line interface is specific to the user interface, and the library can be generic enough to be used to, for example,
inspect Helm chart bytes in flight.

One positive aspect of the command line interface specificity is that its output can be tailored to the methods of
consumption the user expects; in other words, the command line interface can be programmed in such way it can be
represented as either *YAML* or *JSON* formats, in addition to a descriptive representation tailored to human actors.

Primitive functions to manipulate the Helm chart should be provided, since most checks involve inspecting the contents
of the chart itself; for example, whether a `README.md` file exists, or whether `README.md` contains the `values`'
specification, implicating in offering a cache API layer is required to avoid downloading and unpacking the charts for
each test.

## Getting my-chart-verifier with Docker/Podman

Container images built from the source code are hosted in https://quay.io/repository/mgoerens/my-chart-verifier
; to download using `docker` execute the following command:

```text
docker pull quay.io/mgoerens/my-chart-verifier
```

## Getting my-chart-verifier binary directly (Linux only)

Alternatively, download `my-chart-verifier` binary from the [release page](https://github.com/mgoerens/my-chart-verifier/releases) and run `my-chart-verifier verify` command to perform Helm chart checks.

## Building my-chart-verifier

To build `my-chart-verifier` locally, execute `make bin` for macOS and Linux, or `make bin_win` for Windows.

To build `my-chart-verifier` container image, execute `make build-image`:

The container image created by the build program is tagged with the commit ID of the working directory at the time of
the build: `quay.io/mgoerens/my-chart-verifier:0d3706f`.

## Usage

### Local Usage

To verify a chart against all available checks:

```text
> out/my-chart-verifier verify ./chart.tgz
> out/my-chart-verifier verify ~/src/chart
> out/my-chart-verifier verify https://www.example.com/chart.tgz
```

To apply only the `is-helm-v3` check:

```text
> out/my-chart-verifier verify --enable is-helm-v3 https://www.example.com/chart.tgz
```

To apply all checks except `is-helm-v3`:

```text
> out/my-chart-verifier verify --disable is-helm-v3 https://www.example.com/chart.tgz
```

### Container Usage

The container image produced in 'Building my-chart-verifier' can then be executed with the Docker client
as `docker run -it --rm quay.io/mgoerens/my-chart-verifier:0d3706f verify`.