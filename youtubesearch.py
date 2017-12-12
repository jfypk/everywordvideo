#!/usr/bin/python

# This sample executes a search request for the specified search term.
# Sample usage:
#   python youtubesearch.py --q=surfing --max-results=10
# NOTE: To use the sample, you must provide a developer key obtained
#       in the Google APIs Console. Search for "REPLACE_ME" in this code
#       to find the correct place to provide that key..

import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

CLIENT_SECRETS_FILE = "client_secret_everywordvideo.json"

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = 'AIzaSyCDYN6Akw3_8KraU8kmlwi4KfkBrQtCbOU'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def search_list_by_keyword(client, **kwargs):
      # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs)

  response = client.search().list(
    **kwargs
  ).execute()

  return print_response(response)

def youtube_search(query, results):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

  vidID = ""

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=query,
    part='id,snippet',
    maxResults=results
  ).execute()

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      vidID = search_result['id']['videoId']

  return vidID


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--q', help='Search term', default='Google')
  parser.add_argument('--max-results', help='Max results', default=25)
  args = parser.parse_args()

  try:
    youtube_search(args)
  except HttpError, e:
    print 'An HTTP error %d occurred:\n%s' % (e.resp.status, e.content)

