## Inspiration
We all know how tough it can be to wake up before the sun is up, but did you know that there are health benefits associated with rising with the sun? Research has shown that syncing your wake and sleep cycle with the sun can result in less grogginess, easier wake-ups, and higher productivity. SunLite allows you to do this every day- even on dark winter mornings!

## What it does
The SunLite sunrise lamp allows you to schedule a simulated sunrise that syncs with your morning alarm. All you need is a smart lightbulb and a phone number, and then through our web app, you can register for an account, giving you access to our scheduling capabilities. From here, you can set your sunrise in two ways. First, you can do it through the web app UI. Second, if you're in a hurry, you can send a text to our phone number. Both of these will set up your lamp to start the sunrise 30 minutes before you have to wake up.

## How we built it
Our backend was made with **Flask** and **Python** and our frontend was made with **Typescript** and **React**. To support logins and authentication, we used **Auth0**. To store user requests, we implemented a **PostgreSQL** database. Since these requests often won’t be acted upon until several hours after they’re made, we used **Heroku Scheduler** to start the lamp when needed. To handle text-based requests, we used the **Twilio** API. 

## How it works
### Registration:
1. Users navigate to [wakeup2sunlite.tech](http://wakeup2sunlite.tech/).
2. Users create an account and authenticate themselves using Auth0.
3. Users add their phone number and smart light bulb API key under settings. This data will be added to our Users database.

### Sending a request through text:
1. Users send a text with their desired wakeup time (in 24-hour-clock time) to our phone number.
2. Our server's endpoint will be triggered, starting the flow of events.
3. The sender's phone number is validated against our Users database. If a registered user is found, the user's smart light bulb API key is fetched.
4. The user's requested wakeup time is added to our Requests database, along with their light bulb API key. 
5. Our Heroku Scheduler will poll the Requests database every 10 minutes. If there is a request to be executed, a request will be sent to the smart light bulb using the API key.
6. 30 minutes before the desired wake-up time, the light bulb will begin to cycle through the colors of the sunrise, giving the user a gentle wake-up experience.

### Sending a request through UI:
1. Once logged in, users set their desired wake-up time on our web app.
2. Same steps 2-6 as above.

## Challenges we ran into
* Figuring out a good way to execute requests hours after they were made (i.e. turning on the lamp 8 hours after the user sends a text request) was a big challenge. After some research, we came across the Heroku Scheduler. From here, we figured out that we could use a database to store the requests until it was time to use them, and check the database with the scheduler; this worked great!
* Setting up the PostgreSQL database was a big challenge as no one on the team had done it before. We struggled to get the database URL configuration working, but luckily, we were able to work out the bugs!

## Accomplishments that we're proud of
* This is our first hardware hack, and we’re really proud of finishing! Hardware adds an extra layer of complexity and potential for bugs, and we definitely felt the extra challenge along the way.
* It was our goal to have a pretty and user-friendly UI, and we think we did a good job!

## What we learned
* We learned a lot about services such as Twilio and Auth0. Using these services brought our hack to the next level, and we look forward to using them in the future!
* We got familiar with PostgreSQL and how to integrate it with Python. We went from minimal knowledge to a fully working database in a matter of hours.

## What's next for SunLite
The sky’s the limit for SunLite! Here are a few features we hope to add next:
* Recurring sunrise schedules
* Statistic dashboard showing average wake-up times + more
* Custom color settings
* Sunset mode
* Alarm sounds

## Want to try it?
To try out the SunLite sunrise lamp, we recommend using a [LIFX day/dusk smart light bulb](https://www.lifx.com/products/lifx-mini-day-dusk-refurbished). Then, just register your phone number and smart bulb API key at [wakeup2sunlite.tech](http://wakeup2sunlite.tech/). We hope you love it!
