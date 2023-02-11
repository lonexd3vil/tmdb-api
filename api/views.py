from django.shortcuts import render
from tmdbv3api import TMDb, Movie, Search, Season, Trending, Company, Configuration, Discover, Genre, TV, Person
import requests
import pprint
from rest_framework.decorators import api_view
from rest_framework.response import Response
# tmdb helper vars
tmdb = TMDb()
tmdb.api_key = 'API_KEY'
tmdb.debug = True
tmdbImgSourceHD = "https://image.tmdb.org/t/p/w780"
tmdbImgSourceSD = "https://image.tmdb.org/t/p/w500"
tmdbImgSourceSmall = "https://image.tmdb.org/t/p/w342"
tmdbBackdropSourceFHD = "https://image.tmdb.org/t/p/w1280"
tmdbBackdropSourceHD = "https://image.tmdb.org/t/p/w780"
tmdbBackdropSourceSD = "https://image.tmdb.org/t/p/w300"
ytWatch = "https://www.youtube.com/watch?v="
movie = Movie()
tv = TV()
popular = movie.popular()
popularTv = tv.popular()
company = Company()
configuration = Configuration()
discover = Discover()
search = Search()
genre = Genre()
season = Season()
trending = Trending()
person = Person()

def home(request):
    return render(template_name="home.html", request=request)
s = requests.Session()

def movieRecommendations(tmdb_id):
    recommendations = movie.recommendations(movie_id=tmdb_id)
    data = []
    for recommendation in recommendations:
        rcom = {}
        rcom['movie_id'] = recommendation.id
        rcom['movie_title'] = recommendation.title
        rcom['movie_overview'] = recommendation.overview
        if recommendation.poster_path == None:
            pass
        else:
            rcom['movie_poster_hd'] = tmdbImgSourceHD+str(recommendation.poster_path)
            rcom['movie_poster_sd'] = tmdbImgSourceSD+str(recommendation.poster_path)
            rcom['movie_poster_small'] = tmdbImgSourceSmall+str(recommendation.poster_path)
        rcom['type'] = "movie"
        data.append(rcom)
    return data

def TVRecommendations(tmdb_id):
    recommendations = tv.recommendations(tmdb_id)
    data = []
    for recommendation in recommendations:
        rcom = {}
        rcom['tv_id'] = recommendation.id
        rcom['tv_title'] = recommendation.name
        rcom['tv_overview'] = recommendation.overview
        if recommendation.poster_path == None:
            pass
        else:
            rcom['tv_poster_hd'] = tmdbImgSourceHD+str(recommendation.poster_path)
            rcom['tv_poster_sd'] = tmdbImgSourceSD+str(recommendation.poster_path)
            rcom['tv_poster_small'] = tmdbImgSourceSmall+str(recommendation.poster_path)
        rcom['type'] = "tv"
        data.append(rcom)
    return data

def getProductionsCompanies(tmdb_id):
    m = movie.details(tmdb_id)
    prodComp = []
    for i in range(len(m.production_companies)):
        companies = dict(m.production_companies[i-1])
        info = {}
        info['production_company_id'] = companies['id']
        info['production_company_name'] = companies['name']
        if companies['logo_path'] == None:
            pass
        else:
            info['production_company_logo_hd'] = tmdbImgSourceHD+str(companies['logo_path'])
            info['production_company_logo_sd'] = tmdbImgSourceSD+str(companies['logo_path'])
            info['production_company_logo_small'] = tmdbImgSourceSmall+str(companies['logo_path'])
        info['production_company_origin'] = companies['origin_country']
        prodComp.append(info)
    return prodComp

def getProductionsCompaniesTV(tmdb_id):
    m = tv.details(tmdb_id)
    prodComp = []
    for i in range(len(m.production_companies)):
        companies = dict(m.production_companies[i-1])
        info = {}
        info['production_company_id'] = companies['id']
        info['production_company_name'] = companies['name']
        if companies['logo_path'] == None:
            pass
        else:
            info['production_company_logo_hd'] = tmdbImgSourceHD+str(companies['logo_path'])
            info['production_company_logo_sd'] = tmdbImgSourceSD+str(companies['logo_path'])
            info['production_company_logo_small'] = tmdbImgSourceSmall+str(companies['logo_path'])
        info['production_company_origin'] = companies['origin_country']
        prodComp.append(info)
    return prodComp

def getProductionCountries(tmdb_id):
    m = movie.details(tmdb_id)
    prodCountry = []
    for i in range(len(m.production_countries)):
        countries = dict(m.production_countries[i])
        info = {}
        info['production_country_iso'] = countries['iso_3166_1']
        info['production_company_name'] = countries['name']
        prodCountry.append(info)
    return prodCountry

