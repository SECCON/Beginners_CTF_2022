package main

import (
  "net/http"
  "log"
  "fmt"
  "golang.org/x/net/http2"
	"golang.org/x/net/http2/h2c"
)

const SECRET_PATH = "/Z84"

func main() {
  handler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
    if r.URL.Path == SECRET_PATH {
      w.Header().Set("x-flag", "ctf4b{http2_uses_HPACK_and_huffm4n_c0ding}")
    }
    w.WriteHeader(200)
    fmt.Fprintf(w, "Can you find the flag?\n")
  })

  h2s := &http2.Server{}
  h1s := &http.Server{
    Addr:    ":8080",
    Handler: h2c.NewHandler(handler, h2s),
  }

  log.Fatal(h1s.ListenAndServe())
}
