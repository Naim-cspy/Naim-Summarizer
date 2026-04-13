# Contributing to Naïm's Summarizer

Thank you for your interest in contributing! This document provides guidelines for participating in this project.

## How to Contribute

### Reporting Bugs
1. **Check existing issues** to avoid duplicates
2. **Provide details**:
   - What you were trying to do
   - What went wrong
   - The URL you used (if applicable)
   - Browser/OS information
   - Error messages from console (F12)

### Suggesting Features
1. Open an issue with the tag `[Feature Request]`
2. Describe the feature and its potential use cases
3. Provide examples if possible

### Code Contributions

#### Getting Started
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Test thoroughly
5. Commit with clear messages: `git commit -m "Add feature: description"`
6. Push to your fork
7. Open a Pull Request

#### Code Standards
- Use descriptive variable names
- Add comments for complex logic
- Follow PEP 8 for Python code
- Test your changes before submitting
- Update documentation if adding/changing features

#### What We're Looking For
- Bug fixes with test cases
- Performance improvements
- UI/UX enhancements
- Documentation improvements
- New export formats
- Additional content filtering options

#### What We Don't Accept
- Changes that break existing functionality
- Unrelated refactoring
- Code without comments or documentation

## Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/essays.git
cd essays

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python fetch.py
```

## Testing Your Changes

1. Test with various URLs (news, Wikipedia, blogs, etc.)
2. Test in multiple browsers (Chrome, Firefox, Safari, Edge)
3. Test with JavaScript disabled (if applicable)
4. Test light and dark mode toggling
5. Test on mobile viewport (F12 → toggle device toolbar)

## Pull Request Process

1. Update documentation if needed
2. Provide a clear description of your changes
3. Link related issues
4. Wait for review and feedback
5. Address any requested changes
6. Your PR will be merged once approved

## Questions?

- Open an issue with tag `[Question]`
- Check existing issues and documentation first

## Code of Conduct

- Be respectful and inclusive
- No harassment or discrimination
- Welcome diverse perspectives
- Focus on the work, not the person
- Be patient with new contributors

---

Happy coding! 🚀
