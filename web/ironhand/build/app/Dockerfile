ARG GO_VERSION=1.18
ARG ALPINE_VERSION=3.14

# build-stage

FROM golang:${GO_VERSION}-alpine${ALPINE_VERSION} as build-stage

WORKDIR /app

COPY go.mod .
COPY go.sum .

RUN go mod download

COPY . .

RUN go build

# roduction-stage

FROM alpine:${ALPINE_VERSION} as production-stage

RUN addgroup appgroup && adduser --disabled-password --no-create-home appuser -G appgroup

WORKDIR /app

COPY --from=build-stage /app .

RUN chown -R appuser:appgroup /app

RUN chmod +x ./api

USER appuser

CMD ./api