def getProductionCountriesTV(tmdb_id):
    m = tv.details(tmdb_id)
    prodCountry = []
    for i in range(len(m.production_countries)):
        countries = dict(m.production_countries[i])
        info = {}
        info['production_country_iso'] = countries['iso_3166_1']
        info['production_company_name'] = countries['name']
        prodCountry.append(info)
    return prodCountry

def getSpokenLanguages(tmdb_id):
    m = movie.details(tmdb_id)
    langs = []
    for i in range(len(m.spoken_languages)):
        languages = dict(m.spoken_languages[i])
        info = {}
        info['english_name'] = languages['english_name']
        info['name'] = languages['name']
        langs.append(info)
    return langs

def getSpokenLanguagesTV(tmdb_id):
    m = tv.details(tmdb_id)
    langs = []
    for i in range(len(m.spoken_languages)):
        languages = dict(m.spoken_languages[i])
        info = {}
        info['english_name'] = languages['english_name']
        info['name'] = languages['name']
        langs.append(info)
    return langs

def getCasts(tmdb_id):
    m = movie.details(tmdb_id)
    castData = []
    for i in range(len(m.casts['cast'])):
        casts = {}
        # print(m.casts['cast'])
        # input()
        ytt = dict(m.casts['cast'][i])
        casts['actor_id'] = ytt['id']
        casts['adult'] = ytt['adult']
        casts['gender_id'] = ytt['gender']
        casts['cast_id'] = ytt['id']
        casts['known_for_department'] = ytt['known_for_department']
        casts['original_name'] = ytt['original_name']
        casts['popularity'] = ytt['popularity']
        if ytt['profile_path'] == None:
            pass
        else:
            casts['profile_path_hd'] = tmdbImgSourceHD+ytt['profile_path']
            casts['profile_path_sd'] = tmdbImgSourceSD+ytt['profile_path']
            casts['profile_path_small'] = tmdbImgSourceSmall+ytt['profile_path']
        casts['cast_id'] = ytt['cast_id']
        casts['character_role'] = ytt['character']
        casts['credit_id'] = ytt['credit_id']
        casts['order'] = ytt['order']
        castData.append(casts)
    return castData

def getCastsTV(tmdb_id):
    m = tv.details(tmdb_id)
    castData = []
    for i in range(len(m.credits['cast'])):
        casts = {}
        ytt = dict(m.credits['cast'][i])
        casts['actor_id'] = ytt['id']
        casts['adult'] = ytt['adult']
        casts['gender_id'] = ytt['gender']
        casts['cast_id'] = ytt['id']
        casts['known_for_department'] = ytt['known_for_department']
        casts['original_name'] = ytt['original_name']
        casts['popularity'] = ytt['popularity']
        if ytt['profile_path'] == None:
            pass
        else:
            casts['profile_path_hd'] = tmdbImgSourceHD+ytt['profile_path']
            casts['profile_path_sd'] = tmdbImgSourceSD+ytt['profile_path']
            casts['profile_path_small'] = tmdbImgSourceSmall+ytt['profile_path']
        casts['character_role'] = ytt['character']
        casts['credit_id'] = ytt['credit_id']
        casts['order'] = ytt['order']
        castData.append(casts)
    return castData

def getCrewTV(tmdb_id):
    m = tv.details(tmdb_id)
    crewData = []
    for i in range(len(m.credits['crew'])):
        crew = {}
        ytt = dict(m.credits['crew'][i])
        crew['adult'] = ytt['adult']
        crew['gender_id'] = ytt['gender']
        crew['cast_id'] = ytt['id']
        crew['name'] = ytt['name']
        crew['known_for_department'] = ytt['known_for_department']
        crew['original_name'] = ytt['original_name']
        crew['popularity'] = ytt['popularity']
        if ytt['profile_path'] == None:
            pass
        else:
            crew['profile_path_hd'] = tmdbImgSourceHD+ytt['profile_path']
            crew['profile_path_sd'] = tmdbImgSourceSD+ytt['profile_path']
            crew['profile_path_small'] = tmdbImgSourceSmall+ytt['profile_path']
        crew['credit_id'] = ytt['credit_id']
        crew['department'] = ytt['department']
        crew['job'] = ytt['job']
        crewData.append(crew)
    return crewData

