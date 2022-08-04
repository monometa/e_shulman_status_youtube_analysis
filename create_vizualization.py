def create_wordcloud_image(text: str, picture_name: str) -> None:
    mask = np.array(Image.open(picture_name))  # if mask is None?
    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          stopwords=stopwords_list_set,
                          # min_font_size=20,
                          collocations=True,
                          # max_words=1000,
                          mask=mask
                          ).generate(text)
    plt.figure(figsize=(30, 30), facecolor=None)
    image_colors = ImageColorGenerator(mask)
    plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()


def create_bubble_chart(df: pd.DataFrame) -> None:
    """
    Сейчас установлен трейий параметр год, а по идее должны быть просмотры
    :param data_plot:
    :return:
    """
    template = 'seaborn'
    fig = px.scatter(df,
                     x="likes",
                     y="comments",
                     color='views',
                     size="views",
                     log_x=True,
                     log_y=True,
                     template=template,
                     size_max=80,
                     title='Распределение по комментариям, лайкам и просмотрам',
                     hover_data=['title', 'year']
                     )
    ## save to localStorage
    # fig.show()
    # save to cloud
    py.plot(fig, filename='2022_bubble', auto_open=True)
