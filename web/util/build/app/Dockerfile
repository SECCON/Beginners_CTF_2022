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

RUN chmod 1733 /tmp /var/tmp /dev/shm

RUN echo "ctf4b{al1_0vers_4re_i1l}" > /flag_$(cat /dev/urandom | tr -dc "a-zA-Z0-9" | fold -w 16 | head -n 1).txt

WORKDIR /app

COPY --from=build-stage /app/api ./api

COPY --from=build-stage /app/pages ./pages

RUN chmod +x ./api

USER appuser

CMD ./api
