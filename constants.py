from collections import OrderedDict
import re

ZIP_NAME = 'rushal verma.zip'

DATE_REGEX = re.compile(r'/Date\((\d+)([+-]\d+)\)/')

FIELD_NAMES= OrderedDict([
    ('user','user'),
    ('date','date'),
    ('_engagementPerDay','engagement_per_day'),
    ('_blockedFollowersPerDay','blocked_followers_per_day'),
    ('_followersPerDayEx','follower_count'),
    ('_followingsPerDayEx','following_count'),
    ('_followsBackPerDay','follow_backs_per_day'),
    ('_followsPerDayEx','follows_per_day'),
    ('_likesPerDayEx','likes_per_day'),
    ('_unfollowDayEx','unfollows_per_day'),
    ('_commentsPerDayEx','comments_per_day'),
    ('_seenStoriesPerDay','seen_stories_per_day'),
    ('_contactMembersFriendsPerDayEx','dms_per_day'),
])