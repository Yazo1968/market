# Investment Structures: Comprehensive Reference

This file details each investment structure type used in Path B recommendations: how it works, when it's appropriate, key terms, investor protections, negotiation points, and geographic applicability.

---

## 1. Priced Equity Round (Common Stock, Preferred Stock)

### How It Works

Investors purchase preferred stock in the company at an agreed-upon valuation. The preferred stock has specific rights and protections that distinguish it from founder common stock.

- **Common Stock**: Founder/employee equity; voting rights, no liquidation preference, last to be paid in exit
- **Preferred Stock**: Investor equity; liquidation preference (paid first in exit), board seats, approval rights, anti-dilution protection

### When It's Appropriate

- Series A and beyond: standard instrument at all later stages
- Institutional investor participation required: VCs, growth equity firms, strategic investors
- Company has reached product-market fit / clear traction: valuation is defensible
- Professional governance desired: investor brings board seat, governance structure, operational oversight

### Key Terms and Significance

#### Valuation / Price Per Share
- Company valuation (pre-money or post-money)
- Example: "$25M pre-money valuation, $10M investment → 28.6% dilution"
- Calculated from comparable companies, recent M&A, growth rate projections

#### Liquidation Preference
- **1x non-participating**: investor gets 1x investment back; founders get remainder
  - Example: $5M invested at 1x, exit for $50M → investor gets $5M, founders split $45M
- **1x participating capped at 3x**: investor gets $5M back, then participates in next $10M (3x cap)
  - Example: $5M invested at 1x participating (3x cap), exit for $50M → investor gets $5M + $10M = $15M
- **Seniority**: Series A preference senior to founder common; Series B senior to Series A; etc.

#### Liquidation Preference in Down Exit
- In down exit (company sold for less than raised capital): liquidation preference protects investor
- Example: $10M Series A raised, sold for $5M → Series A gets $5M; founders get $0
- Reason: investors protected; founders bear downside risk

