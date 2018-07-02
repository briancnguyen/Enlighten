from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.urls import reverse
from .forms import *
from .models import *

class RegisterView(View):
    def get(self, request):
        user = UserCreateForm()
        profile = ProfileForm()
        return render(request, 'profiles/register.html', {'user': user, 'profile': profile})

    def post(self, request):
        user = UserCreateForm(request.POST or None)
        profile = ProfileForm(request.POST or None)
        if user.is_valid() and profile.is_valid():
            user.save()
            profile.instance.user = user.instance
            profile.save()
            if user is not None:
                login(request, user.instance)
                return HttpResponseRedirect(reverse('posts:post_list'))
            return HttpResponseRedirect(reverse('login'))
        return render(request, 'profiles/register.html', {'user': user, 'profile': profile})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        profile = get_object_or_404(Profile, pk=request.user.profile.pk)
        return render(request, 'profiles/profile_view.html', {'profile': profile})

class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        profile = get_object_or_404(Profile, pk=request.user.profile.pk)
        form = ProfileForm(instance=profile)
        return render(request, 'profiles/profile_update.html', {'form': form})

    def post(self, request):
        profile = get_object_or_404(Profile, pk=request.user.profile.pk)
        form = ProfileForm(request.POST or None, instance=profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profiles:profile_view'))
        return render(request, 'profiles/profile_update.html', {'form': form})

class EducationCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = EducationForm()
        return render(request, 'profiles/education_create.html', {'form': form})

    def post(self, request):
        form = EducationForm(request.POST or None)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('profiles:profile_view'))
        return render(request, 'profiles/education_create.html', {'form': form})

class EducationUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        education = get_object_or_404(Education, pk=pk)
        form = EducationForm(instance=education)
        return render(request, 'profiles/education_update.html', {'form': form})

    def post(self, request, pk):
        education = get_object_or_404(Education, pk=pk)
        form = EducationForm(request.POST or None, instance=education)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profiles:profile_view'))
        return render(request, 'profiles/education_update.html', {'form': form})


class EducationDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):        
        education = get_object_or_404(Education, pk=pk)
        return render(request, 'profiles/education_delete.html', {'education': education})

    def post(self, request, pk):
        education = get_object_or_404(Education, pk=pk)
        education.delete()
        return HttpResponseRedirect(reverse('profiles:profile_view'))


class ExperienceCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = ExperienceForm()
        return render(request, 'profiles/experience_create.html', {'form': form})

    def post(self, request):
        form = ExperienceForm(request.POST or None)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('profiles:profile_view'))
        return render(request, 'profiles/experience_create.html', {'form': form})

class ExperienceUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        experience = get_object_or_404(Experience, pk=pk)
        form = ExperienceForm(instance=experience)
        return render(request, 'profiles/experience_update.html', {'form': form})

    def post(self, request, pk):
        experience = get_object_or_404(Experience, pk=pk)
        form = ExperienceForm(request.POST or None, instance=experience)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profiles:profile_view'))
        return render(request, 'profiles/experience_update.html', {'form': form})


class ExperienceDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        experience = get_object_or_404(Experience, pk=pk)
        return render(request, 'profiles/experience_delete.html', {'experience': experience})

    def post(self, request, pk):
        experience = get_object_or_404(Experience, pk=pk)
        experience.delete()
        return HttpResponseRedirect(reverse('profiles:profile_view'))

class AwardCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = AwardForm()
        return render(request, 'profiles/award_create.html', {'form': form})

    def post(self, request):
        form = AwardForm(request.POST or None)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('profiles:profile_view'))
        return render(request, 'profiles/award_create.html', {'form': form})

class AwardUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        award = get_object_or_404(Award, pk=pk)
        form = AwardForm(instance=award)
        return render(request, 'profiles/award_update.html', {'form': form})

    def post(self, request, pk):
        award = get_object_or_404(Award, pk=pk)
        form = AwardForm(request.POST or None, instance=award)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profiles:profile_view'))
        return render(request, 'profiles/award_update.html', {'form': form})


class AwardDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        award = get_object_or_404(Award, pk=pk)
        return render(request, 'profiles/award_delete.html', {'award': award})

    def post(self, request, pk):
        award = get_object_or_404(Award, pk=pk)
        award.delete()
        return HttpResponseRedirect(reverse('profiles:profile_view'))