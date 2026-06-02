# Goi Lab

> A vocabulary data lab that builds usable learning material from structured language data.

Goi Lab takes simple JSON word lists and turns them into:
- 📇 Anki decks
- 📚 EPUB books
- 📄 PDF sheets

**Philosophy:** Vocabulary learning is more effective when treated as structured, transformable data rather than static lists. Goi Lab enables language learners to convert their vocabulary into multiple learning formats from a single source of truth.

---

## 🧠 Concept

> Vocabulary is not just memorization — it is data.

Traditional vocabulary learning relies on manual creation of flashcards, word lists, or study materials. This process is:
- **Time-consuming**: Creating materials in multiple formats requires duplicate effort
- **Error-prone**: Manual entry leads to inconsistencies
- **Inflexible**: Hard to update or reorganize once created

**Goi Lab's Approach:**
1. **Single Source**: Maintain vocabulary in one structured JSON format
2. **Multiple Outputs**: Generate Anki decks, EPUBs, PDFs from the same data
3. **Extensible**: Easy to add new languages or export formats

---

## 🚀 Quick Start

### Prerequisites
- **Node.js** 18+ (for UI development)
- **Python** 3.8+ (for data parsing)
- **npm** or **yarn**

### Running the UI
```bash
cd ui
npm install
npm run dev
```

The development server will start at `http://localhost:5173`

### Using the Vocabulary Parser
```bash
cd scripts
python vocabParser.py
```

This will parse the Finnish vocabulary data and display sample output.

---

## 📁 Project Structure

```
goi-lab/
├── data/                       # Vocabulary datasets
│   └── fi/                     # Finnish language data
│       └── finnish-1000-words.json
├── scripts/                    # Data processing scripts
│   └── vocabParser.py          # JSON → Flat format converter
├── ui/                         # React frontend
│   ├── src/
│   │   ├── App.jsx            # Main application component
│   │   └── main.jsx           # Entry point
│   ├── public/                # Static assets
│   └── package.json           # Dependencies
└── README.md                  # This file
```

---

## 📊 Data Format

Vocabulary is stored in JSON with the following structure:

```json
[
  {
    "id": 1,
    "word": "tulla",
    "meanings": [
      {
        "translation": "to come",
        "examples": [
          {
            "sentence": "Tulen huomenna.",
            "translation": "I will come tomorrow."
          },
          {
            "sentence": "Hän tulee kotiin.",
            "translation": "He/She is coming home."
          }
        ]
      }
    ]
  }
]
```

### Schema

| Field | Type | Description |
|-------|------|-------------|
| `id` | number | Unique identifier for the word entry |
| `word` | string | The word in the target language |
| `meanings` | array | List of different meanings/translations |
| `meanings[].translation` | string | English translation of the meaning |
| `meanings[].examples` | array | Example sentences demonstrating usage |
| `examples[].sentence` | string | Example sentence in target language |
| `examples[].translation` | string | English translation of the example |

### Why This Format?

- **Hierarchical**: Words can have multiple meanings, each with examples
- **Context-Rich**: Examples provide real-world usage patterns
- **Flexible**: Easy to extend with additional fields (part of speech, pronunciation, etc.)
- **Human-Readable**: JSON is easy to edit manually or programmatically

---

## 🔧 Features

### Current Features ✅

- ✅ **Structured Data Storage**: JSON-based vocabulary format
- ✅ **Data Parser**: Python script to flatten hierarchical data
- ✅ **React UI Scaffold**: Modern frontend setup with Vite

### Planned Features 🚧

- 🚧 **Anki Deck Export**: Generate `.apkg` files for spaced repetition
- 🚧 **EPUB Generation**: Create e-books for reading on devices
- 🚧 **PDF Sheets**: Printable vocabulary reference sheets
- 🚧 **Multi-Language Support**: Easy addition of new languages

---

## 🎯 Use Cases

### 1. Language Learners
- Maintain a personal vocabulary database
- Create reference materials for offline study

### 2. Language Teachers
- Build custom vocabulary sets for students
- Generate teaching materials in multiple formats
- Share structured vocabulary data

### 3. Polyglots
- Manage vocabulary across multiple languages
- Compare learning progress between languages
- Reuse the same tooling for different languages

---

## 🛠️ Development

### UI Development
```bash
cd ui
npm run dev      # Start dev server
npm run build    # Build for production
npm run lint     # Run ESLint
npm run preview  # Preview production build
```

### Adding Vocabulary Data

1. Create a JSON file in `data/<language-code>/`
2. Follow the schema defined above
3. Run the parser to validate:
   ```bash
   cd scripts
   python vocabParser.py
   ```

### Tech Stack

**Frontend:**
- React 19.2.5
- Vite 8.0.10
- ESLint for code quality

**Backend/Scripts:**
- Python 3
- pandas for data manipulation
- JSON for data storage

---

## 📚 Vocabulary Parser

The `vocabParser.py` script transforms hierarchical JSON into flat tabular data.

### Example Usage

```python
from vocabParser import load_vocab, flatten_vocab

# Load vocabulary
data = load_vocab("../data/fi/finnish-1000-words.json")

# Flatten to rows
rows = flatten_vocab(data)

# Each row contains:
# - word: Target language word
# - translation: English meaning
# - sentence: Example sentence
# - sentence_translation: Example translation
```

### Output Format

```python
{
  "word": "mennä",
  "translation": "to go",
  "sentence": "Menen kouluun.",
  "sentence_translation": "I go to school."
}
```

This flat format is ideal for:
- Generating Anki cards (word → translation)
- Creating CSV exports
- Database imports
- Statistical analysis

---

## 🌍 Supported Languages

| Language | Code | Dataset | Status |
|----------|------|---------|--------|
| Finnish | fi | finnish-1000-words.json | ✅ Active |

---

## 🎨 Export Formats

### Anki Decks (.apkg) 🚧
**Status:** Planned  
**Use Case:** Spaced repetition flashcards  
**Fields:**
- Front: Target language word + example
- Back: Translation

### EPUB Books (.epub) 🚧
**Status:** Planned  
**Use Case:** Reading on e-readers or tablets  
**Format:**
- Chapter per word category
- Examples integrated as paragraphs
- Index for quick lookup

### PDF Sheets (.pdf) 🚧
**Status:** Planned  
**Use Case:** Printable reference materials  
**Layout:**
- Table format: Word | Translation | Examples
- A4 size, printer-friendly
- Optional: Blank columns for notes


## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- Vocabulary data sources (add attribution if using existing datasets)

## 🗺️ Roadmap

### Phase 1: Foundation ✅
- [x] Define data schema
- [x] Create parser script
- [x] Set up React UI scaffold

### Phase 2: Core Exports 🚧
- [ ] Implement Anki deck generation
- [ ] Add EPUB book creation
- [ ] Build PDF sheet generator

### Phase 3: UI Development 🚧
- [ ] Vocabulary browser/editor
- [ ] Search and filtering
- [ ] Export configuration UI

---

**Built with ❤️ for language learners everywhere**
