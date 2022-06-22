package main

import (
	"html/template"
	"io"
	"io/ioutil"
	"mime"
	"net/http"
	"net/url"
	"os"
	"path/filepath"
	"time"

	"github.com/golang-jwt/jwt/v4"
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

// Setup Template
// https://echo.labstack.com/guide/templates/
type Template struct {
	templates *template.Template
}

func (t *Template) Render(w io.Writer, name string, data interface{}, c echo.Context) error {
	return t.templates.ExecuteTemplate(w, name, data)
}

type UserClaims struct {
	*jwt.RegisteredClaims
	Username string
	IsAdmin  bool
}

func main() {
	e := echo.New()
	e.Use(middleware.Logger())
	e.Use(middleware.Recover())

	// Setup Template
	t := &Template{
		templates: template.Must(template.ParseGlob("views/*.html")),
	}
	e.Renderer = t

	// Top page
	e.GET("/", func(c echo.Context) error {
		cookie, err := c.Cookie("JWT_KEY")
		if err != nil {
			return c.Redirect(http.StatusFound, "/login")
		}
		token, err := jwt.ParseWithClaims(cookie.Value, &UserClaims{}, func(token *jwt.Token) (interface{}, error) {
			secretKey := os.Getenv("JWT_SECRET_KEY")
			return []byte(secretKey), nil
		})
		if err != nil {
			return c.String(http.StatusBadRequest, "invalid session")
		}
		claims := token.Claims.(*UserClaims)
		// If you are admin, you can get FLAG
		if claims.IsAdmin {
			res, _ := http.Get("http://secret")
			flag, _ := ioutil.ReadAll(res.Body)
			if err := res.Body.Close(); err != nil {
				return c.String(http.StatusInternalServerError, "Internal Server Error")
			}
			return c.Render(http.StatusOK, "admin", map[string]interface{}{
				"username": claims.Username,
				"flag":     string(flag),
			})
		}
		return c.Render(http.StatusOK, "user", claims.Username)
	})

	// Login page
	e.GET("/login", func(c echo.Context) error {
		return c.Render(http.StatusOK, "login", "")
	})

	e.POST("/login", func(c echo.Context) (err error) {
		// Get request parameter
		username := c.FormValue("username")
		if username == "" {
			return c.Render(http.StatusBadRequest, "login", "Username is required.")
		}

		// Generate JWT token
		claims := &UserClaims{
			&jwt.RegisteredClaims{
				ExpiresAt: jwt.NewNumericDate(time.Now().Add(time.Hour * 24 * 7)),
			},
			username,
			false,
		}
		token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
		secretKey := os.Getenv("JWT_SECRET_KEY")
		tokenString, _ := token.SignedString([]byte(secretKey))

		// Set JWT token in cookie
		cookie := &http.Cookie{
			Name:    "JWT_KEY",
			Value:   tokenString,
			Expires: time.Now().Add(time.Hour * 24 * 7),
		}
		c.SetCookie(cookie)

		return c.Redirect(http.StatusFound, "/")
	})

	e.GET("/logout", func(c echo.Context) error {
		cookie := &http.Cookie{
			Name:    "JWT_KEY",
			Value:   "",
			Expires: time.Unix(0, 0),
		}
		c.SetCookie(cookie)

		return c.Redirect(http.StatusFound, "/")
	})

	e.GET("/static/:file", func(c echo.Context) error {
		path, _ := url.QueryUnescape(c.Param("file"))
		f, err := ioutil.ReadFile("static/" + path)
		if err != nil {
			return c.String(http.StatusNotFound, "No such file")
		}
		return c.Blob(http.StatusOK, mime.TypeByExtension(filepath.Ext(path)), []byte(f))
	})

	e.Logger.Fatal(e.Start(":8080"))
}
