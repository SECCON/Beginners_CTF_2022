package main

import (
	"net/http"
	"os"

	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

func main() {
	e := echo.New()

	e.Use(middleware.Logger())
	e.Use(middleware.Recover())

	e.GET("/", func(c echo.Context) error {
		flag := os.Getenv("FLAG")
		return c.String(http.StatusOK, flag)
	})

	e.Logger.Fatal(e.Start(":80"))
}
