# Impromptu Google Meet Meeting

## Metadata

- recording_id: 92322877
- created_at: 2025-10-07T13:05:31Z
- recorded_by: Adrian Rinnus
- meeting_url: https://fathom.video/calls/434203063
- speakers: Luís Braga, Adrian Rinnus

## Summary

{"template_name": "General", "markdown_formatted": "## Meeting Purpose\n\n[Discuss and plan the implementation of NFC functionality for a canteen ordering system.](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=120.0)\n\n## Key Takeaways\n\n  - [Implement a simple NFC-based check-in system for the canteen, focusing on an easy solution first](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=351.0)\n  - [Use NFC cards with unique IDs to retrieve user meal information for the current day](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=186.0)\n  - [Consider fallback options (QR codes, manual ID input) for devices without NFC support](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=712.0)\n  - [Plan to work together on implementing the NFC feature soon](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=791.0)\n\n## Topics\n\n### Current System Issues\n\n  - [Paper-based system is stressful and inefficient](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=226.0)\n  - [Some order contamination and invalid entries exist](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=387.0)\n  - [Challenges with employees changing canteens and order management](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=387.0)\n\n### NFC Implementation Plan\n\n  - [Create a check-in page that listens for NFC read events](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=712.0)\n  - [Use unique IDs on NFC cards to query the database for user's meal info](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=186.0)\n  - [Implement API endpoints to get user meal data based on ID and current date](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=300.0)\n  - [Consider adding a \"delivered\" flag to mark orders as completed](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=300.0)\n\n### Fallback Options\n\n  - [Include QR code scanning as an alternative to NFC](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=712.0)\n  - [Add manual ID input option for devices without NFC support](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=712.0)\n  - [Check for NFC availability in the browser and show appropriate input methods](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=712.0)\n\n### Future Enhancements\n\n  - [Implement a queue system for order preparation](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=327.0)\n  - [Add functionality for employees to specify eating locations (different canteens, on-site, off-site)](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=486.0)\n  - [Consider developing an iPad application for broader device support](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=660.0)\n\n### Testing and Development\n\n  - [Adrian considering ordering a tablet for on-site testing](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=523.0)\n  - [Luís offers to work on the NFC implementation using his old Samsung tablet](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=625.0)\n  - [Discussed potential use of Playwright and Superwright for end-to-end testing](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=902.0)\n  - [Mentioned AI agents for test planning, generation, and healing in Playwright](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=902.0)\n\n## Next Steps\n\n  - [Luís and Adrian to collaborate on implementing the NFC feature](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=791.0)\n  - [Adrian to commit current changes and clean up local development environment](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=1105.0)\n  - [Set up a follow-up meeting to work on the NFC implementation together](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=791.0)\n  - [Research and potentially implement Playwright and Superwright for testing in the future](https://fathom.video/share/EnYzrnxYo5jcRvzo1Lzu56ktnAgC5EN_?tab=summary&timestamp=902.0)\n"}

## Transcript

