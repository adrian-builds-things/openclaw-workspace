# Impromptu Google Meet Meeting

## Metadata

- recording_id: 64566909
- created_at: 2025-05-25T16:47:06Z
- recorded_by: Adrian Rinnus
- meeting_url: https://fathom.video/calls/309574004
- speakers: Adrian Rinnus, Luís Braga

## Summary

{"template_name": "General", "markdown_formatted": "## Meeting Purpose\n\n[Discuss and prioritize tasks for building an MVP UI feedback system for a company with multiple canteens and rotating meal menus.](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=9.0)\n\n## Key Takeaways\n\n  - [Prioritized tasks: menu creation/validation, dish/table/meal search, worker assignment, email confirmation](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=120.0)\n  - [UI focus: avoid pop-ups and complex flows, emphasize mobile readiness and simplicity](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=174.0)\n  - [Database structure needed for meals and assignments; AI consultation planned for optimal UI design](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=544.0)\n  - [Decoupling menu creation from Superbase initially, using JSON objects for flexibility](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=796.0)\n\n## Topics\n\n### MVP Development Priorities\n\n  - [Highest priority: Menu creation and validation](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=120.0)\n      - [UI development assigned to Luís](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=158.0)\n      - [Database work assigned to Adrian](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=125.0)\n  - [High priority tasks:](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=130.0)\n      - [Dish, table, and meal search functionality](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=130.0)\n      - [Add meal selection and search to menu creation](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=139.0)\n      - [API for creating dishes](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=142.0)\n      - [UI interface for dish creation](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=148.0)\n      - [Worker assignment profile](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=155.0)\n      - [Email confirmation system](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=164.0)\n\n### UI/UX Considerations\n\n  - [Avoid pop-ups and complex flows, especially in early MVP stages](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=174.0)\n  - [Focus on mobile readiness](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=174.0)\n  - [Simplify validation to avoid blocking users for minor mistakes](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=220.0)\n  - [Extract reusable components for flexibility (e.g., full page vs. dialog use)](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=908.0)\n  - [Investigate best UI approach for assigning menus to canteens (canteen-based vs. menu-based)](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=685.0)\n\n### Data Structure and Management\n\n  - [Plan to create JSON objects for menu data before finalizing Superbase structure](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=796.0)\n  - [Decouple menu creation from Superbase initially for flexibility](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=796.0)\n  - [Consider database consistency and potential race conditions](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=240.0)\n  - [Unique constraint needed for menus (combination of Week, Year, and Canteen)](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=445.0)\n\n### Business Model\n\n  - [Luís added business model ideas to be developed alongside technical work](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=282.0)\n\n### Workflow and Collaboration\n\n  - [Discussed creating end-of-day logs in the channel to track progress and avoid conflicts](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=987.0)\n  - [Explored using Cursor rules for maintaining code quality and following best practices](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=1046.0)\n\n## Next Steps\n\n  - [Adrian: Create database structure for meals and assignments](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=544.0)\n  - [Luís: Work on UI for menu creation using JSON objects, not tied to Superbase initially](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=920.0)\n  - [Consult AI with database structure to determine best UI for menu-canteen assignments](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=544.0)\n  - [Implement worker meal selection UI](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=718.0)\n  - [Set up end-of-day progress logging in the team channel](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=987.0)\n  - [Explore and implement relevant Cursor rules for code quality and best practices](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=1046.0)\n  - [Research optimal UI flow for assigning menus to canteens based on actual user workflows](https://fathom.video/share/kCdvzJgyVzdJw5WaX7Sxmid6pvhZo9i2?tab=summary&timestamp=576.0)\n"}

## Transcript

