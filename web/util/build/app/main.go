package main

import (
	"os/exec"

	"github.com/gin-gonic/gin"
)

type IP struct {
	Address string `json:"address"`
}

func main() {
	r := gin.Default()

	r.LoadHTMLGlob("pages/*")

	r.GET("/", func(c *gin.Context) {
		c.HTML(200, "index.html", nil)
	})

	r.POST("/util/ping", func(c *gin.Context) {
		var param IP
		if err := c.Bind(&param); err != nil {
			c.JSON(400, gin.H{"message": "Invalid parameter"})
			return
		}

		commnd := "ping -c 1 -W 1 " + param.Address + " 1>&2"
		result, _ := exec.Command("sh", "-c", commnd).CombinedOutput()

		c.JSON(200, gin.H{
			"result": string(result),
		})
	})

	if err := r.Run(); err != nil {
		panic(err)
	}
}
