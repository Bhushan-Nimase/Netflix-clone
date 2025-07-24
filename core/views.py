from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Movie, Profile
from .forms import ProfileForm

# Home page
class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/profile/')
        return render(request, 'index.html')


# Show list of profiles for the user
@method_decorator(login_required, name='dispatch')
class ProfileList(View):
    def get(self, request):
        profiles = request.user.profiles.all()
        return render(request, 'profileList.html', {'profiles': profiles})


# Create a new profile
@method_decorator(login_required, name='dispatch')
class ProfileCreate(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, 'profileCreate.html', {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save()
            request.user.profiles.add(profile)
            return redirect(f'/watch/{profile.uuid}')
        return render(request, 'profileCreate.html', {'form': form})


# Movie list page for a specific profile
@method_decorator(login_required, name='dispatch')
class Watch(View):
    def get(self, request, profile_id):
        try:
            profile = Profile.objects.get(uuid=profile_id)
            if profile not in request.user.profiles.all():
                return redirect('core:profile_list')

            # Get all movies (removed age filtering)
            movies = Movie.objects.all()
            showcase = movies.first() if movies else None

            return render(request, 'movieList.html', {
                'movies': movies,
                'show_case': showcase
            })
        except Profile.DoesNotExist:
            return redirect('core:profile_list')


# Show single movie detail
@method_decorator(login_required, name='dispatch')
class ShowMovieDetail(View):
    def get(self, request, movie_id):
        try:
            movie = Movie.objects.get(uuid=movie_id)
            return render(request, 'movieDetail.html', {'movie': movie})
        except Movie.DoesNotExist:
            return redirect('core:profile_list')


# Show movie video(s)
@method_decorator(login_required, name='dispatch')
class ShowMovie(View):
    def get(self, request, movie_id):
        try:
            movie = Movie.objects.get(uuid=movie_id)
            video_data = movie.videos.values()
            return render(request, 'showMovie.html', {'movie': list(video_data)})
        except Movie.DoesNotExist:
            return redirect('core:profile_list')

