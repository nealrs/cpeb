## Purpose

This script accepts an eventbrite id, organizer's api user key, CP challenge title, and CP challenge URL.

After retrieving event info & attendee contact info, this script sends them an email about how to register & submit on ChallengePost.

**NOTE: This is a proof of concept &mdash; at best.**

## Eventbrite variables

- `ak` - app API key for THIS script
- `uk` - user API key for event organizer
- `eid` - event ID

## Sendgrid variables

- `su` - sendgrid username
- `sp` = sendgrid password
- `o` - organizer [first, last, email] << ideally pulled from CP site
- `u` - event ChallengePost URL << ideally pulled from CP site

## To do

1. Create web interface / scheduler that accepts uk, eid, o, and u parameters.
2. Improve template copy & styling
3. Migrate from Sendgrid to Customer.io if possible.
4. Add logging
5. Profit???

**Copyright 2014 &middot; Neal Shyam**
