package main

import (
	"html/template"
	"log"
	"net/http"
	"os"
	"strings"
)

type Embed struct {
	ImageList []string
}

func IndexHandler(w http.ResponseWriter, r *http.Request) {
	t, err := template.New("index.html").ParseFiles("./static/index.html")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		log.Println(err)
		return
	}

	// replace suspicious chracters
	fileExtension := strings.ReplaceAll(r.URL.Query().Get("file_extension"), ".", "")
	fileExtension = strings.ReplaceAll(fileExtension, "flag", "")
	if fileExtension == "" {
		fileExtension = "jpeg"
	}
	log.Println(fileExtension)

	data := Embed{}
	data.ImageList, err = getImageList(fileExtension)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		log.Println(err)
		return
	}

	if err := t.Execute(w, data); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		log.Println(err)
		return
	}
}

func getImageList(fileExtension string) ([]string, error) {
	files, err := os.ReadDir("static")
	if err != nil {
		return nil, err
	}

	res := make([]string, 0, len(files))
	for _, file := range files {
		// filtered by the fileExtension
		if !strings.Contains(file.Name(), fileExtension) {
			continue
		}
		res = append(res, file.Name())
	}

	return res, nil
}
