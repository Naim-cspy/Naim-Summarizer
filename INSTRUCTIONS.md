# Setup & Usage Instructions

## Getting Started

### Step 1: Installation

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd essays
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

### Step 2: Running the Application

1. **Start the Flask server:**
   ```bash
   python fetch.py
   ```

2. **Expected output:**
   ```
   WARNING in app.run_simple...
   * Running on http://127.0.0.1:5000
   * Press CTRL+C to quit
   * Restarting with reloader
   * Debugger is active!
   ```

3. **Open in browser:**
   - Go to `http://localhost:5000`
   - You should see the Naïm's Summarizer interface

### Step 3: Using the Application

#### Basic Workflow

1. **Input a URL**: Paste any valid website URL into the input field
2. **Click Generate**: Press the "Generate Essay" button
3. **Wait for processing**: The button will show "Analyzing Content..." during processing
4. **View results**: The generated summary appears below
5. **Export**: Copy to clipboard or download as a .txt file

#### URL Requirements

Best results with:
- ✅ News articles
- ✅ Wikipedia pages
- ✅ Blog posts
- ✅ Documentation pages
- ✅ Academic content (research papers, journals)

May have issues with:
- ❌ Protected/paywalled content
- ❌ JavaScript-heavy websites
- ❌ Video-only pages
- ❌ Very short pages (<180 words)

#### Theme Control

- Click the **"🌓 Toggle Theme"** button to switch between light and dark modes
- Your preference is automatically saved and will persist on next visit

### Step 4: Downloading & Exporting

#### Copy to Clipboard
1. Click the **"📋 Copy to Clipboard"** button
2. The button will show **"✅ Copied!"** for 2 seconds
3. Paste anywhere with Ctrl+V (or Cmd+V on Mac)

#### Download as File
1. Click the **"📥 Download .txt"** button
2. The file "Summary.txt" will be downloaded to your default Downloads folder

## Configuration

### Adjusting Extraction Parameters

Edit `fetch.py` to customize behavior:

```python
# Adjust word count minimum (line ~31)
if len(text) > 180:  # Change 180 to desired minimum

# Add or remove junk triggers (line ~26)
junk_triggers = ['cookie', 'subscribe', 'sign up', ...]

# Modify academic filters (line ~27)
academic_junk = ['lancet', 'geneva', ...]

# Add relevance keywords (line ~28)
essay_keywords = ['history', 'result', 'cause', ...]
```

### Styling Customization

Edit `static/style.css` to modify appearance:

```css
/* Light mode colors */
:root {
    --bg: #f4f7f6;        /* Background color */
    --text: #333;         /* Text color */
    --btn: #27ae60;       /* Button color */
    --accent: #2c3e50;    /* Accent color */
}

/* Dark mode colors */
body.dark-mode {
    --bg: #1a1a1a;        /* Dark background */
    --text: #f4f4f4;      /* Light text */
    --btn: #2ecc71;       /* Light button */
    --accent: #3498db;    /* Light accent */
}
```

## Troubleshooting

### Application Won't Start

**Error**: `ModuleNotFoundError: No module named 'flask'`
- **Solution**: Run `pip install -r requirements.txt`

**Error**: `Address already in use`
- **Solution**: The port 5000 is occupied. Either:
  - Close other Flask apps running on port 5000
  - Change port in `fetch.py`: `app.run(debug=True, port=5001)`

**Error**: `Not a valid URL`
- **Solution**: Enter a complete URL with `http://` or `https://`

### Content Not Extracted

**Problem**: "System could not find enough readable text on this page"
- The page doesn't have enough suitable content
- Try pages with substantial paragraphs (news articles, blog posts)
- Avoid very short pages or pages with minimal text

**Problem**: "Refinement Error" message
- The webpage is protected or has unusual structure
- Try a different URL
- Check browser console for more details (F12 → Console tab)

### Styling Issues

**Problem**: Dark mode not saving
- Clear browser cache and localStorage
- Try a different browser

**Problem**: Text overflowing in the summary box
- This is fixed in the current CSS with `word-wrap: break-word`
- If still occurring, check browser compatibility (use latest Chrome/Firefox/Safari)

## Development

### Modifying the Core Logic

The main summarization logic is in the `get_essay_data()` function:

1. **Extraction** (lines 12-43): Fetches and filters paragraphs
2. **Refinement** (lines 45-62): Builds introduction, body, and conclusion
3. **Formatting** (lines 64-74): Creates the final essay output

### Adding Features

Examples of modifications:
- **Custom headers**: Edit the essay formatting template (line 64-74)
- **Different summarization approach**: Modify the scoring algorithm (line 36)
- **Additional export formats**: Add new routes similar to `/download`
- **Content preferences**: Add filters in the junk_triggers list

## Deployment

### Local Network Access

To access from other devices on your network:

1. Find your machine's IP address:
   ```bash
   # Windows
   ipconfig
   
   # macOS/Linux
   ifconfig
   ```

2. Modify `fetch.py`:
   ```python
   if __name__ == '__main__':
       app.run(debug=True, host='0.0.0.0', port=5000)
   ```

3. Access from other devices:
   ```
   http://<your-ip>:5000
   ```

### Production Deployment

For deployment to services like Heroku, Railway, or PythonAnywhere:

1. Create a `Procfile`:
   ```
   web: gunicorn fetch:app
   ```

2. Add gunicorn to requirements.txt

3. Follow each platform's specific deployment guide

## Performance Tips

- ⚡ **Faster results**: Use simple, text-heavy websites
- ⚡ **Avoid**: PDF-heavy or JavaScript-dependent sites
- ⚡ **Best sources**: Wikipedia, news sites, technical blogs

## Support

If you encounter issues:
1. Check this document for solutions
2. Review browser console errors (F12)
3. Check the terminal output for Python errors
4. Verify your internet connection is stable

Enjoy using Naïm's Summarizer!