def getCompanyMovies(id):
    movies = company.movies(id)
    data = []
    for movie in movies:
        info = {}
        info['movie_id'] = movie.id
        info['movie_title'] = movie.title
        info['movie_overview'] = movie.overview
        if movie.poster_path:
            info['movie_poster_hd'] = tmdbImgSourceHD+str(movie.poster_path)
            info['movie_poster_sd'] = tmdbImgSourceSD+str(movie.poster_path)
            info['movie_poster_small'] = tmdbImgSourceSmall+str(movie.poster_path)
        else:
            pass
        data.append(info)
    return data

def similarMoviesHandler(tmdb_id):
    similar = movie.similar(tmdb_id)
    data = []
    for result in similar:
        info = {}
        info['name'] = result.title
        info['id'] = result.id
        info['overview'] = result.overview
        if result.poster_path and result.poster_path != None:
            info['poster_hd'] = tmdbImgSourceHD+str(result.poster_path)
            info['poster_sd'] = tmdbImgSourceSD+str(result.poster_path)
            info['poster_small'] = tmdbImgSourceSmall+str(result.poster_path)
        else:
            pass
        data.append(info)
    return data

def similarTVHandler(tmdb_id):
    similar = tv.similar(tmdb_id)
    data = []
    for result in similar:
        info = {}
        info['id'] = result.id
        info['name'] = result.name
        info['overview'] = result.overview
        if result.poster_path and result.poster_path != None:
            info['poster_hd'] = tmdbImgSourceHD+str(result.poster_path)
            info['poster_sd'] = tmdbImgSourceSD+str(result.poster_path)
            info['poster_small'] = tmdbImgSourceSmall+str(result.poster_path)
        else:
            pass
        info['type'] = "tv"
        data.append(info)
    return data

def TVSeasonHandler(tmdb_id):
    m = tv.details(tmdb_id)
    seasonData = []
    for i in m.seasons:
        infoSeason = {}
        infoSeason['id'] = i.id
        infoSeason['name'] = i.name
        infoSeason['overview'] = i.overview
        infoSeason['air_date'] = i.air_date
        infoSeason['episode_count'] = i.episode_count
        infoSeason['season_number'] = i.season_number
        seasonData.append(infoSeason)
    return seasonData

@api_view(['GET'])
def apiMoviesHome(request):
    movies = discover.discover_movies({"sort_by": "popularity.desc"})
    data = []
    for p in movies:
        info = {}
        info['movie_id'] = p.id
        info['movie_name'] = p.title
        info['movie_overview'] = p.overview
        if p.poster_path and p.poster_path != None:
            info['poster_hd'] = tmdbImgSourceHD+str(p.poster_path)
            info['poster_sd'] = tmdbImgSourceSD+str(p.poster_path)
            info['poster_small'] = tmdbImgSourceSmall+str(p.poster_path)
        else:
            pass
        if p.backdrop_path and p.backdrop_path != None:
            info['backdrop_fhd'] = tmdbBackdropSourceFHD+str(p.backdrop_path)
            info['backdrop_hd'] = tmdbBackdropSourceFHD+str(p.backdrop_path)
            info['backdrop_sd'] = tmdbBackdropSourceFHD+str(p.backdrop_path)
        else:
            pass
        data.append(info)
    return Response(data)

@api_view(['GET'])
def apiMoviesTopRated(request):
    m = movie.top_rated()
    data = []
    for i in m:
        mv = {}
        mv['id'] = i['id']
        mv['adult'] = i['adult']
        mv['name'] = i['title']
        mv['original_title'] = i['original_title']
        mv['orginal_language'] = i['original_language']
        mv['overview'] = i['overview']
        mv['popularity'] = i['popularity']
        mv['release_date'] = i['release_date']
        if i['backdrop_path'] == None:
            pass
        elif i['backdrop_path']:
            mv['backdrop_fhd'] = tmdbBackdropSourceFHD+i.backdrop_path
            mv['backdrop_hd'] = tmdbBackdropSourceHD+i.backdrop_path
            mv['backdrop_sd'] = tmdbBackdropSourceSD+i.backdrop_path
        else:
            pass

        if i['poster_path'] == None:
            pass
        elif i['poster_path']:
            mv['poster_fhd'] = tmdbBackdropSourceFHD+i.poster_path
            mv['poster_hd'] = tmdbBackdropSourceHD+i.poster_path
            mv['poster_sd'] = tmdbBackdropSourceSD+i.poster_path
        else:
            pass
        if i['genre_ids']:
            mv['genre_id'] = i['genre_ids']
        else:
            pass
        data.append(mv)
    return Response(data)

