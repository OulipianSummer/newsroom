from .models import Section
import datetime


# A simple context processor for inserting tags into the layout
def section_render(request):
    return {
        'allSections': Section.objects.all().order_by('name')
    }

# A timestamp based off of the current time
def current_time_render(request):
    return {
        'currentTime': datetime.datetime.now().strftime('%H:%M %p')
    }