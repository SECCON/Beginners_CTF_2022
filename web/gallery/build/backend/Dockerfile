FROM golang:1.18.0

WORKDIR /go/src/backend
COPY go.* /go/src/backend/
RUN go mod download

COPY . /go/src/backend/

# flag check
RUN ls -l /go/src/backend/static/flag*
CMD ["go", "run", "."]