@api_view(['GET'])
def apiMoviesUpcoming(request):
    m = movie.upcoming()
    data = []
    for i in m:
        mv = {}
        mv['id'] = i['id']
        mv['adult'] = i['adult']
        mv['name'] = i['title']
        mv['original_title'] = i['original_title']
        mv['orginal_language'] = i['original_language']
        mv['overview'] = i['overview']
        mv['popularity'] = i['popularity']
        mv['release_date'] = i['release_date']
        if i['backdrop_path'] == None:
            pass
        elif i['backdrop_path']:
            mv['backdrop_fhd'] = tmdbBackdropSourceFHD+i.backdrop_path
            mv['backdrop_hd'] = tmdbBackdropSourceHD+i.backdrop_path
            mv['backdrop_sd'] = tmdbBackdropSourceSD+i.backdrop_path
        else:
            pass

        if i['poster_path'] == None:
            pass
        elif i['poster_path']:
            mv['poster_fhd'] = tmdbBackdropSourceFHD+i.poster_path
            mv['poster_hd'] = tmdbBackdropSourceHD+i.poster_path
            mv['poster_sd'] = tmdbBackdropSourceSD+i.poster_path
        else:
            pass
        if i['genre_ids']:
            mv['genre_id'] = i['genre_ids']
        else:
            pass
        data.append(mv)
    return Response(data)

@api_view(['GET'])
def apiMoviesPopular(request):
    data = []
    for i in popular:
        info = {}
        info['tmdb_id'] = i.id
        info['name'] = i.title
        info['description'] = i.overview
        if i.poster_path == None:
            pass
        elif i.poster_path:
            info['poster_hd'] = tmdbImgSourceHD+i.poster_path
            info['poster_sd'] = tmdbImgSourceSD+i.poster_path
            info['poster_small'] = tmdbImgSourceSmall+i.poster_path
        else:
            pass
        info['adult'] = i.adult
        if i.backdrop_path == None:
            pass
        elif i.backdrop_path:
            info['backdrop_fhd'] = tmdbBackdropSourceFHD+i.backdrop_path
            info['backdrop_hd'] = tmdbBackdropSourceHD+i.backdrop_path
            info['backdrop_sd'] = tmdbBackdropSourceSD+i.backdrop_path
        else:
            pass
        info['original_language'] = i.original_language
        info['original_title'] = i.original_title
        info['release_date'] = i.release_date
        info['average_vote'] = i.vote_average
        info['popularity'] = i.popularity
        data.append(info)
    # print(popular)
    print(request.method)
    return Response(data)

@api_view(['GET'])
def searchMoviesTitle(request, query):
    search = movie.search(query)
    data = []
    for res in search:
        info = {}
        info['id'] = res.id
        info['movie_name'] = res.title
        info['overview'] = res.overview
        if res.poster_path and res.poster_path != None:
            info['poster_hd'] = tmdbImgSourceHD+str(res.poster_path)
            info['poster_sd'] = tmdbImgSourceSD+str(res.poster_path)
            info['poster_small'] = tmdbImgSourceSmall+str(res.poster_path)
        else:
            pass
        info['average_vote'] = res.vote_average
        data.append(info)
    return Response(data)

@api_view(['GET'])
def searchPage(request, query):
    results = search.multi({"query": query, "page": 1})
    data = []
    for result in results:
        info = {}
        pprint.pprint(result)
        if result.media_type == "tv":
            if result.name and result.name != None:
                info['id'] = result.id
                info['name'] = result.name
                info['original_name'] = result.original_name
                info['release_date'] = result.first_air_date                
                info['media_type'] = result.media_type
        elif result.media_type == "movie":
            if result.title and result.title != None:
                info['id'] = result.id
                info['name'] = result.title
                info['original_name'] = result.original_title
                info['release_date'] = result.release_date                
                info['media_type'] = result.media_type
        else:
            pass
        if result.media_type == "tv" or result.media_type == "movie":
            if result.poster_path and result.poster_path != None:
                info['poster_hd'] = tmdbImgSourceHD+result.poster_path
                info['poster_sd'] = tmdbImgSourceSD+result.poster_path
                info['poster_small'] = tmdbImgSourceSmall+result.poster_path
            else:
                pass
            if result.original_language and result.original_language != None:
                info['original_language'] = result.original_language
            else:
                pass
        data.append(info)
    return Response(data)

