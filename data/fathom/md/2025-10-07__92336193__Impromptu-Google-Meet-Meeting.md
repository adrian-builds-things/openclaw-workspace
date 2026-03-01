# Impromptu Google Meet Meeting

## Metadata

- recording_id: 92336193
- created_at: 2025-10-07T15:44:33Z
- recorded_by: Adrian Rinnus
- meeting_url: https://fathom.video/calls/434249700
- speakers: Adrian Rinnus, Luís Braga

## Summary

{"template_name": "General", "markdown_formatted": "## Meeting Purpose\n\n[Implement NFC tag reading functionality for kitchen meal delivery system](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=278.0)\n\n## Key Takeaways\n\n  - [Successfully set up local development environment accessible from mobile devices on same network](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=4148.0)\n  - [Created initial UI for manual order lookup by internal user ID](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=1021.0)\n  - [Attempted to implement NFC reading but encountered device compatibility issues](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=7893.0)\n  - [Discussed potential fallback options like background Android service if Web NFC API not widely supported](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=7774.0)\n\n## Topics\n\n### Local Development Setup\n\n  - [Configured Next.js and Superbase to allow connections from local network IP addresses](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=4148.0)\n  - [Updated middleware, client config, and next.config.js to enable access from mobile devices](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=6783.0)\n  - [Resolved CORS and authentication issues to get login working on tablet](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=6783.0)\n\n### Manual Order Lookup UI\n\n  - [Created new \"Delivery\" page in kitchen dashboard](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=524.0)\n  - [Implemented form to lookup orders by internal user ID](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=1021.0)\n  - [Fetches and displays order details grouped by day part (lunch/dinner)](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=3642.0)\n  - [Uses server action to query custom Postgres view for efficient data retrieval](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=2079.0)\n\n### NFC Implementation Attempts\n\n  - [Researched Web NFC API usage and sample implementations](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=5806.0)\n  - [Created initial NFC reader React component](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=7095.0)\n  - [Encountered \"NFC not supported\" errors on test devices](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=7893.0)\n  - [Discussed potential issues with browser/device compatibility](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=7893.0)\n\n### Database Modifications\n\n  - [Created new Postgres view `v_user_daily_orders` to efficiently query order data](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=2079.0)\n  - [Added `picked_up_at` timestamp to `order_line` table to track delivery status](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=5466.0)\n\n### Future Considerations\n\n  - [Explore fallback options like Android background service for NFC reading](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=7774.0)\n  - [Implement \"mark as picked up\" functionality](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=5466.0)\n  - [Refine UI to show orders in card layout grouped by meal type](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=4311.0)\n  - [Add NFC-based login option with proper security measures](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=6563.0)\n\n## Next Steps\n\n  - [Test on additional Android devices to verify NFC support](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=8601.0)\n  - [Research Web NFC API browser/device compatibility](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=7893.0)\n  - [Implement fallback manual entry option if NFC not widely supported](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=248.0)\n  - [Refine order display UI and add pickup marking functionality](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=4311.0)\n  - [Consider separate NFC feature implementation for reusability](https://fathom.video/share/vcEEpxXtHEppdzNaaejpya8eabeU4esg?tab=summary&timestamp=7117.0)\n"}

## Transcript