**Adrian Rinnus** (00:00:00): Where is it?
**Adrian Rinnus** (00:00:01): Where am I?
**Adrian Rinnus** (00:00:02): What the ?
**Adrian Rinnus** (00:00:04): Ah, here.
**Adrian Rinnus** (00:00:06): Let's go.
**Adrian Rinnus** (00:00:09): So what I was writing is, you are an productivity expert and expert in building MVPs.
**Adrian Rinnus** (00:00:13): Your job is to create an action plan with the required priorities.
**Adrian Rinnus** (00:00:17): I want to do the following.
**Adrian Rinnus** (00:00:19): You will receive a transcript of a meeting.
**Adrian Rinnus** (00:00:21): Identify all tasks that we were talking about.
**Adrian Rinnus** (00:00:23): Be very detailed.
**Adrian Rinnus** (00:00:24): Prioritize them.
**Adrian Rinnus** (00:00:25): Create a list for Luís and Adrian with tasks assigned and order them by priority.
**Adrian Rinnus** (00:00:30): Ask questions to increase clarity.
**Adrian Rinnus** (00:00:32): Give us hints about blind spots and based on experience as an entrepreneur and product designer and developer.
**Adrian Rinnus** (00:00:39): Give us hints about improving our UI based on the topics we discussed.
**Adrian Rinnus** (00:00:44): So now I'm answering the questions and then we are good to go.
**Adrian Rinnus** (00:00:49): So Prestige, we are building the MVP UI feedback level.
**Adrian Rinnus** (00:01:25): I'm ready, all right, , here we go.
**Luís Braga** (00:01:31): Let's see.
**Luís Braga** (00:01:35): Drums.
**Adrian Rinnus** (00:01:55): Mm-hmm.
**Adrian Rinnus** (00:01:58): Okay.
**Luís Braga** (00:02:00): Okay.
**Adrian Rinnus** (00:02:00): That means highest priority in menu creation and validation.
**Adrian Rinnus** (00:02:05): So you do the UI, I do the database.
**Adrian Rinnus** (00:02:08): OK, I'm good with that.
**Adrian Rinnus** (00:02:10): Second, dishes, table, and meal search.
**Adrian Rinnus** (00:02:13): OK.
**Adrian Rinnus** (00:02:19): Add meal selection, search, the menu creation.
**Adrian Rinnus** (00:02:22): OK, and for the dishes, we need the API to create the dishes.
**Adrian Rinnus** (00:02:28): There's also we need the UI interface to create dishes in that sense.
**Adrian Rinnus** (00:02:31): OK, I know we did that with a great new dish thingy.
**Adrian Rinnus** (00:02:35): OK, worker assignment profile is also high.
**Adrian Rinnus** (00:02:38): OK, now it's always assigned you to the UI, but OK.
**Adrian Rinnus** (00:02:44): Email confirmation back, yes, also high.
**Adrian Rinnus** (00:02:47): Then menu, sick leave, medium, quick win UI.
**Adrian Rinnus** (00:02:54): OK, review avoid pop-ups, complex flows, especially, mm-hmm, for now.
**Adrian Rinnus** (00:03:00): This group page is not lined up, okay, assign Luís.
**Adrian Rinnus** (00:03:03): Okay, this is yours.
**Adrian Rinnus** (00:03:06): Filtering navigation, this is also yours.
**Adrian Rinnus** (00:03:08): Okay, ask the person, here, we can go.
**Adrian Rinnus** (00:03:15): And it's already, no, it's not.
**Adrian Rinnus** (00:03:18): Is this the priority, at least one dish?
**Adrian Rinnus** (00:03:22): Yeah, dish table, yeah, okay, this is the table.
**Adrian Rinnus** (00:03:30): Clarifying questions.
**Adrian Rinnus** (00:03:32): Okay, this is cool, we have the questions here.
**Adrian Rinnus** (00:03:35): Blind spots, complex validations, don't overcomplicate.
**Adrian Rinnus** (00:03:38): Okay.
**Luís Braga** (00:03:39): Nice.
**Adrian Rinnus** (00:03:40): Avoid blocking users for minor mistakes in early MVP.
**Adrian Rinnus** (00:03:44): Okay.
**Adrian Rinnus** (00:03:45): Role management, without a clear role structure, may, yeah, this is something we have to tackle.
**Adrian Rinnus** (00:03:50): Copy assigning menus, ever need separate menus, make them, yeah, exactly, this is what we want to do with the meal or menu.
**Adrian Rinnus** (00:03:59): Do things.
**Adrian Rinnus** (00:04:00): Okay, mobile readiness, database consistency, okay, race conditions, good, all right, Blana, reply with answers, keep, I think that's pretty okay, all right, so if copy it and put it to Notion, what's happening then?
**Adrian Rinnus** (00:04:30): Let me see, I will just create a meeting notes, I know page, meeting notes.
**Luís Braga** (00:04:42): By the way, I just added there business model with some ideas I was writing ChatGPT with, so something to develop as well along the way.
**Adrian Rinnus** (00:04:56): Mm-hmm, it's fine.
**Luís Braga** (00:04:59): Thank
**Adrian Rinnus** (00:05:02): So, here we go, this is chat GPT action plan, plan, and ba-boom, alright, thank you for sharing the transcript, below is your Notion style, okay for Luís,-boom, ciao, alrighty, that's good, thank you, thank you, thank you, good, then we have that, I will also link to the meeting thingy, where is it, this one here, all right, meeting.
**Adrian Rinnus** (00:06:00): good all right so do we know what to do I think yes yes we need nothing so let me check ocean ocean ocean ocean ocean I hear they also say avoid models and poppers for main workflows you are right yeah scroll in UI it's not me
**Luís Braga** (00:07:01): How do we do this uniqueness of the menus for the combination of Week, Year, and Canteen?
**Luís Braga** (00:07:12): It's back-end validation, right?
**Adrian Rinnus** (00:07:18): You mean...
**Adrian Rinnus** (00:07:20): yeah.
**Adrian Rinnus** (00:07:21): But we can also do a front-end as well, because...
**Adrian Rinnus** (00:07:25): So, the point here is, no, we don't need it in the front-end, because we will do it like that, that we are assigning one meal to a canteen for a specific time range, and you can just assign one thing to one canteen, I would say, or...?
**Luís Braga** (00:07:52): So...
**Luís Braga** (00:07:54): I'll use it again, we have...
**Luís Braga** (00:07:56): So you're saying we have...
**Luís Braga** (00:07:58): ...
**Luís Braga** (00:07:59): ...
**Adrian Rinnus** (00:08:19): I think we should have one menu page and then a canteen page.
**Adrian Rinnus** (00:08:29): And then we can assign on the canteen page, we can assign them, is that logical in the way of UI?
**Adrian Rinnus** (00:08:35): I don't know.
**Adrian Rinnus** (00:08:55): This is something we could do some research on, what is the best way to do that in case it is.
**Adrian Rinnus** (00:09:04): Okay, I know what to do, I will create the database structure now for the meals and all the assignments and how we can handle that, and then we just put the database structure into an AI and ask it, hey, we have that kind of tables, what is the best way in the UI to do the assignments and connecting them?
**Adrian Rinnus** (00:09:25): Yeah, right.
**Luís Braga** (00:09:28): Because it's either going through, there's just two things, either going through the menus or through the canteens.
**Adrian Rinnus** (00:09:36): And I would say it makes more sense to go through the canteens because usually, so what is the workflow when we do that?
**Adrian Rinnus** (00:09:45): That's the question.
**Adrian Rinnus** (00:09:46): And for that it's important to know from the guys how they usually work.
**Adrian Rinnus** (00:09:50): How do they create the menu?
**Adrian Rinnus** (00:09:51): Is it based on the canteen if they do it or is it based on the menu and then they say, oh, okay, I will assign it to that canteen now or whatever.
**Adrian Rinnus** (00:10:00): at that's
**Adrian Rinnus** (00:10:00): There's a question we should ask them as well.
**Luís Braga** (00:10:01): The thing is, I'm pretty sure they simplify by having the same thing for all kinds of things.
**Luís Braga** (00:10:19): That's what makes sense.
**Luís Braga** (00:10:21): But then it's even easier, you know?
**Adrian Rinnus** (00:10:30): Because in the first moment it would just be assign menu to canteens.
**Adrian Rinnus** (00:10:36): Boom.
**Luís Braga** (00:10:37): Yes.
**Luís Braga** (00:10:38): The final goal really is to know what menus go to each canteens.
**Adrian Rinnus** (00:10:52): So we can also do it here, no?
**Adrian Rinnus** (00:10:54): We just use now the notetaker.
**Adrian Rinnus** (00:10:56): Okay, lovely notetaker.
**Adrian Rinnus** (00:10:58): We have the following situation.
**Adrian Rinnus** (00:10:59): We have...
**Adrian Rinnus** (00:11:00): A company which has multiple canteens and also they have in a three-week horizon they have changing meals and they said they change these three-week turns cycles three times a year.
**Adrian Rinnus** (00:11:18): That means they have about four different menus for three weeks that they are changing.
**Adrian Rinnus** (00:11:25): Now the question is, how can we build a UI that is assigning the menu and the time range to a canteen?
**Adrian Rinnus** (00:11:35): What is the best UI here?
**Adrian Rinnus** (00:11:37): This is a question we have to ask and we have to get clearance about.
**Adrian Rinnus** (00:11:41): Thank you.
**Adrian Rinnus** (00:11:42): So I'm just lazy.
**Adrian Rinnus** (00:11:44): I will copy that over and put it in JetGPT and see.
**Adrian Rinnus** (00:11:48): Let's see what happens.
**Adrian Rinnus** (00:11:50): Okay.
**Adrian Rinnus** (00:11:52): Good.
**Adrian Rinnus** (00:11:53): Good.
**Adrian Rinnus** (00:11:53): Do you want to tackle the...
**Adrian Rinnus** (00:11:58): Unless this is not...
**Adrian Rinnus** (00:12:00): Verify, do you want to tackle the worker thing of selecting meals or, no, do the menu creation in that sense.
**Adrian Rinnus** (00:12:10): will figure, just the UI for it.
**Luís Braga** (00:12:15): You mean this?
**Luís Braga** (00:12:17): No.
**Luís Braga** (00:12:18): no.
**Adrian Rinnus** (00:12:19): Yeah, the thing you were working on, I think that makes sense.
**Luís Braga** (00:12:25): Yeah, and to recap, what was the thing?
**Adrian Rinnus** (00:12:28): The validation on the database, so, I think it makes sense to extract components out of that, because then it doesn't matter if you use it on the full page later on or in the pop-up, in the dialog, and also the meal creation, you know, could you work on a JSON object and build it based on a JSON object and I can, later on, adjust the data.
**Adrian Rinnus** (00:13:00): So,
**Adrian Rinnus** (00:13:00): Based on the data that you need, it's easier if we see what data is required to build it, you know?
**Luís Braga** (00:13:06): What do you mean?
**Luís Braga** (00:13:08): Sorry?
**Luís Braga** (00:13:09): JSON what, you said?
**Adrian Rinnus** (00:13:11): It's JSON object, so JSON data object which is containing all the data.
**Adrian Rinnus** (00:13:16): So not writing the data to Superbase now, but just having a JSON object containing all the dummy data.
**Adrian Rinnus** (00:13:22): And as soon as we know what data do we need, I can adjust the Superbase structure once.
**Adrian Rinnus** (00:13:32): So decoupling the menu creation from Superbase for now, using dummy objects to have all the data which needs to be there, and not storing it in the database for the first moment, and then using that structure of the JSON database to create the tables, you know?
**Luís Braga** (00:13:49): I guess, but isn't it what we're doing with this?
**Adrian Rinnus** (00:13:56): Yeah, sure it is, but we don't know what needs to
**Luís Braga** (00:14:00): to be in the mutes, what, how is the data object looking like, so, no, okay, you're right, okay, I will, I, yeah, okay, you're right, I will, I will tackle that, yeah, okay, I will tackle that, uh, but listen, I, so as soon as I have these, uh, more lines as we want, the menus, creation, I can either, no, uh, I, I guess the best thing to do is to start thinking about the, the selection from the worker's side, and the question is, what do I need for that, I need the menus to be created, that's done, and what else, and nothing else.
**Luís Braga** (00:15:00): you.
**Luís Braga** (00:15:00): you.
**Luís Braga** (00:15:00): Thank Thank
**Adrian Rinnus** (00:15:00): The worker profile, more or less, yeah.
**Adrian Rinnus** (00:15:03): No, and to work on the UI, you just need, I would do it like that.
**Adrian Rinnus** (00:15:08): Work on the UI, don't think about the data, and then we will map it and create the data which is required, you know?
**Luís Braga** (00:15:16): True, true, very true.
**Luís Braga** (00:15:20): Just drop components there.
**Luís Braga** (00:15:22): Exactly.
**Luís Braga** (00:15:24): Yeah, I'm gonna try as much as I can now to care about Superbase or...
**Luís Braga** (00:15:28): Yeah.
**Luís Braga** (00:15:33): I can take care of validation, just submitting is not doing something else, just log the data in the form, something like that.
**Adrian Rinnus** (00:15:42): You can also do Superbase if you want to.
**Adrian Rinnus** (00:15:45): I can show you what I would do, stuff like that.
**Adrian Rinnus** (00:15:47): So that's fine.
**Luís Braga** (00:15:49): Yeah, okay.
**Luís Braga** (00:15:50): Let's go for another round of...
**Luís Braga** (00:15:53): as you wish.
**Luís Braga** (00:15:54): I think I'm required...
**Luís Braga** (00:15:58): so...
**Luís Braga** (00:15:58): I'm required...
**Luís Braga** (00:15:59): required...
**Luís Braga** (00:16:00): to attend some movie.
**Luís Braga** (00:16:02): Beatrice wants to go to see Stitch.
**Adrian Rinnus** (00:16:05): Okay, yeah, Sola also wants to go there, and I don't want to, but anyways.
**Luís Braga** (00:16:08): Yeah, so we're gonna go around seven-something, I'm not sure, so I have one hour more of fun here.
**Luís Braga** (00:16:17): Okay, enjoy.
**Adrian Rinnus** (00:16:24): I've read that one, and I really liked it.
**Adrian Rinnus** (00:16:27): Should we write some kind of little end-of-day log in the evening in the channel that we know what you were doing, what I was doing, what we are planning to do tomorrow?
**Adrian Rinnus** (00:16:35): We just know that we are not getting in conflict with the code, so just, hey, I was doing this, I'm planning to do this next, and blah, blah, blah, blah, I have these issues, or whatever.
**Adrian Rinnus** (00:16:45): Just two minutes of dumping what we did, and we can, we can.
**Luís Braga** (00:16:51): I also was thinking about, I'm not sharing, no.
**Luís Braga** (00:16:56): Yeah, are you sure?
**Luís Braga** (00:16:58): I am.
**Luís Braga** (00:16:58): I am, I'm Yeah.
**Luís Braga** (00:17:01): I was wondering if there's something, but I don't think so for now if I'm not playing much with Superbase, but would, the thing that I told you about, what's this, I don't need, oh there, rules, memories, workflows, R-safe prompts that KSK can follow, that's interesting.
**Adrian Rinnus** (00:17:26): I need to explore more of these, but rules for the workspace would be awesome, and can you think of something, what you can do is, ah, there's something for Cursor, and I have found it, wait, I'm looking for it and send it to you, they had some predefined rules, Cursor rules, yeah, awesome Cursor rules.
**Adrian Rinnus** (00:18:00): And there you go.
**Adrian Rinnus** (00:18:02): It's in Sled for you.
**Adrian Rinnus** (00:18:06): And they have some rules to create super bass, blah, blah, blah, blah, blah.
**Adrian Rinnus** (00:18:12): And I think it's not that bad.
**Luís Braga** (00:18:16): Cursor rules.
**Luís Braga** (00:18:18): Ah, cool.
**Luís Braga** (00:18:20): Okay, this is...
**Adrian Rinnus** (00:18:23): And you can also go to the rules new on the left, in the top one.
**Adrian Rinnus** (00:18:28): And they have split it up, but you have more modularized rules that you can apply.
**Adrian Rinnus** (00:18:33): So you can also have look at them.
**Adrian Rinnus** (00:18:34): I think it also makes sense.
**Luís Braga** (00:18:40): So this means...
**Luís Braga** (00:18:41): Link to guidelines is always good, in my opinion.
**Luís Braga** (00:18:45): So, let's say, if I put this as a rule, VV, I just go there, coastal guide, right?
**Luís Braga** (00:18:54): And this would be...
**Luís Braga** (00:18:55): Well, what's their name?
**Luís Braga** (00:18:57): Tailwind, just Tailwind.
**Luís Braga** (00:18:59): Tailwind.
**Luís Braga** (00:19:00): Boom.
**Luís Braga** (00:19:01): Oof.
**Luís Braga** (00:19:02): Whatever I am telling.
**Luís Braga** (00:19:05): Man, this activation mode, this flow can be, you that is always on.
**Luís Braga** (00:19:14): Or, boom.
**Luís Braga** (00:19:19): Do I need this?
**Luís Braga** (00:19:20): No, this is for Cursor.
**Adrian Rinnus** (00:19:22): This is more or less exactly the always-on stuff from Cursor which they use.
**Adrian Rinnus** (00:19:27): And I am also not sure about the commenting and stuff like that.
**Adrian Rinnus** (00:19:30): If that works like that here, you have to check that in the documentation.
**Adrian Rinnus** (00:19:34): But I think the content is already pretty good.
**Luís Braga** (00:19:39): All right.
**Luís Braga** (00:19:40): Saved.
**Luís Braga** (00:19:41): Tailwind and probably react and send.
**Luís Braga** (00:19:45): code.
**Luís Braga** (00:19:45): Clean code, I think.
**Adrian Rinnus** (00:19:46): Code quality also makes sense.
**Adrian Rinnus** (00:19:48): Database is also cool.
**Adrian Rinnus** (00:19:51): Next.js is also there.
**Adrian Rinnus** (00:19:53): Yeah.
**Luís Braga** (00:19:55): TypeScript.
**Luís Braga** (00:19:55): Great.
**Luís Braga** (00:19:56): Awesome.
**Luís Braga** (00:19:57): I wonder how this is gonna...
**Adrian Rinnus** (00:20:02): All right, you know what, I'm going for a walk for some minutes to move a little bit and get some fresh air, and then I will start the database stuff.
**Luís Braga** (00:20:10): Cool, all right.
**Luís Braga** (00:20:12): Have fun in the cinema later on.
**Luís Braga** (00:20:15): Will do, later, man.
**Luís Braga** (00:20:16): Thanks, bye-bye.
**Luís Braga** (00:20:17): Bye.

## Kontext & Navigation
- [[DASHBOARD]]
- [[MEMORY]]
- [[OBSIDIAN_ROUTING]]
