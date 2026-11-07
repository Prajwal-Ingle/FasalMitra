# Design System: FasalMitra AI (Playful Neo-Brutalist)

<!-- impeccable:design-tokens 1 -->

## Design Philosophy: Playful Neo-Brutalism
Inspired by modern, tactile, friendly neo-brutalist digital craft (Gumroad / LearnHub style). It features thick crisp dark borders, playful hard offset drop shadows (`4px 4px 0px #1E293B`), warm cream linen backgrounds (`#FFFDF7`), pastel color-blocked icon badges, and vibrant green primary calls to action. The aesthetic is friendly, accessible, extremely tactile, and enjoyable for users of all technical levels.

## Color Tokens

### Canvas & Surfaces
- `--neo-canvas`: `#FFFDF7` (Warm cream / soft ivory background)
- `--neo-canvas-alt`: `#D9EBF5` (Pastel sky blue section canvas)
- `--neo-surface`: `#FFFFFF` (Card container fill)
- `--neo-border`: `#1E293B` (Thick dark navy/charcoal border, 2.5px)
- `--neo-shadow`: `#1E293B` (Crisp 0-blur hard offset shadow)

### Brand & Interactive
- `--neo-primary-green`: `#22C55E` (Vibrant emerald CTA button fill)
- `--neo-primary-dark`: `#16A34A` (Hover green)
- `--neo-secondary-blue`: `#93C5FD` (Pastel sky blue secondary button fill)
- `--neo-accent-yellow`: `#FACC15` (Star rating & highlight yellow)

### Pastel Badges & Icon Blocks
- `--neo-pastel-mint`: `#DCFCE7` (Crop health & positive badges)
- `--neo-pastel-blue`: `#BAE6FD` (Diagnosis & tech badges)
- `--neo-pastel-coral`: `#FED7AA` (Warning & target alerts)
- `--neo-pastel-pink`: `#FCE7F3` (Pest & action badges)
- `--neo-pastel-lavender`: `#E0E7FF` (Knowledge & guide badges)

### Typography
- `--neo-text-primary`: `#1E293B` (Deep navy charcoal, maximum contrast)
- `--neo-text-secondary`: `#475569` (Subtle muted body text)
- `--neo-text-green`: `#16A34A` (Highlight header accent)

## Elevation & Structural Tokens
- **Borders**: `2.5px solid #1E293B` (applied to cards, buttons, badges, inputs, and nav).
- **Hard Offset Shadows**:
  - Cards: `box-shadow: 4px 4px 0px #1E293B;`
  - Large Hero / Modals: `box-shadow: 6px 6px 0px #1E293B;`
  - Pills & Badges: `box-shadow: 2px 2px 0px #1E293B;`
  - Hover Interaction: `transform: translate(2px, 2px); box-shadow: 2px 2px 0px #1E293B;`
- **Border Radius**:
  - Cards: `18px - 22px`
  - Buttons: `12px - 14px`
  - Nav Bar: `22px - 26px`
  - Category Pills: `9999px` (Fully rounded oval pill)
  - Icon Badges: `10px - 12px` (Squircle with 2px border)
