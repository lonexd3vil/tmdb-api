# tmdb-api
<p align="center"><img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/version-1.0.0-blue" /></p>

<p>This is a Django + Django Rest Framework based backend built upon the tmdb-api.</p>

# urls endpoints
<p>Although url endpoints and setup in <code>api/urls.py</code>but here is a quick run down and explanation for each endpoint</p>

<p><code>' '</code>home url, which is basically of no use</p>
<p><code>/api/movies/</code>will load movies based on popularity in decending order</p>
<p><code>/api/movies/popular/</code>will load popular movies at that time</p>
<p><code>/api/movies/theaters/</code>will load movies that are currently playing on theaters</p>
<p><code>/api/movies/toprated/</code>will load movies that are top-rated at that time</p>
<p><code>/api/movies/upcoming/</code>will load movies that are upcoming on theaters</p>
<p><code>/api/movies/tmdbid/</code>will load movie based with the corrosponding given id</p>
<p><code>/api/movies/search/query/</code>will search for movies based on the given query</p>
<p><code>/api/company/id/</code>will search for a production company based on the given id, you will get this id while u look for any movie or series, you will be provided with production company details. use that id here</p>
<p><code>/api/search/query/</code>will search for movies and series both based on the given query</p>
<p><code>/api/search/query/page/int/</code>will search for movies and series both based on the given query and based on given page number, thus allowing for a multi-page search</p>
<p><code>/api/genres/</code>this will get a list of genres available on tmdb along with genre id</p>
<p><code>/api/tv/</code>will load TV Shows based on popularity in an desending order</p>
<p><code>/api/tv/popular/</code>will load popular TV Shows</p>
<p><code>/api/tv/toprated/</code>will load Top-Rated TV Shows</p>
<p><code>/api/tv/ongoing/</code>will load On-Going TV Shows</p>
<p><code>/api/tv/tmdbid/</code>will load TV Show based on id</p>
<p><code>/api/tv/tmdbid/season/int</code>will load complete season based on the given TV show id</p>
<p><code>/api/tv/tmdbid/season/int/episode/int</code>will load the specified episode corrosponding to the season and the given TV show id</p>
<p><code>/api/tv/videos/tmdbid/season/int</code>will load all the videos available to the corrosponding tv show's season</p>
<p><code>/api/tv/images/tmdbid/season/int</code>will load all the images available to the corroponsindg tv show's season</p>
<p><code>/api/person/id</code>will load details regarding the given actor id</p>

# Requirments
<p>just run <code>pip install -r requirements.txt</code>and it will setup all the neccasary modules</p>