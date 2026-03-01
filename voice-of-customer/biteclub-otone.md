# Voice of Customer — Bite Club O-Töne

Updated: 2026-02-28 13:30 UTC

Total quotes: 20

## 1. Adrian Rinnus — 2025-05-19 (meeting 63277269, 00:20:00)
> I'm even not sure if this is needed because for me it's so what I understood is it's about collecting how many or how many different dishes they have to prepare to buy the groceries and I think what you are talking about is already the next step is that right because in the first one it's just hey I want to order this food and then the chefs know okay you need 50 of these kind of dishes 75 of them 52 of this whatever and then they can buy the groceries and prepare and then as soon as the people are coming in this is something I think they have cashier anyways they are just scanning the QR code and then they are getting the meal somehow so I don't think that this is already an over-engineered solution in my opinion with a screen I know what you want to achieve did you just say it's over-engineered yeah a bit yeah yeah yeah yeah

## 2. Adrian Rinnus — 2025-05-19 (meeting 63277269, 00:32:04)
> I think we can do it, and it should not be that hard in my opinion, you know the MVP approach, to have something that works means people, so cookers or admins can create menus, people, workers, employees can order food for a week, and cookers get a list of stuff they have to deliver and that they have to provide.

## 3. Luís Braga — 2025-05-19 (meeting 63277269, 00:11:30)
> Okay, they select the thing, and let's imagine today, on the, I don't know, Monday, they get to the canteen for lunch, no, sorry, for dinner, or whatever, when the meal is on the canteen, or whenever they need to pick their food, they need to do some sort of check-in.

## 4. Adrian Rinnus — 2025-05-28 (meeting 65023708, 00:01:00)
> creating menus assigning menus to calendar weeks and then we have the my meals part where the people can select what they want to choose and that's MVP my opinion right yeah yeah and one thing is missing an important one and we need some kind of summary whatever for the to buy the groceries and stuff like that how many meals do we have or do we need and stuff like that this is missing yeah the reports yes exactly yeah to what extent that goes like ingredients I don't know because there would not from that for later I think it's really cool because yeah because later you can get the whole grocery list out of it and do the ordering out of it that would be really cool but in the first one it's just we have 50 of that meal and 100 of this and whatever so that we have the numbers and yeah yeah yeah yeah yeah yeah yeah you

## 5. Adrian Rinnus — 2025-05-25 (meeting 64566156, 00:22:00)
> Filtering, so not for the workers, so dishes, dishes are missing, and, and, and, and, and that's it, menus, there you have the meals, okay, this is now a JSONDB, this will change, and one menu is a week number, year, and canteen ID, and there I'm not sure, I think we should have an, and another table which is tackling the canteen and menu assignment with the calendar week, or the time slot more or less, and this is not related to the menu, because if you want to reuse the menu, it should not be hardly connected to the canteen and the week and the year, so I have to split it up, right, so basically a table, with two foreign keys, menus and canteen, subscribe.

## 6. Adrian Rinnus — 2025-05-21 (meeting 63832203, 00:01:01)
> So if I can interrupt for a second, I think it makes sense if we have a little bit of a structured approach, so I would like to know how, so as far as I know, I can tell you what I already know, so it's about, you have some canteens for your construction site, and it's a mess, the workers order food, and you have a mess there, and you don't know how to handle it, that's the short version.

## 7. Adrian Rinnus — 2025-10-07 (meeting 92269354, 01:06:27)
> All right, so just to summarize a bit up, I will finish working the stuff with that for canteen assignment, changing order stuff, I will work on that, finish that one, and then I will take care about the NFC and the kitchen queue for the orders which are lining up, and I will let you know with the timeline how I can handle it, if I have an idea about it today or tomorrow.

## 8. Adrian Rinnus — 2025-05-21 (meeting 63832203, 00:09:17)
> So now what you want to have is that the workers are ordering the food in the morning, for example, no, until Saturdays for the next week and they order breakfast, no, not breakfast, but it's mainly lunch and dinner and okay, so you have these two and you have a meal plan for three weeks usually and this is changing two to three times a year.

