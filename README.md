# Weather Recommendations App

This light Django app was built to learn about the Django framework and begin to solve a problem that many people with Autism and ADHD struggle with daily; decision fatigue with clothing choices.

This Stage 1 Minimum Viable Product shows the weather in given locations, and some general recomendations for those weather conditions.

It uses OpenWeatherAPI to get basic temperature data as well as an icon to display.

![example_1](https://github.com/ryanlatch/weather_clothes_app/blob/master/examples/example1.png)

You can add as many locations as you'd like. If you try to add one that already exists, it will return an error.

![example_2](https://github.com/ryanlatch/weather_clothes_app/blob/master/examples/example%202.png)

### Planned stage 2:

- Set up user login and authentication.
- Set a place to store what type of clothing you have, per user in a DB and apply rudimentary catagories, such as 't-shirt' or 'dress' to those items.
- Display all of the clothes that user has that would suit that temperature range.

### Stage 3:

- Use the AI and ML to determine which colours go with eachother to put together a good outfit.