@api_view(['GET'])
def searchMultiPage(request, query, num):
    search = Search()
    results = search.multi({"query": query, "page": num})
    data = []
    for result in results:
        info = {}
        pprint.pprint(result)
        if result.media_type == "tv":
            if result.name and result.name != None:
                info['id'] = result.id
                info['name'] = result.name
                info['original_name'] = result.original_name
                info['release_date'] = result.first_air_date                
                info['media_type'] = result.media_type
        elif result.media_type == "movie":
            if result.title and result.title != None:
                info['id'] = result.id
                info['name'] = result.title
                info['original_name'] = result.original_title
                info['release_date'] = result.release_date                
                info['media_type'] = result.media_type
        else:
            pass
        if result.media_type == "tv" or result.media_type == "movie":
            if result.poster_path and result.poster_path != None:
                info['poster_hd'] = tmdbImgSourceHD+result.poster_path
                info['poster_sd'] = tmdbImgSourceSD+result.poster_path
                info['poster_small'] = tmdbImgSourceSmall+result.poster_path
            else:
                pass
            if result.original_language and result.original_language != None:
                info['original_language'] = result.original_language
            else:
                pass
        data.append(info)
    return Response(data)

@api_view(['GET'])
def apiTVHome(request):
    tvShows = discover.discover_tv_shows({"sort_by": "popularity.desc"})
    data = []
    for p in tvShows:
        info = {}
        info['movie_id'] = p.id
        info['movie_name'] = p.name
        info['movie_overview'] = p.overview
        info['media_type'] = "tv"
        if p.poster_path and p.poster_path != None:
            info['poster_hd'] = tmdbImgSourceHD+str(p.poster_path)
            info['poster_sd'] = tmdbImgSourceSD+str(p.poster_path)
            info['poster_small'] = tmdbImgSourceSmall+str(p.poster_path)
        else:
            pass
        if p.backdrop_path and p.backdrop_path != None:
            info['backdrop_fhd'] = tmdbBackdropSourceFHD+str(p.backdrop_path)
            info['backdrop_hd'] = tmdbBackdropSourceFHD+str(p.backdrop_path)
            info['backdrop_sd'] = tmdbBackdropSourceFHD+str(p.backdrop_path)
        else:
            pass
        data.append(info)
    return Response(data)

@api_view(['GET'])
def apiTVPopular(request):
    data = []
    for i in popularTv:
        info = {}
        info['tmdb_id'] = i.id
        info['name'] = i.name
        info['description'] = i.overview
        info['media_type'] = "tv"
        if i.poster_path == None:
            pass
        elif i.poster_path:
            info['poster_hd'] = tmdbImgSourceHD+i.poster_path
            info['poster_sd'] = tmdbImgSourceSD+i.poster_path
            info['poster_small'] = tmdbImgSourceSmall+i.poster_path
        else:
            pass
        if i.backdrop_path == None:
            pass
        elif i.backdrop_path:
            info['backdrop_fhd'] = tmdbBackdropSourceFHD+i.backdrop_path
            info['backdrop_hd'] = tmdbBackdropSourceHD+i.backdrop_path
            info['backdrop_sd'] = tmdbBackdropSourceSD+i.backdrop_path
        else:
            pass
        info['original_language'] = i.original_language
        info['original_title'] = i.original_name
        info['release_date'] = i.first_air_date
        info['average_vote'] = i.vote_average
        info['popularity'] = i.popularity
        data.append(info)
    # print(popular)
    print(request.method)
    return Response(data)

@api_view(['GET'])
def FetchMovieID(request,tmdbid):
    try:
        m = movie.details(tmdbid)
        data = []
        info = {}
        info['tmdb_id'] = m.id
        info['name'] = m.title
        info['description'] = m.overview
        if m.poster_path == None:
            pass
        elif m.poster_path:
            info['poster_hd'] = tmdbImgSourceHD+m.poster_path
            info['poster_sd'] = tmdbImgSourceSD+m.poster_path
            info['poster_small'] = tmdbImgSourceSmall+m.poster_path
        else:
            pass

        info['popularity'] = m.popularity
        info['adult'] = m.adult
        if m.backdrop_path == None:
            pass
        elif m.backdrop_path:
            info['backdrop_fhd'] = tmdbBackdropSourceFHD+m.backdrop_path
            info['backdrop_hd'] = tmdbBackdropSourceHD+m.backdrop_path
            info['backdrop_sd'] = tmdbBackdropSourceSD+m.backdrop_path
        else:
            pass

        info['budget'] = m.budget
        info['imdb_id'] = m.imdb_id
        info['original_language'] = m.original_language
        info['original_title'] = m.original_title
        info['release_date'] = m.release_date
        info['revenue'] = m.revenue
        info['runtime'] = m.runtime
        info['status'] = m.status
        info['tagline'] = m.tagline
        info['average_vote'] = m.vote_average
        info['total_voters'] = m.vote_count
        if m.genres:
            gg = dict(m.genres[0])
            info['genre_id'] = gg['id']
            info['genre_name'] = gg['name']
        else:
            pass
        info['type'] = "movie"
        info['production_comapanies'] = getProductionsCompanies(m.id)
        info['production_countries'] = getProductionCountries(m.id)
        info['spoken_languages'] = getSpokenLanguages(m.id)
        info['casts'] = getCasts(m.id)
        trailersData = []
        for i in range(len(m.trailers['youtube'])):
            trailers = {}
            ytt = dict(m.trailers['youtube'][i])
            trailers['trailer_name'] = ytt['name']
            trailers['source'] = ytWatch+ytt['source']
            trailers['quaility'] = ytt['size']
            trailers['type'] = ytt['type']
            trailersData.append(trailers)
        info['trailers'] = trailersData
        info['recommended_movies'] = movieRecommendations(m.id)
        info['similar_movies'] = similarMoviesHandler(m.id)
        data.append(info)
        return Response(data)
    except Exception as e:
        if str(e) == "The resource you requested could not be found.":
            error={}
            error['msg'] = "Requested Media Not Found"
            error['code'] = 404
            return Response(error)
        else:
            return Response(str(e))