**Adrian Rinnus** (00:00:00): I was just checking the home page, the sample project you sent, and it's working really cool.
**Adrian Rinnus** (00:00:07): So what the ?
**Adrian Rinnus** (00:00:08): It's freaking easy.
**Luís Braga** (00:00:10): I think the code is not that hard to do.
**Luís Braga** (00:00:14): I was trying to run it locally, but I cannot even start the dev servers.
**Adrian Rinnus** (00:00:20): Okay, I was trying the URL that they had there in place.
**Luís Braga** (00:00:26): So what I was thinking was just run by clause, start creating the page.
**Luís Braga** (00:00:32): And just one more thing.
**Adrian Rinnus** (00:00:34): I was thinking about what do we need.
**Adrian Rinnus** (00:00:36): So what are the requirements?
**Adrian Rinnus** (00:00:38): not just reading the NFC tag and then doing .
**Adrian Rinnus** (00:00:41): We also need an interface for them to write the NFC tags.
**Luís Braga** (00:00:46): To write?
**Luís Braga** (00:00:47): Yes.
**Luís Braga** (00:00:47): I would propose them just to install something on their...
**Luís Braga** (00:00:52): This could be the...
**Adrian Rinnus** (00:00:53): Yeah, you're right.
**Adrian Rinnus** (00:00:54): It's over-engineering already, but it would be even cooler if they have the employees because they have the employees.
**Adrian Rinnus** (00:01:00): And then they get some batch.
**Luís Braga** (00:01:02): And hey, hang on.
**Luís Braga** (00:01:05): I'm all log-free.
**Luís Braga** (00:01:06): Sorry.
**Luís Braga** (00:01:07): What if the API really supports writing?
**Adrian Rinnus** (00:01:13): It does.
**Adrian Rinnus** (00:01:14): It does.
**Adrian Rinnus** (00:01:15): Wait.
**Luís Braga** (00:01:16): Let's just go to the user profile and have a button there to write a tag.
**Luís Braga** (00:01:20): Cool.
**Luís Braga** (00:01:20): OK.
**Luís Braga** (00:01:21): And wait.
**Adrian Rinnus** (00:01:24): Scan.
**Adrian Rinnus** (00:01:25): So I was writing test on it, you see.
**Adrian Rinnus** (00:01:27): And now we can also write, and write, wait, Luís.
**Adrian Rinnus** (00:01:35): You see?
**Adrian Rinnus** (00:01:36): We are writing Luís.
**Adrian Rinnus** (00:01:38): OK.
**Adrian Rinnus** (00:01:38): Save.
**Adrian Rinnus** (00:01:40): OK.
**Adrian Rinnus** (00:01:41): And now, scan.
**Adrian Rinnus** (00:01:45): OK.
**Luís Braga** (00:01:47): Man.
**Luís Braga** (00:01:50): So that's even cooler.
**Adrian Rinnus** (00:01:53): Well, yeah, what I said, I will use Fathom now to record the meeting.
**Adrian Rinnus** (00:01:59): doesn't new companion.
**Adrian Rinnus** (00:01:59): You it's it's
**Adrian Rinnus** (00:02:00): I want to create an article out of the thing, so how to write NFC text with super bass, blah, blah, so this is a cool one, and it should be really easy because it's just recording what we say, what we do, so it should be an easy thing to do.
**Luís Braga** (00:02:17): Would it be okay for you if I share my screen and I implement from the user?
**Luís Braga** (00:02:24): So what do you say we start from the user profile page writing, adding a button there to write to NFC?
**Adrian Rinnus** (00:02:34): Nope, let's do it like that.
**Adrian Rinnus** (00:02:35): Let's focus on the real pain point is the scanning, the reading of the NFC tag, and as you said, they can also use something else just to get the most important  done, which is reading, get the order and show it on the display.
**Adrian Rinnus** (00:02:49): Okay, so just reading, right?
**Adrian Rinnus** (00:02:51): Yeah, in the first moment, and then we can always think about getting the, also the writing.
**Luís Braga** (00:03:07): I don't know what the hell I have it here, but so I guess release branch?
**Luís Braga** (00:03:14): Yes, should be the latest and greatest.
**Adrian Rinnus** (00:03:17): 230 commits behind.
**Adrian Rinnus** (00:03:19): I'm sorry.
**Luís Braga** (00:03:22): Late for the party.
**Luís Braga** (00:03:25): So from the release, what do I have there?
**Luís Braga** (00:03:27): Playwrights, discard.
**Luís Braga** (00:03:28): So from here, I create a new feature branch, right?
**Luís Braga** (00:03:34): Yes, new feature branch, right?
**Luís Braga** (00:03:37): Feeds, NFC, NFC, NFC what?
**Adrian Rinnus** (00:03:49): No, that's not NFC kitchen, or let's call it feature a kitchen NFC support or whatever, something like that.
**Adrian Rinnus** (00:03:57): It doesn't Thanks.
**Adrian Rinnus** (00:03:59): Thank you.
**Luís Braga** (00:04:00): Check in with NFC?
**Luís Braga** (00:04:02): Yeah.
**Adrian Rinnus** (00:04:03): Okay.
**Luís Braga** (00:04:04): Check in NFC support.
**Luís Braga** (00:04:07): Yeah.
**Luís Braga** (00:04:08): Well, actually, do you want to focus on this or include the input first?
**Luís Braga** (00:04:18): What do you mean?
**Luís Braga** (00:04:21): Because let's not forget that the very basic scenario, and this will be a fallback every single time, is really just inputting the user internal ID and fetch the thing.
**Adrian Rinnus** (00:04:34): Yeah.
**Adrian Rinnus** (00:04:34): Okay.
**Adrian Rinnus** (00:04:35): Then let's do it like that.
**Adrian Rinnus** (00:04:38): Let's start with the very basic stuff is get the order and display to the people in the kitchen.
**Adrian Rinnus** (00:04:46): And this would be in the very first moment, enter the ID, get the thing, and then we can extend it by putting in NFC to read it.
**Adrian Rinnus** (00:04:53): And then we can put in a QR code, whatever.
**Adrian Rinnus** (00:04:55): So let's handle the delivery.
**Adrian Rinnus** (00:04:59): I try and
**Adrian Rinnus** (00:05:00): mode, more or less, first, and then we add the NFC data in the second step.
**Adrian Rinnus** (00:05:06): So checking, checking, how could we use it, name it, feature, kitchen delivery mode.
**Luís Braga** (00:05:16): Kitchen delivery page, no?
**Adrian Rinnus** (00:05:21): Yeah.
**Adrian Rinnus** (00:05:22): Yeah.
**Luís Braga** (00:05:24): Boom.
**Luís Braga** (00:05:26): Alrighty.
**Luís Braga** (00:05:27): So is there something I should do right away?
**Luís Braga** (00:05:32): As in migrations and whatnot?
**Adrian Rinnus** (00:05:36): No, I think migration, let's brainstorm first what we should do.
**Adrian Rinnus** (00:05:42): I think we should put something in the kitchen dashboard.
**Adrian Rinnus** (00:05:48): So this is in...
**Luís Braga** (00:05:50): What's the package management again?
**Luís Braga** (00:05:53): Ban.
**Adrian Rinnus** (00:05:54): Ban.
**Adrian Rinnus** (00:05:54): Ban.
**Luís Braga** (00:05:55): Should I run it, maybe?
**Luís Braga** (00:05:56): You can, but BanE, right?
**Adrian Rinnus** (00:05:58): And then also get Superbase up and...
**Luís Braga** (00:06:01): Superbase, I believe, I might have it running already.
**Luís Braga** (00:06:08): BiClub, yes, it's running, I guess.
**Luís Braga** (00:06:13): Does it look right?
**Luís Braga** (00:06:14): I'm sorry.
**Adrian Rinnus** (00:06:16): Yeah, I think so.
**Adrian Rinnus** (00:06:17): Then do a Superbase db reset to get the latest migrations.
**Adrian Rinnus** (00:06:23): No, sorry, db, not, no, blank.
**Adrian Rinnus** (00:06:29): Yeah.
**Adrian Rinnus** (00:06:36): I did not manage to fix my thing, for sure.
**Adrian Rinnus** (00:06:39): .
**Luís Braga** (00:06:49): Restarting containers.
**Luís Braga** (00:06:56): And then Bandev.
**Luís Braga** (00:07:00): Right, just a second, yeah, exactly.
**Luís Braga** (00:07:16): So login, I have no idea if localhost 54323, I guess authentication, oh, there's the default admin, right?
**Adrian Rinnus** (00:07:36): I'm sorry, just a second, for a second on the other thing to finish that one while we do it here.
**Adrian Rinnus** (00:07:48): This one, no, this one.
**Adrian Rinnus** (00:07:54): No, I'm back.
**Adrian Rinnus** (00:07:56): Yes, you can use the test, test, test, test,
**Adrian Rinnus** (00:08:00): Test, test, test, test, yeah.
**Luís Braga** (00:08:08): All righty.
**Luís Braga** (00:08:11): So administration, daily operations, menu management.
**Adrian Rinnus** (00:08:15): Wait.
**Adrian Rinnus** (00:08:16): If you go back to the dashboard, you have the chance in the top right corner to switch between the kitchen and admin dashboard.
**Adrian Rinnus** (00:08:24): So I would propose to put it on the kitchen dashboard, in my opinion.
**Luís Braga** (00:08:33): So this would be an actual dashboard, right?
**Adrian Rinnus** (00:08:37): Yeah.
**Adrian Rinnus** (00:08:37): This is the dashboard that the chefs do see.
**Adrian Rinnus** (00:08:40): So if someone is registered as a chef, they see that one.
**Luís Braga** (00:08:44): But what do you say we have a dedicated page for?
**Luís Braga** (00:08:49): We can also do that, yeah, sure.
**Adrian Rinnus** (00:08:52): Okay, then let's create a dedicated page.
**Luís Braga** (00:08:55): I'm not sure the dashboard should really be about .
**Luís Braga** (00:08:59): I'm .
**Luís Braga** (00:09:00): So letís create a new page for it.
**Adrian Rinnus** (00:09:03): So then, how do we start?
**Adrian Rinnus** (00:09:04): We go to the sidebar.
**Adrian Rinnus** (00:09:08): I donít know, itís in components probably.
**Adrian Rinnus** (00:09:10): Or search for sidebar, app sidebar, app minus sidebar.tsx, I think, yeah, that one.
**Adrian Rinnus** (00:09:19): Is it the same?
**Luís Braga** (00:09:20): Yeah.
**Luís Braga** (00:09:21): No.
**Luís Braga** (00:09:23): App sidebar.
**Luís Braga** (00:09:26): All righty.
**Adrian Rinnus** (00:09:27): And then I think I need to switch places to have a bigger screen.
**Adrian Rinnus** (00:09:33): Just a second.
**Adrian Rinnus** (00:09:34): Or do you want reduce mine?
**Adrian Rinnus** (00:09:36): No, no, no, itís fine.
**Adrian Rinnus** (00:09:37): Iím walking over.
**Adrian Rinnus** (00:09:40): All right.
**Luís Braga** (00:09:41): So core functionality, always usable first, daily operations, I guess this is needs.
**Luís Braga** (00:09:48): And so menu management, what do we call these?
**Luís Braga** (00:09:56): Delivery.
**Luís Braga** (00:09:57): All right.
**Luís Braga** (00:09:59): next
**Luís Braga** (00:10:00): I guess I'll just do delivery for now.
**Adrian Rinnus** (00:10:18): So, are you still here?
**Adrian Rinnus** (00:10:20): Yep.
**Luís Braga** (00:10:21): Okay.
**Luís Braga** (00:10:22): Let me see.
**Adrian Rinnus** (00:10:23): see.
**Luís Braga** (00:10:27): Title Items.
**Luís Braga** (00:10:37): Ah, because this is navigation groups, do I really need a group?
**Luís Braga** (00:10:48): Groupies for?
**Adrian Rinnus** (00:10:49): Wait, wait, wait, I will try to explain you.
**Adrian Rinnus** (00:10:55): That's not sure.
**Adrian Rinnus** (00:10:58): Navigation here.
**Adrian Rinnus** (00:11:01): Yes, exactly.
**Adrian Rinnus** (00:11:04): So what is the question?
**Adrian Rinnus** (00:11:05): The group overview?
**Adrian Rinnus** (00:11:07): Yes, we have groups.
**Luís Braga** (00:11:08): How do we add a single, like first level thingy?
**Luís Braga** (00:11:17): On the sidebar, you mean?
**Adrian Rinnus** (00:11:20): Yes.
**Adrian Rinnus** (00:11:20): it should be like menu selection.
**Adrian Rinnus** (00:11:23): Take the item, copy menu selection, and make a new one here.
**Adrian Rinnus** (00:11:28): Down below?
**Adrian Rinnus** (00:11:30): Let's put it somewhere, and then, no, I think below the menu management thing, for example.
**Adrian Rinnus** (00:11:36): Because I think it's a little bit too, yeah, exactly.
**Adrian Rinnus** (00:11:40): And then...
**Adrian Rinnus** (00:11:41): Okay, that was my point, because this way...
**Luís Braga** (00:11:44): Ah.
**Adrian Rinnus** (00:11:45): Yeah.
**Adrian Rinnus** (00:11:46): No, what is it?
**Adrian Rinnus** (00:11:46): The sub-items they are getting.
**Adrian Rinnus** (00:11:49): Ah, the operations.
**Adrian Rinnus** (00:11:50): Okay, got it.
**Adrian Rinnus** (00:11:51): It's the group.
**Luís Braga** (00:11:52): All right, all right, got it.
**Luís Braga** (00:11:54): So, second, I need my good mouse.
**Adrian Rinnus** (00:11:59): Yeah, no worries.
**Luís Braga** (00:12:00): So this would be delivery, delivery, all right.
**Luís Braga** (00:12:30): All righty, all righty, ends, delivery, ends, ends, whatever, ends helping, or yeah, Fathom something.
**Adrian Rinnus** (00:12:53): righty.
**Adrian Rinnus** (00:12:54): Okay.
**Adrian Rinnus** (00:12:54): righty.
**Luís Braga** (00:12:57): All righty.
**Luís Braga** (00:12:58): righty.
**Luís Braga** (00:13:00): How do I deal with this?
**Adrian Rinnus** (00:13:02): is, yeah, so this is, we have to go to the en.json and pt.json and add it there.
**Adrian Rinnus** (00:13:12): We have to check the search for menu management or menu selection, yeah, exactly.
**Adrian Rinnus** (00:13:19): And then we have to add the new one, which is menu delivery or delivery, right.
**Adrian Rinnus** (00:13:27): Just call it delivery for now and that's fine.
**Adrian Rinnus** (00:13:30): And also add it to the pt.json.
**Luís Braga** (00:13:38): And I guess there's five results anyway.
**Adrian Rinnus** (00:13:47): but this is enough, but this is fine.
**Luís Braga** (00:13:49): Okay, so this would be entregasch.
**Luís Braga** (00:13:55): Entregasch, yeah, sounds good.
**Luís Braga** (00:13:56): And now also the roles, yeah.
**Adrian Rinnus** (00:14:00): Exactly, you already managed the roads in that sense, and the Ahrefs would be...
**Adrian Rinnus** (00:14:04): Falking up, yep, delivery.
**Luís Braga** (00:14:07): Kitchen and admin.
**Luís Braga** (00:14:09): Yeah, exactly.
**Adrian Rinnus** (00:14:11): Righty.
**Adrian Rinnus** (00:14:12): So then we need to create a new page after that.
**Adrian Rinnus** (00:14:16): Delivery, right?
**Adrian Rinnus** (00:14:17): Nice.
**Luís Braga** (00:14:19): Okay, sidebar is done, but let's leave it there.
**Luís Braga** (00:14:22): Do a commit first, then this is already in place.
**Adrian Rinnus** (00:14:28): Remember the conventional comet?
**Luís Braga** (00:14:32): Atomic comets?
**Adrian Rinnus** (00:14:33): No, conventional, so means feature, feed, F-E-A-T, no, then the bracket to know what it is, navbar, or navigation, app navigation, no, the round brackets.
**Adrian Rinnus** (00:14:48): The what?
**Luís Braga** (00:14:49): The round, the common, the eight times, yes.
**Adrian Rinnus** (00:14:53): And I think without a blank in between.
**Adrian Rinnus** (00:14:57): And then call it app sidebar.
**Adrian Rinnus** (00:14:59): time.
**Adrian Rinnus** (00:15:02): Yeah, now the colon and then add delivery, that's delivery, yeah, yeah, that's it, John.
**Luís Braga** (00:15:17): Ah, this, so there is a linting thing which is not good?
**Adrian Rinnus** (00:15:24): I'm not sure.
**Adrian Rinnus** (00:15:26): Ah, or is it not written on your side?
**Adrian Rinnus** (00:15:30): No, I think it's something with the GUI.
**Luís Braga** (00:15:33): Ah, okay.
**Luís Braga** (00:15:35): I've seen this before, something with the GUI.
**Luís Braga** (00:15:38): Okay.
**Adrian Rinnus** (00:15:42): Then let's close the sidebar and create the page for it.
**Luís Braga** (00:15:47): So, components, not components.
**Adrian Rinnus** (00:15:51): The app, app, Exactly, now we are in the kitchen, yes.
**Adrian Rinnus** (00:15:57): And then we do here a delivery.
**Adrian Rinnus** (00:15:59): very much.
**Adrian Rinnus** (00:16:00): Thank
**Luís Braga** (00:16:00): Delivery, and I guess with the index or page, I mean, page TSX, and now do just the test page, yeah, and the delivery page with page one,  you, classic, but just fix it because it's the liver page, it's, yeah, but I have my OCD, delivery, delivery, yes, okay, you know, let's see in the pros, and I want to do something, where's my there, let's put it there, and the browser here, not this browser, so get the  away, let me just, here we go, delivery, we have it, awesome, okay, we're done, bye.
**Adrian Rinnus** (00:17:01): All right, so now we need a fancy UI to show the delivery for the user.
**Luís Braga** (00:17:10): Yeah, so boom, and let's do a fancy input.
**Luís Braga** (00:17:17): We have something.
**Luís Braga** (00:17:19): Yes, we do.
**Adrian Rinnus** (00:17:21): Oh, they also have a new component there, which is called input group.
**Adrian Rinnus** (00:17:26): I have seen that one yesterday.
**Adrian Rinnus** (00:17:29): Shade CM, yes.
**Adrian Rinnus** (00:17:35): But we have to edit because it's not yet there in that case.
**Adrian Rinnus** (00:17:38): Input group, so they have now display additional information or action to an input or text area.
**Adrian Rinnus** (00:17:45): can add, ah, okay.
**Adrian Rinnus** (00:17:47): But this is not, yeah, it could be interesting.
**Adrian Rinnus** (00:17:50): If you search for it.
**Luís Braga** (00:17:55): Yeah, without, yeah.
**Adrian Rinnus** (00:17:58): Search for input group, for instance.
**Adrian Rinnus** (00:18:00): For example, you see you can add now that results and  to the inputs, thatís cool, and they also do have button groups now and empty, empty page, what is field, combines, labels, controls and help text to compose accessible form, oh thatís also cool, awesome, oh this is cool, okay, and what else, item, basic item, okay, keyboard, okay, spinner is updated, okay, yeah, these are the important, okay, anyways.
**Luís Braga** (00:18:44): Alright, so we have the delivery page, we have, letís go, letís go, letís go raw, I donít know, internal user id, letís set up button, we donít have to make it fancy right away, right?
**Adrian Rinnus** (00:18:56): Yeah, just get it, and, uh, send, or.
**Adrian Rinnus** (00:19:01): Read, read, read order, whatever.
**Luís Braga** (00:19:04): Button, and I guess read order, and what am I doing, a fork, oh, I have so many things, what's this one, day trip, right, what else do have there, let me just close this sheet, alright, read order, we got it.
**Luís Braga** (00:19:29): Yes, but at least I'm gonna do, I guess we have a container somewhere, yes, yeah, but I think I'm usually not using it, but yeah, you can check it, if there is something, container, no, I don't think so, that there is, how do I handle it usually, I don't know, what are we using for styles, is it style compliance, tailwind, tailwind, alright, so, let's see.
**Adrian Rinnus** (00:19:59): It's, it's, sure, it's the,
**Adrian Rinnus** (00:20:00): The class name, and then we have a container there.
**Adrian Rinnus** (00:20:03): You can use that one for now.
**Luís Braga** (00:20:05): Well, is there really a container?
**Luís Braga** (00:20:07): Okay, cool.
**Luís Braga** (00:20:08): So I guess you will...
**Adrian Rinnus** (00:20:10): Let's see.
**Adrian Rinnus** (00:20:11): I don't have an idea what it is doing.
**Luís Braga** (00:20:15): Right now, really?
**Luís Braga** (00:20:17): Oh, it's centering.
**Luís Braga** (00:20:18): Yeah, for sure.
**Adrian Rinnus** (00:20:22): Well, so...
**Luís Braga** (00:20:24): And maybe max with...
**Luís Braga** (00:20:27): Oh, it doesn't matter.
**Adrian Rinnus** (00:20:28): All right.
**Adrian Rinnus** (00:20:29): Wait.
**Adrian Rinnus** (00:20:30): So just check, for example, the kitchen dashboard page, how we handle it there.
**Adrian Rinnus** (00:20:35): have no idea how it's done.
**Adrian Rinnus** (00:20:36): I know why I'm complicating.
**Luís Braga** (00:20:38): We can totally go like this.
**Luís Braga** (00:20:41): Close this.
**Luís Braga** (00:20:43): And you said what?
**Luís Braga** (00:20:44): Which one?
**Luís Braga** (00:20:44): For example, the kitchen dashboard.
**Adrian Rinnus** (00:20:47): What have I...
**Adrian Rinnus** (00:20:48): Kitchen dashboards.
**Adrian Rinnus** (00:20:50): So how do they do it here?
**Luís Braga** (00:20:53): Class names space Y.
**Luís Braga** (00:20:57): Canceled...
**Luís Braga** (00:20:58): Return space Y.
**Luís Braga** (00:21:00): And said...
**Luís Braga** (00:21:02): Flex, a lot of flex, I don't see, ah, it could also be on the page, if you check the page for the kitchen dashboard.
**Luís Braga** (00:21:14): Help me out.
**Adrian Rinnus** (00:21:16): If you scroll up, higher, and here, for example, it doesn't know which one.
**Adrian Rinnus** (00:21:24): So kitchen dashboard, yes, and then here the page, how do we do it here.
**Adrian Rinnus** (00:21:29): Return there.
**Adrian Rinnus** (00:21:30): Also space, justify between item center.
**Adrian Rinnus** (00:21:34): Just layouts, well, it doesn't matter.
**Luís Braga** (00:21:38): Yeah, that's also something we can do later on.
**Adrian Rinnus** (00:21:41): Flex, item center, justify center, what the , go on.
**Luís Braga** (00:21:47): But this is row, this, okay, how do I do column, flex column, direction column?
**Luís Braga** (00:21:52): It's minus call, C-O-L.
**Adrian Rinnus** (00:21:55): Ah, cool, okay, cool.
**Luís Braga** (00:21:57): There, all right.
**Luís Braga** (00:21:59): That's it.
**Adrian Rinnus** (00:22:00): Okay.
**Adrian Rinnus** (00:22:00): Now we should have something to display the thing below, right?
**Adrian Rinnus** (00:22:06): As soon as the order was read.
**Luís Braga** (00:22:08): It's true, let's do it already.
**Luís Braga** (00:22:10): So, I would, let's do another div for now, which can as well be flex call gap.
**Luís Braga** (00:22:27): Do it for me, come on.
**Luís Braga** (00:22:30): The lazy AI  thing,  fucker,  fucker.
**Luís Braga** (00:22:37): Man, I miss this.
**Luís Braga** (00:22:40): Maybe, maybe it'd be boring for you.
**Luís Braga** (00:22:43): No, it's fine.
**Adrian Rinnus** (00:22:44): Do you know when I wrote the last code, it's, it feels like infinity.
**Adrian Rinnus** (00:22:51): I have not written one component by myself in the whole project.
**Adrian Rinnus** (00:22:55): You know, this is, it's actually fun to see it like that again.
**Adrian Rinnus** (00:22:59): All right.
**Adrian Rinnus** (00:22:59): This is a.
**Luís Braga** (00:23:00): A server component, right?
**Adrian Rinnus** (00:23:05): Yes, we can do it as a server component, but in that way it is already a server component because it's not used client, that's fine.
**Adrian Rinnus** (00:23:13): All right, cool.
**Luís Braga** (00:23:13): All right.
**Luís Braga** (00:23:14): But wait, so this will eventually be, or at least part of it will be a client component, right?
**Adrian Rinnus** (00:23:24): I think we need a client component to read.
**Adrian Rinnus** (00:23:28): No, not at all.
**Adrian Rinnus** (00:23:31): No?
**Adrian Rinnus** (00:23:31): Because we just do a server action which is triggered on read order and then it should do it in the background and...
**Adrian Rinnus** (00:23:39): Ah, so can you read the same page?
**Luís Braga** (00:23:42): So I guess, let's say one, two, three, and I do read, it will be query param?
**Adrian Rinnus** (00:23:48): No, we don't even need that because we just use a server action and send the one, three to the server action and the server action should trigger it, in my opinion.
**Adrian Rinnus** (00:23:57): All right, tell me about it.
**Luís Braga** (00:23:58): All right, thank you.
**Luís Braga** (00:23:59): you you and Thank You
**Adrian Rinnus** (00:24:00): Okay, you need to guide me then server action let's let's let's build the UI first and so we need what do we need we need the actual date.
**Luís Braga** (00:24:11): Yeah, we will get we will I guess the server action can just infer current day today.
**Luís Braga** (00:24:21): And the results will be I don't actually know what's the shape of the but it's going to be.
**Adrian Rinnus** (00:24:28): Once you know what I also have to check for a second because I'm a little bit lost with the the  which is happening right now.
**Adrian Rinnus** (00:24:37): And the code.
**Adrian Rinnus** (00:24:41): Let me close this.
**Luís Braga** (00:24:43): What's the actual entity meal orders, I suppose.
**Luís Braga** (00:24:48): Yeah.
**Luís Braga** (00:24:49): I see the entities or something like that.
**Adrian Rinnus** (00:24:53): You mean the yeah, they are in the features also as types and it's if you go in the features folder.
**Adrian Rinnus** (00:25:03): And now, for example, check the, I don't know, meals, I would create a new entity because it's a different one.
**Adrian Rinnus** (00:25:13): We should split the, in my opinion, it's a own domain.
**Adrian Rinnus** (00:25:18): So create the types for it.
**Luís Braga** (00:25:22): Okay, so new feature, you mean?
**Adrian Rinnus** (00:25:26): Yes, I would call, build a new feature for it, and also create the types in there for it, as well as the server actions and .
**Adrian Rinnus** (00:25:34): One second, I need to get something to drink.
**Adrian Rinnus** (00:25:37): Yep.
**Adrian Rinnus** (00:25:54): All right.
**Luís Braga** (00:25:58): I was just thinking we're gonna need as well.
**Luís Braga** (00:26:00): week.
**Luís Braga** (00:26:00): And
**Luís Braga** (00:26:06): That means to reset, class name, flex, get four, reset, and button, button, this, is there variants?
**Luís Braga** (00:26:32): Variants, I guess.
**Adrian Rinnus** (00:26:36): Melly or ghosts?
**Adrian Rinnus** (00:26:38): Okay, yeah, okay.
**Luís Braga** (00:26:42): All righty, reset, use the results, so hr, no.
**Luís Braga** (00:26:55): Well, Gap, where else?
**Luís Braga** (00:26:59): Gap.
**Adrian Rinnus** (00:27:02): all right good so resets all right okay uh so then let's let's sorry new feature yes i would say new feature and then we also put the the whole page in the feature you know that the content of the page at least well so what do call it engine delivery or delivery mode i don't know delivery delivery meal delivery is it delivery meal yeah good wait no delivery i it's well if distribution food distribution in that sense ah yeah because you're you're looking for a like more generic yeah general distribution meal distribution that's meal
**Luís Braga** (00:28:06): Yeah, that's fine for now.
**Adrian Rinnus** (00:28:08): So, and then?
**Adrian Rinnus** (00:28:09): Well, this, I don't know, distribution sounds a bit too much.
**Adrian Rinnus** (00:28:14): Yeah, yeah, yeah.
**Adrian Rinnus** (00:28:16): It is the distribution in that sense.
**Adrian Rinnus** (00:28:18): So we put in the new folder with the server actions for now, action, and then let's do one which is called get order by user ID or something like that.
**Luís Braga** (00:28:41): Is it order?
**Adrian Rinnus** (00:28:43): Yeah.
**Adrian Rinnus** (00:28:45): By user ID?
**Luís Braga** (00:28:48): Yeah.
**Luís Braga** (00:28:51): Or would it be internal ID?
**Luís Braga** (00:28:53): I have no idea.
**Adrian Rinnus** (00:28:54): Yeah, let's call it internal user ID.
**Adrian Rinnus** (00:28:56): Okay.
**Adrian Rinnus** (00:28:56): Yeah.
**Luís Braga** (00:28:58): Internal user ID.
**Luís Braga** (00:28:59): you.
**Luís Braga** (00:29:00): P6, yes.
**Adrian Rinnus** (00:29:03): RTS should also be fine, yeah.
**Adrian Rinnus** (00:29:05): And then we need a use server on top of it.
**Luís Braga** (00:29:11): Use server?
**Luís Braga** (00:29:13): To import?
**Luís Braga** (00:29:13): Yes.
**Adrian Rinnus** (00:29:14): No, not import, just the...
**Adrian Rinnus** (00:29:17): How is it called?
**Adrian Rinnus** (00:29:21): I send it to you.
**Adrian Rinnus** (00:29:22): I check it.
**Adrian Rinnus** (00:29:23): Yeah, got it.
**Adrian Rinnus** (00:29:25): Okay, and then...
**Luís Braga** (00:29:27): What's directive?
**Luís Braga** (00:29:28): Directive.
**Adrian Rinnus** (00:29:30): Nothing.
**Adrian Rinnus** (00:29:31): Okay, that's a directive, yeah, exactly.
**Adrian Rinnus** (00:29:34): So then they know it's a server action.
**Adrian Rinnus** (00:29:38): And now...
**Adrian Rinnus** (00:29:39): And then I can export...
**Adrian Rinnus** (00:29:42): Async function, just for example, yeah, exactly.
**Adrian Rinnus** (00:29:46): Take that one and we...
**Luís Braga** (00:29:48): And this would be this one, blah, blah, blah.
**Adrian Rinnus** (00:29:52): And we get the user ID and the date, probably the date is even necessary because we can...
**Adrian Rinnus** (00:29:58): get it also here because it's too...
**Adrian Rinnus** (00:30:00): Okay, we're going to return something.
**Luís Braga** (00:30:08): We don't know yet.
**Luís Braga** (00:30:10): Should I do the types here?
**Luís Braga** (00:30:13): You can do it here and we can still move it.
**Adrian Rinnus** (00:30:16): Oh, create a types file, come on.
**Adrian Rinnus** (00:30:19): I know for that, the props is fine.
**Adrian Rinnus** (00:30:21): The props is fine for me.
**Luís Braga** (00:30:24): Yeah, so this would be type, internal ID.
**Luís Braga** (00:30:34): How is this again?
**Luís Braga** (00:30:36): What's the  syntax?
**Adrian Rinnus** (00:30:38): You have to put it in the curly brackets.
**Adrian Rinnus** (00:30:43): Oh, yeah.
**Adrian Rinnus** (00:30:44): Yeah, yeah.
**Luís Braga** (00:30:45): And man, is it like so?
**Adrian Rinnus** (00:30:56): I'm having a brain fart.
**Luís Braga** (00:30:58): Me too.
**Adrian Rinnus** (00:30:59): Don't ask me.
**Adrian Rinnus** (00:31:00): I have not...
**Adrian Rinnus** (00:31:00): Written code since ages.
**Adrian Rinnus** (00:31:02): And the old user ID.
**Luís Braga** (00:31:04): No, it's not like that.
**Luís Braga** (00:31:05): So this would be, this would be normally.
**Adrian Rinnus** (00:31:08): I, this curly brackets, then the colon.
**Adrian Rinnus** (00:31:12): Did this, this is the return?
**Luís Braga** (00:31:15): Exactly.
**Adrian Rinnus** (00:31:15): But in the, in the, in the round brackets, no curly brackets.
**Adrian Rinnus** (00:31:19): brace it.
**Adrian Rinnus** (00:31:19): Yeah.
**Luís Braga** (00:31:20): Like so, right?
**Luís Braga** (00:31:21): Yeah, exactly.
**Adrian Rinnus** (00:31:22): Yeah.
**Adrian Rinnus** (00:31:23): Damn it.
**Adrian Rinnus** (00:31:24): Look at us.
**Adrian Rinnus** (00:31:26): What the .
**Adrian Rinnus** (00:31:27): Okay.
**Adrian Rinnus** (00:31:28): Okay.
**Adrian Rinnus** (00:31:28): Now we have to get a super base thing.
**Adrian Rinnus** (00:31:31): Can you go back to the other ad serve action?
**Adrian Rinnus** (00:31:33): It's create SSR, blah, blah, blah.
**Adrian Rinnus** (00:31:36): What's that again?
**Adrian Rinnus** (00:31:37): Yeah.
**Adrian Rinnus** (00:31:37): Go there.
**Adrian Rinnus** (00:31:38): Then we see it more or less.
**Adrian Rinnus** (00:31:39): create SSR client.
**Adrian Rinnus** (00:31:41): This is what we need.
**Adrian Rinnus** (00:31:42): Yes.
**Luís Braga** (00:31:42): I'll put it there as a reference.
**Luís Braga** (00:31:45): So boom, boom.
**Adrian Rinnus** (00:31:49): Okay.
**Luís Braga** (00:31:50): So we have a super base SSR clients.
**Luís Braga** (00:31:54): And we don't want the current user.
**Luís Braga** (00:31:56): No, we want to have the, the app user.
**Adrian Rinnus** (00:31:59): So we.
**Adrian Rinnus** (00:32:01): Okay.
**Adrian Rinnus** (00:32:01): Anyway, so we just need to get the meal order in that sense.
**Adrian Rinnus** (00:32:05): means now we need const.
**Luís Braga** (00:32:09): Oh, hang on.
**Luís Braga** (00:32:10): Not even the user.
**Adrian Rinnus** (00:32:11): We need to get the meal today.
**Adrian Rinnus** (00:32:15): Exactly.
**Adrian Rinnus** (00:32:16): then just get the meal for today.
**Adrian Rinnus** (00:32:18): Of course.
**Luís Braga** (00:32:20): What the  am I doing today?
**Luís Braga** (00:32:22): Today equals new needs.
**Adrian Rinnus** (00:32:25): I have a helper class that we should use because we don't care about the time.
**Adrian Rinnus** (00:32:32): was getting so many  issues with the time.
**Adrian Rinnus** (00:32:35): There is a date only thing.
**Adrian Rinnus** (00:32:37): There should be auto-completion.
**Adrian Rinnus** (00:32:39): Date only.
**Adrian Rinnus** (00:32:42): And then with date only, if you scroll down past date only.
**Adrian Rinnus** (00:32:49): Only.
**Adrian Rinnus** (00:32:50): Format date only, I think.
**Adrian Rinnus** (00:32:53): Format date only?
**Adrian Rinnus** (00:32:54): Yeah.
**Luís Braga** (00:32:57): Yeah.
**Adrian Rinnus** (00:32:58): Parse date only?
**Luís Braga** (00:33:01): It doesn't matter which one.
**Adrian Rinnus** (00:33:03): think the format is fine.
**Adrian Rinnus** (00:33:05): Okay.
**Adrian Rinnus** (00:33:07): And then put the new date in there.
**Adrian Rinnus** (00:33:09): Yeah.
**Luís Braga** (00:33:11): All right.
**Luís Braga** (00:33:12): Then, let's say, order.
**Luís Braga** (00:33:15): Supervenger.
**Adrian Rinnus** (00:33:16): No, we have curly braces there because we have data and error instead of order.
**Adrian Rinnus** (00:33:26): And then do data colon order comma error.
**Adrian Rinnus** (00:33:31): Sorry, I'm lost.
**Adrian Rinnus** (00:33:33): In line 15, don't call it order because it's data.
**Adrian Rinnus** (00:33:38): The return thing from Superbase is data.
**Adrian Rinnus** (00:33:41): Incorrect.
**Adrian Rinnus** (00:33:42): Error.
**Luís Braga** (00:33:43): Error?
**Luís Braga** (00:33:44): Error.
**Adrian Rinnus** (00:33:46): Error.
**Adrian Rinnus** (00:33:47): Error.
**Adrian Rinnus** (00:33:48): Yes.
**Adrian Rinnus** (00:33:49): And loading, I guess.
**Adrian Rinnus** (00:33:50): Yeah, if we want to, yes.
**Luís Braga** (00:33:53): Okay.
**Adrian Rinnus** (00:33:54): then await Superbase dot from.
**Adrian Rinnus** (00:34:04): And now let me think about it.
**Adrian Rinnus** (00:34:08): I need to check.
**Adrian Rinnus** (00:34:10): Can you open Superbase?
**Adrian Rinnus** (00:34:12): You have it already in the browser?
**Adrian Rinnus** (00:34:15): No, the left one, yes.
**Adrian Rinnus** (00:34:16): And then let's see, we have a meal order thing.
**Adrian Rinnus** (00:34:20): And this is updated menu week.
**Adrian Rinnus** (00:34:24): But this is for the whole week.
**Adrian Rinnus** (00:34:27): And then we have a menu, no, an order line.
**Adrian Rinnus** (00:34:31): Can you check for the order line?
**Adrian Rinnus** (00:34:34): And this is based on the slot.
**Adrian Rinnus** (00:34:36): Okay.
**Adrian Rinnus** (00:34:37): And then we have the order slot.
**Adrian Rinnus** (00:34:39): So I think we should build a Postgres view to get the order.
**Adrian Rinnus** (00:34:43): If you go one more, there's the order slot.
**Adrian Rinnus** (00:34:47): Okay, meal.
**Adrian Rinnus** (00:34:49): So slot is the bigger one and the line is in the slot.
**Adrian Rinnus** (00:34:52): So we need to check more or less the order.
**Adrian Rinnus** (00:34:54): Order slot.
**Adrian Rinnus** (00:34:56): Let's build a Postgres view for it because otherwise we get crazy.
**Adrian Rinnus** (00:35:00): Priority.
**Adrian Rinnus** (00:35:00): great.
**Adrian Rinnus** (00:35:00): Has need see really calmly, bit a Mo.
**Adrian Rinnus** (00:35:01): Yeah,
**Adrian Rinnus** (00:35:01): Mm-hmm.
**Adrian Rinnus** (00:35:01): Postgres view you said.
**Luís Braga** (00:35:03): Okay.
**Adrian Rinnus** (00:35:05): So do you still have some credits on WinSurf to run it with the MCP server?
**Adrian Rinnus** (00:35:10): Oh, yeah.
**Luís Braga** (00:35:11): Then let's use that one.
**Adrian Rinnus** (00:35:13): So you can connect the MCP, the Postgres MCP, or I can send you the settings for it.
**Adrian Rinnus** (00:35:21): Just a second.
**Adrian Rinnus** (00:35:22): Let me just check.
**Luís Braga** (00:35:24): It's been a while that I'm not using WinSurf.
**Luís Braga** (00:35:28): Where's MCPs?
**Luís Braga** (00:35:29): I guess.
**Luís Braga** (00:35:30): Oh, this is what I have.
**Luís Braga** (00:35:33): MongoDB.
**Luís Braga** (00:35:35): There is also...
**Adrian Rinnus** (00:35:37): Give me a second.
**Adrian Rinnus** (00:35:39): It's called...
**Adrian Rinnus** (00:35:42): It's called dbhub-postgres-npx.
**Adrian Rinnus** (00:35:48): Okay.
**Luís Braga** (00:35:49): How do I add db or db?
**Adrian Rinnus** (00:35:54): dbhub-postgres-npx.
**Adrian Rinnus** (00:35:59): Yeah.
**Adrian Rinnus** (00:36:00): That one.
**Adrian Rinnus** (00:36:00): one.
**Luís Braga** (00:36:02): Let's see if I can quickly add it, windsurf, winds, I just want to get you the  fact, what are you doing, stupido?
**Luís Braga** (00:36:19): Mm-hmm, dbf, dbf, windsurf, mtp.
**Luís Braga** (00:36:44): Or, first, sir, set up instructional cloud calls.
**Luís Braga** (00:36:48): Well, you know what, I'll just add it to cloud calls.
**Luís Braga** (00:36:53): You can also do it like that, sure.
**Luís Braga** (00:36:56): So, get the  away and let's do...
**Adrian Rinnus** (00:37:09): Okay, and now what we need is, wait, okay, here is the setting that you need to run, I sent it to you in Slack, right, the JSON settings here.
**Luís Braga** (00:37:37): All right, I never know what to have cloud MCP server, I guess, these, and then there's the cloud and then commands, commands, cloud, cloud MCP servers, JSON.
**Luís Braga** (00:37:57): And shortcuts, blah, blah, blah, Wi-Fi, boom, boom.
**Luís Braga** (00:38:01): And also add context 7, I think that makes sense.
**Luís Braga** (00:38:05): Yeah, that one I have it somehow, mcp-list.
**Adrian Rinnus** (00:38:11): Yeah.
**Luís Braga** (00:38:12): It's there, dbf failed.
**Luís Braga** (00:38:16): You send me something.
**Luís Braga** (00:38:19): All right, I guess, comments, do I need it at all?
**Adrian Rinnus** (00:38:25): The port is wrong, it's 5, 4, 3, 2, 2 instead of 5, 4.
**Adrian Rinnus** (00:38:31): And it's Postgres, yeah.
**Adrian Rinnus** (00:38:33): just use the one in six seconds.
**Luís Braga** (00:38:38): And I guess, let's see, close.
**Luís Braga** (00:38:52): Okay, all right, now let's do it like that.
**Adrian Rinnus** (00:38:57): Tell it to read the Postgres or Postgres or...
**Adrian Rinnus** (00:39:01): Superbase documentation on Context 7 in regards of how to create a view.
**Luís Braga** (00:39:09): Okay, you were a bit too fast.
**Luís Braga** (00:39:11): Sorry.
**Adrian Rinnus** (00:39:12): Read in Context 7 the documentation about Postgres and Superbase on how to create a database view.
**Adrian Rinnus** (00:39:31): Good.
**Adrian Rinnus** (00:39:32): Is that?
**Adrian Rinnus** (00:39:32): Yes.
**Luís Braga** (00:39:35): Thinking on one plan mode doesn't, I don't know.
**Luís Braga** (00:39:38): All right, let's see.
**Luís Braga** (00:39:39): What's this crap?
**Luís Braga** (00:39:43): Again?
**Luís Braga** (00:39:44): Ah.
**Luís Braga** (00:39:47): Okay, got you.
**Luís Braga** (00:39:49): Yes, I'm going to ask again, please.
**Luís Braga** (00:39:53): All right.
**Luís Braga** (00:40:07): Yes, isn't confused with the value API key, let me use webfetch context app, do I even need an API key?
**Adrian Rinnus** (00:40:14): so for me it's working usually, but anyways.
**Luís Braga** (00:40:22): I don't know.
**Luís Braga** (00:40:26): I, like lately I'm so not giving that much of a  to these things, but, and it's so, you see, I have, I don't even have what I have in, I don't even know what I have in Docker, like, because they have this MCP toolkit and I know I have, oh, I don't have any actually right now.
**Luís Braga** (00:40:47): But they're pushing forward Docker, you know, models and, anyway, what's going on?
**Luís Braga** (00:40:54): here.
**Adrian Rinnus** (00:40:59): Okay, now it has the information.
**Adrian Rinnus** (00:41:01): And now tell it to use execute under SQL, it's the command execute underscore, it's written together, and without the blank, just to understand the database structure of, no, it is, wait, let me see.
**Adrian Rinnus** (00:41:29): I will tell you how the tables are called, it's menu underscore order, wait, but he used to understand the structure, oh, I'm in the wrong database, wait.
**Adrian Rinnus** (00:41:59): Here we go.
**Adrian Rinnus** (00:42:00): you.
**Adrian Rinnus** (00:42:01): Thank
**Adrian Rinnus** (00:42:04): Here it is called a meal order, not menu order, meal order.
**Adrian Rinnus** (00:42:15): Then it's called order line and order slot, order underscore line, exactly, and the app user table, and get the information which is required to build a few that delivers the order for the current day for the specific, for a specific user.
**Adrian Rinnus** (00:43:02): You know, something like that, let's see what happens.
**Luís Braga** (00:43:17): I always like when I see success.
**Adrian Rinnus** (00:43:23): Now it reads the database structure more or less and then it can create a few for us.
**Adrian Rinnus** (00:43:28): That's pretty cool.
**Luís Braga** (00:43:29): It will create the view in Superbase?
**Adrian Rinnus** (00:43:33): Yeah, no, it looks in the local Postgres, not on Superbase because I don't want to touch the production system.
**Adrian Rinnus** (00:43:39): This one is not checking the local Postgres database, which is in the backend of Superbase in that sense.
**Adrian Rinnus** (00:43:48): But it fetches now the structure of the database and understands what is happening and how it is set together in that sense and then it knows what to do, actually.
**Adrian Rinnus** (00:44:01): In most of the cases, and it's  up a lot of times, but it's not that I had a lot of, ah, you see here, proposed few, use daily order.
**Luís Braga** (00:44:14): oh, sorry, do you want to go database structure summary may be useful to invalidate this.
**Luís Braga** (00:44:28): So, what's this interval?
**Adrian Rinnus** (00:44:31): Current date, date, start, slot date, interval, one day, yeah, should be right, let's see, now you can tell it that it should create a new migration, create a new migration using, create a new migration with super base, migration new, migration blank new, and, um...
**Adrian Rinnus** (00:45:00): um...
**Adrian Rinnus** (00:45:01): And create the proposed view.
**Luís Braga** (00:45:09): Excellent.
**Luís Braga** (00:45:11): Yep.
**Luís Braga** (00:45:16): We're current date.
**Adrian Rinnus** (00:45:19): Yeah.
**Adrian Rinnus** (00:45:21): New active user.
**Luís Braga** (00:45:24): Migration.
**Luís Braga** (00:45:26): NPX.
**Luís Braga** (00:45:28): Yeah.
**Luís Braga** (00:45:29): Sounds good.
**Adrian Rinnus** (00:45:30): Yeah, but there is something error, script database.
**Luís Braga** (00:45:34): Yeah, I think it  up the command, but now it's proposed.
**Luís Braga** (00:45:38): Yeah.
**Luís Braga** (00:45:38): Yeah.
**Luís Braga** (00:45:39): Okay.
**Adrian Rinnus** (00:45:39): Exactly.
**Adrian Rinnus** (00:45:40): Mm-hmm.-hmm.
**Adrian Rinnus** (00:45:44): Mm-hmm.
**Luís Braga** (00:45:58): Mm-hmm.
**Luís Braga** (00:46:00): Mm-hmm.
**Luís Braga** (00:46:01): ?
**Adrian Rinnus** (00:46:08): Well, this is working.
**Adrian Rinnus** (00:46:14): I can also put myself to work in the window.
**Adrian Rinnus** (00:46:20): Come on.
**Adrian Rinnus** (00:46:23): What's happening here?
**Luís Braga** (00:46:28): Why are you taking so long?
**Luís Braga** (00:46:31): !
**Luís Braga** (00:46:40): Slytherin, there we go, whoa, no, not really, also I'm over there.
**Luís Braga** (00:46:52): Alright.
**Luís Braga** (00:46:57): Maybe, maybe, maybe in the meantime.
**Luís Braga** (00:47:00): Well, I'm.
**Luís Braga** (00:47:00): I'm I'm.
**Luís Braga** (00:47:01): I'm.
**Luís Braga** (00:47:01): I'm.
**Luís Braga** (00:47:01): I'm.
**Luís Braga** (00:47:05): Can you check if it has created a...
**Adrian Rinnus** (00:47:08): Not yet, it doesn't look...
**Luís Braga** (00:47:13): It's still doing something, not sure what's...
**Adrian Rinnus** (00:47:17): there, okay.
**Luís Braga** (00:47:18): It's coming.
**Adrian Rinnus** (00:47:20): Okay, yeah.
**Adrian Rinnus** (00:47:20): It's still coming.
**Luís Braga** (00:47:31): Ooh.
**Luís Braga** (00:47:33): All right, we like this.
**Luís Braga** (00:47:37): Just a second.
**Luís Braga** (00:47:41): For the current day for each user.
**Luís Braga** (00:47:52): Okay, it's doing its joins and .
**Adrian Rinnus** (00:47:56): So now go to the command line or in the terminal and apply it.
**Adrian Rinnus** (00:48:01): Can I accept this?
**Luís Braga** (00:48:04): No, do it by yourself.
**Adrian Rinnus** (00:48:06): It's easier.
**Adrian Rinnus** (00:48:08): Yeah, can do that.
**Adrian Rinnus** (00:48:12): I think it's okay.
**Adrian Rinnus** (00:48:14): Then we just test it out and see what is happening there.
**Adrian Rinnus** (00:48:18): Superbase.
**Adrian Rinnus** (00:48:20): Okay.
**Luís Braga** (00:48:21): Do I need some npx?
**Luís Braga** (00:48:23): Superbase.
**Luís Braga** (00:48:24): Superbase.
**Adrian Rinnus** (00:48:24): No, no, db push, minus, minus, local.
**Adrian Rinnus** (00:48:36): Yes, please.
**Adrian Rinnus** (00:48:39): Okay, and now let's go to Superbase.
**Adrian Rinnus** (00:48:43): And let's see that user order   thing that we have created.
**Adrian Rinnus** (00:48:49): Where is in here?
**Luís Braga** (00:48:51): User daily orders.
**Adrian Rinnus** (00:48:53): A little bit up.
**Adrian Rinnus** (00:48:55): A little bit down.
**Adrian Rinnus** (00:48:57): Yes, here.
**Adrian Rinnus** (00:48:58): And it's nothing in here.
**Adrian Rinnus** (00:49:00): Why?
**Adrian Rinnus** (00:49:02): This is f*****g f*****g.
**Adrian Rinnus** (00:49:04): Why is it not there?
**Adrian Rinnus** (00:49:07): Should I have something, actually?
**Adrian Rinnus** (00:49:08): think so, because check the other slots.
**Adrian Rinnus** (00:49:12): Yeah.
**Adrian Rinnus** (00:49:13): Okay, then I think this...
**Adrian Rinnus** (00:49:17): Can you please go to the other slots here?
**Adrian Rinnus** (00:49:20): Go back to the other slots.
**Adrian Rinnus** (00:49:26): Where is the...
**Adrian Rinnus** (00:49:29): Can we go back to Cloud Code to see what it was doing and how it was building the relations?
**Adrian Rinnus** (00:49:36): No, when he was describing it, more or less up there.
**Adrian Rinnus** (00:49:40): So, the connection is...
**Adrian Rinnus** (00:49:42): Scroll a bit more up, please.
**Adrian Rinnus** (00:49:46): Okay, app user to meal order, or meal order is pointing to app user.
**Adrian Rinnus** (00:49:50): Okay, then the meal order is pointing to menu weak, that's okay.
**Adrian Rinnus** (00:49:54): The meal order, or the order slot is pointing to the order.
**Adrian Rinnus** (00:49:58): Okay.
**Adrian Rinnus** (00:49:59): User ID.
**Adrian Rinnus** (00:50:03): What could be the case is that app user and the user ID is a different one, so ask Cloud Code, tell it, hey, this is not working, please check if the user ID is the right one or if the user ID from auth.users.
**Adrian Rinnus** (00:50:32): Yeah, it's the right one, or if there is a mess, and also tell it that it should call the view, no, it's the second one, that the view should always have an V underscore in front of it, the name of the view that we have it.
**Adrian Rinnus** (00:50:48): The name of the view should always start with V underscore.
**Adrian Rinnus** (00:50:56): V underscore.
**Luís Braga** (00:50:57): underscore, like so?
**Luís Braga** (00:50:58): Yeah.
**Adrian Rinnus** (00:50:59): Good.
**Adrian Rinnus** (00:51:00): you.
**Adrian Rinnus** (00:51:01): This is not working, maybe I should be explicit and say, we don't have any, yeah, you can enter it that it can check it with execute SQL in the database now, by using execute SQL, yeah, good, yeah, let's go.
**Luís Braga** (00:51:42): So, I guess he needs to update the migration.
**Adrian Rinnus** (00:51:49): Just a second, what is happening here, yeah, no, it should fix it, right.
**Luís Braga** (00:51:55): Well, what you meant was here, V underscore, right?
**Luís Braga** (00:51:58): Yes, exactly.
**Luís Braga** (00:51:59): you.
**Luís Braga** (00:52:00): Just
**Luís Braga** (00:52:01): Convention of ourselves.
**Luís Braga** (00:52:03): Yep.
**Adrian Rinnus** (00:52:04): Just to make it easier to find it in that way.
**Luís Braga** (00:52:10): So basically a view is like a custom table where you do whatever SQL operations you want.
**Luís Braga** (00:52:18): Yeah, exactly.
**Adrian Rinnus** (00:52:19): So that you don't have to write the joins all the time.
**Adrian Rinnus** (00:52:21): And if we now use the server action, we can read the view and don't have to build all the joins in Superbase.
**Adrian Rinnus** (00:52:29): So this is just easier code.
**Adrian Rinnus** (00:52:31): And we are using every word of view later on and not writing the code on every Superbase instance, you know.
**Luís Braga** (00:52:39): And, ah, okay, cool.
**Luís Braga** (00:52:46): But we have way more than we actually need, right?
**Luís Braga** (00:52:49): Here, I guess.
**Luís Braga** (00:52:50): Yeah, think so.
**Adrian Rinnus** (00:52:52): We can also clean it up later and then, yeah.
**Adrian Rinnus** (00:52:56): Perfect.
**Luís Braga** (00:52:56): On the issue, meal order, user ID references up, blah, blah, not app user ID.
**Luís Braga** (00:53:01): Exactly.
**Adrian Rinnus** (00:53:09): Okay, now we have to do in the terminal a super-based db reset because we can't push again because it's already there.
**Luís Braga** (00:53:22): Yeah.
**Adrian Rinnus** (00:53:30): We have now three paying customers on the trading journal.
**Adrian Rinnus** (00:53:34): Awesome.
**Adrian Rinnus** (00:53:36): We're getting there.
**Adrian Rinnus** (00:53:40): That's it.
**Adrian Rinnus** (00:53:41): No, actually we have even more because one of the educators is also starting with a new cohort now and he is paying us also for that at least three months.
**Adrian Rinnus** (00:53:55): How about subscribers and ?
**Luís Braga** (00:53:58): Yeah, three paying customers.
**Adrian Rinnus** (00:54:01): Yes, we-
**Adrian Rinnus** (00:54:01): We have a lot of other ones, but we have three paying customers, subscribers.
**Luís Braga** (00:54:10): No, I meant newsletter subscribers and stuff.
**Luís Braga** (00:54:14): Yeah, we were addressing them.
**Adrian Rinnus** (00:54:17): It's, yeah, we have 1,300 subscribers, but no one is reading it really and it's a little bit .
**Adrian Rinnus** (00:54:25): So the user daily orders on a, ah, here we go.
**Adrian Rinnus** (00:54:32): You see, .
**Adrian Rinnus** (00:54:34): So, all right.
**Adrian Rinnus** (00:54:36): All right, back to the call, I guess.
**Adrian Rinnus** (00:54:42): And now we can at least go there.
**Adrian Rinnus** (00:54:46): Can you go to the terminal and run, run, ah, super base, run run.
**Adrian Rinnus** (00:54:55): Super base, colon, type, gen, or something.
**Adrian Rinnus** (00:55:00): Can you check the.
**Adrian Rinnus** (00:55:02): Check the package, Jason, for a second.
**Adrian Rinnus** (00:55:05): Superbase types.
**Adrian Rinnus** (00:55:07): Okay.
**Adrian Rinnus** (00:55:09): Okay.
**Adrian Rinnus** (00:55:11): And now you can go there, exactly, and from v underscore user...
**Adrian Rinnus** (00:55:17): Okay.
**Adrian Rinnus** (00:55:22): This is actually it.
**Adrian Rinnus** (00:55:26): Dot select...
**Adrian Rinnus** (00:55:34): Bracers.
**Adrian Rinnus** (00:55:35): Yeah.
**Adrian Rinnus** (00:55:36): Yeah.
**Adrian Rinnus** (00:55:37): Something like that.
**Luís Braga** (00:55:42): Wow.
**Luís Braga** (00:55:44): Cool.
**Luís Braga** (00:55:45): Can we log this?
**Adrian Rinnus** (00:55:46): Yeah, sure, you can.
**Adrian Rinnus** (00:55:49): I'm excited if it works, because I'm not just the data.
**Adrian Rinnus** (00:55:55): Let's see.
**Adrian Rinnus** (00:55:55): And what we need...
**Adrian Rinnus** (00:55:58): just remove the EQ things.
**Adrian Rinnus** (00:56:03): Just to get everything to see if it's working, if we have it right.
**Adrian Rinnus** (00:56:08): And how do we call this guy?
**Adrian Rinnus** (00:56:11): Just, okay, now we, yeah, we go here, and then, yeah, good question,  , I'm sorry.
**Adrian Rinnus** (00:56:19): Check another page?
**Adrian Rinnus** (00:56:20): Yeah, just check another one where we use something like that.
**Adrian Rinnus** (00:56:23): Okay.
**Adrian Rinnus** (00:56:25): So I think it's just in the page you call the function with an async await, and that's it.
**Adrian Rinnus** (00:56:31): It's, here it is.
**Adrian Rinnus** (00:56:33): Yeah.
**Luís Braga** (00:56:34): All right, so const, const  equals await, get order, blah, blah, blah.
**Luís Braga** (00:56:41): And we need some internal ID, right?
**Luís Braga** (00:56:45): Yep.
**Luís Braga** (00:56:47): Which I can take from...
**Luís Braga** (00:56:50): User ID here, yeah.
**Adrian Rinnus** (00:56:53): This one?
**Adrian Rinnus** (00:56:54): Yep.
**Adrian Rinnus** (00:56:55): Oh, or is it the internal number?
**Adrian Rinnus** (00:56:57): Ah, internal number, internal number, right, sorry.
**Adrian Rinnus** (00:56:59): Yep.
**Adrian Rinnus** (00:57:01): Oh, that's good.
**Luís Braga** (00:57:08): Oh, wait, because I think, and what, you have to put it in as an object, huh?
**Adrian Rinnus** (00:57:23): Okay.
**Luís Braga** (00:57:25): Uh-huh.
**Adrian Rinnus** (00:57:32): And now you can see it in the terminal where Bandev is running.
**Adrian Rinnus** (00:57:37): If you call the page, then you see the server stuff and you should also see it in the console log for the browser.
**Luís Braga** (00:57:44): Oh.
**Luís Braga** (00:57:45): Again, because we did the database reset.
**Luís Braga** (00:57:49): Is it like so, test?
**Luís Braga** (00:57:50): Test, test, yes.
**Adrian Rinnus** (00:57:53): So, right.
**Adrian Rinnus** (00:57:55): Let's go to the delivery page.
**Adrian Rinnus** (00:57:58): Ah, yes.
**Luís Braga** (00:58:00): .
**Adrian Rinnus** (00:58:01): Yeah, .
**Adrian Rinnus** (00:58:02): Nothing.
**Adrian Rinnus** (00:58:03): Okay.
**Adrian Rinnus** (00:58:05): Let's go to the...
**Adrian Rinnus** (00:58:07): but here's something.
**Adrian Rinnus** (00:58:08): Data.
**Adrian Rinnus** (00:58:09): Uh-huh.
**Adrian Rinnus** (00:58:10): Whoa, whoa, whoa, what?
**Luís Braga** (00:58:12): Yeah, that's fine.
**Luís Braga** (00:58:14): Oh, because I probably need to...
**Luís Braga** (00:58:18): Oh, because I'm returning nothing.
**Luís Braga** (00:58:19): Of course, I'm stupid.
**Luís Braga** (00:58:21): Right, data is good.
**Adrian Rinnus** (00:58:23): Yep.
**Adrian Rinnus** (00:58:23): And now we can filter to see what is happening.
**Adrian Rinnus** (00:58:26): So add the equal stuff back again.
**Adrian Rinnus** (00:58:30): Uh, the question is, is there an order for today?
**Adrian Rinnus** (00:58:33): I'm not sure about it.
**Adrian Rinnus** (00:58:34): Right.
**Luís Braga** (00:58:35): But let's see.
**Luís Braga** (00:58:37): Oh, I don't want to remove this.
**Luís Braga** (00:58:39): I also don't like the .
**Luís Braga** (00:58:44): And I guess...
**Luís Braga** (00:58:46): Oh, really?
**Luís Braga** (00:58:48): I need to refresh?
**Luís Braga** (00:58:52): Just...
**Luís Braga** (00:58:53): sorry.
**Luís Braga** (00:58:55): Data.
**Luís Braga** (00:58:56): Data 5.
**Luís Braga** (00:58:57): Is it really today?
**Luís Braga** (00:58:58): Come on.
**Adrian Rinnus** (00:58:59): Wow.
**Adrian Rinnus** (00:59:00): How is this possible, man?
**Adrian Rinnus** (00:59:00): because it's...
**Adrian Rinnus** (00:59:01): Because it's...
**Adrian Rinnus** (00:59:01): For lunch and dinner, I guess.
**Adrian Rinnus** (00:59:04): And it's every meal is getting returned, you know, it's the dessert, it's the soup, it's the main, and the soup and the main for dinner.
**Adrian Rinnus** (00:59:12): So it's, we have five orders.
**Adrian Rinnus** (00:59:15): So every, every, every component of the menu is one order, you know, my question was, I guess, because the database seed is using today's date somehow, or?
**Adrian Rinnus** (00:59:27): All right, right, it does.
**Adrian Rinnus** (00:59:30): Yeah.
**Adrian Rinnus** (00:59:31): I mean, check the view in Superbase, I think it was that current date, blah, blah, blah, thingy, the view, no, in the browser.
**Adrian Rinnus** (00:59:43): Yeah, and here, it should be all the date, you see, it's everything from today, because if you go, if you go down, bottom right, bottom right, there's definition.
**Luís Braga** (00:59:56): Uh, mouse, come on.
**Luís Braga** (00:59:57): Yeah.
**Adrian Rinnus** (00:59:58): And then there is the, here, um, we.
**Adrian Rinnus** (01:00:01): Start date, double precision one day, this is one thing, then, yeah, current date, exactly, where current date.
**Luís Braga** (01:00:08): But I mean, okay, but my thing, my question is, our seed data is considering today's date.
**Adrian Rinnus** (01:00:20): Yeah, yeah, exactly.
**Adrian Rinnus** (01:00:22): On every DB reset, it's creating for the present week order, so, yeah.
**Adrian Rinnus** (01:00:27): Cool.
**Luís Braga** (01:00:29): So now, I guess we can, what's the, what's the schema again, user ID, what, do we really, should I return all this for now?
**Adrian Rinnus** (01:00:42): The question now is, is it lunch or dinner?
**Luís Braga** (01:00:47): Well, we should group it by the day part, right?
**Adrian Rinnus** (01:00:53): Exactly, and also, I would suggest that we run it once for dinner, or that we show just the dinner and just the lunch.
**Adrian Rinnus** (01:01:01): say Thank That
**Luís Braga** (01:01:08): I mean, we could return everything and have, let's say, a tab or a switcher because it could be, I don't know, useful.
**Luís Braga** (01:01:19): Let's start it for now and build something.
**Adrian Rinnus** (01:01:21): It doesn't matter.
**Adrian Rinnus** (01:01:22): Okay, now we have the data.
**Adrian Rinnus** (01:01:23): So you have learned serve actions right now and super basic views.
**Adrian Rinnus** (01:01:29): You all learned, my friend.
**Luís Braga** (01:01:30): So we have the thing working and getting data for us.
**Luís Braga** (01:01:34): And I suppose we have a type here.
**Luís Braga** (01:01:39): Yeah, this is already there.
**Adrian Rinnus** (01:01:41): Exactly.
**Adrian Rinnus** (01:01:42): We have the type.
**Luís Braga** (01:01:45): How can I know the type?
**Luís Braga** (01:01:48): What's, what's, where is this?
**Luís Braga** (01:01:49): Is it generally?
**Adrian Rinnus** (01:01:50): We can, we can, so let's create a types file.
**Adrian Rinnus** (01:01:58): For the style to start your view.
**Adrian Rinnus** (01:02:01): Yeah, types.ts.
**Adrian Rinnus** (01:02:05): And then you can, can you search for database somewhere, or can you check, for example, the mili-selection in the types.ts file?
**Luís Braga** (01:02:16): Mili-Selection, types.
**Adrian Rinnus** (01:02:19): Without the minus, I think.
**Adrian Rinnus** (01:02:22): Yeah.
**Adrian Rinnus** (01:02:23): And there is the export type, order line, insert.
**Adrian Rinnus** (01:02:26): Do you see that one, database?
**Adrian Rinnus** (01:02:27): Copy just that line and I will tell you.
**Adrian Rinnus** (01:02:29): Yep.
**Adrian Rinnus** (01:02:31): Now go back to our types file.
**Adrian Rinnus** (01:02:34): And paste it and then import the database.
**Adrian Rinnus** (01:02:38): Exactly.
**Adrian Rinnus** (01:02:39): And now don't do it on tables, just use views.
**Adrian Rinnus** (01:02:44): Or view.
**Adrian Rinnus** (01:02:45): No, exactly.
**Adrian Rinnus** (01:02:46): And then the, here we have the V underscore.
**Adrian Rinnus** (01:02:51): Oh, my God.
**Adrian Rinnus** (01:02:52): Yeah.
**Adrian Rinnus** (01:02:54): Distribution.
**Adrian Rinnus** (01:02:54): No, it's the user.
**Adrian Rinnus** (01:02:58): And I think we need one.
**Adrian Rinnus** (01:03:00): If you check it, I think it's.
**Adrian Rinnus** (01:03:02): We need one more bracket in the end.
**Adrian Rinnus** (01:03:07): Man, he's so smart.
**Adrian Rinnus** (01:03:09): And then there is the row.
**Adrian Rinnus** (01:03:11): Yes, and now we should be good to go.
**Adrian Rinnus** (01:03:14): What call this?
**Adrian Rinnus** (01:03:16): Huh?
**Luís Braga** (01:03:18): What should I call the export type?
**Adrian Rinnus** (01:03:21): Call it user orders, I don't know, user order distribution.
**Luís Braga** (01:03:39): Yeah, let's care about it later.
**Luís Braga** (01:03:43): We will never care about it, but let's care about it later.
**Adrian Rinnus** (01:03:47): Okay.
**Luís Braga** (01:03:49): Oh, you know what?
**Luís Braga** (01:03:51): I wonder, if I give this to Claude, will he know what I'm talking about?
**Luís Braga** (01:04:07): So, we have the thing, what do you say we pass it to Claude and see what it does?
**Adrian Rinnus** (01:04:13): Sure, let's try it.
**Luís Braga** (01:04:20): Okay, so, I'm gonna clear context and I'll say given the web page, this one, is okay, and that I've already set up a server action for it, for it, and it's this one.
**Luís Braga** (01:04:54): Finish or plan the implementation to get...
**Luís Braga** (01:05:10): And what a  prompt, let's see, let's see, oh, I should have put this in plan mode, but yes, 3, 8, 8, all right, what does he say, I'll read both files, well, I'm going to fix the server action to return the data, very good, rendering proper types, create the source features, mill distribution components, leave, reform, nice, this follows a feature-based app.
**Luís Braga** (01:06:00): Mm-hmm.
**Luís Braga** (01:06:02): pattern, build interactive form, delivery form, react.
**Luís Braga** (01:06:06): Is it correct?
**Luís Braga** (01:06:07): use Zod and...
**Adrian Rinnus** (01:06:09): React hook form, yes, but Zod, I think, yes.
**Luís Braga** (01:06:13): We do?
**Luís Braga** (01:06:14): Zod?
**Luís Braga** (01:06:16): No, I don't think so, Zod.
**Luís Braga** (01:06:19): Yeah, we do.
**Luís Braga** (01:06:21): Zod, yes.
**Luís Braga** (01:06:24): It's fine, yeah?
**Luís Braga** (01:06:26): And where was I?
**Luís Braga** (01:06:28): Damn it.
**Luís Braga** (01:06:30): Zod, state management for input, loading state, order results, blah, blah, blah, keep my server components, import, da, da, da, da, loading, displaying, no results,  awesome, 10 stack query for caching, centralized .id, toast.
**Luís Braga** (01:06:48): Sounds good.
**Adrian Rinnus** (01:06:49): Yeah, but you can also tell it cannot use the query registry because this is crazy  and we can also do it separately.
**Adrian Rinnus** (01:06:59): So don't use query registry?
**Luís Braga** (01:07:01): Yeah.
**Luís Braga** (01:07:02): because it's too big and find a good solution that is working to be just find what's a good solution for handling the query.
**Luís Braga** (01:07:20): Did he mention it?
**Luís Braga** (01:07:22): Ah, query.
**Luís Braga** (01:07:23): So we were dropping this, whatever this is, because we have to reflect it at some place.
**Adrian Rinnus** (01:07:29): It's just a huge monsters thing.
**Luís Braga** (01:07:32): Okay, so simplify implementation plan, call server action directly, unform submit, simple redempt clear state, show the query should be used in my opinion, but not the query registry.
**Adrian Rinnus** (01:07:51): Should still be used.
**Adrian Rinnus** (01:08:00): And also, real tool form can be used.
**Adrian Rinnus** (01:08:02): I don't mind.
**Adrian Rinnus** (01:08:03): He said he wouldn't?
**Luís Braga** (01:08:05): Yeah.
**Luís Braga** (01:08:07): Oh, also keep the actual form and Zod.
**Luís Braga** (01:08:12): I don't know if he mentioned Zod.
**Luís Braga** (01:08:18): Leverage, yeah, of course, pending error data.
**Luís Braga** (01:08:33): I mean, yes, I would.
**Luís Braga** (01:08:41): It's so tempting to just use now do the same thing with for NFC using NFC API, but I would actually like to.
**Adrian Rinnus** (01:08:49): Yeah, let's let's let's figure it out by ourselves at least a bit that we understand what it is doing.
**Luís Braga** (01:08:54): And the truck is to pair programming with this.
**Luís Braga** (01:09:01): Super.
**Luís Braga** (01:09:02): I yes, because I'll have to switch forward to the tablets.
**Adrian Rinnus** (01:09:08): We have, I have a staging environment, and I can also spin up some branches somewhere on AWS that we can test it there, or, no, the band server is also able that you can connect to it locally, so you can connect with the tablet to it, in my opinion.
**Adrian Rinnus** (01:09:28): Yeah, sure, sure, sure.
**Luís Braga** (01:09:30): I just don't know, I just don't know what, I mean, yeah, why am I complicated, like, I just access by the IP, and it's good.
**Luís Braga** (01:09:41): Exactly.
**Luís Braga** (01:09:42): I mean, you won't see, yeah, that's my point, you won't see my screen.
**Adrian Rinnus** (01:09:49): Yeah, okay, but that's, okay, I can still see it on your screen.
**Luís Braga** (01:09:55): Or, we should be able to, do we, maybe we need Android Studio to use a simulated device.
**Adrian Rinnus** (01:10:02): No, I don't think so, and Mac OS Android screen share, screen mirror, okay, mirror Android phone screen on macOS.
**Luís Braga** (01:10:17): Maybe there's a way to, let's see.
**Luís Braga** (01:10:21): How to mirror Android on Mac 2025.
**Adrian Rinnus** (01:10:30): Any viewer, Android, there are some, any viewer is the easiest one.
**Adrian Rinnus** (01:10:38): Best screen sharing software, doesn't require any complicated settings.
**Adrian Rinnus** (01:10:44): Any viewer, I think something like team viewer in that sense.
**Adrian Rinnus** (01:10:52): And there is also, what was this?
**Adrian Rinnus** (01:11:01): Yes.
**Adrian Rinnus** (01:11:01): Yes.
**Adrian Rinnus** (01:11:02): Yes.
**Luís Braga** (01:11:02): Yeah, you've heard some videos, what's going on?
**Adrian Rinnus** (01:11:07): Cast presents itself as a great choice to mirror via USB connection.
**Adrian Rinnus** (01:11:14): Ah, USB connection?
**Luís Braga** (01:11:16): Hmm.
**Luís Braga** (01:11:18): Airdroid is the thing.
**Adrian Rinnus** (01:11:21): And then you can use USB too.
**Adrian Rinnus** (01:11:28): Or you use Xmirage.
**Luís Braga** (01:11:37): Well, the guy says it's done.
**Luís Braga** (01:11:40): Then let's see.
**Adrian Rinnus** (01:11:43): One, two, three, four, five would be the...
**Luís Braga** (01:11:51): So, okay, I forgot to mention that I would like to group by day parts.
**Adrian Rinnus** (01:11:59): Day part and also it should be in one...
**Adrian Rinnus** (01:12:02): The more or less, for the main, the soup, and the dessert.
**Adrian Rinnus** (01:12:05): It should be one card for lunch, one card for dinner, and then a nice-looking UI, .
**Luís Braga** (01:12:12): It's grouped by, what was it again?
**Luís Braga** (01:12:15): TheyParts, by theyParts, theyParts, and uses single cards with this type.
**Adrian Rinnus** (01:12:34): And use a single card for the day part, for each day part, and should we also add something to mark the order as delivered, in that sense, or picked up?
**Luís Braga** (01:12:54): I wouldn't say, at least for now.
**Luís Braga** (01:12:57): How can we tell?
**Luís Braga** (01:12:59): Ah, you mean to mark?
**Adrian Rinnus** (01:13:01): Yeah.
**Adrian Rinnus** (01:13:01): Yeah.
**Adrian Rinnus** (01:13:02): Yeah.
**Luís Braga** (01:13:02): For sure.
**Luís Braga** (01:13:04): But, yeah, let's start one by one, one by one.
**Luís Braga** (01:13:09): Yeah, yeah, let's do the reading.
**Luís Braga** (01:13:23): All right, where's Google Chrome?
**Luís Braga** (01:13:31): Yeah, so supposedly I can, supposedly I can access by IP address, right?
**Luís Braga** (01:13:45): it should work.
**Luís Braga** (01:13:49): 3102, and what's the port we're running?
**Luís Braga** (01:13:53): 3000, I guess.
**Adrian Rinnus** (01:13:54): Yeah, one, two.
**Luís Braga** (01:13:58): It's cleaner.
**Luís Braga** (01:14:00): What?
**Luís Braga** (01:14:01): What the  is here?
**Luís Braga** (01:14:02): We done user results, good, because we list the thing and the order, cool, internal number, cool, main, yeah, what the fun.
**Adrian Rinnus** (01:14:10): we should also have, can you check in Superbase if there is also the meal or the name of the, no, you have to switch, if you go back to the view, and now go to, no, it's data, okay, is there also the name of the meal, I think this is missing, right?
**Adrian Rinnus** (01:14:25): I know that it is, the meal name should be displayed, and it should use, but this is for later, no, we should, we should do it, it should use the translation in my opinion, so we have a, but this is a view change, okay, tell it that it should update the view again, and it should use the, you should update the view, and use and use, use the,
**Adrian Rinnus** (01:15:02): Meal translations table, and it should take an example, let me see, an example which is used, for example, on, just a second, kitchen, all the lines, because I have that one already somewhere, kitchen, vMenuSlots, and the view, no, where is it?
**Adrian Rinnus** (01:15:32): I need to find the right view, just a second, where is it, , , here, it should, for example, use the v underscore kitchen, weekly, weekly underscore menu, underscore enriched,
**Adrian Rinnus** (01:16:04): To see how the Mule translations are handled, and then use the same idea, it's also called Mule Translations, the column is called Mule Translations.
**Luís Braga** (01:16:19): I should do, you should have picked the SQL view, right, or something like that?
**Adrian Rinnus** (01:16:25): Yeah.
**Adrian Rinnus** (01:16:26): SQL view and use Mule Translations table.
**Luís Braga** (01:16:32): I guess the goal is to display the Mule names in the cards.
**Adrian Rinnus** (01:16:40): Yeah, and the Mule names in the right language, in the selected language.
**Adrian Rinnus** (01:16:47): And one thing is, you can check the Mule selection, how it is done there.
**Adrian Rinnus** (01:16:56): The Mule selection.
**Adrian Rinnus** (01:16:59): Yeah, Mule selection page, and it will find its way.
**Adrian Rinnus** (01:17:04): No, sorry, it's called meal selection page.
**Adrian Rinnus** (01:17:07): think it's a bit better.
**Luís Braga** (01:17:09): Right, meal selection, meal selection page.
**Adrian Rinnus** (01:17:18): You can see that one.
**Adrian Rinnus** (01:17:19): Yeah.
**Adrian Rinnus** (01:17:21): Yeah.
**Adrian Rinnus** (01:17:22): Okay, let's go.
**Luís Braga** (01:17:26): All right, meanwhile, is it, I'm going to try and do and log in with my tablet.
**Luís Braga** (01:17:34): And this would be, what would this be?
**Luís Braga** (01:17:40): Is this going to work out of the box?
**Luís Braga** (01:17:43): For it to work, needs to, the dev server should be listening to connections on.
**Luís Braga** (01:17:51): It should, I guess.
**Adrian Rinnus** (01:17:52): So Tech Solutions Group?
**Luís Braga** (01:17:54): No, is...
**Luís Braga** (01:17:55): Yeah, yeah.
**Adrian Rinnus** (01:17:56): Okay, I'm wrong.
**Luís Braga** (01:17:58): Non-employee login.
**Adrian Rinnus** (01:17:59): Admin.
**Adrian Rinnus** (01:18:00): Admin.
**Adrian Rinnus** (01:18:01): Admin.
**Luís Braga** (01:18:03): Come on, admin login.
**Luís Braga** (01:18:06): What are you doing?
**Adrian Rinnus** (01:18:13): Can you also tell it that it should use execute SQL to get the information from the database?
**Adrian Rinnus** (01:18:19): Because no, it should be fine.
**Luís Braga** (01:18:23): I'm not sure what's going on with this Fathom.
**Luís Braga** (01:18:27): Yeah, I don't think this is working.
**Luís Braga** (01:18:29): Probably it's not working.
**Adrian Rinnus** (01:18:31): Because of the database.
**Luís Braga** (01:18:33): Yeah, maybe.
**Luís Braga** (01:18:36): I mean, when I click on my Thaladin admin login, there, rewritten URL, I think a while ago I was trying to clean, and I think we need to tweak some other dev server, or maybe I've No, go to the middleware.
**Adrian Rinnus** (01:18:58): Middleware.
**Adrian Rinnus** (01:18:58): Yeah.
**Luís Braga** (01:19:00): So, middleware.
**Luís Braga** (01:19:01): .
**Luís Braga** (01:19:02): Where is it?
**Luís Braga** (01:19:03): In the source?
**Luís Braga** (01:19:04): Yeah, search for it.
**Adrian Rinnus** (01:19:06): I think it's in the source, in the main form of the source.
**Adrian Rinnus** (01:19:12): And then here we have to ignore the one.
**Adrian Rinnus** (01:19:18): So there is in line 28, see staging WWW.
**Adrian Rinnus** (01:19:23): We also have to ignore the 192.
**Luís Braga** (01:19:30): So add something to the array.
**Luís Braga** (01:19:33): Yeah.
**Adrian Rinnus** (01:19:35): Like so.
**Luís Braga** (01:19:37): 192.
**Adrian Rinnus** (01:19:38): Yeah.
**Adrian Rinnus** (01:19:38): This should really do the trick, hopefully.
**Adrian Rinnus** (01:19:42): Try to reload the page on the...
**Adrian Rinnus** (01:19:45): Indeed.
**Luís Braga** (01:19:47): It's working.
**Luís Braga** (01:19:49): Yeah.
**Luís Braga** (01:19:50): All right.
**Luís Braga** (01:19:51): So tests.
**Luís Braga** (01:19:56): Okay.
**Luís Braga** (01:19:57): Clause still working.
**Luís Braga** (01:19:58): So tests at test.com.
**Luís Braga** (01:20:03): And tests, tests, tests, tests, no, wrong password.
**Adrian Rinnus** (01:20:12): Yeah, because it's doing a Superbase reset at the moment.
**Adrian Rinnus** (01:20:16): So it could be that it's not working there because of that.
**Adrian Rinnus** (01:20:21): Okay, now you can try it again.
**Adrian Rinnus** (01:20:24): What was it?
**Luís Braga** (01:20:24): I did, Claude, .
**Luís Braga** (01:20:26): Okay, tests, tests, go, fill to fetch, some things off still, and we both.
**Luís Braga** (01:20:39): It's still not working.
**Luís Braga** (01:20:43): I got error, like fill to fetch, let's see, what?
**Adrian Rinnus** (01:20:48): But then try to log in on your Macbook to see if it's working there.
**Adrian Rinnus** (01:20:53): It could be that there is also an issue with the cookies.
**Luís Braga** (01:20:59): I'm actually trying, what?
**Luís Braga** (01:21:01): on up other ways.
**Luís Braga** (01:21:01): Thank you.
**Luís Braga** (01:21:02): This should...
**Luís Braga** (01:21:06): Ah, missing the ports.
**Luís Braga** (01:21:11): What?
**Luís Braga** (01:21:14): Confused.
**Luís Braga** (01:21:17): Okay.
**Luís Braga** (01:21:20): Login, test at test.com, test, test.
**Luís Braga** (01:21:33): Ooh, what happened?
**Luís Braga** (01:21:39): All right, but let's finish this guy first.
**Luís Braga** (01:21:44): Localhost 3000, login, test at test.com, and then it's test, test, sign in.
**Luís Braga** (01:21:57): All right.
**Luís Braga** (01:21:58): Here is working.
**Luís Braga** (01:22:00): Delivery.
**Luís Braga** (01:22:03): One, two, three, four, five reads.
**Luís Braga** (01:22:07): Yeah, okay.
**Adrian Rinnus** (01:22:08): This looks good, actually.
**Adrian Rinnus** (01:22:09): And can you switch the language to Portuguese ones, please?
**Luís Braga** (01:22:14): Where's the switcher?
**Luís Braga** (01:22:15): Language, Portuguese.
**Luís Braga** (01:22:18): Nice.
**Luís Braga** (01:22:19): Awesome.
**Adrian Rinnus** (01:22:20): What the  is this?
**Luís Braga** (01:22:21): Times one.
**Luís Braga** (01:22:22): don't need it.
**Adrian Rinnus** (01:22:23): this is the amount of orders that they had there, so they can be removed.
**Luís Braga** (01:22:29): And so delivery form, this is the page, so everything is displaying on the form?
**Luís Braga** (01:22:35): Yeah.
**Luís Braga** (01:22:36): That's weird, but  it, where's the times?
**Luís Braga** (01:22:40): Times, times, internal number, quantity there.
**Luís Braga** (01:22:47): So we don't need it.
**Adrian Rinnus** (01:22:50): Just this, right?
**Luís Braga** (01:22:52): Yeah.
**Luís Braga** (01:22:54): Right.
**Luís Braga** (01:22:56): Lunch, dinner.
**Luís Braga** (01:22:59): All right.
**Luís Braga** (01:23:00): And reset.
**Luís Braga** (01:23:01): Okay, cool.
**Luís Braga** (01:23:02): One, two, three, four, five, three.
**Adrian Rinnus** (01:23:05): And now ADM001 would be the other one, I guess.
**Adrian Rinnus** (01:23:10): Which one?
**Adrian Rinnus** (01:23:11): Sorry?
**Adrian Rinnus** (01:23:14): ADM001, I guess.
**Adrian Rinnus** (01:23:16): Yeah.
**Adrian Rinnus** (01:23:17): Nice.
**Luís Braga** (01:23:18): Man, it's funny.
**Luís Braga** (01:23:20): Lovely.
**Adrian Rinnus** (01:23:23): All right, baby.
**Adrian Rinnus** (01:23:26): So commit, I guess.
**Luís Braga** (01:23:28): Yes.
**Adrian Rinnus** (01:23:30): Ah, what, no, wait, one thing we should do is add the translation already now.
**Adrian Rinnus** (01:23:35): Tell it to utilize it and do all the translation also of the form and stuff.
**Adrian Rinnus** (01:23:42): Using the petita.chson and the ender.chson with next.inter.
**Luís Braga** (01:23:47): And all string runs, all string translation.
**Luís Braga** (01:23:55): And the current changes using.
**Adrian Rinnus** (01:24:00): Next.
**Adrian Rinnus** (01:24:01): Yeah.
**Adrian Rinnus** (01:24:01): Yeah.
**Adrian Rinnus** (01:24:02): Yeah.
**Luís Braga** (01:24:05): And waiting as needed.en.json.
**Luís Braga** (01:24:11): Yeah, and tt.
**Adrian Rinnus** (01:24:13): Yes, tt.json.
**Luís Braga** (01:24:15): Yeah.
**Adrian Rinnus** (01:24:17): All good?
**Luís Braga** (01:24:19): That's good, yeah.
**Adrian Rinnus** (01:24:20): I will carry away the stuff I was drinking of back in a second.
**Adrian Rinnus** (01:24:26): All right.
**Adrian Rinnus** (01:24:34): Thank you.
**Adrian Rinnus** (01:24:35): Thank You
**Luís Braga** (01:26:02): Thank you.
**Luís Braga** (01:26:32): Thank
**Luís Braga** (01:27:13): Thank you very I have a fail to fetch on the login, it doesn't work, and I think it's related to the thing I was in this group.
**Luís Braga** (01:28:02): Describing before, I think it's, I don't remember, but what was it, I think it was, ah, there, okay, this, ah, this, yeah, I remember this, hostname, maybe that was even me, could be, so basically it's the port, sorry, the interface where listening to, otherwise it's just gonna accept from local hosts, something, some  like that, anyway, so if I stop this and do one devnet, devnet work, this should work, but let's see what this guy did.
**Adrian Rinnus** (01:28:52): Yep, the translation is there, looks good.
**Luís Braga** (01:29:02): Is it working?
**Luís Braga** (01:29:05): And one, two, three, four, five.
**Luís Braga** (01:29:10): Cool.
**Luís Braga** (01:29:12): Email.
**Luís Braga** (01:29:14): All right.
**Luís Braga** (01:29:15): All right.
**Luís Braga** (01:29:16): What do you say?
**Luís Braga** (01:29:17): Do I commit?
**Luís Braga** (01:29:20): For now.
**Luís Braga** (01:29:24): I need to take a bit.
**Luís Braga** (01:29:36): But I mean this alone.
**Luís Braga** (01:29:38): Are you there?
**Luís Braga** (01:29:39): Yes.
**Luís Braga** (01:29:40): This alone will already save them a lot of work.
**Adrian Rinnus** (01:29:47): Yes.
**Adrian Rinnus** (01:29:48): A lot of pain.
**Adrian Rinnus** (01:29:49): You're right.
**Luís Braga** (01:29:51): But now is when we will make him happy.
**Luís Braga** (01:29:56): Yeah.
**Adrian Rinnus** (01:29:57): So should I commit?
**Luís Braga** (01:29:59): I you can commit?
**Adrian Rinnus** (01:30:01): Totally.
**Adrian Rinnus** (01:30:02): Or to create a conventional commit for it, and then it should be fine.
**Luís Braga** (01:30:07): Oh, do we have some guidelines, commit guidelines?
**Luís Braga** (01:30:10): Yes, it is in .chiro.
**Adrian Rinnus** (01:30:12): Yeah, but if you tell it to do a conventional commit, it's fine.
**Adrian Rinnus** (01:30:15): Just tell it to do a conventional commit.
**Adrian Rinnus** (01:30:18): Convention commit?
**Adrian Rinnus** (01:30:20): Conventional, or yeah, I think it knows.
**Luís Braga** (01:30:31): I'm sorry, I'm having a sneaky smoke.
**Adrian Rinnus** (01:30:36): Mm-hmm.
**Luís Braga** (01:30:40): Man, this was fun.
**Luís Braga** (01:30:42): Mm-hmm.
**Adrian Rinnus** (01:30:45): Yes, it was.
**Luís Braga** (01:30:51): I mean, look at these .
**Luís Braga** (01:30:53): With some minor tweaking, we can already tell them for free, hey.
**Luís Braga** (01:30:58): Yes.
**Luís Braga** (01:30:59): But, I mean, we're a fart, a fart away.
**Adrian Rinnus** (01:31:06): We also have to do the pick up button that we set the status in the database that it was picked up, yes, yes, and we have to do the pick up.
**Luís Braga** (01:31:32): We have to change the schema in a way that we have pick up for each meal type.
**Adrian Rinnus** (01:31:38): I think it's already there if you check the schema.
**Adrian Rinnus** (01:31:41): If I remember right, it's already there.
**Adrian Rinnus** (01:31:44): Order slot, there is a user ID, no decision, no.
**Adrian Rinnus** (01:31:50): It's the order line, guess, order line.
**Adrian Rinnus** (01:31:53): Of course, status, quantity.
**Adrian Rinnus** (01:31:56): Nope, it's not skipped.
**Adrian Rinnus** (01:32:00): Okay, it's not there.
**Adrian Rinnus** (01:32:02): right.
**Adrian Rinnus** (01:32:02): It's
**Adrian Rinnus** (01:32:03): But this is an easy one, you know, I thought there was something like that, but anyways.
**Adrian Rinnus** (01:32:15): And there's not?
**Adrian Rinnus** (01:32:18): No, it's not, no longer, but that's an easy one.
**Adrian Rinnus** (01:32:21): It's just a timestamp and located.
**Adrian Rinnus** (01:32:25): All right, yes, go for it.
**Adrian Rinnus** (01:32:28): Does it look right?
**Luís Braga** (01:32:30): Yeah, it looks good.
**Adrian Rinnus** (01:32:32): Oh, this is just, yeah, okay.
**Luís Braga** (01:32:34): Yeah, just that.
**Adrian Rinnus** (01:32:36): Is it easy at all?
**Luís Braga** (01:32:41): Come on, Claude.
**Luís Braga** (01:32:43): Lost in the types file, yes, sounds good.
**Adrian Rinnus** (01:32:50): Middleware.
**Adrian Rinnus** (01:32:51): Yeah, maybe it's supposed to change you, mate.
**Luís Braga** (01:32:53): All this card is, I don't think.
**Adrian Rinnus** (01:32:55): Yeah, but now you need it, because otherwise you are not able to access the login.
**Adrian Rinnus** (01:33:00): Okay.
**Adrian Rinnus** (01:33:01): .
**Adrian Rinnus** (01:33:01): All right.
**Luís Braga** (01:33:02): Thank you.
**Luís Braga** (01:33:02): I'll let it.
**Luís Braga** (01:33:04): All right.
**Luís Braga** (01:33:05): Well, let's see.
**Luís Braga** (01:33:08): Okay.
**Luís Braga** (01:33:08): So I'm a  .
**Luís Braga** (01:33:09): So where's the comments?
**Luís Braga** (01:33:12): Feeds delivery.
**Luís Braga** (01:33:14): My kitchen with user order lookup.
**Luís Braga** (01:33:17): Good.
**Adrian Rinnus** (01:33:18): Awesome.
**Luís Braga** (01:33:20): So my friend, what are you saying?
**Luís Braga** (01:33:22): What do think?
**Luís Braga** (01:33:23): We have the reading.
**Luís Braga** (01:33:26): What do you think we should do now?
**Luís Braga** (01:33:31): Yeah.
**Adrian Rinnus** (01:33:33): The thing is, how the  do we do this together?
**Adrian Rinnus** (01:33:42): Yeah, let's write the code and you tell me what is happening on the tablet.
**Adrian Rinnus** (01:33:45): That's fine.
**Luís Braga** (01:33:47): Okay.
**Luís Braga** (01:33:47): So I'm going to try and have this working.
**Luís Braga** (01:33:50): Again, the middleware boom 192.
**Luís Braga** (01:33:55): Yeah.
**Luís Braga** (01:33:57): So I guess compiled sign in.
**Luís Braga** (01:34:00): Oh, what?
**Luís Braga** (01:34:01): Okay.
**Luís Braga** (01:34:02): Some.
**Luís Braga** (01:34:03): Request detected.
**Adrian Rinnus** (01:34:04): Matches in future versions.
**Adrian Rinnus** (01:34:07): Allow dev origins.
**Adrian Rinnus** (01:34:09): Okay, next config allows this.
**Adrian Rinnus** (01:34:14): Okay, but it's working, right?
**Luís Braga** (01:34:17): I guess I had an error in the tablet.
**Luís Braga** (01:34:23): I'm not sure.
**Luís Braga** (01:34:26): Can I even close it?
**Luís Braga** (01:34:28): No, it gives me field fetch, so I need to address this.
**Luís Braga** (01:34:32): I guess.
**Adrian Rinnus** (01:34:34): Yeah.
**Luís Braga** (01:34:35): So I need to add allow dev origins.
**Luís Braga** (01:34:39): And is it, where is it?
**Luís Braga** (01:34:45): Air, maybe?
**Luís Braga** (01:34:48): Future versions of it.
**Adrian Rinnus** (01:34:51): Next config.
**Adrian Rinnus** (01:34:53): You can also, okay.
**Adrian Rinnus** (01:34:56): Okay.
**Luís Braga** (01:35:00): So sign sign in.
**Luís Braga** (01:35:02): Okay.
**Luís Braga** (01:35:02): Thank you.
**Adrian Rinnus** (01:35:08): What you could do is you can clean the context in the cloud code and tell it to read the documentation of Next.js and tell it to that what you want to do and try to access the app from a tablet in the same network while I have an error, what if I do sign in, help me get the config correct.
**Adrian Rinnus** (01:35:52): Wait, it should check context 7 for the right thing.
**Adrian Rinnus** (01:36:00): Use context 7.
**Luís Braga** (01:36:03): M-C-P for docs, context 7, you're going to work, did you clear the context, I did, it's just when you resize it, you see clear there, I don't know, anyway, maybe it's in the wrong place, because it still, it seems I have added it there, but it still complains.
**Luís Braga** (01:36:46): Okay, in the meantime, let's have a look at the NFC documentation, why have I closed, let me open the pitch again.
**Luís Braga** (01:37:01): you.
**Luís Braga** (01:37:01): Thank you.
**Luís Braga** (01:37:02): Thank you.
**Luís Braga** (01:37:02): You
**Luís Braga** (01:37:03): Commits page, page, page, page, page.
**Luís Braga** (01:37:07): And do I have the page?
**Luís Braga** (01:37:08): Yes.
**Luís Braga** (01:37:09): So let's say this is cleaned.
**Luís Braga** (01:37:11): We, do we want to have, we don't need a button.
**Luís Braga** (01:37:16): No.
**Luís Braga** (01:37:17): The listener could be there.
**Luís Braga** (01:37:19): Yeah.
**Luís Braga** (01:37:21): All right.
**Luís Braga** (01:37:22): Can I, I'll use another quote.
**Adrian Rinnus** (01:37:30): Let me see if there is something on Context 7 about the NFC stuff.
**Adrian Rinnus** (01:37:37): Web NFC is it called, right?
**Adrian Rinnus** (01:37:40): Ah,  it.
**Luís Braga** (01:37:42): Let's use Claude.
**Adrian Rinnus** (01:37:45): No.
**Adrian Rinnus** (01:37:46): No?
**Adrian Rinnus** (01:37:47): We can use Claude to understand what is happening, but we will at least understand by ourselves that we know what is happening there and how it works.
**Adrian Rinnus** (01:37:56): Yeah.
**Adrian Rinnus** (01:37:56): Hey.
**Adrian Rinnus** (01:37:57): Do you know?
**Luís Braga** (01:37:58): Yes, of course.
**Luís Braga** (01:37:59): This was.
**Luís Braga** (01:38:00): Okay.
**Luís Braga** (01:38:00): Let's see.
**Luís Braga** (01:38:01): Signing.
**Luís Braga** (01:38:02): No.
**Luís Braga** (01:38:03): So.
**Luís Braga** (01:38:03): Filled to fetch, let me refresh the page, yeah, here we go, 200, wasn't me yet, I don't know, I mean, I just reloaded the page, test at test.com and test, test, boom, filled to fetch, no, it's not even, there is nothing popping in.
**Adrian Rinnus** (01:38:33): But network 0003000, I'm not sure if that is right, because I think the network started with bun.
**Luís Braga** (01:38:43): Man, all I know, yeah, it does load for me, you see, but I'm pretty sure it was me adding that one on the package and it was a means for me to, because think about it.
**Luís Braga** (01:39:01): Anyway, test, test, okay, but.
**Luís Braga** (01:39:03): It's weird that it doesn't even eat the server when I do login, so I wonder, is it 102, it should be 102.3, okay, so why the , if I, okay, back to home page, yeah, okay, it's there, then I do login, it's there, then I do tests at test.com, and then tests.
**Luís Braga** (01:39:33): Tests, go, bell to fetch, what the , there's one issue, what does it say, ah, it doesn't ring a bell to me, look at this, can I maybe try and show you what I have, can can you.
**Adrian Rinnus** (01:40:03): It's weird that it doesn't even eat the server when I do login, so I wonder, is it 102, it should be 102.3, okay, so why the , if I, okay, back to home page, yeah, okay, it's there, then I do login, it's there, then I do tests at test.com, and then tests.
**Luís Braga** (01:40:33): Tests, go, bell to fetch, what the , there's one issue, what does it say, ah, it doesn't ring a bell to me, look at this, can I maybe try and show you what I have, can can you.
**Adrian Rinnus** (01:41:03): Yeah, I'm trying.
**Adrian Rinnus** (01:41:05): Or just take a picture and send it to me on Slack or WhatsApp, I can't see.
**Luís Braga** (01:41:10): I don't know.
**Luís Braga** (01:41:11): Remove the background blur, then it should also work.
**Luís Braga** (01:41:29): Copy.
**Luís Braga** (01:41:33): Slack.
**Luís Braga** (01:41:34): Slack my  up.
**Luís Braga** (01:41:38): Oh, , really?
**Luís Braga** (01:41:41): I'll drop them.
**Luís Braga** (01:41:45): Hmm?
**Luís Braga** (01:41:46): Yep.
**Luís Braga** (01:41:47): Yeah, I'll show it here on the screen.
**Luís Braga** (01:41:49): You don't have to send it to me.
**Luís Braga** (01:41:50): You can even just show it here.
**Luís Braga** (01:41:52): Yep.
**Luís Braga** (01:41:54): There.
**Luís Braga** (01:41:55): Okay.
**Luís Braga** (01:41:56): Sububase, sign in with password, log in.
**Luís Braga** (01:41:59): And I think that the problem is that the superfaces.
**Luís Braga** (01:42:03): Superfaces.
**Luís Braga** (01:42:03): It's not accepting it in that sense.
**Luís Braga** (01:42:07): What if, what if I do this and I ask Clause, I'm still having this error.
**Adrian Rinnus** (01:42:20): Check also Superbase.
**Adrian Rinnus** (01:42:22): By the way, using, what is it again?
**Adrian Rinnus** (01:42:42): Maybe, there's some Superbase config needed?
**Luís Braga** (01:42:49): I don't know.
**Adrian Rinnus** (01:42:52): I don't know.
**Adrian Rinnus** (01:42:53): I don't know.
**Luís Braga** (01:42:53): What the  do I know?
**Adrian Rinnus** (01:43:00): Cultivating.
**Adrian Rinnus** (01:43:00): look.
**Adrian Rinnus** (01:43:00): Thanks.
**Adrian Rinnus** (01:43:00): you.
**Luís Braga** (01:43:13): The issue is that your Superbase URL sets are, yep.
**Adrian Rinnus** (01:43:19): Yep.
**Adrian Rinnus** (01:43:19): Okay.
**Adrian Rinnus** (01:43:20): Yeah, sure.
**Adrian Rinnus** (01:43:25): But where is the Superbase set in the wrong way?
**Adrian Rinnus** (01:43:29): Ah, yes.
**Adrian Rinnus** (01:43:31): Okay.
**Adrian Rinnus** (01:43:32): Yeah, that's the thing.
**Luís Braga** (01:43:33): Well, this sucks.
**Adrian Rinnus** (01:43:35): Oh, it's local.
**Adrian Rinnus** (01:43:37): Yeah.
**Luís Braga** (01:43:37): Okay, as long as this is.
**Luís Braga** (01:43:40): But this is, does it still work on your machine now with the, on the MacBook if you run it?
**Luís Braga** (01:43:46): What is he doing?
**Luís Braga** (01:43:47): What's the subconfig?
**Luís Braga** (01:43:49): Yeah, this is Superbase, I think, yeah, that's pretty fine.
**Luís Braga** (01:43:53): I mean, as long as I have a reserved IP address.
**Luís Braga** (01:43:57): Nice.
**Adrian Rinnus** (01:43:58): Yeah, and it's just a local one, that should be fine.
**Adrian Rinnus** (01:44:01): Yeah.
**Adrian Rinnus** (01:44:02): But please don't push down.
**Adrian Rinnus** (01:44:06): Do we really need it?
**Adrian Rinnus** (01:44:08): Yeah, this is Superbase configuration, we need that one.
**Luís Braga** (01:44:12): right, so Superbase restart, maybe?
**Luís Braga** (01:44:16): Yeah.
**Luís Braga** (01:44:20): No, it's not BAN run, if you have the Superbase CLI, just Superbase.
**Luís Braga** (01:44:27): No, it's not in BAN, not BAN, yeah.
**Luís Braga** (01:44:32): Yeah.
**Luís Braga** (01:44:33): Okay, stop.
**Luís Braga** (01:44:34): Yeah.
**Luís Braga** (01:44:35): And stop.
**Luís Braga** (01:44:40): BANDEV network, I don't know where the  he got this package.
**Luís Braga** (01:44:47): BANDEV-network, it's not there, I don't know.
**Luís Braga** (01:44:51): So, starts, are you still good with time?
**Luís Braga** (01:44:58): Hmm?
**Luís Braga** (01:44:58): Are you still good with time?
**Luís Braga** (01:45:00): Yeah.
**Luís Braga** (01:45:01): I think half an hour more.
**Luís Braga** (01:45:03): Then I will have dinner, and then I need to take care about Matisse.
**Adrian Rinnus** (01:45:16): All right, Bonnetwork.
**Luís Braga** (01:45:22): Oh, it's ready.
**Adrian Rinnus** (01:45:23): Check on your local machine first to see if it's working there.
**Adrian Rinnus** (01:45:27): All right.
**Luís Braga** (01:45:29): All right, in my local machine, reload, tests, at test.com, test tests.
**Adrian Rinnus** (01:45:41): Yes, right, so.
**Adrian Rinnus** (01:45:48): All right, so now, moment of truth.
**Adrian Rinnus** (01:45:53): Tests at tests.com, tests, tests, go.
**Adrian Rinnus** (01:46:03): Achilles, You
**Adrian Rinnus** (01:46:07): Uh, what the ?
**Adrian Rinnus** (01:46:11): Right, it just exploded.
**Luís Braga** (01:46:18): It looks like you resetted the form and I went nowhere.
**Luís Braga** (01:46:24): So could it be redirect or something?
**Luís Braga** (01:46:27): What is the IP that you are using now?
**Luís Braga** (01:46:30): In the tablets?
**Luís Braga** (01:46:32): Yeah.
**Adrian Rinnus** (01:46:34): Same thing.
**Adrian Rinnus** (01:46:35): And this is the middleware, which is  with us here, because it is checking for the subdomain Kaseich and redirecting it there.
**Luís Braga** (01:46:48): Tech localhost null null, localhost Kaseich, Kaseich tech.
**Luís Braga** (01:46:53): The point is, if there is a dot inside, this is  with us.
**Luís Braga** (01:47:01): 192 is there.
**Luís Braga** (01:47:03): Can you scroll even further down, further?
**Luís Braga** (01:47:11): think the return includes...
**Luís Braga** (01:47:18): Should I ask Claude?
**Luís Braga** (01:47:20): Yeah.
**Luís Braga** (01:47:26): Double check if any change is necessary.
**Adrian Rinnus** (01:47:32): And also, describe the fault that you see, or the issue that you see.
**Adrian Rinnus** (01:47:37): The redirect to the application is not working, it's sending us always back to the sign-in.
**Luís Braga** (01:47:43): Login in my network device.
**Luís Braga** (01:47:53): Sign-in and it seems I'm redirected.
**Luís Braga** (01:48:02): To...
**Luís Braga** (01:48:02): ...
**Luís Braga** (01:48:03): ...
**Luís Braga** (01:48:04): And also write that you are using the IP address.
**Adrian Rinnus** (01:48:09): And this device, device, I'm using, well, And in the meantime, I'll try, I think I have NFC tools in my iPhone.
**Adrian Rinnus** (01:48:48): I should put the internal ID or something there.
**Luís Braga** (01:48:59): NFC tools.
**Luís Braga** (01:49:00): Escrever.
**Luís Braga** (01:49:02): Write.
**Adrian Rinnus** (01:49:02): So.
**Adrian Rinnus** (01:49:03): How do I do this, right, add to save, what, I guess we want, we want what, just plain text?
**Luís Braga** (01:49:23): No, I think if we put the password on it, because we could also think about that they use the NFC tag to log in, and then we should have it transcripted, somehow encrypted, but in the first step, it's plain text.
**Luís Braga** (01:49:39): Let's do it plain text in the first one, but later on, I would also use an encrypted password, and with a salt and stuff that they just put it, for example, you could use your phone to log in by just putting the on the back of the phone, and it's logging you in.
**Luís Braga** (01:49:56): But it means it's, yeah, let's think about it later, but because it means doesn't make a problem.
**Luís Braga** (01:50:03): we lose it, it's sensitive data.
**Luís Braga** (01:50:05): don't know.
**Luís Braga** (01:50:06): Yeah.
**Adrian Rinnus** (01:50:08): But if they lose it, we can disable it.
**Luís Braga** (01:50:09): So I would use a different login thing.
**Luís Braga** (01:50:12): Yeah, good point.
**Luís Braga** (01:50:14): Yeah.
**Luís Braga** (01:50:15): That we are able to disable it.
**Adrian Rinnus** (01:50:19): Right.
**Adrian Rinnus** (01:50:20): Did I just save?
**Adrian Rinnus** (01:50:21): Anyway, fixed.
**Adrian Rinnus** (01:50:23): What has it done?
**Adrian Rinnus** (01:50:25): Middleware.
**Adrian Rinnus** (01:50:26): Where's the change?
**Luís Braga** (01:50:28): There.
**Luís Braga** (01:50:28): What?
**Luís Braga** (01:50:29): No.
**Luís Braga** (01:50:30): Where?
**Luís Braga** (01:50:30): Where?
**Luís Braga** (01:50:32): And circle-based middleware.
**Luís Braga** (01:50:33): Okay.
**Luís Braga** (01:50:35): There.
**Luís Braga** (01:50:36): Does it make sense to you?
**Luís Braga** (01:50:37): I don't know.
**Luís Braga** (01:50:38): Let's see.
**Luís Braga** (01:50:39): Let's see.
**Luís Braga** (01:50:39): Just in case, I'll do this.
**Luís Braga** (01:50:46): I don't need cable anymore.
**Luís Braga** (01:50:49): All right.
**Luís Braga** (01:50:49): Ready.
**Luís Braga** (01:50:50): And I'll do refresh.
**Luís Braga** (01:50:51): Compile.
**Luís Braga** (01:50:53): Login.
**Adrian Rinnus** (01:50:54): Good.
**Adrian Rinnus** (01:50:55): Now.
**Luís Braga** (01:50:58): Test.
**Luís Braga** (01:51:00): Test.
**Luís Braga** (01:51:01): .com.
**Luís Braga** (01:51:02): Test.
**Luís Braga** (01:51:03): Let's test my balls.
**Luís Braga** (01:51:05): Go.
**Luís Braga** (01:51:06): Invalid login credentials, we're getting somewhere.
**Luís Braga** (01:51:09): I wonder why there's nothing there.
**Luís Braga** (01:51:13): What?
**Luís Braga** (01:51:14): That's weird.
**Luís Braga** (01:51:16): Test?
**Luís Braga** (01:51:17): Yeah, because it's redirected to Superbase, that's fine.
**Luís Braga** (01:51:21): That makes sense.
**Luís Braga** (01:51:22): Sign in?
**Luís Braga** (01:51:24): Don't use the main form.
**Luís Braga** (01:51:27): , nothing happened.
**Luís Braga** (01:51:29): I don't know what the  is going on.
**Luís Braga** (01:51:31): So again, test, test.com, test, test.
**Luís Braga** (01:51:39): I'm gonna do this.
**Luís Braga** (01:51:41): Sign in, what do I see?
**Luís Braga** (01:51:42): I don't  know what I'm seeing.
**Adrian Rinnus** (01:51:49): But again, it goes to the login again.
**Adrian Rinnus** (01:51:53): Okay.
**Adrian Rinnus** (01:51:55): We start with that server.
**Adrian Rinnus** (01:51:57): Let's see.
**Adrian Rinnus** (01:51:58): What's this  comment is suggesting?
**Adrian Rinnus** (01:52:02): It's for shins, right?
**Adrian Rinnus** (01:52:03): Thank you.
**Adrian Rinnus** (01:52:03): Mm-hmm, sorry for the new IP address detection, blah, blah, blah, all right, again, back to one page, actually, back to one page, and login, past.
**Adrian Rinnus** (01:52:35): test.com, test, test, go, yeah, bullshits.
**Adrian Rinnus** (01:52:44): Okay, but then, let me see.
**Luís Braga** (01:53:03): Script and onboarding rework issues, no, it was subdomain, takes middleware, ignoring the cell deployment, that was me, featuring subdomain employee, this is it, so we have the API tenants route, check for, I will send you the commit message, then we have all the files that we need to check.
**Luís Braga** (01:53:37): This is the commit hash, and there it is, there we see what is changed, super base client, what is happening here, a lot of  , get the main cookie.
**Luís Braga** (01:53:51): So you send me a commit hash, do you want me to ask for to check it?
**Luís Braga** (01:53:55): Yeah, that was the change for the subdomain and this needs to be aligned to, that we now need to run.
**Luís Braga** (01:54:03): And localhost as well, and it should work, because there's the shop domain handling, there's changes that are probably later.
**Luís Braga** (01:54:33): And then read, and so it's reading the tag, and I have, I don't know, I don't know what's this, can you see the screen, can you see the two bottom rows, so it says recordable.
**Luís Braga** (01:55:03): Yes.
**Luís Braga** (01:55:06): So maybe there's a way for us to lock writing on the NFC.
**Luís Braga** (01:55:11): I'm not sure.
**Luís Braga** (01:55:12): But the last line is what's interesting.
**Luís Braga** (01:55:15): It says recording one dash text and then the value.
**Luís Braga** (01:55:22): I'm not sure why it says recording one, but if I press it, it says text.
**Adrian Rinnus** (01:55:33): And I don't know.
**Adrian Rinnus** (01:55:35): We should try it later.
**Luís Braga** (01:55:37): So more changes in the clients.
**Luís Braga** (01:55:42): That's a problem.
**Luís Braga** (01:55:43): The client-side cookie function also needs the IP fix.
**Adrian Rinnus** (01:55:49): Fixed, he said.
**Adrian Rinnus** (01:55:50): I don't know.
**Adrian Rinnus** (01:55:54): Let's see.
**Luís Braga** (01:55:55): Perfect.
**Luís Braga** (01:55:56): He's confident.
**Luís Braga** (01:55:57): I'm confident as well.
**Adrian Rinnus** (01:55:59): All right.
**Adrian Rinnus** (01:56:00): Ready?
**Adrian Rinnus** (01:56:01): Refresh.
**Adrian Rinnus** (01:56:02): There we go.
**Adrian Rinnus** (01:56:03): well.
**Adrian Rinnus** (01:56:03): Let's
**Luís Braga** (01:56:03): All right, so email address, test, and I'll test, test, please  work.
**Luís Braga** (01:56:13): I think it's going to work, man.
**Luís Braga** (01:56:15): It is.
**Luís Braga** (01:56:18): All righty.
**Luís Braga** (01:56:19): It's also still working on your MacBook.
**Adrian Rinnus** (01:56:23): Yeah, for sure.
**Adrian Rinnus** (01:56:26): Wow, reloading is working.
**Luís Braga** (01:56:27): So good.
**Luís Braga** (01:56:29): All right.
**Luís Braga** (01:56:31): Delivery.
**Luís Braga** (01:56:32): Of course.
**Luís Braga** (01:56:33): All right, then do a comment for that.
**Luís Braga** (01:56:35): Tell Claude to do a comment.
**Luís Braga** (01:56:38): But, but wait, what, what, you mentioned that Tom, this one?
**Luís Braga** (01:56:47): Yeah, this should not be, because it's your specific.
**Luís Braga** (01:56:54): This is not mine specific, is it?
**Luís Braga** (01:56:57): It is your IP address, but anyways, yeah.
**Luís Braga** (01:56:59): Keep this.
**Luís Braga** (01:57:00): Yeah, keep it.
**Adrian Rinnus** (01:57:01): It's okay.
**Adrian Rinnus** (01:57:02): Commit it.
**Adrian Rinnus** (01:57:03): It's fine.
**Adrian Rinnus** (01:57:03): fine.
**Luís Braga** (01:57:07): Do a comment, please.
**Luís Braga** (01:57:13): And now, what do you propose?
**Luís Braga** (01:57:15): Go in Cabo style with Claude or do it by ourselves and learn?
**Luís Braga** (01:57:23): Do it by ourselves to understand what we are doing.
**Luís Braga** (01:57:27): Cool.
**Luís Braga** (01:57:28): NFC API.
**Luís Braga** (01:57:32): Old school.
**Luís Braga** (01:57:33): Blah, blah, blah.
**Adrian Rinnus** (01:57:35): Okay.
**Adrian Rinnus** (01:57:36): I am already lost.
**Adrian Rinnus** (01:57:38): I never got these pages.
**Adrian Rinnus** (01:57:41): Whatís this?
**Adrian Rinnus** (01:57:43): Ender reader is the thing that we have to tackle.
**Adrian Rinnus** (01:57:46): All right.
**Luís Braga** (01:57:47): So thereís a scan method.
**Luís Braga** (01:57:49): We want it.
**Luís Braga** (01:57:52): Okay.
**Luís Braga** (01:57:53): New NFC reader.
**Luís Braga** (01:57:55): And I suppose we are going to need a client component.
**Luís Braga** (01:58:00): So we have the...
**Luís Braga** (01:58:01): What was the commit message now?
**Luís Braga** (01:58:03): What You know are
**Luís Braga** (01:58:03): Off the fucker.
**Luís Braga** (01:58:05): Let's see.
**Luís Braga** (01:58:07): Fix config enable local network.
**Luís Braga** (01:58:09): That's good.
**Luís Braga** (01:58:10): Yep.
**Luís Braga** (01:58:11): All right.
**Luís Braga** (01:58:15): So I guess we're going to have a new component called, let's see, features delivery.
**Luís Braga** (01:58:25): Where is it?
**Luís Braga** (01:58:27): Distribution, meal distribution, one of them.
**Luís Braga** (01:58:31): Components.
**Luís Braga** (01:58:32): Cool.
**Luís Braga** (01:58:32): And we're going to call it.
**Luís Braga** (01:58:36): Yeah, let's put it there.
**Luís Braga** (01:58:37): But I think we should move it later on.
**Luís Braga** (01:58:38): Because if we think about NFC login also for ordering, it would be an own feature.
**Adrian Rinnus** (01:58:44): But anyways, let's put it here for now.
**Adrian Rinnus** (01:58:48): NFC reader.
**Adrian Rinnus** (01:58:49): Yep.
**Adrian Rinnus** (01:58:51): All right.
**Adrian Rinnus** (01:58:52): And then react arrow function component.
**Luís Braga** (01:58:55): I don't think this is working for me anymore.
**Luís Braga** (01:58:57): So exports.
**Adrian Rinnus** (01:59:01): Costs.
**Adrian Rinnus** (01:59:01): Consts.
**Adrian Rinnus** (01:59:03): After you.
**Adrian Rinnus** (01:59:03): Either, I'll just do it like this, and SEO Reader, my God, I love, you're so  smart, and SEO Reader wears these, all right, we got it, what the  is this, colon, doing, oh, good, so, and this was gonna be use client, yes, yep, and now, boom, what the  is this, no  idea.
**Luís Braga** (01:59:44): Here, what the scan method, the Fath activates, plan by promise, scan method, let's check the GitHub repository of the guy, and let's see what he did.
**Luís Braga** (01:59:56): That I've sent you, and where is this?
**Luís Braga** (01:59:58): I wait, I have it open still, and I can send it to you.
**Luís Braga** (02:00:02): What, the account?
**Luís Braga** (02:00:07): No, sent it in, tell me, in Google Meet, I will send it to you.
**Luís Braga** (02:00:14): Please.
**Luís Braga** (02:00:17): Here we go.
**Adrian Rinnus** (02:00:23): This is already a scan.
**Luís Braga** (02:00:28): How do you work with the different desktops?
**Luís Braga** (02:00:34): What do you mean exactly?
**Luís Braga** (02:00:36): So what is your workflow with it?
**Luís Braga** (02:00:39): I'm not very strict, but normally I have some  open, but as you see, ideally I do this.
**Luís Braga** (02:00:49): have, for instance, commit there and then I just do control left or right and switch.
**Luís Braga** (02:00:55): The thing is, I'm so used to use command tab to, it shows in my main screen.
**Adrian Rinnus** (02:01:03): You know this.
**Luís Braga** (02:01:03): to cycle between apps that it messes a bit the order that we see here.
**Luís Braga** (02:01:11): Okay.
**Luís Braga** (02:01:11): Normally I keep in my mind, so here I have the editor, here I have the browser or whatever.
**Luís Braga** (02:01:17): Mm-hmm.
**Luís Braga** (02:01:18): For instance, now it's  up.
**Luís Braga** (02:01:20): I guess this is the browser, yes.
**Adrian Rinnus** (02:01:23): Okay.
**Luís Braga** (02:01:23): Yeah, anyways.
**Luís Braga** (02:01:25): You see, I'm gonna close this because it's not really the browser.
**Adrian Rinnus** (02:01:30): I don't know where the browser is, you see.
**Luís Braga** (02:01:34): I'm  up this.
**Luís Braga** (02:01:37): Did I  close the browser?
**Luís Braga** (02:01:40): Oh, it's there.
**Luís Braga** (02:01:41): Okay, good.
**Luís Braga** (02:01:41): So I put it there.
**Luís Braga** (02:01:43): Now browser code, browser code.
**Luís Braga** (02:01:45): I shouldn't have asked you.
**Adrian Rinnus** (02:01:49): All right, cool.
**Adrian Rinnus** (02:01:50): But I think we need, scanner, they have a component scanner, I guess they might have, ah, window.
**Adrian Rinnus** (02:01:56): Yeah, and the window, the, okay, this is it.
**Adrian Rinnus** (02:02:00): Okay, let's go simple for now, I guess?
**Adrian Rinnus** (02:02:03): Yeah.
**Adrian Rinnus** (02:02:03): of line, it's Okay.
**Adrian Rinnus** (02:02:03): Oh, Okay,
**Luís Braga** (02:02:03): So, new window dot, maybe needs types, new, did I, just copy and paste the whole , yeah, we probably need types, no, interesting, that vitals, I don't see, don't see , user events, no, no, oh, what the  then, or maybe there's some TS special config, I don't see, NFC, SVG, no, set up test, no, and the FJS probably because it's a, could be because it's a react app, is there something happening, nope.
**Luís Braga** (02:03:03): It's not.
**Luís Braga** (02:03:10): Ah, the action context, do you see use context action, but this is no, this is something from the scanner,  , .
**Luís Braga** (02:03:19): This would be scan, scan, scan, ah, on reading, so.
**Luís Braga** (02:03:30): Yeah, use the whole code block from there to see if it's working, so.
**Luís Braga** (02:03:35): Scan, scan.
**Luís Braga** (02:03:38): Let's copy and paste the code from here to see if we get something up and work, then we use chat.
**Luís Braga** (02:03:45): I would use the whole, the whole thing.
**Luís Braga** (02:03:47): Really?
**Luís Braga** (02:03:49): Really?
**Luís Braga** (02:03:49): The whole thing there?
**Luís Braga** (02:03:51): So copy and paste and yeah, scanner.
**Adrian Rinnus** (02:03:58): What, what's scanner?
**Adrian Rinnus** (02:04:00): Scanner.
**Adrian Rinnus** (02:04:02): Scanner.
**Adrian Rinnus** (02:04:03): Scanner.
**Adrian Rinnus** (02:04:03): don't
**Adrian Rinnus** (02:04:03): Scanner, ah , context, context, context, Jesus, should I copy all this, well whatís the scanner doing, just showing actions from actions context, it takes actions and set actions and I donít get it, actions, where the  is actions coming from, scanner, actions, what man, I donít get this, use context, actions, context, two levels up, context, context, set actions and actions, I donít see actions, am I  lying?
**Luís Braga** (02:04:57): Ah, the, but the, what the hell, okay.
**Luís Braga** (02:05:04): I don't, I also don't get it, um, again, again, or, this is weird, actions, use context, there's nothing special about use context, like, this isn't, actions is not  returns, context, set action, okay, probably, it's a  library here, so yeah, wait, um, next.js, Hey, NFC Link Manager,
**Luís Braga** (02:06:04): It's using Superbase and Next.js, okay, I just found, I have no idea what it is doing, let me see, link mention of a cell app, sign into your account, okay, what is it?
**Luís Braga** (02:06:23): And, but I think, log, and that, what, what  name is this, and that, I'm curious to see what the browser should, window is not a constructor, man, I'm looking for, to try a cloth, what are you saying?
**Luís Braga** (02:06:51): Yeah, that's okay.
**Luís Braga** (02:07:02): I want to...
**Luís Braga** (02:07:04): Use these components to read NFC tags, plan.
**Luís Braga** (02:07:30): I've logged in as admin, but I can switch delivery.
**Luís Braga** (02:07:36): Do I need to switch from the dashboard?
**Luís Braga** (02:07:40): No.
**Luís Braga** (02:07:43): Tablet, I don't think I see the switch.
**Luís Braga** (02:07:45): Ah, yeah, in the dashboard, there's the switcher.
**Luís Braga** (02:07:48): And I do kitchen dashboards and then delivery, I guess.
**Luís Braga** (02:07:58): And I can do this.
**Luís Braga** (02:08:00): And actually, one, two, three, four, five.
**Luís Braga** (02:08:04): Reads, amazing.
**Luís Braga** (02:08:13): Oh.
**Luís Braga** (02:08:14): do do do do do do do do do do do do do do do And that freedom, what the  hell.
**Luís Braga** (02:08:28): The next dress.
**Luís Braga** (02:08:31): Ponceva, it doesn't matter.
**Luís Braga** (02:08:34): Now I understand the context.
**Adrian Rinnus** (02:08:36): This is for a kitchen delivery page where staff can look up employee meal orders either by manually entering an internal.
**Adrian Rinnus** (02:08:46): Okay, implement the main NFC reading functionality.
**Adrian Rinnus** (02:08:49): Check browser and, yes, support.
**Adrian Rinnus** (02:08:51): Yes, cool.
**Luís Braga** (02:08:52): Add scan.
**Luís Braga** (02:08:54): Requires user.
**Adrian Rinnus** (02:08:55): Ah, got it.
**Adrian Rinnus** (02:08:56): It makes sense.
**Adrian Rinnus** (02:08:57): It's kind of security.
**Adrian Rinnus** (02:08:59): Yeah.
**Adrian Rinnus** (02:08:59): That is interaction.
**Adrian Rinnus** (02:09:01): So we really need a button.
**Luís Braga** (02:09:02): We can just, we cannot.
**Luís Braga** (02:09:04): cannot.
**Luís Braga** (02:09:04): We cannot.
**Luís Braga** (02:09:04): Just have it listening all the time.
**Adrian Rinnus** (02:09:05): So handle the, blah, blah, blah, parse, query orders, blah, blah, blah, display results, similar, yes, show, start, all right, cool, translation, oh, cool, you know so much already, use this, navigator, okay, self-contained, okay, looks good.
**Luís Braga** (02:09:27): Do you have any?
**Luís Braga** (02:09:29): No, that's all right.
**Luís Braga** (02:09:32): All right.
**Luís Braga** (02:09:34): I was also thinking about what we could do is, in the worst-case scenario, that we use some kind of background service on the Android device, which is just reading the NFC tag and sending it to our API or to the application, to an API.
**Luís Braga** (02:09:49): Yeah, like with some deep link.
**Luís Braga** (02:09:54): Yeah, or an API, you know, that we have an API in our next OS thing.
**Adrian Rinnus** (02:10:01): Oh, yeah, Like with the coule retirar.
**Adrian Rinnus** (02:10:04): 2014.
**Luís Braga** (02:10:04): Yeah, we were just sending that we get some token, more or less, the app has a token, and the web app has a token, and they are connected somehow, and it's real-time data, and whatever, I don't know.
**Luís Braga** (02:10:19): Let's see if we did it like that.
**Luís Braga** (02:10:35): In the meantime, how was the feeling with Zay, the meeting?
**Luís Braga** (02:10:41): Is he happy?
**Luís Braga** (02:10:42): Yeah, he is.
**Adrian Rinnus** (02:10:43): Like, at least he's, it seems like he's sensitive to the amount of, the crazy amount of work that is put in place, right?
**Adrian Rinnus** (02:10:57): Yeah, he is.
**Adrian Rinnus** (02:10:58): He's aware.
**Luís Braga** (02:10:59): I think so, yes.
**Luís Braga** (02:11:01): And he also sees that we are fixing all the things that they are...
**Adrian Rinnus** (02:11:04): That we are taking care of their wishes and so on and so on.
**Adrian Rinnus** (02:11:08): So look at this, sorry to interrupt, look at this amount of code you already put it in place.
**Luís Braga** (02:11:16): I wonder why, because orders grouped by they part, why is it not using shared components?
**Luís Braga** (02:11:24): Maybe it will.
**Luís Braga** (02:11:25): Yeah, let's see.
**Luís Braga** (02:11:31): Oh, !
**Luís Braga** (02:11:33): I already seen the tablet, NFC is not supported.
**Luís Braga** (02:11:36): Please use Chrome or Edge on an Android device, but I'm using you dumb .
**Luís Braga** (02:11:43): Is that, the, if you open the, um, wait, I sent you, no, you can also check it.
**Luís Braga** (02:11:49): On the GitHub, there is an URL, try to open it and try to scan the NFC tag with the tablet.
**Luís Braga** (02:11:58): So let's see here, you mean?
**Adrian Rinnus** (02:12:02): Yeah, there is, on the top.
**Luís Braga** (02:12:04): Yeah, on the top right there is the, here, React, NFC, blah, blah, blah.
**Luís Braga** (02:12:10): If you scan it, okay, scan.
**Luís Braga** (02:12:13): I need to open it in the browser.
**Luís Braga** (02:12:17): Oh, so much.
**Luís Braga** (02:12:19): No wonder this is slow.
**Luís Braga** (02:12:21): In the meantime, oh, okay, okay, okay, okay, okay.
**Luís Braga** (02:12:30): If not, I might have some old smart phone.
**Luís Braga** (02:12:37): Jesus, so many, oof.
**Luís Braga** (02:12:41): All right, just need some, what?
**Luís Braga** (02:12:46): Just need some grooming.
**Luís Braga** (02:12:49): I have 40, 40 something tabs open.
**Luís Braga** (02:12:53): No wonder this   is slow.
**Luís Braga** (02:12:56): Or it could be that, oh, 32, close.
**Luís Braga** (02:12:59): Which browser do you use on the...
**Luís Braga** (02:13:01): Yeah, this is that in Chrome, but I...
**Luís Braga** (02:13:04): I have no idea what's the version, not even the Android version, but it's not, is it, is it, is it OS-related?
**Luís Braga** (02:13:13): No, I don't think so.
**Luís Braga** (02:13:17): Yeah.
**Luís Braga** (02:13:18): All right.
**Luís Braga** (02:13:19): Close, close.
**Luís Braga** (02:13:25): Where is it?
**Luís Braga** (02:13:26): Okay.
**Luís Braga** (02:13:26): There, got it.
**Luís Braga** (02:13:27): And again, the server, the URL.
**Luís Braga** (02:13:32): Oh, what does it say there?
**Luís Braga** (02:13:34): Yes, not supported, of course.
**Luís Braga** (02:13:37): So, new tab, and it's react-nfc, react, dash, no, react, where is it, dash, dash, dash, dash.
**Luís Braga** (02:13:54): There it's, dash, nfc, dash.
**Luís Braga** (02:14:05): Thatís what, 9146.web.app, scan, allow, scanning it says, so whereís the thing?
**Luís Braga** (02:14:31): Well, it should, I donít know, itís not working, could it be the case?
**Luís Braga** (02:14:37): If you go to write, you can write something on it.
**Luís Braga** (02:14:44): All right, write, enter message, test, what?
**Adrian Rinnus** (02:14:52): So I enter message, test, and then I guess save, but it just empties the input and does nothing.
**Luís Braga** (02:15:01): It looks like itís
**Adrian Rinnus** (02:15:04): It's not working.
**Luís Braga** (02:15:05): But shouldn't the  page tell me it's not supported right away?
**Luís Braga** (02:15:11): I don't know.
**Luís Braga** (02:15:14): Can you commit the changes and push it so I can try it on my phone?
**Luís Braga** (02:15:20): Sure.
**Luís Braga** (02:15:21): Scan.
**Luís Braga** (02:15:22): Yeah, it's doing nothing.
**Luís Braga** (02:15:24): Maybe it just doesn't support.
**Luís Braga** (02:15:27): I wonder if these  developers should have done his work, at least.
**Luís Braga** (02:15:32): No.
**Luís Braga** (02:15:34): All right.
**Luís Braga** (02:15:35): Do a web commit, maybe?
**Luís Braga** (02:15:38): Yeah.
**Luís Braga** (02:15:47): Ah, right, because you have an Android smartphone.
**Luís Braga** (02:15:50): Yes, exactly.
**Luís Braga** (02:15:51): Cool.
**Luís Braga** (02:15:54): What the hell?
**Luís Braga** (02:15:58): Works to use.
**Adrian Rinnus** (02:16:03): No.
**Adrian Rinnus** (02:16:03): .
**Luís Braga** (02:16:04): Because I have, just do a regular comment, don't use my commands, and because I have a custom command, what is checking the log?
**Luís Braga** (02:16:43): If you're able to do it, we can, nice, all right, oh, it pushed, no, no, push, create tracking reference, it's nice, nice, nice, what, ah, I cannot push, the other time, yeah, but then just ignore the push restrictions and we do
**Adrian Rinnus** (02:17:04): not push it but without the hook push it's just my ui it's gonna i'll do it i'm not sure if it's just agree because yeah there's something so just do a push without hook we fix it later push and skip yeah it would be nice um we like you know just yeah no verify okay done thank you
**Adrian Rinnus** (02:18:09): I'll quickly take a piece of this.
**Adrian Rinnus** (02:18:26): Thank you.
**Adrian Rinnus** (02:18:47): Thank you.
**Adrian Rinnus** (02:18:50): Thank you.
**Adrian Rinnus** (02:18:59): Thank you.
**Adrian Rinnus** (02:19:03): Thank you.
**Adrian Rinnus** (02:19:04): Thank you.
**Adrian Rinnus** (02:19:04): Thank Thank
**Adrian Rinnus** (02:19:06): Thank All right, all right, now I'm...
**Adrian Rinnus** (02:20:04): Check out, and now I have to restart everything, I guess, no I don't actually, I have to run now, ban run, what was it, dev network?
**Adrian Rinnus** (02:20:29): Yeah, dev colon network, I believe.
**Adrian Rinnus** (02:20:31): Okay and now I need to figure out what my address is.
**Adrian Rinnus** (02:20:36): How do I do that?
**Adrian Rinnus** (02:20:37): On MAC, press option and click on the wireless icon.
**Adrian Rinnus** (02:20:45): Okay.
**Luís Braga** (02:20:47): Address, yeah okay one, 1 2.168.
**Adrian Rinnus** (02:20:58): 168.178
**Adrian Rinnus** (02:21:06): .49, all in 3,000.
**Adrian Rinnus** (02:21:09): Here we  go.
**Adrian Rinnus** (02:21:11): Okay, let's see.
**Adrian Rinnus** (02:21:14): And now I want to accept employee login.
**Luís Braga** (02:21:23): Tenants not working.
**Adrian Rinnus** (02:21:26): Admin login.
**Adrian Rinnus** (02:21:31): Test at test.com.
**Adrian Rinnus** (02:21:37): Test.
**Adrian Rinnus** (02:21:39): Test.
**Adrian Rinnus** (02:21:40): Sign.
**Adrian Rinnus** (02:21:41): Failed to fetch.
**Adrian Rinnus** (02:21:43): Okay, that means?
**Adrian Rinnus** (02:21:46): What's your IPA?
**Adrian Rinnus** (02:21:52): 192.168.178.
**Adrian Rinnus** (02:21:56): I need to fix that.
**Adrian Rinnus** (02:21:57): Right.
**Adrian Rinnus** (02:21:58): The next config.
**Adrian Rinnus** (02:22:01): Okay.
**Adrian Rinnus** (02:22:03): This is.
**Adrian Rinnus** (02:22:05): I will just change it, like, oh,  off, allowed origins, dev origins, I think it's multiple things that I have to fix, next config, come on, this is  nine, this one here, what is it, option, it's, no, no, it's 178, 168, 178, okay, and then I need to check that one here as well, the config.tomer, superbase, config.tomer 192, I will just add mine as well, no, 178, 168, option 178, , 178, 49.
**Adrian Rinnus** (02:23:07): Okay, now I need to control C, super base, stop, super base, stop.
**Luís Braga** (02:23:21): Okay, I just found that, yeah, there's from the page, from the official, okay, there's a Chrome developers page where you have some official app, and I can see, when I press scan, I can see my, this is not supported in this device.
**Adrian Rinnus** (02:23:46): Okay, that's already the good news, you know, that Docker container response fail to, driver fail programming external connect to endpoint, already allocated,  you, Docker, why, why, echo this.
**Adrian Rinnus** (02:24:04): Okay.
**Adrian Rinnus** (02:24:04): That's Right.
**Adrian Rinnus** (02:24:04): Packer, where is token, yeah, come on, next app, five hours ago, yeah, I'll leave the, on slack I'll leave you the, link to this finding of mine, might come useful, yeah, let's see if it's working on my side, yeah mary
**Adrian Rinnus** (02:25:18): If you have to go, just go.
**Adrian Rinnus** (02:25:29): I will leave in a few minutes, but I also want to see that thing working, you know.
**Luís Braga** (02:25:34): Thatís the point.
**Adrian Rinnus** (02:25:37): Okay, SuperVa is starting.
**Adrian Rinnus** (02:25:39): All right, waiting for Hath checks out here.
**Luís Braga** (02:25:51): Okay, run, run, that network.
**Luís Braga** (02:25:56): Okay, reload.
**Adrian Rinnus** (02:26:03): Thank you.
**Adrian Rinnus** (02:26:04): Thank you.
**Adrian Rinnus** (02:26:04): Thank
**Adrian Rinnus** (02:26:10): Failed to fetch, mother fucker, okay, middleware, what is here, 192, this is here, middleware, yeah, this should be fine, client, this should also be fine, I think.
**Adrian Rinnus** (02:26:30): My changes, have you done the next config?
**Adrian Rinnus** (02:26:34): Yeah, so, wait, I'm checking, so my next config is one, yeah, this is fixed, this is, and the config comment is also there, yeah.
**Adrian Rinnus** (02:26:47): How about client TS, super based client TS?
**Adrian Rinnus** (02:26:53): Yeah.
**Adrian Rinnus** (02:26:55): Well, basically, in my comment, all of these, it's one, two, three, four, five files.
**Adrian Rinnus** (02:27:01): Yeah, exactly, and I was checking them.
**Adrian Rinnus** (02:27:04): Mm-hmm.
**Adrian Rinnus** (02:27:04): Yeah,
**Adrian Rinnus** (02:27:04): More or less, and you're running DevNetwork?
**Adrian Rinnus** (02:27:10): I'm running DevNetwork.
**Adrian Rinnus** (02:27:17): Yeah.
**Adrian Rinnus** (02:27:19): You call?
**Adrian Rinnus** (02:27:20): Yeah, but all's good.
**Adrian Rinnus** (02:27:22): I'm coming.
**Adrian Rinnus** (02:27:23): you want go?
**Adrian Rinnus** (02:27:25): Yeah, in the next few minutes.
**Adrian Rinnus** (02:27:27): I'll it later.
**Adrian Rinnus** (02:27:33): To fetch, why, fucker?
**Adrian Rinnus** (02:27:48): So what have I changed here?
**Adrian Rinnus** (02:27:55): Ah, config.com is there.
**Adrian Rinnus** (02:27:58): This is their host name for a P address.
**Luís Braga** (02:28:02): Host name, this is this.
**Luís Braga** (02:28:12): So, you did the middleware change, this is also here on my side, it's 192, this is okay, the middleware for the client, which is, I have checked out your stuff, so this is here, the client, this is their next config, next config is changed to 178, allowed dev origins, this means I have to enter my device or, but it doesn't matter, it's a wildcard, so...
**Luís Braga** (02:28:50): Yeah, but it's the three, I don't know, you need to...
**Adrian Rinnus** (02:28:53): For me it's 178, so your thing is the three, I have the 178, I have changed that one.
**Adrian Rinnus** (02:29:00): Oh, you did this a lot?
**Adrian Rinnus** (02:29:03): Yeah, I changed it to one...
**Luís Braga** (02:29:15): And you're sure you're on the same wireless network, I suppose, not 3G?
**Luís Braga** (02:29:23): one is okay, we're connected, but it's the same, yeah, and it's also loading here, it's also loading the page you see.
**Luís Braga** (02:29:31): Right, otherwise you wouldn't, yes.
**Luís Braga** (02:29:42): Fail to fetch.
**Adrian Rinnus** (02:29:44): Oh, hang on, could it be these super-based clients?
**Adrian Rinnus** (02:29:47): Because I don't understand  about this regex expression.
**Luís Braga** (02:29:52): Me too, super-based client.ts.
**Luís Braga** (02:29:59): Thank you.
**Adrian Rinnus** (02:30:02): Thank you.
**Adrian Rinnus** (02:30:04): Sisha Cipitini, explain this regex, oops, stuck, matches one to three digits, ah, what, so would it match, you say, one, one, one, six, eight, dot, whatever?
**Luís Braga** (02:30:38): One, seven, no, okay, it says, it will fail, what?
**Adrian Rinnus** (02:30:43): Yeah, but it's the end of the star, which is not working, so.
**Luís Braga** (02:30:49): Ah, okay, so it would do.
**Adrian Rinnus** (02:31:04): Yeah, it's fitting, it's working in that sense.
**Adrian Rinnus** (02:31:08): It's four blocks of three separated by dots.
**Adrian Rinnus** (02:31:13): Oh, yeah, yeah, right.
**Luís Braga** (02:31:17): So not a problem here.
**Luís Braga** (02:31:22): Same there.
**Adrian Rinnus** (02:31:25): Next config.
**Adrian Rinnus** (02:31:26): Ah, I know it.
**Adrian Rinnus** (02:31:27): I know it.
**Adrian Rinnus** (02:31:27): It's the, ah, I got it.
**Adrian Rinnus** (02:31:29): It's the nf.local where I have to use the 192.168.178.
**Adrian Rinnus** (02:31:38): Oh, yes.
**Adrian Rinnus** (02:31:40): The super base URL.
**Adrian Rinnus** (02:31:42): Yeah, exactly.
**Adrian Rinnus** (02:31:44): , man.
**Adrian Rinnus** (02:31:45): That's  .

## Kontext & Navigation
- [[DASHBOARD]]
- [[MEMORY]]
- [[OBSIDIAN_ROUTING]]
