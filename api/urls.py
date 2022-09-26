from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns= [
    path('', home, name="home"),
    # all movies endpoints
    path('api/movies/', apiMoviesHome, name="moviesHome"),
    path('api/movies/popular', apiMoviesPopular, name="popularMovies"),
    path('api/movies/theaters/', moviesInTheater, name="moviesInTheater"),
    path('api/movies/toprated/', apiMoviesTopRated, name="moviesTopRated"),
    path('api/movies/upcoming/', apiMoviesUpcoming, name="moviesUpcoming"),
    path('api/movies/<int:tmdbid>', FetchMovieID, name="FetchMovieID"),
    path('api/movies/search/<str:query>', searchMoviesTitle, name="searchMoviesTitle"),
    # production company endpoint
    path('api/company/<int:id>', getCompany, name="getCompany"),
    # queries endpoints
    path('api/search/<str:query>/', searchPage, name="search"),
    path('api/search/<str:query>/page/<int:num>/', searchMultiPage, name="searchMultiPage"),
    # category or genres endpoint
    path('api/genres/', getGenre, name="getGenre"),
    # tv shows endpoints
    path('api/tv/', apiTVHome, name="tvHome"),
    path('api/tv/popular/', apiTVPopular, name="tvHome"),
    path('api/tv/toprated/', apiTvToprated, name="tvTopRates"),
    path('api/tv/ongoing/', tvOngoing, name="tvOngoing"),
    path('api/tv/<int:tmdbid>/', FetchTvID, name="FetchTvID"),
    path('api/tv/<int:tmdbid>/season/<int:seasonnumb>/', FetchSeason, name="FetchTvSeason"),
    path('api/tv/<int:tmdbid>/season/<int:seasonnumb>/episode/<int:ep>/', FetchEpisode, name="FetchTvEpisode"),
    path('api/tv/videos/<int:tmdbid>/season/<int:seasonnumb>/', FetchTvVideos, name="FetchTvVideos"),
    path('api/tv/images/<int:tmdbid>/season/<int:seasonnumb>/', FetchTvImages, name="FetchTvImages"),
    # casts or person relates endpoints
    path('api/person/<int:personid>/', FetchPerson, name="FetchPerson"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)