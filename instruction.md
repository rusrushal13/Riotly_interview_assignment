# Introduction

We have multiple servers are running an application. The data is store as json file. We want to sync all the data file to one place as csv files.

## System Features

Please create scripts that do follow tasks.

- Login to Cloud Storage with credentials.json
- Download all the json files in `data/` in the bucket
- Convert the json data to csv with following mapping

```bash
_engagementPerDay                 engagement_per_day
_blockedFollowersPerDay           blocked_followers_per_day
_followersPerDayEx                follower_count
_followingsPerDayEx               following_count
_followsBackPerDay                follow_backs_per_day
_followsPerDayEx                  follows_per_day
_likesPerDayEx                    likes_per_day
_unfollowDayEx                    unfollows_per_day
_commentsPerDayEx                 comments_per_day
_seenStoriesPerDay                seen_stories_per_day
_contactMembersFriendsPerDayEx    dms_per_day
```

- The expected output format

`user, date, engagement_per_day, blocked_followers_per_day, follower_count, following_count, follow_backs_per_day, follows_per_day, likes_per_day, unfollows_per_day, comments_per_day, seen_stories_per_day, dms_per_day`

- Merge all the csv files to a single csv file
- Pack all files into a zip file
- Upload the converted csv data to a cloud storage with following naming pattern

`output/{Your full in lowercase with spaces}.zip`

## Implementation Requirements

- Language: Any
- Database: Any
- Platform: Any

## Extras

- The bucket name: riotly-interview-test

## Deliverable

You should send the following Deliverables

- A zip file with source code, output files and readme.md
- Explain your implementation in the readme.md
- Record of time usage in the readme.md

### minimal readme.md sections

- Implementation explanation
- Implementation time logs