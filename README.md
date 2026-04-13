# Naïm's Summarizer & Essay Maker

A powerful web application that transforms any webpage into a well-structured, professional research essay. Simply paste a URL, and the application automatically extracts, analyzes, and summarizes content into a formatted report.

## Features

- **Intelligent Content Extraction**: Scrapes webpages and filters out junk content (ads, cookies, pop-ups)
- **Smart Summarization**: Analyzes paragraphs by relevance and academic quality
- **Professional Formatting**: Generates structured essays with introduction, analysis, and conclusion sections
- **Dark/Light Mode**: Toggle between themes with persistent preference storage
- **Copy & Download**: Export summaries to clipboard or download as .txt file
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Web Scraping**: BeautifulSoup, Requests
- **Styling**: CSS Variables for theme support

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone or navigate to the project directory:**
   ```bash
   cd essays
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python fetch.py
   ```

4. **Open your browser and visit:**
   ```
   http://localhost:5000
   ```

## Usage

1. Paste a website URL into the input field
2. Click **"Generate Essay"** to analyze the content
3. Review the generated summary in the result box
4. Use **"Copy to Clipboard"** to copy the text
5. Use **"Download .txt"** to save the summary as a file
6. Toggle **"🌓 Toggle Theme"** to switch between light and dark modes

## Project Structure

```
essays/
├── fetch.py                 # Main Flask application
├── templates/
│   └── index.html          # Frontend HTML template
├── static/
│   └── style.css           # Styling and theme variables
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## How It Works

The application follows a multi-step process:

1. **Content Extraction**: Fetches the webpage and parses HTML
2. **Title Extraction**: Pulls the main heading and cleans it
3. **Filtering**: Removes junk content using keyword detection
4. **Paragraph Scoring**: Ranks paragraphs by academic relevance
5. **Structure Building**: Creates intro, body, and conclusion sections
6. **Formatting**: Outputs a professional research report

## Features in Detail

### Dark/Light Mode
- Automatically saved to browser's localStorage
- Color scheme adjusts all UI elements
- Custom CSS variables for easy theming

### Content Filtering
- Removes cookie notices, advertisements, and subscription prompts
- Filters academic junk (citations, DOIs, etc.)
- Prioritizes content with relevant keywords

### Smart Summarization
- Extracts key sentences from high-scoring paragraphs
- Limits point length to maintain readability
- Combines insights into a cohesive narrative

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Refinement Error" | The webpage may be protected or have complex structure. Try a different URL. |
| "System could not find enough readable text" | The page doesn't contain enough suitable content. Try a news article or documentation page. |
| Button not responding | Check browser console for errors (F12). Ensure JavaScript is enabled. |

## Future Enhancements

- [ ] Support for PDF input
- [ ] Multi-language summarization
- [ ] Export to PDF with formatting
- [ ] Custom summary length options
- [ ] API endpoint for programmatic access

## License

Open source project. Feel free to modify and distribute.

## Contact

Created by Naïm. For issues or suggestions, feel free to reach out!