@api_view(['GET'])
def getCompany(request,id):
    details = company.details(id)
    data = []
    detailsComp = {}
    if details.id:
        detailsComp['id'] = details.id
    else:
        pass
    if details.name:
        detailsComp['name'] = details.name
    else:
        pass
    if details.description:
        detailsComp['description'] = details.description
    else:
        pass
    if details.homepage:
        detailsComp['homepage'] = details.homepage
    else:
        pass
    if details.logo_path:
        detailsComp['logo'] = details.logo_path
    else:
        pass
    if details.headquarters:
        detailsComp['headquarters'] = details.headquarters
    else:
        pass
    if details.origin_country:
        detailsComp['origin_country'] = details.origin_country
    else:
        pass
    if details.parent_company:
        detailsComp['parent_company'] = details.parent_company
    else:
        pass
    detailsComp['company_movies'] = getCompanyMovies(details.id)
    data.append(detailsComp)

    return Response(data)

@api_view(['GET'])
def getGenre(request):
    tvGenres = genre.tv_list()
    movieGenres = genre.movie_list()
    data = []
    for mv in movieGenres:
        info = {}
        info['genre_id'] = mv.id
        info['genre_name'] = mv.name
        info['genre_type'] = "movies"
        data.append(info)
    for tv in tvGenres:
        info2 = {}
        info2['genre_id'] = tv.id
        info2['genre_name'] = tv.name
        info2['genre_type'] = "tv"
        data.append(info2)
    return Response(data)

@api_view(['GET'])
def moviesInTheater(request):
    m = movie.now_playing()
    data = []
    for i in m:
        mv = {}
        mv['id'] = i['id']
        mv['adult'] = i['adult']
        mv['name'] = i['title']
        mv['original_title'] = i['original_title']
        mv['orginal_language'] = i['original_language']
        mv['overview'] = i['overview']
        mv['popularity'] = i['popularity']
        mv['release_date'] = i['release_date']
        if i['backdrop_path'] == None:
            pass
        elif i['backdrop_path']:
            mv['backdrop_fhd'] = tmdbBackdropSourceFHD+i.backdrop_path
            mv['backdrop_hd'] = tmdbBackdropSourceHD+i.backdrop_path
            mv['backdrop_sd'] = tmdbBackdropSourceSD+i.backdrop_path
        else:
            pass

        if i['poster_path'] == None:
            pass
        elif i['poster_path']:
            mv['poster_fhd'] = tmdbBackdropSourceFHD+i.poster_path
            mv['poster_hd'] = tmdbBackdropSourceHD+i.poster_path
            mv['poster_sd'] = tmdbBackdropSourceSD+i.poster_path
        else:
            pass
        if i['genre_ids']:
            mv['genre_id'] = i['genre_ids']
        else:
            pass
        data.append(mv)
    return Response(data)

@api_view(['GET'])
def tvOngoing(request):
    t = tv.on_the_air()
    data = []
    for i in t:
        mv = {}
        mv['id'] = i['id']
        mv['name'] = i['name']
        mv['original_title'] = i['original_name']
        mv['orginal_language'] = i['original_language']
        mv['origin_country'] = i['origin_country']
        mv['overview'] = i['overview']
        mv['popularity'] = i['popularity']
        mv['release_date'] = i['first_air_date']
        if i['backdrop_path'] == None:
            pass
        elif i['backdrop_path']:
            mv['backdrop_fhd'] = tmdbBackdropSourceFHD+i.backdrop_path
            mv['backdrop_hd'] = tmdbBackdropSourceHD+i.backdrop_path
            mv['backdrop_sd'] = tmdbBackdropSourceSD+i.backdrop_path
        else:
            pass

        if i['poster_path'] == None:
            pass
        elif i['poster_path']:
            mv['poster_fhd'] = tmdbBackdropSourceFHD+i.poster_path
            mv['poster_hd'] = tmdbBackdropSourceHD+i.poster_path
            mv['poster_sd'] = tmdbBackdropSourceSD+i.poster_path
        else:
            pass
        if i['genre_ids']:
            mv['genre_id'] = i['genre_ids']
        else:
            pass
        data.append(mv)
    return Response(data)

