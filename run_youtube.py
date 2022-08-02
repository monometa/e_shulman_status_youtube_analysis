# API client
def get_service() -> object:
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)
    return youtube


def get_video_statistics_by_id(list_of_id: list) -> dict:
    lst_of_data = {}
    index = 0
    skipped_videos = 0
    for id_item in tqdm(list_of_id):
        r = get_service().videos().list(
            part='snippet,statistics',
            id=id_item
        ).execute()
        # raise if r['items'] is Null -> ... & skipped_videos += 1
        text = get_text_from_video(id_item)
        text = transform_text_into_words(text)
        try:
            lst_of_data[index] = {'video_id': id_item,
                                  'published_date': r['items'][0]['snippet']['publishedAt'],
                                  'title': r['items'][0]['snippet']['title'],
                                  'description': r['items'][0]['snippet']['description'],
                                  'views': r['items'][0]['statistics']['viewCount'],
                                  'likes': r['items'][0]['statistics']['likeCount'],
                                  'comments': r['items'][0]['statistics']['commentCount'],
                                  'text': text}
        except IndexError:
            lst_of_data[index] = dict()
            skipped_videos += 1
        index += 1
    return lst_of_data

def get_text_from_video(video_id: str) -> pd.Series:
    try:
        all_symbols = YouTubeTranscriptApi.get_transcript(video_id, languages=['ru'])
        df = pd.DataFrame(all_symbols)
        strings = df['text'].values
    except youtube_transcript_api.TranscriptsDisabled:
        strings = 'na'
    return strings
