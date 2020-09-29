# Win Freelance Jobs
We'll build with the required tech stack because it will make us a low risk hire
## Tech Stack
- airflow
- docker
- object-oriented python
- aws (if we have time)

## Gameplan
+ connect to twitter API (ugly)
+ object-oriented refactor (pretty)
- airflow for weekly rerunning 
  + add two tweet.fields:
    - created_at
    - likes_count
  - schedule tasks:
    - weekly tweet search
    - update top tweets database
      - naive: sort tweets database for top 10 liked tweets, clear out top tweets db, and post new top 10
    - build hugo blog and push to github/netlify
  - publish to netlify blog
    - Intro Page:
      - paulg
        - Paul Graham's Top 10 Tweets Since X
      - naval
      - brennandunn
      - r00k
      - patio11
 
- docker for easy deployment
- deploy app to aws
