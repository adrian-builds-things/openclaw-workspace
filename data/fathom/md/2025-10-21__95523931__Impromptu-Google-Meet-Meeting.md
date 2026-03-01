# Impromptu Google Meet Meeting

## Metadata

- recording_id: 95523931
- created_at: 2025-10-21T08:33:36Z
- recorded_by: Adrian Rinnus
- meeting_url: https://fathom.video/calls/448444155
- speakers: Enes Zorlu, Adrian Rinnus

## Summary

{"template_name": "General", "markdown_formatted": "## Meeting Purpose\n\n[Sync on client feedback, prioritize fixes, and align on product strategy.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=230.0)\n\n## Key Takeaways\n\n  - [**Client Expansion:** Seat's client is rolling out to 140+ employees next week, providing a critical proof-of-concept for a larger presentation at Holka Seisch innovation days.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=230.0)\n  - [**Immediate Fixes:** The rollout requires two fixes: a batch QR code download for 140 users and a kitchen dashboard metric change from \"meals\" to \"people\" to clarify order volume.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=250.0)\n  - [**Strategic Refactor:** Adrian will rewrite the \"meal selection\" module, which is a maintenance bottleneck. The refactor is timed to precede the client expansion, preventing future issues.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=559.0)\n  - [**Security Fix:** Adrian has a fix for the \"tenant leak\" issue (insecure Supabase RLS) and will merge it to the `release` branch for early testing.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=1587.0)\n\n## Topics\n\n### Client Rollout & Feedback\n\n  - [Seat's client is expanding to 140+ employees next week, providing a critical proof-of-concept.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=230.0)\n  - [**Feedback:**](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=250.0)\n      - [**Batch QR Download:** Needed for 140 users.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=250.0)\n      - [**Kitchen Dashboard Metric:** Change \"106 orders\" (meals) to \"20 people\" to clarify order volume for chefs.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=267.0)\n      - [**QR Code Name Cutout:** Fixed by Adrian locally.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=404.0)\n      - [**Dietary Restrictions Bug:** Fixed by Adrian locally.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=447.0)\n  - [**Future Goal:** Seat will present the solution at Holka Seisch innovation days to drive further adoption.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=767.0)\n\n### Technical Priorities & Refactoring\n\n  - [**Meal Selection Refactor:** Adrian will rewrite the module to improve maintainability, using the `query key factory` library.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=559.0)\n      - [**Rationale:** The current code is a maintenance bottleneck, and the refactor is timed to precede the client expansion.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=559.0)\n  - [**Tenant Leak Fix:** Adrian has a fix for the Supabase RLS issue and will merge it to the `release` branch for early testing.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=1587.0)\n  - [**Weekly Menu Cutout:** Enes will fix the visual bug where menu names are cut off.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=460.0)\n\n### Product Strategy & Growth\n\n  - [**NFC Check-in:** Luis built an Arduino-based NFC reader that sends API requests, allowing users to check in without the tablet.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=1315.0)\n  - [**NFC Login:** Adrian proposed using NFC cards for passwordless login, secured with a PIN.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=1357.0)\n  - [**Mobile App:** A native app is a long-term goal for better NFC support and a more natural user experience. Improving the PWA is a near-term alternative.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=1239.0)\n  - [**Sales & Marketing:**](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=1471.0)\n      - [Adrian is engaging two friends with sales experience (one a former chef) to support outreach.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=1471.0)\n      - [Adrian will use the Apollo API lead database to target sustainability managers via cold email.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=1540.0)\n  - [**AI for Development:** Adrian is building a RAG (Retrieval-Augmented Generation) system using Supabase and meeting transcripts to create a searchable knowledge base for AI agents.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=834.0)\n\n## Next Steps\n\n  - [**Adrian:**](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=697.0)\n      - [Implement batch QR code download.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=250.0)\n      - [Update kitchen dashboard metric to show \"people ordered.\"](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=267.0)\n      - [Merge local fixes (QR name cutout, dietary restrictions) to `main`.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=447.0)\n      - [Begin the \"meal selection\" module refactor.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=559.0)\n      - [Merge the tenant leak fix to the `release` branch.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=1587.0)\n  - [**Enes:**](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=534.0)\n      - [Fix the weekly menu name cutout bug.](https://fathom.video/share/QgbArzkGSxsFsaB27iTSinTH5XpYqxTe?tab=summary&timestamp=460.0)\n"}

## Transcript

