FROM golang:1.18.0

WORKDIR /go/src/backend
COPY go.* /go/src/backend/
RUN go mod download

COPY . /go/src/backend/

CMD ["go", "run", "."]
