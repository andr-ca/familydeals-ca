# Family Deals Canada

Public landing shop + Saturday email list for Canadian parents of kids ~5–10.

- Live repo: https://github.com/andr-ca/familydeals-ca
- Intended Pages URL: https://andr-ca.github.io/familydeals-ca/
- Contact: andrey.dev@gmail.com
- Subscriber ledger: https://docs.google.com/spreadsheets/d/1eTR5ibEORQaQiP8NmOMSNcXYK-ArRVu4TgZqNQzW_wE/edit

## What this is

An editorial shop, not a scrape of RedFlagDeals. The watcher skill at
`rfd-hot-deals-checker` alerts; it does not publish. The public feed we
can turn into a page is RFD’s Atom:

https://forums.redflagdeals.com/feed/forum/9

`data/deals.json` is the curated list. `scripts/refresh_family_deals.py`
writes keyword *candidates* only.

## Analytics

Optional GA4. Set `window.FAMILYDEALS_GA4_MEASUREMENT_ID` in `js/ga4-id.js`
to a `G-...` id. An empty string means no tag is injected. Search Console
URL-prefix is tracked in issue #2.

## Amazon

Apply: https://associates.amazon.ca/signup (sign-in required).
Influencer: https://associates.amazon.ca/influencers.

Prior Canada Associates ID `infoocode09-20` was rejected 2023-09-24 for
missing three qualifying sales. Amazon said reapply is allowed.

## Newsletter

Landing capture is mailto:andrey.dev@gmail.com. Beehiiv Launch is free
with no card; starting the publisher account needs a password that was
not invented in this pass.
