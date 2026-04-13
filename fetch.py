from flask import Flask, render_template, request, send_file
import requests
from bs4 import BeautifulSoup
import io
import re

app = Flask(__name__)

def get_essay_data(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        res = requests.get(url, headers=headers, timeout=10)
        
        if res.status_code != 200:
            return None, f"Website returned error code: {res.status_code}"

        soup = BeautifulSoup(res.text, 'html.parser')
        
        # 1. Title Extraction
        title = soup.find('h1').get_text().strip() if soup.find('h1') else "Research Insight"
        title = re.sub(r' - Wikipedia| - .*', '', title)
        
        # 2. Filtering Logic
        junk_triggers = ['cookie', 'subscribe', 'sign up', 'advertisement', 'privacy policy']
        academic_junk = ['lancet', 'geneva', 'world health organization', 'pp.', 'vol.', 'published', 'doi:', 'et al']
        essay_keywords = ['history', 'result', 'cause', 'influence', 'century', 'impact', 'developed', 'known for', 'significant']

        raw_paras = []
        for p in soup.find_all('p'):
            text = p.get_text().strip()
            
            # Clean citations and whitespace
            text = re.sub(r'\[[0-9a-zA-Z]+\]|\([0-9]+\)', '', text)
            text = re.sub(r'\s+', ' ', text)

            if len(text) > 180 and not text.endswith('...') and not any(junk in text.lower() for junk in junk_triggers):
                score = sum(1 for word in essay_keywords if word in text.lower())
                raw_paras.append({'text': text, 'score': score})

        # FIXED: Moved check outside the loop
        if not raw_paras:
            return None, "System could not find enough readable text on this page."

        # 3. Conclusion Guardian
        final_concl_para = ""
        for p_obj in reversed(raw_paras[-5:]):
            if not any(junk in p_obj['text'].lower() for junk in academic_junk):
                final_concl_para = p_obj['text']
                break
        if not final_concl_para: final_concl_para = raw_paras[-1]['text']

        # 4. Refiner Logic
        intro_sentences = re.split(r'(?<=[.!?]) +', raw_paras[0]['text'])
        intro = " ".join(intro_sentences[:3])

        middle_paras = raw_paras[1:-1]
        smartest_paras = sorted(middle_paras, key=lambda x: x['score'], reverse=True)[:6]
        
        body_points = []
        for p_obj in smartest_paras:
            if p_obj['text'] == final_concl_para: continue
            sentences = re.split(r'(?<=[.!?]) +', p_obj['text'])
            point = " ".join(sentences[:2]) if len(sentences) >= 2 else sentences[0]
            if len(point) > 300: point = point[:297] + "..."
            body_points.append(point)
        
        refined_body = "\n\n• " + "\n\n• ".join(body_points)

        concl_sentences = re.split(r'(?<=[.!?]) +', final_concl_para)
        conclusion_text = " ".join(concl_sentences[-3:])
        conclusion = f"In conclusion, the legacy and broader implications of this subject are best summarized by the following: {conclusion_text}"

        divider = "=" * 50
        word_count = sum(len(p['text'].split()) for p in raw_paras)
        
        essay = (
            f"{divider}\n"
            f"PROFESSIONAL RESEARCH REPORT: {title.upper()}\n"
            f"Source Depth: {word_count} words | Analysis: High Precision\n"
            f"{divider}\n\n"
            f"I. OVERVIEW & CONTEXT\n{'-' * 25}\n{intro}\n\n"
            f"II. CORE ANALYSIS & KEY FINDINGS\n{'-' * 35}\n{refined_body}\n\n"
            f"III. SUMMARY & PERSPECTIVE\n{'-' * 30}\n{conclusion}\n\n"
            f"{divider}\n"
            f"Refined & Structured by Naïm's Summarizer v2.0"
        )
        return essay, None
    except Exception as e:
        return None, f"Refinement Error: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    url = request.form.get('url')
    essay, error = get_essay_data(url)
    return render_template('index.html', essay=essay, error=error, original_url=url)

@app.route('/download', methods=['POST'])
def download():
    essay_content = request.form.get('essay_content')
    buffer = io.BytesIO()
    buffer.write(essay_content.encode('utf-8'))
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="Summary.txt", mimetype="text/plain")

if __name__ == '__main__':
    app.run(debug=True)