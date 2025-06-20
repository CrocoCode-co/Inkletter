# Inkletter

**Write your emails like prose, send them like a pro.**

Inkletter is a magical little tool that transforms your plain Markdown files into beautiful, 
responsive MJML and HTML email layouts, ready to be previewed, shared or sent to the world.

## Why Inkletter?

Because writing HTML emails by hand is like ironing socks: pointless and painful.

With Inkletter, you write your content in **Markdown** (like a decent human being), 
and we turn it into **gorgeous, mobile-friendly HTML emails** powered by MJML.

Built with care, clarity and just enough elegance, 
the kind that pairs well with good typography and strong espresso.

## Features

- ✅ Convert Markdown to MJML
- ✅ Convert Markdown to full responsive HTML
- ✅ Live preview in your browser
- ✅ Device simulator (iPhone, iPad, Desktop, etc.)
- ✅ One command, zero headache
- ✅ No vendor lock-in, fully offline

## ✨ Live Samples

Explore the included examples to see Inkletter in action:
- 🔍 [sample.md](sample/sample.md) — the original Markdown source
- 💎 [sample.html](sample/sample.html) — the final responsive HTML output
- 🎨 [preview.html](sample/preview.html) — the interactive split preview (Markdown / MJML / Rendered)

## Installation

Make sure you have Python 3.8+ installed on your system.

Then in your terminal:

```bash
pip install inkletter
```

Or for development:

```bash
git clone https://github.com/your-name/inkletter.git
cd inkletter
pip install -e .
```

## How it works

### 1. Preview your Markdown as a responsive email

```bash
inkletter preview yourfile.md
```

This opens a split view in your browser with:
- Your original Markdown
- The generated MJML
- A live rendered email with responsive device preview

Yes, even iPhone 14. You’re welcome.


### 2. Convert and export to HTML

```bash
inkletter md2mjml input.md -o output.html –view
```

This will:
- Convert the Markdown to MJML
- Render it into clean HTML
- Save the HTML to `output.html`
- Optionally open it in your browser with `–view`

No fuss. No noise. Just results.


## Contributing

French or not, you are welcome to contribute.
Fork it, branch it, test it, PR it — with love.

## License

MIT — but don’t forget to say “merci” 😉

### Made with ❤️ and `markdown` in France.