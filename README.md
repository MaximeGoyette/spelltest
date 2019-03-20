# SpellTest

This script will:
1. Read and parse a word list (1 word per line)
2. Shuffle the word list
3. Create an audio file for each word using the Google Text-To-Speach API
4. Play the audio file and ask the user for the spelling for each word
5. Create a file with the results

## Usage

```sh
./spelltest.py <wordlist file> [<language>]
```

The default value for 'language' is `en`.

## Example

See `example/run.sh`