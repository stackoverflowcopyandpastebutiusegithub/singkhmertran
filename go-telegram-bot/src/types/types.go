package types

// UserInput represents the structure for user input data.
type UserInput struct {
    Original string   // The original input string from the user
    Words    []string // A slice of words extracted from the input
}

// TranslationResult represents the structure for translation results.
type TranslationResult struct {
    TranslatedText string // The translated text
    OriginalText   string // The original text provided by the user
}