@api_view(['GET'])
def apiTvToprated(request):
    t = tv.top_rated()
    data = []
    for i in t:
        mv = {}
        mv['id'] = i['id']
        mv['name'] = i['name']
        mv['original_title'] = i['original_name']
        mv['orginal_language'] = i['original_language']
        mv['origin_country'] = i['origin_country']
        mv['overview'] = i['overview']
        mv['popularity'] = i['popularity']
        mv['release_date'] = i['first_air_date']
        mv['average_votes'] = i['vote_average']
        mv['total_votes'] = i['vote_count']

        if i['backdrop_path'] == None:
            pass
        elif i['backdrop_path']:
            mv['backdrop_fhd'] = tmdbBackdropSourceFHD+i.backdrop_path
            mv['backdrop_hd'] = tmdbBackdropSourceHD+i.backdrop_path
            mv['backdrop_sd'] = tmdbBackdropSourceSD+i.backdrop_path
        else:
            pass

        if i['poster_path'] == None:
            pass
        elif i['poster_path']:
            mv['poster_fhd'] = tmdbBackdropSourceFHD+i.poster_path
            mv['poster_hd'] = tmdbBackdropSourceHD+i.poster_path
            mv['poster_sd'] = tmdbBackdropSourceSD+i.poster_path
        else:
            pass
        if i['genre_ids']:
            mv['genre_id'] = i['genre_ids']
        else:
            pass
        data.append(mv)
    return Response(data)


@api_view(['GET'])
def FetchTvID(request, tmdbid):
    try:
        m = tv.details(tmdbid)
        data = []
        info = {}
        info['tmdb_id'] = m.id
        info['name'] = m.name
        info['description'] = m.overview
        if m.poster_path == None:
            pass
        elif m.poster_path:
            info['poster_hd'] = tmdbImgSourceHD+m.poster_path
            info['poster_sd'] = tmdbImgSourceSD+m.poster_path
            info['poster_small'] = tmdbImgSourceSmall+m.poster_path
        else:
            pass

        info['popularity'] = m.popularity
        info['adult'] = m.adult
        if m.backdrop_path == None:
            pass
        elif m.backdrop_path:
            info['backdrop_fhd'] = tmdbBackdropSourceFHD+m.backdrop_path
            info['backdrop_hd'] = tmdbBackdropSourceHD+m.backdrop_path
            info['backdrop_sd'] = tmdbBackdropSourceSD+m.backdrop_path
        else:
            pass

        info['original_language'] = m.original_language
        info['original_title'] = m.original_name
        info['release_date'] = m.first_air_date
        info['episode_run_time'] = m.episode_run_time
        info['status'] = m.status
        info['tagline'] = m.tagline
        info['tv_type'] = m.type
        info['average_vote'] = m.vote_average
        info['total_voters'] = m.vote_count
        if m.genres:
            gg = dict(m.genres[0])
            info['genre_id'] = gg['id']
            info['genre_name'] = gg['name']
        else:
            pass
        info['type'] = "tv"
        info['in_production'] = m.in_production
        info['homepage'] = m.homepage
        info['production_comapanies'] = getProductionsCompaniesTV(m.id)
        info['production_countries'] = getProductionCountriesTV(m.id)
        info['spoken_languages'] = getSpokenLanguagesTV(m.id)
        info['casts'] = getCastsTV(m.id)
        info['crew'] = getCrewTV(m.id)
        trailersData = []
        for i in range(len(m.videos['results'])):
            trailers = {}
            ytt = dict(m.videos['results'][i])
            if ytt['site'] == "YouTube":
                trailers['trailer_name'] = ytt['name']
                trailers['host'] = ytt['site']
                trailers['url'] = ytWatch+ytt['key']
                trailers['quaility'] = ytt['size']
                trailers['type'] = ytt['type']
                trailersData.append(trailers)
                info['videos'] = trailersData
            else:
                pass
        info['seasons'] = TVSeasonHandler(m.id)
        info['recommended_tv'] = TVRecommendations(m.id)
        info['similar_tv'] = similarTVHandler(m.id)
        data.append(info)
        return Response(data)
    except Exception as e:
        if str(e) == "The resource you requested could not be found.":
            error={}
            error['msg'] = "Requested Media Not Found"
            error['code'] = 404
            return Response(error)
        else:
            return Response(str(e))

