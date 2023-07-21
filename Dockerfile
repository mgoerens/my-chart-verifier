FROM docker.io/golang:1.20 as build

WORKDIR /tmp/src

COPY . .

RUN make bin

FROM registry.access.redhat.com/ubi9/ubi-minimal

COPY --from=build /tmp/src/out/my-chart-verifier /app/my-chart-verifier

WORKDIR /app

ENV PATH "$PATH:/app"

ENTRYPOINT ["/app/my-chart-verifier"]
