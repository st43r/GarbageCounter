from django.shortcuts import render
from .models import Video, CsvReport
from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm
from .forms import CsvForm

def home(request):
    latest_videos = Video.objects.all().order_by('-uploaded_at')[:2]
    csv_reports = CsvReport.objects.all().order_by('-uploaded_at')
    return render(request, 'home.html', {'latest_videos': latest_videos, 'csv_reports': csv_reports})

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})

def upload_csv(request):
    if request.method == 'POST':
        form = CsvForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # или любой другой URL, куда вы хотели бы перенаправить после успешной загрузки
    else:
        form = CsvForm()
    return render(request, 'upload_csv.html', {'form': form})

def analytics(request):
    reports = CsvReport.objects.all()
    data_for_charts = []

    for report in reports:
        with open(report.csv_file.path, 'r') as file:
            lines = file.readlines()
            data = {
                "title": report.title,
                "tree": int(lines[0].strip()),
                "glass": int(lines[1].strip()),
                "plastic": int(lines[2].strip()),
                "metal": int(lines[3].strip())
            }
        data_for_charts.append(data)

    return render(request, 'analytics.html', {"data_for_charts": data_for_charts})