#### Anti-Dilution
- **Weighted-average**: if future down round, investor's conversion price adjusts downward (protects against massive dilution)
  - Math: (old # of shares * old price + new # of shares * new price) / (old # + new #) = adjusted price
  - Example: Series A at $1/share, down round at $0.50/share with 50% dilution → Series A adjusts to ~$0.75/share
- **Broad-based vs. narrow-based**: affects calculation (broad-based is founder-friendly, narrow-based is investor-friendly)
- **Full ratchet**: investor's price drops all the way to new down-round price (most investor-friendly, rare in Series A, more common in down rounds)

#### Conversion
- Preferred automatically converts to common at IPO or change of control
- Allows investor to liquidation preference OR equity upside in exit (whichever is greater)

#### Board Seat / Observation
- Lead investor typically gets 1 board seat
- Other preferred holders may get board observation rights
- Founder retains founder CEO seat

### Investor Protections (Standard Package)

- **Liquidation preference**: paid before common in exit
- **Pro-rata rights**: can participate in future rounds to maintain ownership %
- **Anti-dilution**: weighted average protection in down rounds
- **Approval rights**: veto over major transactions (exit, debt, related-party, new fundraising)
- **Information rights**: monthly financials, quarterly board meetings
- **Registration rights**: demand rights for IPO, piggyback rights, S-3 rights if company qualifies
- **Drag-along**: if majority preferred holders approve exit, can force all holders (including founders) to participate

### Common Negotiation Points

- **Valuation**: founders want higher (less dilution); investors want lower (more upside)
- **Participation cap**: investors want high cap (more upside); founders want lower cap or none
- **Anti-dilution formula**: narrow-based vs. broad-based (affects down round protection)
- **Board seats**: investors want >1 seat; founders want minimal investor board control
- **Approval rights**: investors want extensive veto; founders want operational autonomy
- **Redemption**: investors may want right to force redemption if no exit after 7 years (rare in Series A, more common in Series C+)

### Red Flags (Non-Standard Terms)

- **Full-ratchet anti-dilution**: overly investor-protective; extremely dilutive to founders in down rounds
- **Broad participation rights** (uncapped multi-participation): founders get squeezed in exit
- **Redemption rights**: forces company to return capital; liquidity pressure on company
- **Extensive approval rights**: founder cannot operate company without investor consent
- **Participating preferred** at early stage (Seed/Series A): should be capped; uncapped is aggressive

### Geographic Applicability

- **North America**: Standard for Series A+; NVCA model documents are baseline
- **Europe**: Similar to North America; BVCA model broadly aligned with NVCA
- **GCC/MENA**: Increasingly adopted; regulatory nuances (SAMA, DFSA) for cross-border structures
- **Southeast Asia**: Standard for institutional rounds; family office investors may use simpler common stock structures
- **Cross-border**: regulatory approval required in some jurisdictions (GCC regulators may require review)

---

## 2. SAFE (Simple Agreement for Future Equity)

### How It Works

SAFE is a simple contract between investor and company: investor provides capital, and in exchange, investor receives future equity at a discount or cap when specified triggering event occurs (typically next equity round, IPO, or acquisition).

**Key concept**: SAFE is NOT equity; it's a contract for future equity. Until trigger event, SAFE holder has no voting rights, no board seat, no liquidation preference.

### When It's Appropriate

- Seed stage: standard instrument in early-stage (pre-valuation) rounds
- Speed and simplicity: closes in days not weeks
- Flexible founders: don't want investor board seat or governance requirements
- High-volume investor base: easier to coordinate 20 SAFE investors than 20 preferred equity rounds

### Key Terms and Significance

#### Post-Money SAFE
- Investor provides capital; SAFE cap is "post-money valuation" including SAFE amount
- Example: $500K SAFE with $2M post-money cap → investor will own ~25% at conversion if valuation <$2M
- More founder-friendly: delay valuation uncertainty until later round

#### Pre-Money SAFE (less common)
- SAFE cap is pre-money valuation (excludes SAFE amount)
- Less common now; post-money became standard after 2018

#### Valuation Cap
- Investor converts at lower of: (1) cap price or (2) discount to next round valuation
- Example: $1M SAFE with $3M cap, 20% discount
  - If Series A at $5M valuation: convert at $5M * 80% = $4M valuation (20% discount better than cap)
  - If Series A at $2M valuation: convert at cap ($3M) (cap better than discount)

#### Discount Rate
- Investor gets shares at discount to next priced round
- Typical discount: 10–30% (seed stage 20–30%, later stage 10–20%)
- Incentivizes early investment before valuation clarity

#### Most Favored Nation (MFN) Clause
- If later SAFE holder gets better terms (lower cap, higher discount), earlier holders get same terms
- Example: first SAFE at $2M cap, second SAFE at $1.5M cap → first SAFE investor also gets $1.5M cap
- Protects early investors from being disadvantaged by later terms

### Conversion Triggers

- **Priced round**: typical trigger; when company raises Series A or later, SAFEs convert to preferred stock
- **IPO**: SAFE converts to common stock at set conversion formula
- **Acquisition / exit**: SAFE converts to common or cash (investor receives multiple of SAFE investment, or $1/share, depending on terms)
- **Dissolution / liquidation**: SAFE is treated as debt-like (paid before common, after actual creditors)

### Investor Protections in SAFE

- **No liquidation preference**: SAFE holder does not have preferred liquidation preference (SAFE is treated more like debt in dissolution than preferred equity)
- **Discount / cap**: investor protected by conversion discount and valuation cap
- **Pro-rata rights**: may be included (option to participate in future rounds to maintain ownership %)
- **Most favored nation**: protects against later SAFEs having better terms
- **Note on governance**: SAFE holder has NO voting rights, no board seat, no information rights, no approval rights until conversion

### Standard Conditions
- MFN rights: automatic
- Pro-rata rights: optional (many SAFEs include, increasingly standard)
- Trigger event: next priced round, IPO, acquisition
- Conversion formula: cap or discount, whichever is better for SAFE holder

### Common Negotiation Points

- **Valuation cap**: investor wants lower (more shares); founder wants higher (less dilution)
- **Discount rate**: investor wants higher (more incentive); founder wants lower
- **Pro-rata rights**: investor wants yes; founder wants no (preserves future flexibility)
- **MFN clause**: investor wants yes; founder wants no (avoids retroactive term changes)
- **Board observer rights**: investor may request (though not standard in SAFE)

### Red Flags

- **Very low cap** ($500K for seed when market cap is $2M+): overly investor-favorable
- **Very high discount** (>30%): significantly dilutes later investors
- **Uncapped SAFE**: no valuation cap; investor gets arbitrarily high ownership (extreme case: cap at 1x acquisition price)
- **Aggressive pro-rata rights**: MFN + pro-rata combination can lock founder into long pro-rata obligation across many investors

### Conversion Examples

**Scenario 1: Standard SAFE with Discount**
- SAFE: $500K invested, 20% discount, no cap
- Series A: $5M pre-money valuation, $2M raise
- SAFE conversion: $5M * 80% = $4M conversion price
- SAFE investor ownership: $500K / $4M = 12.5%

**Scenario 2: SAFE with Cap**
- SAFE: $500K invested, 20% discount, $2M cap
- Series A: $1M pre-money valuation, $1M raise
- SAFE conversion: cap price better → convert at $2M (cap)
- SAFE investor ownership: $500K / $2M = 25%

**Scenario 3: SAFE in Acquisition**
- SAFE: $500K invested
- Acquisition for $10M
- SAFE terms: convert to common at $1/share, then participate in acquisition proceeds
- SAFE investor receives: multiple of $500K (per acquisition formula)

### Geographic Applicability

- **North America**: Dominant (90%+ of seed rounds)
- **Europe**: Increasing adoption (SAFE becoming more common than convertibles)
- **GCC/MENA**: Emerging (Y Combinator and accelerator demo day SAFEs increasingly used)
- **Southeast Asia**: Growing adoption (Singapore-based investors prefer; more traditional markets use convertibles)

---

## 3. Convertible Note

### How It Works

Convertible note is a short-term debt instrument that converts to equity upon trigger event (next fundraising round). Until conversion, investor receives interest income and principal repayment obligation (if maturity reached without conversion).

**Key concept**: convertible is debt (not equity) until conversion event occurs.

### When It's Appropriate

- Seed stage: popular for seed rounds (though declining in favor of SAFE)
- Bridge financing: quick close, minimal documentation
- Flexibility: if conversion doesn't happen (acquisition at low valuation), investor can demand debt repayment

### Key Terms and Significance

#### Principal Amount
- Dollar amount invested
- Accrues interest until conversion or maturity

#### Interest Rate
- Typical: 5–8% per annum (seed stage)
- Accrues monthly or annually
- Example: $500K convertible at 6% interest, 24-month maturity = accrued interest of $60K at maturity if not converted

#### Maturity Date
- Typical: 24–36 months from issuance
- If conversion trigger not met, note matures and company must repay principal + accrued interest
- Creates pressure on company to raise Series A before maturity (else faces debt repayment obligation)

#### Valuation Cap
- Maximum valuation at which note converts
- If Series A valuation >cap, note converts at cap price
- If Series A valuation <cap, note converts at Series A price
- Example: $500K note with $3M cap, Series A at $2M → converts at $2M (lower than cap)

#### Discount Rate
- Investor converts at discount to next priced round
- Typical: 20–30% discount
- Incentivizes early investment

#### Conversion to Equity
- Upon Series A (or priced round), note converts to same preferred stock as Series A
- Conversion price: lower of cap or (Series A valuation * (100% - discount %))
- Accrued interest added to conversion amount (increases investor ownership %)

### Conversion in Acquisition
- If acquisition occurs before conversion trigger (Series A), terms dictate outcome:
  - **Conversion at acquisition price**: note converts to common at acquisition valuation
  - **Cash repayment**: investor receives principal + accrued interest (treated as debt)
  - **Multiple of investment**: investor receives 1.2x–1.5x principal (per note terms)
- Terms negotiated; varies by note

### Investor Protections

- **Debt security**: if company fails before Series A, investor is creditor (ahead of founders in liquidation)
- **Interest income**: investors receive interest payments before conversion
- **Valuation cap / discount**: protects against valuation inflation
- **Maturity repayment**: if no conversion, company must repay debt (creates discipline)

### Standard Conditions
- Interest accrual: monthly or annually
- Conversion on Series A or other qualified priced round
- Maturity: typically 24–36 months
- Prepayment: allowed (no penalty, but rare in practice)

### Common Negotiation Points

- **Interest rate**: investor wants higher (more compensation for early risk); founder wants lower
- **Maturity date**: investor wants longer (more time to maturity); founder wants shorter (less time to worry about repayment)
- **Valuation cap**: investor wants lower (more conversion shares); founder wants higher
- **Discount rate**: investor wants higher; founder wants lower
- **Conversion terms in acquisition**: investor wants repayment of principal+interest (favors early stage); founder wants conversion (converts valuation to equity)

### Red Flags

- **Very low cap**: cap at $1M when similar companies at $3M+ is overly investor-favorable
- **Very high interest rate** (>10%): unusual unless company is high-risk
- **Long maturity date** (>36 months): creates extended uncertainty
- **Forced conversion at acquisition**: note terms may force conversion even if acquisition valuation low (founder-unfavorable)
- **Personal guarantee**: sometimes required of founder; unusual for institutional rounds

### Comparison to SAFE

| Dimension | Convertible Note | SAFE |
|-----------|------------------|------|
| Is it debt? | Yes (until conversion) | No (never debt) |
| Interest? | Yes, 5–8% typical | No |
| Maturity date? | Yes, 24–36 months | No |
| Investor repayment obligation? | Yes (if maturity without conversion) | No |
| Speed to close? | Slower (40–60 days) | Faster (15–30 days) |
| Founder-friendly? | Less (debt obligation looms) | More (no repayment obligation) |

### Geographic Applicability

- **North America**: Declining (SAFE now preferred); still used in some markets
- **Europe**: Still common (more so than SAFEs)
- **GCC/MENA**: Common (debt instruments more familiar in region)
- **Southeast Asia**: Common (especially fintech/Southeast Asian traditional markets)

---

## 4. Venture Debt / Credit Facility

### How It Works

Lender provides senior debt (loan) to company. Company repays principal + interest over term (typically 3–5 years). Loan is secured against company assets and/or personal guarantee from founder.

**Key concept**: venture debt is true debt (not equity); lender has no ownership stake (though may have warrant coverage for equity upside).

### When It's Appropriate

- Bridge funding: extend runway between equity rounds without dilution
- Growth capital: fund sales hiring, marketing, product development
- Profitable or near-profitable companies: debt service requires revenue to support
- De-risk equity financing: venture debt allows smaller equity rounds (company raises less equity if supplementing with debt)

### Key Terms and Significance

#### Principal Amount
- Loan size: typically 25–50% of most recent equity round
- Example: $10M Series B → $2.5–5M venture debt facility

#### Interest Rate
- Typical: 8–12% per annum (risk-dependent)
- Early-stage (pre-revenue): 10–12%
- Series A+ (some revenue): 8–10%
- Profitable (or strong EBITDA): 6–8%
- Factors: revenue, growth, burn rate, DSCR (debt service coverage ratio)

#### Term / Amortization
- Typical: 3–5 year amortization
- Example: $2M facility, 48-month term = ~$46K monthly payment (principal + interest)
- Payment frequency: monthly (occasionally quarterly)

#### Warrant Coverage
- Lender receives warrants (option to buy shares at par) as equity upside
- Typical: 10–20% of facility size (in warrant shares)
- Example: $2M facility, 10% warrant coverage = 200K shares (or dollar equivalent) at strike price
- Warrant terms: 7–10 year expiration, full ratchet anti-dilution, 5-year exercisability window

#### Covenants (Restrictions)
- **Minimum monthly revenue**: company must maintain revenue floor (e.g., $50K+ monthly)
- **Minimum cash balance**: company must keep cash >$X (e.g., $500K minimum)
- **Debt service coverage ratio (DSCR)**: if profitable, debt payments must be <X% of cash flow (e.g., 1.25x DSCR required)
- **Revenue decline trigger**: if monthly revenue declines >20%, lender can declare default (cure period typical)
- **Related-party transaction**: lender approval required for related-party transactions >$X

#### Security / Collateral
- **First lien**: lender has senior security interest in company assets (receivables, inventory, IP)
- **Personal guarantee**: founder personally guarantees loan (lender can pursue personal assets if company fails)
- **UCC-1 filing**: lender files lien on company assets (public record)

#### Prepayment
- Typically allowed without penalty
- Rare in practice (companies don't prepay debt early if can preserve cash)

### Investor Protections (Lender Perspective)

- **Senior debt**: paid before equity holders in exit or liquidation
- **Warrant coverage**: equity upside via warrants (participate in upside without diluting equity holders as much)
- **Covenants**: lender can monitor company health via monthly revenue, cash, DSCR
- **Personal guarantee**: recourse to founder personal assets if company fails
- **Security interest**: first lien on company assets

### Conditions Precedent

- Subordination agreement: if future equity raised, equity holders agree venture debt is senior
- Personal guarantee: executed by founder
- UCC-1 filing: lender files security agreement on company assets
- Insurance: general liability, business interruption, key person insurance required
- Legal opinion: company formation, good standing, no litigation

### Common Negotiation Points

- **Interest rate**: lender wants higher (more compensation); company wants lower
- **Warrant coverage**: lender wants higher % (more upside); company wants lower
- **Covenants**: lender wants strict (frequent monitoring); company wants loose (operational flexibility)
- **Prepayment penalties**: company wants no penalty; lender prefers penalty (locks duration)
- **Personal guarantee**: company wants waiver (especially if >$2M equity raised); lender wants guarantee (security)

### Red Flags

- **Very high interest rate** (>15%): indicates lender sees company as very high-risk
- **Excessive warrant coverage** (>30%): significantly dilutive to founders
- **Tight covenants**: revenue floor too high, DSCR too strict, can create unintended default
- **Mandatory prepayment on Series B**: lender requires debt repaid on future fundraising (blocks future growth capital)
- **Personal guarantee for established company**: unusual (suggests lender concern about company stability)

### Geographic Applicability

- **North America**: Dominant market; established venture debt industry (Silicon Valley Bank, Gold Hill, Horizon, others)
- **Europe**: Growing (Barclays Growth Ventures, UK VCs beginning to offer)
- **GCC/MENA**: Emerging (limited availability)
- **Southeast Asia**: Very limited availability (few institutional venture debt lenders)

---

## 5. Revenue-Based Financing

### How It Works

Investor provides capital (non-dilutive, no equity given up). Company repays investor a fixed percentage of monthly revenue until repayment cap is reached (typically 2–2.5x amount financed).

**Key concept**: non-dilutive financing; founder retains 100% ownership.

### When It's Appropriate

- Recurring revenue model: subscription SaaS, digital services, marketplace with predictable take-rate
- Profitable or near-profitable: need predictable revenue to support repayment
- Founder control: founder wants to avoid VC dilution, board seats, governance
- Growth acceleration: fund hiring, marketing, product development without equity dilution

### Key Terms and Significance

#### Capital Amount
- Typically: $250K–$5M
- Based on monthly recurring revenue
- Example: $50K/month ARR, investor finances $1M (based on ~20 months of revenue)

#### Monthly Repayment Percentage
- Typical: 1–3% of monthly revenue
- Example: 2% monthly = 24% annual repayment rate (if revenue constant)
- Higher percentage = faster repayment (company wants lower %; investor wants higher %)
- Varies by revenue stability, growth rate, industry

#### Repayment Cap
- Total repayment cap: typically 2–2.5x amount financed
- Example: $1M financed, repay until $2–2.5M paid (then financing ends)
- Once cap reached: company stops making payments (keeps 100% ownership)
- Remaining term forgiven: if term expires before cap, company keeps financing (no additional payment)

#### Term Length
- Typical: 5–7 years maximum
- Financing ends when: (1) cap reached, (2) term expires, or (3) company liquidates
- No conversion to equity: investor receives cash only, no equity interest

#### Revenue Decline Conditions
- If monthly revenue declines >20%: lender may pause repayment obligations (or adjust repayment down)
- Revenue reporting: monthly (via API integration, accounting software connection, or manual)
- Transparency: investor has visibility into company revenue (may require monthly dashboard)

### Investor Protections

- **Revenue transparency**: monthly revenue reporting via API or accounting sync
- **Repayment from revenue**: cash flow directly linked to revenue (company has cash to pay)
- **No dilution**: even if venture capital later, RBF investor maintains preferred repayment position
- **Cap on upside**: capped at 2–2.5x (predictable returns, not unbounded equity upside)

### Conditions Precedent

- Revenue documentation: 6–12 months of historical revenue (proven consistency)
- Accounting software integration: Stripe, QuickBooks, Xero API access (for automated reporting)
- Fund usage: restrictions (no founder salary increases, no related-party transfers)
- Insurance: business interruption insurance required

### Common Negotiation Points

- **Monthly repayment percentage**: investor wants 2.5%+ (faster payback); company wants 1–1.5% (less cash outlay)
- **Repayment cap**: investor wants 2x (lower exposure); company wants 2.5x (longer repayment window)
- **Revenue decline pause**: company wants pause allowed; investor wants company to continue payments (strict terms)
- **Fund usage restrictions**: investor wants tight (no founder draw, no M&A); company wants loose (operational flexibility)

### Red Flags

- **Repayment % too high**: 3%+ monthly (36%+ annual) may be unsustainable if revenue doesn't grow
- **Revenue decline penalties**: lender requires payments even if revenue drops >20% (punitive)
- **Restrictive fund usage**: cannot hire, cannot invest in growth (defeats purpose of RBF)
- **Very low revenue threshold**: RBF investor tries to finance company with <$30K/month (high risk of default)

### Comparison to Venture Debt vs. RBF

| Dimension | Venture Debt | RBF |
|-----------|--------------|-----|
| Debt repayment? | Yes, fixed payment | Percentage of revenue |
| Equity upside (warrants)? | Yes (10–20%) | No |
| Founder retains 100% equity? | Yes | Yes |
| Suitable for early-stage? | Series A+ | $30K+/month revenue |
| Debt covenants? | Yes (revenue floor, DSCR, cash minimum) | Less strict (revenue pause allowed) |
| Time to close? | 30–45 days | 15–30 days |
| Founder-friendly? | Moderate | High |

### Geographic Applicability

- **North America**: Dominant (Clearco, Uncapped, Lighter Capital, Pipe major players)
- **Europe**: Growing (Uncapped UK-based, Wayflyer Ireland-based)
- **GCC/MENA**: Emerging (limited availability)
- **Southeast Asia**: Emerging (very limited; mostly e-commerce seller financing)

---

## 6. Strategic Investment with Commercial Terms

### How It Works

Corporate or strategic investor (larger company, acquirer, customer) invests equity in startup, typically with commercial terms embedded: preferred supplier status, revenue sharing, exclusivity, right of first refusal on future customer deals.

**Key concept**: investment includes both financial interest (equity) and commercial benefit (preferred terms, partnership obligations).

### When It's Appropriate

- Strategic investor identifies startup as potential supplier, partner, or acquisition target
- Startup benefits from: capital, customer relationships, potential downstream revenue, acquirer optionality
- Corporate investor wants: equity upside, preferential commercial terms, potential acquisition path
- Growth stage: typically Series B+ (large enough to be relevant to corporate buyer, but early enough to benefit from capital + partnership)

### Key Terms and Significance

#### Equity Stake Size
- Typical: 5–20% of company
- Example: corporate investor takes 10% stake + $50M Series C

#### Preferred Commercial Terms
- **Exclusivity**: startup cannot work with competitors in specific product vertical or customer segment
  - Example: "Cannot work with other cloud infrastructure providers for data analytics use case"
  - Scope: must be defined (which competitors, which markets, time period)
- **Preferred supplier status**: corporate prioritizes buying from startup vs. other vendors
  - Benefit: guaranteed minimum purchase volume or revenue commitment
  - Example: "Corporate commits to $10M/year minimum purchase from startup for 3 years"
- **Preferred pricing**: startup offers corporate better pricing than other customers
  - Example: 20% volume discount vs. list price for corporate's use
- **Right of first refusal (ROFR)**: startup must offer new product/feature/market to corporate before launching publicly
  - Protection: corporate can match any third-party terms, has right to negotiate first

#### Strategic Investment Terms

#### Board Seat / Representation
- Corporate investor may negotiate 1 board seat or observer seat
- Provides visibility into strategy, product roadmap
- May include decision rights on matters affecting corporate's business

#### Revenue Share / Milestone Payments
- If commercial transaction exceeds thresholds, corporate investor receives additional upside beyond equity
- Example: "If startup reaches $100M ARR, corporate investor receives 5% of incremental revenue above $100M for 3 years"
- Aligns corporate and startup incentives

#### Acquisition Option
- Corporate may negotiate right of first refusal on acquisition
  - Startup cannot sell to third party without offering to corporate first at same terms
- Or exclusive negotiation period: startup must negotiate with corporate before third parties (e.g., 30-day exclusive window)

#### Management Continuity
- Corporate investor typically requires key founders/executives to stay through term
- Non-compete clause: founders cannot work for competitors for 2–3 years post-exit

### Investor Protections (Corporate Perspective)

- **Equity upside**: participate in company growth financially
- **Preferred commercial terms**: guaranteed access to product/service at better pricing
- **Information rights**: board seat or observer provides visibility into strategy, product roadmap
- **ROFR on acquisition**: opportunity to acquire if third party offers purchase
- **Exclusivity**: startup bound to corporate strategically (cannot work with competitors)

### Founder / Company Protections

- **Carve-outs on exclusivity**: startup can negotiate carve-outs (e.g., "exclusivity does not apply to market X, customer Y")
- **Minimum purchase commitments**: corporate commits to purchasing volume (reduces startup's customer concentration risk)
- **Fair pricing**: startup ensures corporate doesn't abuse preferred pricing to starve company of cash
- **Non-controlling equity**: startup retains operational control (corporate board seat is monitor, not control)
- **Defined term**: exclusivity, ROFR, other commercial terms have defined expiration date

### Common Negotiation Points

- **Scope of exclusivity**: startup wants narrow (fewer competitors, specific verticals); corporate wants broad
- **Minimum purchase commitment**: startup wants high (guaranteed revenue); corporate wants low (flexibility)
- **Pricing discount**: startup wants small (protects margins); corporate wants large (more savings)
- **Board seat vs. observer**: startup wants observer (less control); corporate wants board seat (more influence)
- **ROFR scope**: startup wants narrow (easier to sell to third parties); corporate wants broad (opportunity to block acquisition)
- **Carve-outs**: startup wants extensive (operational flexibility); corporate wants minimal (controls startup strategy)

### Red Flags

- **Broad exclusivity**: "Cannot work with any large tech company" locks startup into limited market
- **High minimum purchase commitment** that startup cannot meet: sets up situation where startup fails to honor obligations
- **Unfair pricing discount**: 50%+ discount may make startup unprofitable serving corporate
- **ROFR on acquisition**: corporate can block third-party acquisition indefinitely (reduces exit options)
- **Personal non-compete for founders**: 3+ year non-compete after exit prevents founder from working in industry
- **Acquisition option**: corporate has right to acquire at discount (option pricing unfair to founders)

### Exit Scenarios with Strategic Investment

**Scenario 1: Acquisition by Third Party**
- If third party acquires: strategic investor's equity converts to common (subject to cap table waterfall)
- ROFR triggered: corporate has right to match third-party offer
- Founder non-compete: founders bound by agreement post-exit

**Scenario 2: Acquisition by Corporate Investor**
- Strategic investor exercises acquisition option or invokes ROFR
- Earnout possible: corporate offers base price + earnout contingent on achieving milestones
- Management continuity required: founders typically required to stay 1–3 years

**Scenario 3: Financing Exit (Later Venture Round)**
- Strategic investor's equity dilutes (but pro-rata rights protect ownership %)
- Commercial terms continue through venture round (unless renegotiated)
- Potential conflict: new VC wants autonomy; corporate investor wants continued exclusivity

### Geographic Applicability

- **North America**: Common in strategic corporate venture (Google Ventures, Amazon, Salesforce, etc.)
- **Europe**: Growing (large European companies increasing strategic venture)
- **GCC/MENA**: Emerging (family offices and strategic conglomerates increasing venture participation)
- **Southeast Asia**: Increasing (corporates participating in ecosystem-building)

---

## 7. Milestone-Tranched Investment

### How It Works

Investor commits capital in tranches, with each tranche released upon company achieving predefined milestones (product launch, customer validation, revenue target, team hire, etc.).

**Key concept**: investor capital disbursed in phases; company must achieve targets to unlock next tranche.

### When It's Appropriate

- Early-stage with uncertain product-market fit: investor wants to de-risk investment
- Cash constraints: company doesn't need full capital upfront; investor prefers staged funding
- Alignment building: milestones create accountability between investor and founder
- Conditional go determinations: Path B structure for CONDITIONAL GO determinations

### Key Terms and Significance

#### Tranches and Trigger Milestones
- **Tranche 1** (at close): typically 40–50% of total committed capital
  - Example: $2M Tranche 1 at close
- **Tranche 2** (upon achievement of milestone 1): typically 30–40%
  - Example: $1.5M released upon hitting $500K ARR
- **Tranche 3** (upon achievement of milestone 2): remaining balance
  - Example: $1M released upon hiring VP Sales and closing 3 enterprise customers

#### Milestone Definition
- **Objective**: quantifiable, verifiable milestones (not subjective)
  - Good: "Achieve $500K annual recurring revenue (verified by third-party audit)"
  - Bad: "Achieve product-market fit (subjective)"
- **Achievable**: within 12–18 months, feasible for typical company at that stage
- **Material**: tied to de-risking factors relevant to investor thesis

#### Milestone Examples
- Revenue milestones: $100K ARR, $500K ARR, $2M ARR
- Customer milestones: 10 paying customers, 5 enterprise customers, $50K+ ACV customers
- Product milestones: launch to production, reach specific usage/retention thresholds
- Team milestones: hire VP Sales, hire VP Product, fill out C-suite
- Financing milestones: raise Series A before tranche release date

#### Verification and Governance
- Verification method: defined upfront (third-party audit, board verification, investor site visit)
- Cure period: if milestone not met by target date, company has 30–60 day cure period (renegotiate, achieve milestone, or lose tranche)
- Investor discretion: some terms give investor discretion on whether milestone is "substantially achieved"

### Investor Protections

- **Staged funding**: investor capital at risk only as company de-risks
- **Objective milestones**: verifiable achievements; investor can verify tranche release conditions
- **Governance rights**: investor sits on board, observes milestone achievement directly
- **Hold harmless**: if company fails to achieve milestones, investor can withhold remaining tranches (capital preserved)

### Company Protections

- **Certainty of funding**: tranches committed in advance (investor cannot back out if milestones are met)
- **Reasonable milestones**: founder negotiates that milestones are achievable and realistic
- **Cure period**: if milestone narrowly missed, company has time to achieve before losing tranche
- **Milestone adjustment**: if market conditions change, founder can renegotiate milestone (mutual consent)
- **Interest on delayed tranche**: if investor delays tranche release, company may receive interest on deployment lag

### Common Negotiation Points

- **Milestone achievability**: founder wants achievable (likely to hit); investor wants aggressive (de-risks more)
- **Cure period**: company wants longer (more time to hit); investor wants shorter (faster visibility)
- **Discretionary language**: investor may want "investor's reasonable discretion" on whether milestone achieved (founder wants objective)
- **Failure consequences**: founder wants: extend timeline; investor wants: tranche forfeited or reduced
- **Valuation adjustments**: if later tranches valued differently, how does valuation adjust per tranche? (common point of disagreement)

### Red Flags

- **Excessively aggressive milestones**: investor sets milestones founder likely to miss (sets up failure scenario)
- **Subjective verification**: investor retains discretion on milestone achievement (potential for dispute)
- **Valuation cliff**: later tranches priced significantly lower than first tranche (increases founder dilution)
- **Founder non-compete in failure scenario**: if tranche missed, founder subject to non-compete (punitive)
- **No cure period**: milestone missed = tranche forfeited (overly strict)

### Valuation Adjustment Across Tranches

**Scenario 1: Fixed Valuation Across Tranches**
- $10M Series A at fixed $30M pre-money valuation
- Tranche 1: $5M at $30M pre-money
- Tranche 2: $3M at $30M pre-money (same price)
- Tranche 3: $2M at $30M pre-money (same price)
- Founder benefit: if company performs, ownership dilution same per dollar

**Scenario 2: Milestone-Adjusted Valuation**
- Tranche 1: $5M at $30M pre-money
- Tranche 2: $3M at $35M pre-money (if milestones exceeded, price steps up)
- Tranche 3: $2M at $40M pre-money (further step-up on achievement)
- Founder benefit: outperformance rewarded with less dilution for later tranches
- Investor benefit: downside protected (lower valuation if milestones missed)

### Exit Scenarios with Tranched Investment

**Scenario 1: Early Exit Before All Tranches Released**
- Company acquired for $100M
- Only Tranches 1–2 funded ($8M received)
- Tranche 3 trigger not met before acquisition
- Outcome: investor's preferred stock converts at implied valuation of 2 tranches (founder negotiates to include "deemed valuation" for unfunded tranches)

**Scenario 2: Series A Extension**
- Company needs more capital than initially committed
- Tranche 3 released on milestone achievement
- Company raises Series B shortly after
- Outcome: investor's ownership dilutes further; pro-rata rights determine participation in Series B

---

## 8. Earnout / Contingent Payment Structure

### How It Works

Founder / company receives base purchase price upon exit (M&A or private equity acquisition), plus additional contingent "earnout" payment if company achieves post-acquisition performance milestones (EBITDA, revenue, customer retention, product targets).

**Key concept**: portion of acquisition price is contingent on post-close performance.

### When It's Appropriate

- PE acquisition: private equity wants to de-risk acquisition by tying portion of price to performance
- Founder retention: earnout incentivizes founder to stay post-close and ensure targets are hit
- Financing gaps: if acquirer and seller disagree on valuation, earnout bridges gap
  - Example: founder valued company at $100M, acquirer at $80M; compromise at $80M + $20M earnout over 3 years

### Key Terms and Significance

#### Base Purchase Price
- Upfront payment at close (no contingency)
- Example: $80M base price, paid at close in cash or stock

#### Earnout Targets
- **EBITDA earnout**: if company achieves $10M EBITDA in 2 years post-close, founder receives additional $10M
  - Formula: (Actual EBITDA - Target EBITDA) * X multiplier = earnout payment
  - Example: Target $10M, actual $12M → ($12M - $10M) * 1x = $2M earnout
- **Revenue earnout**: if company achieves $50M revenue by year 3, founder receives earnout
  - Example: Each $1M revenue above target = $500K earnout (capped at $20M)
- **Customer retention earnout**: if customer churn stays below X%, earnout paid
- **Product milestone earnout**: if product achieves specific feature/adoption target, earnout paid

#### Earnout Measurement and Dispute
- Typically measured by acquirer's accountants (audited, third-party verified)
- Dispute mechanism: if founder disagrees with calculation, arbitration clause (pays for mediator/arbitrator)
- Lookback period: typically 2–4 years post-close

#### Escrow / Holdback
- Base price may include escrow (10–20% held back for 12–18 months to cover indemnification claims)
- Example: $80M base price, $10M escrowed for 18 months; if no claims, released to founders
- Earnout funds typically NOT escrowed (separate payment stream)

### Earnout Incentive Problems

- **Acquirer incentive**: acquirer may have incentive to suppress EBITDA or revenue to reduce earnout
  - Example: reduce salaries, cut R&D investment post-close to suppress earnings (harms founders)
- **Founder incentive**: founder wants to maximize earnout (may make decisions not aligned with acquirer's broader strategy)
  - Example: founder may resist restructuring, cost-cutting that acquirer wants post-acquisition
- **Dispute likelihood**: earnout disputes common; founders and acquirers often disagree on measurement

### Earnout Terms to Reduce Disputes

- **Objective measurement**: use audited GAAP earnings (not adjusted EBITDA)
- **Standalone accounting**: measure earnout subsidiary separately (isolate performance)
- **Reps and warranties escrow**: separate from earnout; covers indemnification claims, not earnout
- **Earnout cap**: cap earnout upside (example: earnout capped at 20% of base price)
- **Earnout floor**: minimum threshold (example: no earnout if EBITDA below $5M, even if modest growth)

### Exit Scenarios with Earnout

**Scenario 1: Earnout Targets Met or Exceeded**
- Base price paid at close
- Earnout milestones achieved post-acquisition
- Founder receives full earnout + base price (or retained equity if stock deal)
- Total proceeds: $100M+ (assuming targets hit)

**Scenario 2: Earnout Targets Missed**
- Base price paid at close
- Earnout milestones not achieved
- Founder receives base price only (no earnout)
- Dispute likely: founder may claim acquirer sabotaged results; litigation possible

**Scenario 3: Earnout Partially Achieved**
- Base price paid at close
- Targets partially achieved (e.g., 80% of EBITDA target)
- Earnout partially paid (pro-rata or threshold-based)
- Example: 80% of earnout = $8M (if full earnout was $10M)

### Geographic Applicability

- **North America**: Standard for PE acquisitions, M&A with valuation disagreements
- **Europe**: Similar to North America
- **GCC/MENA**: Emerging (becoming more common in regional M&A)
- **Southeast Asia**: Growing (PE and strategic acquisitions increasingly use earnouts)

---

## Summary: Instrument Comparison Matrix

| Instrument | Founder Dilution | Speed to Close | Governance Burden | Debt Risk | Suitable Stage |
|------------|------------------|-----------------|-------------------|-----------|-------------------|
| SAFE | Minimal | Fast (15–30 days) | None | No | Seed |
| Convertible | Minimal | Moderate (40–60 days) | Minimal | Yes (debt obligation) | Seed |
| Priced Equity | Significant | Moderate (60–120 days) | High (board seat) | No | Series A+ |
| Venture Debt | None | Moderate (30–45 days) | Moderate (covenants) | Yes (senior debt) | Series A+ |
| RBF | None | Fast (15–30 days) | Low | No (revenue-based) | $30K+/month revenue |
| Strategic | Moderate | Moderate (60–120 days) | High (exclusivity) | No | Series B+ |
| Milestone-Tranched | Significant | Slow (90–120 days) | High (milestones) | No | Early-stage |
| Earnout | None (M&A context) | N/A | Moderate (post-close) | Potential (acquirer disputes) | Exit context |

---

## References

- NVCA Model Terms: https://nvca.org/
- Y Combinator SAFE: https://www.ycombinator.com/documents
- Gust: convertible note templates
- Venture Debt Best Practices: SVB, Gold Hill Capital, Horizon Technology Finance
- Corporate Venture: Kauffman Foundation, CVG (Corporate Venture Group)
