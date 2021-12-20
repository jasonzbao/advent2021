package req

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"strings"
)

func MakeRequest(day int) string {
	url := fmt.Sprintf("https://adventofcode.com/2021/day/%v/input", day)

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		panic(err)
	}

	req.AddCookie(
		&http.Cookie{
			Name:  "session",
			Value: os.Getenv("AOC_SESSION"),
		},
	)

	client := http.Client{}
	response, err := client.Do(req)
	if err != nil {
		panic(err)
	}

	body, err := ioutil.ReadAll(response.Body)
	if err != nil {
		panic(err)
	}

	return string(body)
}

func FormattedRequest(day int) []string {
	return strings.Split(strings.TrimSuffix(MakeRequest(day), "\n"), "\n")
}