## 9. Adrian Rinnus — 2025-05-21 (meeting 63832203, 00:10:03)
> And you need an admin access to change the meal, and you need an admin access to move people from one canteen to another, and there are different companies, which are internal companies, that are in the same canteen, so you need to assign the people from one canteen to the other.

## 10. Adrian Rinnus — 2025-05-21 (meeting 63832203, 00:18:04)
> I think we have now a pretty good picture about the thing, that the question is, so there are so many things that you would like to solve, what is the most important one, what is your biggest pain point, it's the pre-ordering of the food that you don't have that much food waste.

## 11. Adrian Rinnus — 2025-11-28 (meeting 104897323, 00:52:06)
> For the new landing page, I'm also building a food waste calculator right now, where you enter how many people are working in the company, how many meals you serve, and then you get a number of euros that you save per meal that you are serving.

## 12. Xavier Sá — 2025-11-28 (meeting 104897323, 00:02:23)
> So the first one, I don't know if you are aware or not, if you switch some worker from one canteen to another, imagine in the middle of the week, it won't transfer the meal selection from one canteen to another.

## 13. Adrian Rinnus — 2025-11-04 (meeting 98921252, 00:15:14)
> Yeah, and it's a win-win situation, because if they use it, they have a reduction in food waste and whatever, and also they reduce the time that they need to organize the food distribution and whatever.

## 14. Adrian Rinnus — 2025-06-05 (meeting 66621582, 00:38:00)
> This is just theming, we are working on the theme, to have it looking better or different, and now I think it's about the worker management and then also the worker meal selection, what you're doing.

## 15. Luís Braga — 2025-06-05 (meeting 66621582, 00:18:00)
> We the chef scanning some QR code or just enter some worker ID and we can actually try it out like so, let's say this is obviously fake, it will give the thing and the meal, if there's any.

## 16. Filipe Fernandes — 2025-11-28 (meeting 104897323, 00:15:27)
> You mean the administrator does the meal selection for a worker?

## 17. Enes Zorlu — 2026-02-13 (meeting 122206235, 00:02:59)
> It's a big topic for us at the moment to focus on the mobile and improve the usability for employees so they have ease of use from their end, just remove the frictions for them so it's easier for them to book meals for example, it's easier for them to navigate between screens so I think that's the main focus because I remember most of the requests from you in terms of bugs and improvements the urgent ones they have been addressed and of course we are interested to hear if there are more hot topics on your end so we can put them on priority list as well but I think from Kassai's side of things main thing we are working on improving the UI starting with employee mobile and then continuing with the other screens maybe you already seen some of the updates that we really that

## 18. Adrian Rinnus — 2025-10-07 (meeting 92336193, 00:27:02)
> all right good so resets all right okay uh so then let's let's sorry new feature yes i would say new feature and then we also put the the whole page in the feature you know that the content of the page at least well so what do call it engine delivery or delivery mode i don't know delivery delivery meal delivery is it delivery meal yeah good wait no delivery i it's well if distribution food distribution in that sense ah yeah because you're you're looking for a like more generic yeah general distribution meal distribution that's meal

## 19. Luís Braga — 2025-05-25 (meeting 64566909, 00:14:00)
> to be in the mutes, what, how is the data object looking like, so, no, okay, you're right, okay, I will, I, yeah, okay, you're right, I will, I will tackle that, yeah, okay, I will tackle that, uh, but listen, I, so as soon as I have these, uh, more lines as we want, the menus, creation, I can either, no, uh, I, I guess the best thing to do is to start thinking about the, the selection from the worker's side, and the question is, what do I need for that, I need the menus to be created, that's done, and what else, and nothing else.

## 20. Xavier Sá — 2026-02-13 (meeting 122206235, 00:19:03)
> Yeah, the much information we have, the better, we just need to see how we're going to manage it, that's it, because if I have, instead of 5 reports, if I have 15, at some point they will be useful to me, Yeah, basically that, like I said, we or you need to go through the reports to make sure that they are aligned, because when we'll do these implementations about discounting the meal and etc., we want to make sure that the data is correct, because we could tell people that they didn't, and the...
