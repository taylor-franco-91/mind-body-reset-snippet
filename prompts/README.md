# Mind Body Reset — Raw Prompt Library (Extended)

This folder contains my raw AI prompts used to design, write, and iterate the **Mind Body Reset** website, content, and flows.  
These are developer-facing prompts (plain text) to complement the polished PDF in my portfolio.

---

## Web Design & Styling (HTML/CSS — Tailwind)
You are a senior web designer. Write custom **HTML/CSS with Tailwind** for a Mind Body Reset landing page hero. Use brand accents **#80cc28 (green)** and **#3871c1 (blue)**. Mobile-first, accessible (semantic tags, alt text, focus-visible). Include headline, italic subhead, and a primary CTA that scrolls to `#epiphany`.

## eBook Showcase (Angle + CTA)
Create a centered block for the **7-Day Mind-Body Reset** eBook with a slight angled cover (hover un-tilt). Add an italic caption and a secondary CTA (“✨ Claim your reset now”). Tailwind-only HTML; include meaningful `alt`.

## Section Layout (Story / “Epiphany”)
Create a calm, focused section titled **“How I Discovered the Power of Fasting”** with one short paragraph (≤120 words). Use a soft gradient background, rounded container, and generous spacing. Output clean **HTML (Tailwind)** only; prioritize readability and contrast.

## Benefits Grid (6 Cards)
Generate a **6-card** benefits grid (title ≤3 words + one sentence):
- Mind Clarity
- Energy
- Lightness
- Inner Peace
- Gentle Healing
- Lifestyle Shift  
Output responsive **HTML (Tailwind)** with rounded cards, soft shadows, subtle hover.

## Video Microcopy (“Start Here!”)
Write:
1) One-line intro above a meditation video (≤22 words).  
2) Tooltip for the **Start** button (reveals video; begins calm focus).  
Tone: invitational, kind. Output plain text lines.

## Testimonials (Cards + Semantics)
Write **3 testimonial cards** with short quotes (italic) and attributions (`<blockquote>` + `<cite>`). Non-medical, supportive tone. Output: mobile scroll-snap row → 3-column grid on md+ (Tailwind).

## Purchase Module (Offer + Price + Stripe)
Write a conversion-focused purchase panel for a **60-page eBook**:
- Title
- 4 feature bullets (✓)
- Price line: strike-through original → discounted
- Reassurance line (e.g., “Instant access · 30-day guarantee”)
- Primary CTA → Stripe URL  
Ethical urgency only (limited-time pricing, no fake scarcity). Semantic HTML (Tailwind).

## “What Happens After You Buy?” (Reassurance)
Two short paragraphs explaining instant email delivery + how to start today, plus one italic reassurance line. Output a centered, soft-gradient section (Tailwind).

## Upsell Title and Progression bar
lets change up some things some where it says "wait! your order isnt ready yet..." that title alone needs to go right under the progression bar and then lets take the "thank you for claiming your reset!" off since i will say that in the video! and then the message under the "wait your order isnt complete yet.." needs to stay where its at position wise on the page, can you make those adjustments for me please

## Hero Copy (Headline/Subhead/CTA)
Generate 3 hero variants:
1) Headline (≤12 words) with “New Beginnings” vibe
2) Subheadline (≤9 words, italic-friendly)
3) One CTA label (≤5 words)
 Tone: calm, encouraging, non-medical. Output as a simple list.

## Section Layout (Story / “Epiphany”)
Create a calm, focused section titled “How I Discovered the Power of Fasting” with one short paragraph (≤120 words). Use soft gradient background, rounded container, and generous spacing. Prioritize readability and contrast. Output clean HTML (Tailwind) only.

## Countdown Hook Rewrite
“Refactor the countdown messaging and microcopy in the purchase section. Current line: ‘Offer Ends in: HH:MM:SS’. Rewrite it to reduce urgency fatigue and feel more aligned with healing. Suggest 2 alternatives.”

## Objection Busters (Q&A)
Write **6 concise Q&A** items (≤55 words each) for:
- “7 days sounds hard”
- “Cleanses didn’t work”
- “Muscle loss”
- “Is it worth it?”
- “No time”
- “Is it safe?”
Tone: reassuring, honest, **non-medical**. Output as semantic `<dl><dt><dd>` with Tailwind classes.

---

### Notes
- This raw library complements my polished PDF (portfolio “Prompts” button).
- It’s organized for engineers reviewing practical prompt usage in a repo context.