@api_view(['GET'])
def FetchSeason(request, tmdbid, seasonnumb):
    m = season.details(tmdbid, seasonnumb)
    data = []
    teps = {}
    teps['total_episodes'] = len(m['episodes'])
    data.append(teps)
    for i in m['episodes']:
        infoep = {}
        infoep['name'] = i['name']
        infoep['id'] = i['id']
        infoep['episode_number'] = i['episode_number']
        infoep['overview'] = i['overview']
        infoep['runtime'] = i['runtime']
        infoep['corrosponding_season_number'] = i['season_number']
        infoep['corrosponding_season_id'] = i['show_id']
        infoep['average_vote'] = i['vote_average']
        infoep['vote_count'] = i['vote_count']
        if i['still_path'] and i['still_path'] != None:
            infoep['poster_hd'] = tmdbImgSourceHD+str(i['still_path'])
            infoep['poster_sd'] = tmdbImgSourceSD+str(i['still_path'])
            infoep['poster_small'] = tmdbImgSourceSmall+str(i['still_path'])
        else:
            pass
        infoep['crew'] = i['crew']
        infoep['guest_stars'] = i['guest_stars']
        # infoep['m'] = m
        data.append(infoep)
    return Response(data)

@api_view(['GET'])
def FetchEpisode(request, tmdbid, seasonnumb, ep):
    m = season.details(tmdbid, seasonnumb)
    data = []
    for i in m['episodes']:
        infoep = {}
        if i['episode_number'] == ep:
            infoep['name'] = i['name']
            infoep['id'] = i['id']
            infoep['episode_number'] = i['episode_number']
            epNumb = i['episode_number']
            infoep['overview'] = i['overview']
            infoep['runtime'] = i['runtime']
            infoep['corrosponding_season_number'] = i['season_number']
            infoep['corrosponding_season_id'] = i['show_id']
            infoep['average_vote'] = i['vote_average']
            infoep['vote_count'] = i['vote_count']
            if i['still_path'] and i['still_path'] != None:
                infoep['poster_hd'] = tmdbImgSourceHD+str(i['still_path'])
                infoep['poster_sd'] = tmdbImgSourceSD+str(i['still_path'])
                infoep['poster_small'] = tmdbImgSourceSmall+str(i['still_path'])
            else:
                pass
            data.append(infoep)
        else:
            pass        
    return Response(data)

@api_view(['GET'])
def FetchTvVideos(request, tmdbid, seasonnumb):
    m = season.videos(tmdbid, seasonnumb)
    return Response(m)

@api_view(['GET'])
def FetchTvImages(request, tmdbid, seasonnumb):
    m = season.images(tmdbid, seasonnumb)
    return Response(m)

@api_view(['GET'])
def FetchPerson(request, personid):
    p = person.details(personid)
    pp = {}
    pp['id'] = p['id']
    pp['name'] = p['name']
    pp['biography'] = p['biography']
    pp['birthday'] = p['birthday']
    pp['deathday'] = str(p['deathday'])
    pp['also_known_as'] = p['also_known_as']
    pp['gender'] = p['gender']
    pp['homepage'] = str(p['homepage'])
    pp['imdb_id'] = p['imdb_id']
    pp['known_for'] = p['known_for_department']
    pp['birthplace'] = p['place_of_birth']
    pp['popularity'] = p['popularity']
    if p['profile_path'] and p['profile_path'] != None:
        pp['profile_hd'] = tmdbImgSourceHD+str(p['profile_path'])
        pp['profile_sd'] = tmdbImgSourceSD+str(p['profile_path'])
        pp['profile_small'] = tmdbImgSourceSmall+str(p['profile_path'])
    else:
        pass
    profileData = []
    for i in range(len(p.images['profiles'])):
            prof = {}
            imgs = dict(p.images['profiles'][i])
            prof['profile_path_hd'] = tmdbImgSourceHD+str(imgs['file_path'])
            prof['profile_path_sd'] = tmdbImgSourceSD+str(imgs['file_path'])
            prof['profile_path_small'] = tmdbImgSourceSmall+str(imgs['file_path'])
            prof['height'] = imgs['height']
            prof['width'] = imgs['width']
            profileData.append(prof)
    pp['profiles'] = profileData
    return Response(pp)