**Luís Braga** (00:00:02): Hello, hello.
**Adrian Rinnus** (00:00:04): What's happening?
**Luís Braga** (00:00:06): Not much.
**Luís Braga** (00:00:07): Same, same.
**Luís Braga** (00:00:09): But I'm having, like, since yesterday I was supposed to go to gym and I dressed up and .
**Luís Braga** (00:00:17): But I was, so I was having a rest because I was a bit tired and I was, like, doing lazy work on my bed with my laptop.
**Luís Braga** (00:00:30): Anyway, when I got up I had dizziness and I was like, okay, I was laid down, might be it, but then I wasn't good.
**Luís Braga** (00:00:46): So I didn't work out, Celia did, and since I was dizzy all the time, more or less.
**Luís Braga** (00:00:57): Like, something really light, not...
**Luís Braga** (00:00:59): Alright.
**Luís Braga** (00:00:59): Let's go.
**Luís Braga** (00:01:00): very severe but still I never I don't think I ever felt this way and I had a good rest and I still feel a bit dizzy I don't know what the  is going on but but all good all good all good I don't know your body is talking to you and you should you should tackle your your topics that you are facing you know yeah not sure you should you should check for I'm not sure if a psychologist is the is it psychologist is the right thing but check for a coach to to tackle your your topics your your yeah your life topics whatever yeah but to be honest there's nothing really I don't know nothing change I'm it's not that I'm particularly stressed with work I mean I I was a bit but nothing know anything
**Luís Braga** (00:02:00): Very serious, so I don't know, maybe lack of rest or proper eating, I don't know, so I was, and I actually just took, I just wrote in my team channel, I'll take Freddy off, at least, and I was checking the video, of the meeting, and I didn't check it all, because it's quite a long meeting, but I, like I'm, I've seen 45 minutes, anyway, the thing I was thinking is, and I get his, his idea with the NFC things, but as far as I understand, because, like a queue, like, as in McDonald's kind of thing, was never really.
**Luís Braga** (00:03:00): It was never really the primary idea, let's say.
**Luís Braga** (00:03:06): So the way I see this, for us to get it delivered, is just to have an ID on each NFC card.
**Luís Braga** (00:03:14): The way I see this, except for iOS, it's supported.
**Luís Braga** (00:03:18): There's an API, browser API for NFC.
**Luís Braga** (00:03:22): So suppose the cooker has this page to scan.
**Luís Braga** (00:03:27): Let's scan or check-in page, whatever.
**Luís Braga** (00:03:30): And it just puts the NFC card there.
**Luís Braga** (00:03:33): It will be the ID.
**Luís Braga** (00:03:34): It will get the current day.
**Luís Braga** (00:03:36): And we query the database.
**Adrian Rinnus** (00:03:40): Well, OK, but OK.
**Adrian Rinnus** (00:03:42): And so I think I got your point.
**Adrian Rinnus** (00:03:45): So the people.
**Luís Braga** (00:03:46): Sorry, because what he says, it's quite stressful to rely just on a paper, right?
**Luís Braga** (00:03:54): Exactly, to find the stuff on.
**Adrian Rinnus** (00:03:55): Yeah, OK, you're right.
**Adrian Rinnus** (00:03:56): So the first and easier thing would be.
**Adrian Rinnus** (00:03:59): right.
**Adrian Rinnus** (00:03:59): OK.
**Adrian Rinnus** (00:03:59): you.
**Adrian Rinnus** (00:04:00): People are coming in, putting the NFC card to the tablet on the kitchen, more or less, and they see, okay, he ordered this and that, yeah.
**Luís Braga** (00:04:12): And if this thing, and everything looks like it should work good, it's actually also possible to write, if I read this right, to write the NFC tags.
**Luís Braga** (00:04:31): Yeah, this is not the point, writing and reading it, that this is...
**Luís Braga** (00:04:34): We just write it.
**Luís Braga** (00:04:36): But the way I see this, but even extending the thing further to the queue...
**Adrian Rinnus** (00:04:47): Yeah, but you're right, and I think that the first thing would be just getting there, putting the NFC card somewhere, and then get the information popping up would be already it.
**Luís Braga** (00:04:59): Yeah.
**Luís Braga** (00:05:00): Say we have API endpoints to get user mail, that just receives the ID, and based on the current day, it just gets it.
**Adrian Rinnus** (00:05:13): And then we also mark it as delivered.
**Luís Braga** (00:05:17): Yeah.
**Luís Braga** (00:05:18): Do we have it already?
**Luís Braga** (00:05:19): Delivered flag?
**Luís Braga** (00:05:20): No, but this should not be, because we have to order.
**Luís Braga** (00:05:23): Yeah.
**Luís Braga** (00:05:25): Yeah.
**Adrian Rinnus** (00:05:27): And then I think also the order queue would be also cool.
**Adrian Rinnus** (00:05:31): So that would be because I think they have, I know they have two tablets, one in the entrance, one in the kitchen.
**Adrian Rinnus** (00:05:37): So when the people come in on the entrance, so they can queue up more or less, and they know what thing they have to prepare.
**Adrian Rinnus** (00:05:44): And then when they pick it up, they put again the card somewhere on the NFC reader or whatever.
**Luís Braga** (00:05:51): Yeah, but let's focus on the easy solution first, you're right.
**Luís Braga** (00:05:56): In this screen, because it will solve.
**Luís Braga** (00:05:59): well.
**Luís Braga** (00:06:00): Okay.
**Luís Braga** (00:06:00): Problem with the paper.
**Luís Braga** (00:06:01): It feels very easy.
**Luís Braga** (00:06:06): And it will shut them out for a while until we figure the queue thing.
**Luís Braga** (00:06:14): Yeah, that's true.
**Adrian Rinnus** (00:06:15): Good point, yeah.
**Luís Braga** (00:06:17): My feeling with what I see is there's so much things in the details, right?
**Luís Braga** (00:06:21): And they keep  crazy.
**Adrian Rinnus** (00:06:24): Yeah.
**Adrian Rinnus** (00:06:25): know, already the point.
**Adrian Rinnus** (00:06:27): So what I have seen is we have some order contamination.
**Adrian Rinnus** (00:06:31): So there are orders which are not valid.
**Adrian Rinnus** (00:06:33): We have double entries for some users and .
**Adrian Rinnus** (00:06:36): And there was a bug.
**Adrian Rinnus** (00:06:38): But also the point is, so if the people, so if one employee is changing canteens, so he did the orders on the one canteen, then get changed to another one, then the old orders are still there.
**Adrian Rinnus** (00:06:50): So how to handle that one?
**Adrian Rinnus** (00:06:52): And even if they are just working on one canteen at the moment, it could happen.
**Adrian Rinnus** (00:06:57): So this is something I have to log for now, right?
**Adrian Rinnus** (00:07:00): Or give them the possibility to delete the orders and whatever.
**Adrian Rinnus** (00:07:05): I don't know how to handle it, to be honest.
**Adrian Rinnus** (00:07:09): This is not a problem that we have to face now, but I want to finish it in a way that we don't get in trouble here.
**Luís Braga** (00:07:17): You know, I don't know if this is in place, but you just said something that I realize we do, for instance, in Daytrip, for whatever entity, we have this class where we log changes.
**Luís Braga** (00:07:40): And so, for instance, let's say, yeah, it doesn't matter.
**Luís Braga** (00:07:44): Like, whatever changes to the user entity, it changes, for instance, phone number.
**Luís Braga** (00:07:50): And we have an entity, or somehow I don't know exactly the implementation, but in management, we can see this value changed.
**Luís Braga** (00:07:59): The old one was this.
**Luís Braga** (00:08:00): And this is the new one.
**Luís Braga** (00:08:01): This could be useful.
**Luís Braga** (00:08:04): Yeah, then you have some kind of history also.
**Adrian Rinnus** (00:08:06): Yeah, and also I was thinking about that we get something, but these are all important but not urgent things so that we have some kind of, hey, at lunch I'm eating in the canteen X and on dinner I'm eating in the canteen Y, whatever, know, or I'm eating on site or I'm eating in the canteen or whatever.
**Adrian Rinnus** (00:08:27): So that, or hey, on Monday and Tuesday I'm in that location and on Wednesday and Thursday I'm here and on Friday I'm off or whatever.
**Adrian Rinnus** (00:08:39): Yeah, you can go crazy there.
**Adrian Rinnus** (00:08:40): But this is important stuff but not urgent.
**Adrian Rinnus** (00:08:43): The urgent one is the NFC part and I'm thinking about ordering a tablet to run tests on my site.
**Luís Braga** (00:08:56): Or, well, it's always nice to have a physical device but maybe you.
**Luís Braga** (00:09:00): ...
**Luís Braga** (00:09:00): ...
**Luís Braga** (00:09:00): ...
**Luís Braga** (00:09:02): I know which device they have.
**Adrian Rinnus** (00:09:05): It's not that expensive, and I won't have the same device here to not have any troubles, you know.
**Adrian Rinnus** (00:09:10): What do they have?
**Adrian Rinnus** (00:09:12): They have two.
**Adrian Rinnus** (00:09:14): One for the kitchen and one in the entrance for the ordering, yes.
**Luís Braga** (00:09:22): Ah, they do have one in the entrance already?
**Luís Braga** (00:09:26): Yeah.
**Luís Braga** (00:09:26): And what can they do there?
**Adrian Rinnus** (00:09:28): Yeah, they can order.
**Adrian Rinnus** (00:09:29): So the kitchen has it to see the orders, the reporting, and , and at the entrance is for employees?
**Luís Braga** (00:09:37): Yes, for the ordering.
**Luís Braga** (00:09:42): So it's what I sent things to you.
**Adrian Rinnus** (00:09:45): Oh, man, it's all right, and let's do it like that, and we have it in the recording.
**Adrian Rinnus** (00:09:50): I'm sharing just my screen here.
**Luís Braga** (00:09:52): I actually just took a...
**Luís Braga** (00:09:55): Here, you see, this is it.
**Adrian Rinnus** (00:09:58): It's the dodgy...
**Adrian Rinnus** (00:10:00): Tap A9+, and here the Amor Pad 2.
**Adrian Rinnus** (00:10:05): I like the name.
**Luís Braga** (00:10:06): Why this?
**Luís Braga** (00:10:08): I think because it's also IP68K, whatever, so it's not sensitive to water and .
**Luís Braga** (00:10:17): Right.
**Luís Braga** (00:10:17): It's construction workers.
**Adrian Rinnus** (00:10:22): Exactly.
**Adrian Rinnus** (00:10:23): For those clean hands.
**Luís Braga** (00:10:25): Anyway, I just took my Samsung whatever old tablet from my closet.
**Luís Braga** (00:10:33): And I don't know, I would be happy to chase this one, actually, the NFC tags.
**Luís Braga** (00:10:43): have plenty around.
**Luís Braga** (00:10:46): Okay.
**Adrian Rinnus** (00:10:47): I could try and tackle it.
**Adrian Rinnus** (00:10:50): But let's think about a concept and then, yeah, sure.
**Adrian Rinnus** (00:10:54): We can also do it together if you want to.
**Adrian Rinnus** (00:10:58): Or that you do...
**Adrian Rinnus** (00:11:00): ...
**Adrian Rinnus** (00:11:00): ...
**Adrian Rinnus** (00:11:00): I don't know, I'm also thinking about should we, to have that, at the moment we have the issue that Chrome could probably not work with the NFC properly, or even if we say, hey, and this is already overengineering because we know what kind of tablet they are using, but if a customer is using iPad, it's not working because iPad doesn't support NFC in the browser.
**Adrian Rinnus** (00:11:29): What do you mean customer?
**Adrian Rinnus** (00:11:32): Let's think about a different tenant, the, I don't know, X, Y, Z company.
**Luís Braga** (00:11:39): Yeah.
**Luís Braga** (00:11:40): Yeah.
**Luís Braga** (00:11:40): You mean, but yeah, whoever is using the scan.
**Luís Braga** (00:11:45): And it's overengineering already, I know.
**Adrian Rinnus** (00:11:48): But then it would make sense to have some kind of iPad application.
**Luís Braga** (00:11:52): But then, look, there's even one thing that we can do.
**Luís Braga** (00:11:59): so cool.
**Luís Braga** (00:11:59): read Yeah.
**Luís Braga** (00:12:00): Yeah.
**Luís Braga** (00:12:01): Letís say check-in page, letís call it check-in page, and itís going to listen for NFC read events, but it could have an input ID where you just put the internal ID of the user.
**Adrian Rinnus** (00:12:15): Yeah, or a barcode, and you scan the QR code, you put a QR code on the card as well, and you can scan it or whatever.
**Luís Braga** (00:12:23): Yeah, and use the camera, yeah, for sure.
**Luís Braga** (00:12:29): So they could actually, letís say they order NFC tags in the form of the card, they could print QR codes and glue it there, stickers or whatever.
**Luís Braga** (00:12:44): Yeah, sounds good.
**Luís Braga** (00:12:49): And yeah, and we can check NFC availability in that browser if it, if itís not supported, we just show the.
**Luís Braga** (00:12:57): that.
**Luís Braga** (00:12:57): may Yeah.
**Luís Braga** (00:12:58): Oh, Oh, See
**Luís Braga** (00:13:00): The other ones, inputs and things.
**Luís Braga** (00:13:09): Sounds good.
**Adrian Rinnus** (00:13:11): So you want to tackle it or should I also check how I would implement it and then we do it together?
**Luís Braga** (00:13:19): Man, what I would do would be to, like for sure I might, I would go fast in terms of what's needed to create the backend parts.
**Luís Braga** (00:13:35): Whatever, it works.
**Luís Braga** (00:13:38): Honestly, I would, I would like to do it with you.
**Luís Braga** (00:13:46): The thing is, when do you want to do it?
**Luís Braga** (00:13:49): I'm looking for it.
**Adrian Rinnus** (00:13:51): I'm working on the, the thing with the canteen change now.
**Adrian Rinnus** (00:13:59): thing.
**Adrian Rinnus** (00:13:59): on, don't, let can can do If It's
**Adrian Rinnus** (00:14:00): As soon as this is done, I will switch to the NFC part.
**Luís Braga** (00:14:05): Okay, so here's my plan for today.
**Luís Braga** (00:14:10): If you're working on something, honestly, I think we can do this quite fast and make Z happier, happy and happier.
**Luís Braga** (00:14:23): I don't have anything today, I just have a trip, so I guess if you're working on something, you said, right?
**Luís Braga** (00:14:32): You can ping me.
**Adrian Rinnus** (00:14:34): Yeah, so I have to take care about the son of Sofia today at 6, and then I will go to the gym afterwards.
**Adrian Rinnus** (00:14:42): So 6 is 5, your time.
**Adrian Rinnus** (00:14:46): At 5, your time?
**Luís Braga** (00:14:48): No, your time.
**Luís Braga** (00:14:50): 5, my time.
**Adrian Rinnus** (00:14:51): I can also stop working on the thing right now, and we do it now if you want to, I don't care.
**Adrian Rinnus** (00:14:57): You know what?
**Luís Braga** (00:14:58): But let me check.
**Luís Braga** (00:15:00): Thank you.
**Adrian Rinnus** (00:15:02): Oh, do you know what, I was also checking for two things, I want to do end-to-end testing, and I was checking Playwright a bit, and there is a cool thing which is called Superwright, guess.
**Luís Braga** (00:15:23): Superwright?
**Adrian Rinnus** (00:15:24): Yeah, and this is some kind of helper for Superbase, which is creating database entries based on the end-to-end test, and is cleaning up the database afterwards.
**Adrian Rinnus** (00:15:37): So it's a test fixture, more or less, so it creates the necessary data in the database, so you can test against that data, and cleans the database up after the test.
**Adrian Rinnus** (00:15:47): And also, what is  crazy, Playwright has now agents, and they have an agent for planning, generating, and healing, so you send the agent on the application.
**Adrian Rinnus** (00:16:00): that's okay.
**Adrian Rinnus** (00:16:00): And then...
**Adrian Rinnus** (00:16:00): The agent writes a test specification, what it should test, and blah, blah, blah, and then the generator creates the test for it, and then you have also a healer, which runs fixes on the code modus.
**Luís Braga** (00:16:13): Cool.
**Luís Braga** (00:16:15): Yeah.
**Adrian Rinnus** (00:16:16): This is something also, but I need to take a development break when we have the most important stuff done to just clean up and run tests and do  like that, so, yeah.
**Luís Braga** (00:16:30): I mean, what do you say we work on this now?
**Luís Braga** (00:16:34): Yeah, we can, sure.
**Luís Braga** (00:16:36): Because I could actually take a break from day trip , and I can manage.
**Luís Braga** (00:16:42): So what I want is to get my, I don't know where my NFT tags are, but I guess...
**Adrian Rinnus** (00:16:55): Okay, can we do it like that, then, Luís?
**Adrian Rinnus** (00:16:58): Look, you are looking for your tablet and...
**Adrian Rinnus** (00:17:00): The NFC tags and stuff.
**Adrian Rinnus** (00:17:01): I also have an NFC tag.
**Adrian Rinnus** (00:17:02): Let me see if I can use that one.
**Adrian Rinnus** (00:17:05): Just a second.
**Luís Braga** (00:17:06): Yeah.
**Luís Braga** (00:17:10): Oh, I found it.
**Luís Braga** (00:17:12): I still have one.
**Adrian Rinnus** (00:17:14): I still have one from the door.
**Luís Braga** (00:17:20): Let me see what is here.
**Adrian Rinnus** (00:17:22): If I can read it.
**Adrian Rinnus** (00:17:26): , no.
**Luís Braga** (00:17:28): Play Store.
**Adrian Rinnus** (00:17:35): Whatever.
**Luís Braga** (00:17:37): Man, I have a  tablet in front of me.
**Luís Braga** (00:17:42): But I cannot see the screen because brightness is  up.
**Luís Braga** (00:17:49): All right.
**Luís Braga** (00:17:54): Jesus.
**Luís Braga** (00:17:58): I can see .
**Luís Braga** (00:18:00): Hey.
**Luís Braga** (00:18:00): Hey.
**Luís Braga** (00:18:00): Hey.
**Luís Braga** (00:18:00): you.
**Adrian Rinnus** (00:18:07): Oh, okay, I can read it.
**Adrian Rinnus** (00:18:10): Awesome.
**Luís Braga** (00:18:12): Cool.
**Luís Braga** (00:18:13): And maybe I just previously checked some, what is this, React NFC sample app.
**Luís Braga** (00:18:22): All right.
**Luís Braga** (00:18:22): There we go.
**Luís Braga** (00:18:23): I'm sending you this.
**Luís Braga** (00:18:24): Mm-hmm.
**Adrian Rinnus** (00:18:25): Can we do it like that?
**Adrian Rinnus** (00:18:26): I would just want to commit the changes that I made and clean up my local development thing, and then we can take it.
**Adrian Rinnus** (00:18:39): Is that fine?
**Luís Braga** (00:18:40): Sure.
**Luís Braga** (00:18:41): Okay.
**Luís Braga** (00:18:42): So give me five minutes.
**Luís Braga** (00:18:43): I will come back to you, and then we...
**Luís Braga** (00:18:44): All right.
**Luís Braga** (00:18:45): See ya, see ya.
**Luís Braga** (00:18:46): See ya.
**Luís Braga** (00:18:47): Wait, I'm just opening the link.
**Adrian Rinnus** (00:18:49): Don't lose it.
**Adrian Rinnus** (00:18:50): And I will also send the link with the agents to you in the meantime.
**Adrian Rinnus** (00:18:53): All right.
**Luís Braga** (00:18:54): See ya.
**Adrian Rinnus** (00:18:55): Bye-bye.
**Adrian Rinnus** (00:18:56): Bye-bye.

## Kontext & Navigation
- [[DASHBOARD]]
- [[MEMORY]]
- [[OBSIDIAN_ROUTING]]
