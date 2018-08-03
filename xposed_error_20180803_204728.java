public abstract interface ApiService
{
  @POST("utils/adjust-exp")
  public abstract Call<RegisterResponse> adjustExp(@Header("authorization") String paramString, @Body AdjustExpBody paramAdjustExpBody);
  
  @POST("comics/{comicId}/favourite")
  public abstract Call<GeneralResponse<ActionResponse>> bookmarkComicWithId(@Header("authorization") String paramString1, @Path("comicId") String paramString2);
  
  @POST("auth/forgot-password")
  public abstract Call<RegisterResponse> forgotPassword(@Body ForgotPasswordBody paramForgotPasswordBody);
  
  @GET("announcements")
  public abstract Call<GeneralResponse<AnnouncementsResponse>> getAnnouncements(@Header("authorization") String paramString, @Query("page") int paramInt);
  
  @GET("applications?platform=android")
  public abstract Call<GeneralResponse<ApplicationsResponse>> getApplications(@Header("authorization") String paramString, @Query("page") int paramInt);
  
  @GET("banners")
  public abstract Call<GeneralResponse<BannersResponse>> getBanners(@Header("authorization") String paramString);
  
  @GET("categories")
  public abstract Call<GeneralResponse<CategoryResponse>> getCategories(@Header("authorization") String paramString);
  
  @GET("chat")
  public abstract Call<GeneralResponse<ChatroomListResponse>> getChatroomList(@Header("authorization") String paramString);
  
  @GET("comics/{comicId}/eps")
  public abstract Call<GeneralResponse<ComicEpisodeResponse>> getComicEpisode(@Header("authorization") String paramString1, @Path("comicId") String paramString2, @Query("page") int paramInt);
  
  @GET("comics")
  public abstract Call<GeneralResponse<ComicListResponse>> getComicList(@Header("authorization") String paramString1, @Query("page") int paramInt, @Query("c") String paramString2, @Query("t") String paramString3, @Query("a") String paramString4, @Query("f") String paramString5, @Query("s") String paramString6, @Query("ct") String paramString7, @Query("ca") String paramString8);
  
  @GET("comics/search")
  public abstract Call<GeneralResponse<ComicListResponse>> getComicListWithSearchKey(@Header("authorization") String paramString1, @Query("page") int paramInt, @Query("q") String paramString2);
  
  @GET("comics/{comicId}")
  public abstract Call<GeneralResponse<ComicDetailResponse>> getComicWithId(@Header("authorization") String paramString1, @Path("comicId") String paramString2);
  
  @GET("comics/{comicId}/comments")
  public abstract Call<GeneralResponse<CommentsResponse>> getCommentsWithComicId(@Header("authorization") String paramString1, @Path("comicId") String paramString2, @Query("page") int paramInt);
  
  @GET("comments/{commentId}/childrens")
  public abstract Call<GeneralResponse<CommentsResponse>> getCommentsWithCommentId(@Header("authorization") String paramString1, @Path("commentId") String paramString2, @Query("page") int paramInt);
  
  @GET("games/{gameId}/comments")
  public abstract Call<GeneralResponse<CommentsResponse>> getCommentsWithGameId(@Header("authorization") String paramString1, @Path("gameId") String paramString2, @Query("page") int paramInt);
  
  @GET("users/favourite")
  public abstract Call<GeneralResponse<ComicListResponse>> getFavourite(@Header("authorization") String paramString, @Query("page") int paramInt);
  
  @GET("games/{gameId}")
  public abstract Call<GeneralResponse<GameDetailResponse>> getGameDetail(@Header("authorization") String paramString1, @Path("gameId") String paramString2);
  
  @GET("games")
  public abstract Call<GeneralResponse<GameListResponse>> getGameList(@Header("authorization") String paramString, @Query("page") int paramInt);
  
  @GET("init?platform=android")
  public abstract Call<GeneralResponse<InitialResponse>> getInit(@Header("authorization") String paramString);
  
  @GET("keywords")
  public abstract Call<GeneralResponse<KeywordsResponse>> getKeywords(@Header("authorization") String paramString);
  
  @GET("comics/knight-leaderboard")
  public abstract Call<GeneralResponse<LeaderboardKnightResponse>> getKnightLeaderboard(@Header("authorization") String paramString);
  
  @GET("comics/leaderboard")
  public abstract Call<GeneralResponse<LeaderboardResponse>> getLeaderboard(@Header("authorization") String paramString1, @Query("tt") String paramString2, @Query("ct") String paramString3);
  
  @GET("eps/{epsId}/download")
  public abstract Call<GeneralResponse<ComicPagesResponse>> getPagesWithEpisodeId(@Header("authorization") String paramString1, @Path("epsId") String paramString2);
  
  @GET("eps/{epsId}/pages")
  public abstract Call<GeneralResponse<ComicPagesResponse>> getPagesWithEpisodeId(@Header("authorization") String paramString1, @Path("epsId") String paramString2, @Query("page") int paramInt);
  
  @GET("comics/{comicId}/order/{order}/pages")
  public abstract Call<GeneralResponse<ComicPagesResponse>> getPagesWithOrder(@Header("authorization") String paramString1, @Path("comicId") String paramString2, @Path("order") int paramInt1, @Query("page") int paramInt2);
  
  @GET("users/my-comments")
  public abstract Call<GeneralResponse<ProfileCommentsResponse>> getProfileComments(@Header("authorization") String paramString, @Query("page") int paramInt);
  
  @GET("comics/random")
  public abstract Call<GeneralResponse<ComicRandomListResponse>> getRandomComicList(@Header("authorization") String paramString);
  
  @GET("tags")
  public abstract Call<GeneralResponse<TagListResponse>> getTags(@Header("authorization") String paramString);
  
  @GET("users/profile")
  public abstract Call<GeneralResponse<UserProfileResponse>> getUserProfile(@Header("authorization") String paramString);
  
  @GET("users/{userId}/profile")
  public abstract Call<GeneralResponse<UserProfileResponse>> getUserProfileWithUserId(@Header("authorization") String paramString1, @Path("userId") String paramString2);
  
  @GET("init")
  public abstract Call<WakaInitResponse> getWakaInit();
  
  @POST("comments/{commentId}/hide")
  public abstract Call<GeneralResponse<MessageResponse>> hideCommentWithCommentId(@Header("authorization") String paramString1, @Path("commentId") String paramString2);
  
  @POST("comics/{comicId}/like")
  public abstract Call<GeneralResponse<ActionResponse>> likeComicWithId(@Header("authorization") String paramString1, @Path("comicId") String paramString2);
  
  @POST("comments/{commentId}/like")
  public abstract Call<GeneralResponse<ActionResponse>> likeCommentWithId(@Header("authorization") String paramString1, @Path("commentId") String paramString2);
  
  @POST("games/{gameId}/like")
  public abstract Call<GeneralResponse<ActionResponse>> likeGameWithId(@Header("authorization") String paramString1, @Path("gameId") String paramString2);
  
  @POST("comments/{commentId}/top")
  public abstract Call<GeneralResponse<CommentPostToTopResponse>> postCommentToTheTop(@Header("authorization") String paramString1, @Path("commentId") String paramString2);
  
  @POST("comics/{comicId}/comments")
  public abstract Call<GeneralResponse<PostCommentResponse>> postCommentWithComicId(@Header("authorization") String paramString1, @Path("comicId") String paramString2, @Body CommentBody paramCommentBody);
  
  @POST("comments/{commentId}")
  public abstract Call<GeneralResponse<PostCommentResponse>> postCommentWithCommentId(@Header("authorization") String paramString1, @Path("commentId") String paramString2, @Body CommentBody paramCommentBody);
  
  @POST("games/{gameId}/comments")
  public abstract Call<GeneralResponse<PostCommentResponse>> postCommentWithGameId(@Header("authorization") String paramString1, @Path("gameId") String paramString2, @Body CommentBody paramCommentBody);
  
  @POST("users/{userId}/dirty")
  public abstract Call<GeneralResponse<UserProfileDirtyResponse>> postDirty(@Header("authorization") String paramString1, @Path("userId") String paramString2);
  
  @POST("users/punch-in")
  public abstract Call<GeneralResponse<PunchInResponse>> punchIn(@Header("authorization") String paramString);
  
  @PUT("users/avatar")
  public abstract Call<GeneralResponse<PutAvatarResponse>> putUserAvatar(@Header("authorization") String paramString, @Body AvatarBody paramAvatarBody);
  
  @POST("auth/register")
  public abstract Call<RegisterResponse> register(@Body RegisterBody paramRegisterBody);
  
  @POST("auth/resend-activation")
  public abstract Call<RegisterResponse> resendActivation(@Body ForgotPasswordBody paramForgotPasswordBody);
  
  @POST("auth/sign-in")
  public abstract Call<GeneralResponse<SignInResponse>> signIn(@Body SignInBody paramSignInBody);
  @SerializedName("email")
  String email;
  @SerializedName("password")
  String password;
  
  
  @PUT("users/profile")
  public abstract Call<RegisterResponse> updateProfile(@Header("authorization") String paramString, @Body UpdateProfileBody paramUpdateProfileBody);
  
  @PUT("users/password")
  public abstract Call<RegisterResponse> updateUserPassword(@Header("authorization") String paramString, @Body ChangePasswordBody paramChangePasswordBody);
  
  @PUT("users/{userId}/title")
  public abstract Call<RegisterResponse> updateUserTitle(@Header("authorization") String paramString1, @Path("userId") String paramString2, @Body UpdateUserTitleBody paramUpdateUserTitleBody);
}