**Enes Zorlu** (00:00:00): They believe in you.
**Enes Zorlu** (00:00:01): They don't double check or anything like that.
**Enes Zorlu** (00:00:03): For example, I received a letter last year saying that I need to do a tax statement.
**Enes Zorlu** (00:00:11): I need to just declare all my earnings and everything.
**Enes Zorlu** (00:00:15): I called them.
**Enes Zorlu** (00:00:16): I'm not earning anything other than my daily job.
**Enes Zorlu** (00:00:19): They said, okay, we'll cancel it.
**Enes Zorlu** (00:00:20): Don't worry.
**Enes Zorlu** (00:00:22): It was like two minutes and somehow I received a letter saying, oh yeah, now you opt out.
**Enes Zorlu** (00:00:29): You are entitled to receive 400 pounds.
**Adrian Rinnus** (00:00:33): Okay.
**Enes Zorlu** (00:00:34): I took the money out with the check and they haven't asked yet.
**Enes Zorlu** (00:00:39): So let's see.
**Enes Zorlu** (00:00:40): You know, on my side, it was different.
**Adrian Rinnus** (00:00:43): There was, when I did the, the, the, the invoice, the tax statement for 2023, then there was for January, um, a letter.
**Adrian Rinnus** (00:00:52): Yay.
**Adrian Rinnus** (00:00:52): Okay.
**Adrian Rinnus** (00:00:52): So you did the tax statement.
**Adrian Rinnus** (00:00:54): So you have an income.
**Adrian Rinnus** (00:00:54): Okay.
**Adrian Rinnus** (00:00:55): Now you're obligated to pay 1,500 bucks every three months.
**Adrian Rinnus** (00:00:59): I'm.
**Adrian Rinnus** (00:00:59): And it.
**Adrian Rinnus** (00:01:00): Just call them, hey guys, I don't make any money, what the  do you want, bro?
**Adrian Rinnus** (00:01:06): Okay.
**Enes Zorlu** (00:01:07): Okay, yeah.
**Enes Zorlu** (00:01:08): What is the minimum you need to pay for health insurance then?
**Enes Zorlu** (00:01:12): It's 260 euros a month.
**Adrian Rinnus** (00:01:16): It doubled, so basically doubled then.
**Enes Zorlu** (00:01:18): Yeah?
**Adrian Rinnus** (00:01:19): Yeah.
**Enes Zorlu** (00:01:22): Good luck.
**Adrian Rinnus** (00:01:24): Anyways, I will figure it out, and one more reason to hack the system, triple the system, and just...
**Adrian Rinnus** (00:01:30): I think my challenge is how do I get out of the health insurance and don't have to pay for because I don't need it.
**Adrian Rinnus** (00:01:37): I simply don't need it at the moment, yeah?
**Adrian Rinnus** (00:01:40): what the ?
**Enes Zorlu** (00:01:43): Well, unfortunately, it's obligation, same.
**Enes Zorlu** (00:01:47): But then you are not able to get the...
**Enes Zorlu** (00:01:53): I think in Germany, when you are not working, you are able to get some kind of help or anything like that.
**Enes Zorlu** (00:01:59): Do you have...
**Enes Zorlu** (00:02:00): You don't want that?
**Enes Zorlu** (00:02:02): Okay.
**Adrian Rinnus** (00:02:03): Nowadays, I would receive it, I guess.
**Adrian Rinnus** (00:02:05): But then they also put a lot of pressure on me that I get a new job and blah, blah, blah.
**Adrian Rinnus** (00:02:10): And on the other hand, I was in that program for a year where I was receiving money because I didn't have a job.
**Adrian Rinnus** (00:02:20): And I felt like this is not for me because then life is easy.
**Adrian Rinnus** (00:02:26): You don't have to do anything.
**Adrian Rinnus** (00:02:27): You get money.
**Adrian Rinnus** (00:02:27): So you don't have to take care about it.
**Adrian Rinnus** (00:02:30): I think the pressure is fine because now I have to speed up even more and find new clients.
**Enes Zorlu** (00:02:36): Yeah.
**Enes Zorlu** (00:02:36): The reason I was asking is just when they do that, they sort out the health issues themselves.
**Enes Zorlu** (00:02:42): I was just trying to understand that.
**Enes Zorlu** (00:02:43): Okay.
**Enes Zorlu** (00:02:44): Yeah.
**Enes Zorlu** (00:02:45): Okay.
**Adrian Rinnus** (00:02:45): Then it's getting paid by government and then it's fine.
**Adrian Rinnus** (00:02:48): Yeah.
**Enes Zorlu** (00:02:49): What you need to do, you need to get that and create an account for Zola and don't receive the money.
**Enes Zorlu** (00:02:57): So you don't need to pay the health insurance.
**Enes Zorlu** (00:02:59): Yes.
**Enes Zorlu** (00:03:00): Yes.
**Enes Zorlu** (00:03:00): Yes.
**Enes Zorlu** (00:03:00): And all the money you don't receive, it goes to Zola's account, so you're still in the same situation, but at least getting the money back from the government.
**Enes Zorlu** (00:03:07): That will be a good investment for Zola for the future.
**Enes Zorlu** (00:03:11): That's true, that's true.
**Enes Zorlu** (00:03:17): Governments generally take a lot of money from us, so when we have the rights, we should use the benefits as well.
**Adrian Rinnus** (00:03:25): And you know what, now we do the founding here, is there any support from the government?
**Adrian Rinnus** (00:03:31): No, nothing.
**Adrian Rinnus** (00:03:33): It's just putting rocks in the way that you are not able to move and what the .
**Adrian Rinnus** (00:03:38): Anyways.
**Adrian Rinnus** (00:03:41): Exactly.
**Adrian Rinnus** (00:03:43): Whatever.
**Adrian Rinnus** (00:03:44): I stop complaining now and do my work and then all is good.
**Adrian Rinnus** (00:03:49): Yeah.
**Adrian Rinnus** (00:03:50): I just had a call with Seat a few minutes ago and he is really happy with the solution.
**Adrian Rinnus** (00:03:57): That's nice.
**Enes Zorlu** (00:03:58): And he will start, so they will start next week.
**Adrian Rinnus** (00:04:00): With the full-blown, all employees will receive the card, and so, yeah.
**Enes Zorlu** (00:04:08): Perfect.
**Enes Zorlu** (00:04:10): Any feature requests?
**Enes Zorlu** (00:04:12): Any...
**Enes Zorlu** (00:04:12): Yeah, just two small things.
**Adrian Rinnus** (00:04:14): He said he would like to have a batch download for the PNGs, all QR codes, because otherwise he had to click 140 users, so he would like to have all the QR code and things.
**Adrian Rinnus** (00:04:25): That makes sense, yeah.
**Adrian Rinnus** (00:04:27): Yeah, and then there was one thing in the kitchen dashboard where the chefs are confused.
**Adrian Rinnus** (00:04:32): There is that, if you have a look, there is, at the moment, I will show you, let me see it.
**Adrian Rinnus** (00:04:46): Yeah, for example, and he loves the sidebar, which is minimized and stuff, so he was really happy and really satisfied.
**Adrian Rinnus** (00:04:58): Exactly what he said was here...
**Adrian Rinnus** (00:05:03): That 106 orders.
**Adrian Rinnus** (00:05:05): This is confusing the chefs because it's, yes, sure, it's 106 meals, but it's the soup, the dessert, and the main dishes.
**Adrian Rinnus** (00:05:13): So what would be better here is one of, for example, 20 people have ordered.
**Adrian Rinnus** (00:05:18): So that would help them more because it's more obvious that they have 20 boxes out, something like that.
**Adrian Rinnus** (00:05:25): So, yeah.
**Adrian Rinnus** (00:05:26): Okay.
**Enes Zorlu** (00:05:26): Yeah.
**Enes Zorlu** (00:05:26): Makes sense.
**Enes Zorlu** (00:05:27): Yeah.
**Enes Zorlu** (00:05:27): And this was the only request that he had in that sense.
**Enes Zorlu** (00:05:31): So do we, do we want to add a couple more information or keep it simple and just people, we can say this many people ordered, this many main, this, but you don't need to say that actually.
**Enes Zorlu** (00:05:45): Yeah.
**Enes Zorlu** (00:05:46): Let's keep it simple for now.
**Enes Zorlu** (00:05:48): Yeah.
**Enes Zorlu** (00:05:48): We can say this many main, this many dessert, this many soup as well, but we have it yet.
**Enes Zorlu** (00:05:54): We have it more or less here.
**Enes Zorlu** (00:05:55): we have it.
**Enes Zorlu** (00:05:55): Yeah, exactly.
**Enes Zorlu** (00:05:56): I was thinking about it.
**Enes Zorlu** (00:05:57): It's just, I was thinking out loud.
**Enes Zorlu** (00:05:59): time.
**Enes Zorlu** (00:06:00): Yeah.
**Enes Zorlu** (00:06:00): Okay.
**Enes Zorlu** (00:06:01): Just people.
**Enes Zorlu** (00:06:02): Okay.
**Enes Zorlu** (00:06:03): For the week as well, I guess.
**Enes Zorlu** (00:06:07): Let me see.
**Enes Zorlu** (00:06:09): the week, portions, dinner portions.
**Enes Zorlu** (00:06:13): It's a bit different in the week.
**Enes Zorlu** (00:06:15): So we need to say people for the week as well, or keep it like this.
**Enes Zorlu** (00:06:24): I would also do it here, I guess.
**Adrian Rinnus** (00:06:27): yeah.
**Enes Zorlu** (00:06:28): Yeah.
**Enes Zorlu** (00:06:28): Okay.
**Enes Zorlu** (00:06:29): But also I think the information there is nice as well.
**Enes Zorlu** (00:06:33): Yeah.
**Enes Zorlu** (00:06:33): Lunch portions, dinner portions, maybe on top of it, this many people ordered or something like that.
**Enes Zorlu** (00:06:39): Yeah.
**Enes Zorlu** (00:06:40): Yeah.
**Adrian Rinnus** (00:06:40): That's also fine.
**Adrian Rinnus** (00:06:41): Sure.
**Adrian Rinnus** (00:06:42): And then, yeah.
**Adrian Rinnus** (00:06:44): What also was an issue on his side is the QR code.
**Adrian Rinnus** (00:06:48): For example, if you have a look at, I think I printed it out.
**Adrian Rinnus** (00:06:54): Wait.
**Adrian Rinnus** (00:06:55): Yeah.
**Enes Zorlu** (00:06:56): Yeah.
**Enes Zorlu** (00:06:56): The name is getting, it was on my list.
**Adrian Rinnus** (00:07:00): I have already done something here.
**Adrian Rinnus** (00:07:03): So this is now okay, I guess.
**Enes Zorlu** (00:07:07): Yeah.
**Enes Zorlu** (00:07:10): The problem is Portuguese names are too long.
**Enes Zorlu** (00:07:14): Yeah, it's crazy.
**Enes Zorlu** (00:07:17): It's crazy.
**Enes Zorlu** (00:07:18): Not Lewish ones.
**Adrian Rinnus** (00:07:20): His is really short, but his names, it's crazy now.
**Adrian Rinnus** (00:07:27): And also the bug that I was reporting yesterday, but I've already fixed it.
**Adrian Rinnus** (00:07:32): I have fixed the QR code stuff and also the dietary restrictions.
**Adrian Rinnus** (00:07:35): I have just to merge it and then...
**Adrian Rinnus** (00:07:37): Okay, perfect.
**Enes Zorlu** (00:07:40): And there was two more things they requested in the message.
**Enes Zorlu** (00:07:44): Let me see.
**Adrian Rinnus** (00:07:46): Yeah, the closing dates in the canteen or something, but yeah, this is important, not urgent.
**Enes Zorlu** (00:07:57): And I can...
**Enes Zorlu** (00:07:58): I have that PR...
**Enes Zorlu** (00:08:00): There are four reports already, so I can fix that weekly menu cutout of the name.
**Enes Zorlu** (00:08:06): can fix that issue.
**Adrian Rinnus** (00:08:07): The cutout, I have already fixed it.
**Adrian Rinnus** (00:08:10): Oh, you fixed it already, okay.
**Enes Zorlu** (00:08:12): Yesterday, think, yeah.
**Enes Zorlu** (00:08:13): Okay, okay.
**Enes Zorlu** (00:08:14): Give me a second.
**Enes Zorlu** (00:08:15): I didn't have a look, I didn't have a look.
**Adrian Rinnus** (00:08:17): It was, I'm also not sure at the moment, to be honest.
**Adrian Rinnus** (00:08:22): Did I even create a PR?
**Enes Zorlu** (00:08:23): No, the one I merged actually has the same issue still.
**Enes Zorlu** (00:08:30): When I rebased, so maybe you have it in your local?
**Adrian Rinnus** (00:08:40): Here, the branch is there, but it's not yet merged, so.
**Enes Zorlu** (00:08:44): Okay, okay, so you have it in your branch then, okay.
**Adrian Rinnus** (00:08:48): Yeah, so the QR code and the dietary restriction should be fixed by these two things here.
**Enes Zorlu** (00:08:54): And also the weekly menu cutout then.
**Enes Zorlu** (00:08:59): Ah!
**Adrian Rinnus** (00:09:00): have move content.
**Adrian Rinnus** (00:09:00): That's
**Adrian Rinnus** (00:09:00): Sorry, then I just understood cutout, and I was thinking about the QR code, which is cutting out the name.
**Adrian Rinnus** (00:09:07): No, no, no, this is not yet.
**Adrian Rinnus** (00:09:10): This is something you could do.
**Enes Zorlu** (00:09:11): Yeah, sorry.
**Enes Zorlu** (00:09:12): I'll sort that on my report branch, so I'll do it this morning.
**Enes Zorlu** (00:09:18): Yeah.
**Adrian Rinnus** (00:09:19): And what I'm doing at the moment is I'm rewriting the whole meal selection because it's just a mess.
**Enes Zorlu** (00:09:25): Don't do that.
**Adrian Rinnus** (00:09:25): I do it because I'm not able to maintain it.
**Adrian Rinnus** (00:09:28): I was sitting there two days to figure out the last issue, and I was not able to do it.
**Enes Zorlu** (00:09:33): didn't you refactor it already?
**Enes Zorlu** (00:09:36): Yeah, the hook, but still, it is so crazy.
**Adrian Rinnus** (00:09:39): And if I have a look at the code, it's ,  off.
**Enes Zorlu** (00:09:43): Yeah, but the problem is it's just, yeah, it's working.
**Adrian Rinnus** (00:09:49): It's working, but if we have to touch it one more time before anything or for any bug, it's getting just messier and messier.
**Adrian Rinnus** (00:09:57): Yeah.
**Enes Zorlu** (00:09:58): Yeah.
**Enes Zorlu** (00:10:00): Yeah.
**Enes Zorlu** (00:10:00): Yeah, only thing I'm getting afraid of is just we try to refactor it and then break it and they're opening up to bigger group now.
**Enes Zorlu** (00:10:09): think it just doesn't feel like the right time to mess with it.
**Adrian Rinnus** (00:10:14): Yeah, I see your point.
**Adrian Rinnus** (00:10:15): The problem is there will come more and more people and there will never be the right time.
**Adrian Rinnus** (00:10:20): This is what I learned at Bosch.
**Adrian Rinnus** (00:10:23): Sometimes you have to do the ugly refactoring because otherwise it just gets messier and messier and you will never do it because it's just getting more.
**Adrian Rinnus** (00:10:30): It's not getting less, you know?
**Enes Zorlu** (00:10:32): Yeah, true.
**Adrian Rinnus** (00:10:34): I found a really cool library yesterday because this is exactly what I wanted to do with the query registry thing, which is also a monster, but this is cool.
**Adrian Rinnus** (00:10:47): It's more or less exactly a query registry for 10 stack query, which handles also the cache invalidation and .
**Adrian Rinnus** (00:10:55): So you can do exactly that, but in that thing here, and it's-
**Adrian Rinnus** (00:11:00): Not as such a mess.
**Adrian Rinnus** (00:11:01): So if you then use it, this is what we did at Mindtreasure, get query key thing.
**Adrian Rinnus** (00:11:07): This is a library for it where you can also put the functions directly inside.
**Adrian Rinnus** (00:11:12): You can do context queries.
**Adrian Rinnus** (00:11:15): You can do all that kind of fancy stuff.
**Adrian Rinnus** (00:11:17): It's really cool.
**Adrian Rinnus** (00:11:18): What's the name?
**Adrian Rinnus** (00:11:19): It's called a query key factory.
**Adrian Rinnus** (00:11:22): I can send the link to you.
**Enes Zorlu** (00:11:28): You'll find it, yeah.
**Enes Zorlu** (00:11:30): It looks really cool, Sam.
**Adrian Rinnus** (00:11:36): All right.
**Adrian Rinnus** (00:11:37): So then I will tackle the batch PNG download.
**Adrian Rinnus** (00:11:43): And yeah.
**Enes Zorlu** (00:11:46): Isn't there anything else then, all those then, on the list?
**Enes Zorlu** (00:11:51): Yeah.
**Adrian Rinnus** (00:11:51): For now, it's just nothing.
**Enes Zorlu** (00:11:53): Okay.
**Enes Zorlu** (00:11:54): That's good.
**Enes Zorlu** (00:11:55): So yeah.
**Enes Zorlu** (00:11:56): Once these are sorted, then I can go back to Mindtreasure as well.
**Adrian Rinnus** (00:12:02): And Zey was really happy about the NFC writing and stuff like that.
**Adrian Rinnus** (00:12:06): That's cool.
**Enes Zorlu** (00:12:08): That's cool.
**Enes Zorlu** (00:12:10): It's a really cool feature.
**Enes Zorlu** (00:12:12): I didn't even know that you can do that with the Android device.
**Enes Zorlu** (00:12:18): I thought you need those fancy writers to be able to do that.
**Enes Zorlu** (00:12:23): Yeah.
**Enes Zorlu** (00:12:25): That's really cool.
**Enes Zorlu** (00:12:26): Yeah.
**Enes Zorlu** (00:12:27): Okay.
**Enes Zorlu** (00:12:29): So what's the plan on their end then?
**Enes Zorlu** (00:12:32): They will open up to a bigger group now.
**Enes Zorlu** (00:12:34): Yeah.
**Enes Zorlu** (00:12:34): How many people are we talking about?
**Enes Zorlu** (00:12:37): The 200 at the moment.
**Adrian Rinnus** (00:12:39): So I think all the 140 that they have at the moment, but they are adding more and more there.
**Adrian Rinnus** (00:12:45): Yeah.
**Adrian Rinnus** (00:12:47): And then as soon as they have more, as soon as Zey has the proof that this is working and help them, he will also present it on that innovation days of Holka Seisch.
**Adrian Rinnus** (00:12:59): He's trying to roll.
**Adrian Rinnus** (00:13:05): And he said the Christmas party has been rescheduled to 22nd of November, but this is not working for me, probably, and also for you.
**Adrian Rinnus** (00:13:22): No, because probably I will not get the visa until then.
**Enes Zorlu** (00:13:27): Yeah, maybe in the new year.
**Enes Zorlu** (00:13:29): Yeah.
**Enes Zorlu** (00:13:30): we can have a visit.
**Enes Zorlu** (00:13:32): Yeah.
**Adrian Rinnus** (00:13:33): And he still said we can still come on the 13th of December and also enjoy Christmas stuff in Brussels and whatever.
**Adrian Rinnus** (00:13:38): So let's see.
**Enes Zorlu** (00:13:40): We can also do that.
**Enes Zorlu** (00:13:43): Let's see.
**Enes Zorlu** (00:13:44): I'll let you know when I get my visa back.
**Enes Zorlu** (00:13:47): Yeah.
**Enes Zorlu** (00:13:49): So, okay.
**Enes Zorlu** (00:13:51): Oh, and I need to show you something.
**Adrian Rinnus** (00:13:53): This is fun.
**Adrian Rinnus** (00:13:54): And what I want to build is also an RAG.
**Adrian Rinnus** (00:14:00): Have you heard about that?
**Adrian Rinnus** (00:14:01): That personal knowledge-based stuff for AI, for example, that you could use for AI?
**Adrian Rinnus** (00:14:07): Something like Context 7, but for your AI agents with your knowledge.
**Adrian Rinnus** (00:14:11): And also what I did is every Fathom meeting that I have triggers now an N8N thing, and I want to create the nodes automatically, extract feature requests out of the meeting nodes automatically and stuff like that so that I don't have to do it.
**Adrian Rinnus** (00:14:29): So, for example, that was the meeting with SAE.
**Adrian Rinnus** (00:14:32): And this is cool because I have all the data in here.
**Adrian Rinnus** (00:14:35): I have to hold a transcript, the summary, whatever.
**Adrian Rinnus** (00:14:38): And now I can use automations to extract whatever I want from it.
**Adrian Rinnus** (00:14:42): So that's cool.
**Enes Zorlu** (00:14:44): That's cool.
**Adrian Rinnus** (00:14:44): And I also want to build that RAG thingy with a Superbase.
**Adrian Rinnus** (00:14:50): And so you can just put documents in a Google Drive and it's putting it to a Superbase.
**Adrian Rinnus** (00:14:55): And then you can connect your software and cloud code, whatever you use to that.
**Adrian Rinnus** (00:15:00): That RIG, and you have the whole documentation that you need in the MCP there, more or less, so that's also cool.
**Adrian Rinnus** (00:15:06): And I want to use all the transcripts for it, you know?
**Adrian Rinnus** (00:15:09): So if there is some feature thing we are talking about, we have all the meeting notes in the RIG, and we know exactly what the request was and can work on that.
**Enes Zorlu** (00:15:19): Yeah, the only problem is, when we get the AI to develop it, then we have to refactor it later on.
**Enes Zorlu** (00:15:29): But still, it helps to understand, so I need to change my work working again.
**Adrian Rinnus** (00:15:34): I was freaking out at the weekend, it's just, I can't work like that anymore, it's ...
**Adrian Rinnus** (00:15:39): How were you working?
**Enes Zorlu** (00:15:42): Was it full, pure AI then?
**Enes Zorlu** (00:15:45): Yeah, more or less.
**Enes Zorlu** (00:15:46): Okay.
**Enes Zorlu** (00:15:48): Yeah.
**Enes Zorlu** (00:15:48): It's good to make progress, know, but the code is...
**Enes Zorlu** (00:15:51): definitely, yeah.
**Enes Zorlu** (00:15:52): It's just, yeah, when you do that, I think, what I find, I...
**Enes Zorlu** (00:16:00): Get AI to do so many stuff as well, but I find then I'm turning into more of a test engineer rather than developer.
**Enes Zorlu** (00:16:10): So all I do, test, test, test, test, and sometimes it fails to do what I want to do.
**Enes Zorlu** (00:16:15): And sometimes it's easier to just write manually.
**Enes Zorlu** (00:16:19): Yeah.
**Adrian Rinnus** (00:16:20): And also you, I saw, no, not you, I have lost track.
**Adrian Rinnus** (00:16:24): I didn't know what it was doing and I didn't understand the code at all.
**Adrian Rinnus** (00:16:28): And now if you have to change it, you have to fix it.
**Adrian Rinnus** (00:16:30): It's just pain in the .
**Enes Zorlu** (00:16:32): didn't have, yeah, I didn't have that problem because I think our mindset is a bit different with you and me.
**Enes Zorlu** (00:16:40): For example, the, if you look at the PRs from last week, the bug fixes I do is a couple hundred lines of code change because I'm, that moment I'm focusing on the bug itself.
**Enes Zorlu** (00:16:53): But when you do, you want to do it, you want to do it properly.
**Enes Zorlu** (00:16:58): So it's a couple of thousands.
**Enes Zorlu** (00:17:00): Soft lines, because what you did was amazing with the query, making the queries really fast and everything.
**Enes Zorlu** (00:17:07): rather than just fixing the box, you were just structuring the entire thing.
**Enes Zorlu** (00:17:13): So when you want to restructure the entire thing, it's a bit of a big mess to understand the entire thing.
**Enes Zorlu** (00:17:20): So it's sometimes easier to rewrite it, but when you just want to fix the bug, I think I'm able to understand it, but it's just when you want to fix a specific bug, not when you want to understand what's going on, whatever.
**Enes Zorlu** (00:17:34): You need to spend more time, as you say.
**Adrian Rinnus** (00:17:36): My problem there is, if I don't understand what the thing does, I can't find the bug.
**Adrian Rinnus** (00:17:41): This is where I'm messed, you know, then.
**Enes Zorlu** (00:17:45): Yeah, different things, but yeah, the changes last week was really cool.
**Enes Zorlu** (00:17:54): Right, yeah, it's blazing fast now.
**Enes Zorlu** (00:17:58): I see the, right now the...
**Enes Zorlu** (00:18:01): The slowest thing is the admin dashboard, I think, in the app.
**Enes Zorlu** (00:18:06): It's bugging me, so it's one day.
**Enes Zorlu** (00:18:08): I want to touch that one as well.
**Enes Zorlu** (00:18:10): I think when you go to the main ByteClub website, everything loads really fast except the admin dashboard.
**Adrian Rinnus** (00:18:21): Oh, and I was also asking Mudita if he can design a logo and some stuff for us.
**Adrian Rinnus** (00:18:27): And he did one for now.
**Adrian Rinnus** (00:18:29): He will do more because he's really good in logo design.
**Adrian Rinnus** (00:18:34): I will show you.
**Adrian Rinnus** (00:18:38): I need to open it.
**Adrian Rinnus** (00:18:47): Where is he?
**Adrian Rinnus** (00:18:50): Here.
**Adrian Rinnus** (00:18:57): Here we go.
**Adrian Rinnus** (00:19:00): Here
**Adrian Rinnus** (00:19:00): He did some more.
**Enes Zorlu** (00:19:05): Like Fight Club.
**Enes Zorlu** (00:19:07): Yeah, exactly.
**Adrian Rinnus** (00:19:08): I told him that more or less the idea was a little bit from Fight Club, so that was done.
**Adrian Rinnus** (00:19:15): And he did some new.
**Enes Zorlu** (00:19:18): I like the top left one, yeah.
**Adrian Rinnus** (00:19:21): Yeah, me too.
**Enes Zorlu** (00:19:24): This is also funny, but...
**Enes Zorlu** (00:19:26): But I think top left one, but with a bite to a cookie or something like that on left, so you understand what the bite means.
**Enes Zorlu** (00:19:38): Yeah.
**Enes Zorlu** (00:19:38): Not a fork.
**Enes Zorlu** (00:19:39): Well, actually, there is actually one part.
**Enes Zorlu** (00:19:42): Actually, yeah, B is a bite, but yeah.
**Enes Zorlu** (00:19:45): Yeah.
**Adrian Rinnus** (00:19:48): Yeah, right.
**Adrian Rinnus** (00:19:49): We need something that we can use as favicon or whatever, and this is missing here.
**Adrian Rinnus** (00:19:53): Yeah.
**Enes Zorlu** (00:19:55): We have that small thing, but yeah.
**Enes Zorlu** (00:20:00): I like it.
**Adrian Rinnus** (00:20:02): And I also like the landing page, because I did it, I was just talking to JGPT tell, hey, I love the post hoc landing page, do something like that with a little bit of irony and humor on it and stuff like that.
**Adrian Rinnus** (00:20:16): And I like the copy a lot, because it's also, I was laughing about it, and this is something I, this is, yeah, I will try to do something like that in a better state now.
**Adrian Rinnus** (00:20:31): That sounds good.
**Enes Zorlu** (00:20:33): Definitely.
**Enes Zorlu** (00:20:35): Yeah, it's quite nice at the moment.
**Enes Zorlu** (00:20:39): I'm very happy with the app.
**Enes Zorlu** (00:20:41): It's just one question.
**Enes Zorlu** (00:20:43): Do you want to do anything for a mobile app?
**Adrian Rinnus** (00:20:53): I think it's working as it is right now.
**Adrian Rinnus** (00:20:56): And yes, there are still plans because NFC would be better supported and
**Adrian Rinnus** (00:21:00): And stuff like that, so, yeah.
**Enes Zorlu** (00:21:05): For the main, for the users, for menu selection, for example.
**Adrian Rinnus** (00:21:11): Yeah, I think the PWA stuff is also something we could work and improve on.
**Adrian Rinnus** (00:21:19): Then you can install it more or less on your phone.
**Enes Zorlu** (00:21:22): Yeah.
**Adrian Rinnus** (00:21:23): And still, yeah, you can also add the offline functionality, yeah, I don't know.
**Adrian Rinnus** (00:21:30): Yeah.
**Adrian Rinnus** (00:21:31): And we can also think about a mobile app, if you want to do something like that, go for it, sure.
**Adrian Rinnus** (00:21:37): Yeah.
**Enes Zorlu** (00:21:38): Well, yeah, I'm thinking it just would be nice to have an app instead of going to a website.
**Enes Zorlu** (00:21:44): It would feel more natural.
**Enes Zorlu** (00:21:47): Yeah, that's true.
**Enes Zorlu** (00:21:49): Yeah, let's see how they get along with the bigger group.
**Adrian Rinnus** (00:21:55): And what Luis did is, he bought a small NFC.
**Adrian Rinnus** (00:22:00): We read a thing, and build an Arduino interface with an HTTP client more or less, and now his idea was that it sends API requests to our API so that they have the box in front of the tablet, and they just put the cards on, and this is going to the queue in that sense so that they don't have to put it to the tablet.
**Adrian Rinnus** (00:22:23): So they have an external device which is connected to Wi-Fi and sends API requests based on the card.
**Enes Zorlu** (00:22:29): Okay, so what then is displaying what they...
**Enes Zorlu** (00:22:34): Yeah, exactly, for displaying what they are.
**Adrian Rinnus** (00:22:37): Okay, yeah, And what I was also thinking about is we could go there even with the QR code or the NFC and do the user login based on that so that they get the QR code, they have the card credentials, and they get a second factor in PIN or whatever.
**Adrian Rinnus** (00:22:56): They just put the card on the back of the phone or scan the QR code.
**Adrian Rinnus** (00:23:00): code code.
**Adrian Rinnus** (00:23:00): Now, Let's Thank
**Adrian Rinnus** (00:23:00): And then they just have to enter the PIN and get logged in.
**Adrian Rinnus** (00:23:03): So we are also rid of the password stuff.
**Enes Zorlu** (00:23:09): Yeah.
**Enes Zorlu** (00:23:09): With the card, you don't need to even get a PIN or anything like that.
**Adrian Rinnus** (00:23:14): should, because otherwise you lose it and someone else is able to...
**Adrian Rinnus** (00:23:18): I would add a second factor, but yeah.
**Enes Zorlu** (00:23:22): Yeah, but just imagine in the workplace, you don't get second factor to go into a secret room or anything like that.
**Enes Zorlu** (00:23:31): You just, you have the responsibility to keep your card and when you lose it, you need to report it.
**Enes Zorlu** (00:23:38): So that's why I think, come on, you are selecting a meal and the company cards are used for more secretive things.
**Enes Zorlu** (00:23:47): So I think it will be all right, because how many times it will happen?
**Enes Zorlu** (00:23:52): Probably 0.5% less than that, maybe one million times.
**Enes Zorlu** (00:23:57): That's true.
**Enes Zorlu** (00:23:57): Everyone will be using their cards every day, so it will be easy.
**Enes Zorlu** (00:24:00): Before them to just scan it and select it, that's true, but yeah, it would be nice, probably it would be a tablet or something like that in the place where they can NFC scan it.
**Enes Zorlu** (00:24:18): Yeah, exactly.
**Adrian Rinnus** (00:24:19): They have two tablets, one in the kitchen, one in the entrance more or less, and then the people can order there or pick up the food.
**Adrian Rinnus** (00:24:31): So I have also, I have to talk to two friends of mine who said they can also do some kind of sales for Bike Club.
**Adrian Rinnus** (00:24:38): So one of them is he did, he was a chef in earlier times, actually, so he knows.
**Adrian Rinnus** (00:24:47): I was also talking with him about it and he said, hey, if I would do it like that or if I would use it, I would love to have it like that and blah, blah, blah.
**Adrian Rinnus** (00:24:54): So that was also cool.
**Adrian Rinnus** (00:24:56): And he's also in sales now.
**Adrian Rinnus** (00:24:58): So he also said, hey, I can support you there.
**Adrian Rinnus** (00:25:00): And he knows also some, because he's in sales and industry, he knows the companies.
**Adrian Rinnus** (00:25:05): And he also said, yeah, I can do the cold calling and talk to people.
**Adrian Rinnus** (00:25:10): And then another friend of mine, a Greek guy, I know him from Larissa and the investment stuff we did, he is also doing software sales.
**Adrian Rinnus** (00:25:22): And he also has contacts to a lot of companies, to big companies.
**Adrian Rinnus** (00:25:26): So I also was talking to him about that, and he can also do some sales and support us.
**Adrian Rinnus** (00:25:31): So it would be really cool to have also the two guys doing the sales, so I will talk to them.
**Adrian Rinnus** (00:25:38): Yeah.
**Enes Zorlu** (00:25:39): To expand it.
**Enes Zorlu** (00:25:40): Yeah.
**Adrian Rinnus** (00:25:40): Oh, and I will also try to run on that, there is the Apollo API, do you know that?
**Adrian Rinnus** (00:25:47): It's a leads database, more or less, with, I guess, 8 million leads inside, and you can search for B2B contacts, so sustainability managers, for example.
**Adrian Rinnus** (00:25:57): This is something I want to, to, um.
**Adrian Rinnus** (00:26:00): Yeah.
**Adrian Rinnus** (00:26:00): to contact in that sense with some code emails and let's see if they are interested in something like that because this is sustainability, it's fighting.
**Adrian Rinnus** (00:26:09): definitely, yeah.
**Enes Zorlu** (00:26:10): Why not?
**Enes Zorlu** (00:26:13): Yeah, would be nice.
**Enes Zorlu** (00:26:14): Yes, now start talking about more getting more customers.
**Enes Zorlu** (00:26:17): It's feels nice.
**Enes Zorlu** (00:26:19): Yeah.
**Adrian Rinnus** (00:26:20): And we have to prove so they are happy they use it.
**Adrian Rinnus** (00:26:23): We provide value.
**Adrian Rinnus** (00:26:24): It's a cool thing.
**Enes Zorlu** (00:26:26): definitely.
**Enes Zorlu** (00:26:27): Yeah, talking about that, yeah, I need to fix also the tenant leak issue.
**Adrian Rinnus** (00:26:34): Which issue?
**Enes Zorlu** (00:26:35): The leak.
**Enes Zorlu** (00:26:37): Ah, yeah, right.
**Adrian Rinnus** (00:26:38): I can also do, I have already a fix in place.
**Adrian Rinnus** (00:26:41): Okay.
**Adrian Rinnus** (00:26:42): Because I was also sending out the AI again, but I was copying all the warnings from Superbase with the unrestricted tables, and it was putting the RLS stuff in place.
**Adrian Rinnus** (00:26:54): So I just didn't want to put it in this release because I want to test it properly before.
**Adrian Rinnus** (00:26:59): I did a database cleanup.
**Enes Zorlu** (00:27:00): have been.
**Adrian Rinnus** (00:27:00): Also put in the restrictions for the table.
**Adrian Rinnus** (00:27:03): So it should hopefully.
**Enes Zorlu** (00:27:06): OK, then not touching that one.
**Enes Zorlu** (00:27:08): It's in progress.
**Enes Zorlu** (00:27:09): OK, yeah, perfect.
**Enes Zorlu** (00:27:10): I can merge it to release.
**Adrian Rinnus** (00:27:12): Then we have it there.
**Adrian Rinnus** (00:27:13): Because the earlier we have it there, the more we see the issues that we face.
**Adrian Rinnus** (00:27:18): I can merge, release, and yeah.
**Adrian Rinnus** (00:27:22): Yeah, so I can give it the test as well.
**Adrian Rinnus** (00:27:26): How should we handle the?
**Adrian Rinnus** (00:27:28): No, I will merge it to release as soon as we have the changes that we do now on main.
**Adrian Rinnus** (00:27:36): then I will put it on release so that we have a slightly bigger time horizon to test.
**Enes Zorlu** (00:27:41): OK, yeah.
**Enes Zorlu** (00:27:42): All right, let's do it like that.
**Adrian Rinnus** (00:27:43): Enes?
**Enes Zorlu** (00:27:45): Perfect.
**Enes Zorlu** (00:27:46): Thank you.
**Enes Zorlu** (00:27:46): Pleasure to talk to you.
**Adrian Rinnus** (00:27:48): We have to do that more regularly.
**Adrian Rinnus** (00:27:50): Yeah, same.
**Enes Zorlu** (00:27:53): Yeah, especially when I'm on afternoon shift, it's easier.
**Adrian Rinnus** (00:27:57): Yeah.
**Enes Zorlu** (00:27:58): Yeah, this week I'll be on afternoon shift, so.
**Enes Zorlu** (00:28:00): Yeah, whenever.
**Enes Zorlu** (00:28:01): Let's talk tomorrow again and see what's happening.
**Enes Zorlu** (00:28:04): Yeah, talk to you tomorrow then.
**Enes Zorlu** (00:28:06): All right.
**Enes Zorlu** (00:28:06): See you tomorrow.

## Kontext & Navigation
- [[DASHBOARD]]
- [[MEMORY]]
- [[OBSIDIAN_ROUTING]]
