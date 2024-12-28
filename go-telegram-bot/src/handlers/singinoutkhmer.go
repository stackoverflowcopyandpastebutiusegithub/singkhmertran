package handlers

import (
	"encoding/csv"
	"os"
	"regexp"
	"strings"

	"github.com/go-telegram-bot-api/telegram-bot-api/v5"
)

func GenerateLowercaseAndOriginal(word string) []string {
	lowercaseWord := strings.ToLower(strings.TrimSpace(word))
	if lowercaseWord == word {
		return []string{lowercaseWord}
	}
	return []string{lowercaseWord, word}
}

func SplitText(text string) []string {
	re := regexp.MustCompile(`[a-zA-Z0-9']+|[^\w\s]`)
	return re.FindAllString(text, -1)
}

func SingInOutKhmer(input string) (map[string][]string, error) {
	// Get the current directory of the script
	scriptDir, err := os.Getwd()
	if err != nil {
		return nil, err
	}

	// Construct the full path to the TSV file
	tsvPath := scriptDir + "/sing khmer translator/dic.tsv"

	// Read the TSV file
	file, err := os.Open(tsvPath)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	reader := csv.NewReader(file)
	reader.Comma = '\t' // Set the delimiter to tab

	// Read all rows from the TSV file
	records, err := reader.ReadAll()
	if err != nil {
		return nil, err
	}

	// Split the input string into words and symbols
	wordsAndSymbols := SplitText(input)

	// Create a dictionary to store the variables
	invar := make(map[string][]string)

	// Generate lowercase and original capitalization for each word and assign to variables
	for _, word := range wordsAndSymbols {
		if regexp.MustCompile(`[a-zA-Z0-9']+`).MatchString(word) {
			invar[strings.ToLower(strings.TrimSpace(word))] = GenerateLowercaseAndOriginal(word)
		}
	}

	// Compare with data in the 3rd column from the start (left)
	thirdColumnData := make([]string, len(records))
	for i, record := range records {
		if len(record) > 2 {
			thirdColumnData[i] = strings.ToLower(strings.TrimSpace(record[2]))
		}
	}

	// Further processing can be done here based on the requirements

	return invar, nil
}