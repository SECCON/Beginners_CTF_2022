package main

import (
	"bytes"
	"net/http"

	"github.com/gorilla/mux"
)

const (
	PORT = "8080"
	DIR  = "static"
)

type MyResponseWriter struct {
	http.ResponseWriter
	lengthLimit int
}

func (w *MyResponseWriter) Header() http.Header {
	return w.ResponseWriter.Header().Clone()
}

func (w *MyResponseWriter) Write(data []byte) (int, error) {
	filledVal := []byte("?")

	length := len(data)
	if length > w.lengthLimit {
		w.ResponseWriter.Write(bytes.Repeat(filledVal, length))
		return length, nil
	}

	w.ResponseWriter.Write(data[:length])
	return length, nil
}

func middleware() func(http.Handler) http.Handler {
	return func(h http.Handler) http.Handler {
		return http.HandlerFunc(func(rw http.ResponseWriter, r *http.Request) {
			h.ServeHTTP(&MyResponseWriter{
				ResponseWriter: rw,
				lengthLimit:    10240, // SUPER SECURE THRESHOLD
			}, r)
		})
	}
}

func main() {
	r := mux.NewRouter()
	r.PathPrefix("/images/").Methods("GET").Handler(http.StripPrefix("/images/", http.FileServer(http.Dir(DIR))))

	r.HandleFunc("/", IndexHandler)

	http.ListenAndServe(":"+PORT, middleware()(r))
}
