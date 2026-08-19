# Alps technical training @ Swiss AI Initiative Annual Meeting 2026 — build entry point.
#
#   make all       build PPTX, HTML and PDF of the full deck
#   make pptx      PowerPoint, with Marpit presenter notes in the speaker-notes pane
#   make html      self-contained HTML; press "p" for the built-in presenter view
#   make pdf       PDF with the speaker notes attached as annotations
#   make handout   handout/quickstart.md -> build/quickstart.pdf
#   make M=01 module   build one module on its own (fast rehearsal loop)
#   make serve     live-reloading preview of the full deck
#   make check     slide count per module — the 60-minute budget lives or dies on this
#   make clean     remove build/
#
# Requires Node.js (for npx) and a Chromium that marp-cli can drive.
#
# Two things that are easy to get wrong and are deliberate here:
#   * --html is needed for EVERY target, not just the HTML one: the slides use
#     <div class="cols"> / <div class="card"> layout blocks, stripped otherwise.
#   * --pptx-editable is NOT used: that experimental mode drops presenter notes.

# --no-stdin is not optional: without a terminal, marp-cli waits on stdin forever and
# the build hangs rather than failing. That bites any non-interactive run — a script, a
# background job, CI.
MARP        := npx --yes @marp-team/marp-cli@4.5.0 --no-stdin
BUILD       := build

# The theme is rebuilt with its logos inlined as data URIs. Marp injects the theme
# into the rendered HTML, where the source's relative asset paths would resolve
# against the output directory and silently drop the logos.
THEME_SRC   := slides/theme/cscs.css
THEME       := $(BUILD)/theme/cscs.css

MARP_FLAGS  := --allow-local-files --html --theme $(THEME)

SLIDES      := $(sort $(wildcard slides/[0-9]*.md))
DECK        := $(BUILD)/deck.md

.PHONY: all pptx html pdf handout module serve clean check runsheet footers

all: pptx html pdf

$(THEME): $(THEME_SRC) $(wildcard assets/logos/*) tools/inline-assets.py
	python3 tools/inline-assets.py $(THEME_SRC) -o $@

$(DECK): $(SLIDES) tools/assemble.py
	@mkdir -p $(BUILD)
	python3 tools/assemble.py $(SLIDES) -o $@

pptx: $(BUILD)/deck.pptx
html: $(BUILD)/deck.html
pdf:  $(BUILD)/deck.pdf

$(BUILD)/deck.pptx: $(DECK) $(THEME)
	$(MARP) $(MARP_FLAGS) -o $@ -- $(DECK)

$(BUILD)/deck.html: $(DECK) $(THEME)
	$(MARP) $(MARP_FLAGS) -o $@ -- $(DECK)

$(BUILD)/deck.pdf: $(DECK) $(THEME)
	$(MARP) $(MARP_FLAGS) --pdf --pdf-notes -o $@ -- $(DECK)

# Build a single module: make M=01 module
module: $(THEME)
	@test -n "$(M)" || { echo "usage: make M=01 module"; exit 1; }
	$(eval SRC := $(wildcard slides/$(M)-*.md))
	@test -n "$(SRC)" || { echo "no slides/$(M)-*.md found"; exit 1; }
	$(MARP) $(MARP_FLAGS) -o $(BUILD)/module-$(M).html -- $(SRC)
	$(MARP) $(MARP_FLAGS) -o $(BUILD)/module-$(M).pptx -- $(SRC)

# The handout is A4 portrait, not a slide, so it uses its own theme. Marp takes the
# page size from that theme's section width/height.
handout: $(BUILD)/quickstart.pdf

$(BUILD)/quickstart.pdf: handout/quickstart.md handout/handout.css
	@mkdir -p $(BUILD)
	$(MARP) --allow-local-files --html --theme handout/handout.css --pdf -o $@ -- $<

serve: $(DECK) $(THEME)
	$(MARP) $(MARP_FLAGS) --server $(BUILD)

check:
	@python3 tools/slide-count.py $(SLIDES)
	@python3 tools/sync-footers.py --check $(SLIDES)

# Each slide's footer carries the docs page it came from, derived from its DOCS: line.
# Edit the DOCS line in the speaker notes, then run this — never edit a footer by hand.
footers:
	@python3 tools/sync-footers.py $(SLIDES)

# Who speaks when, and what each module drops if the clock slips. Budgets are read from
# the module dividers, so this cannot drift from what is on screen.
runsheet: $(BUILD)/run-sheet.pdf

$(BUILD)/run-sheet.md: $(SLIDES) tools/run-sheet.py
	@mkdir -p $(BUILD)
	python3 tools/run-sheet.py $(SLIDES) -o $@ --start 13:30

$(BUILD)/run-sheet.pdf: $(BUILD)/run-sheet.md handout/handout.css
	$(MARP) --allow-local-files --html --theme handout/handout.css --pdf -o $@ -- $<

clean:
	rm -rf $(BUILD)
