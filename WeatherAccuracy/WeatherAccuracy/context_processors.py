from datetime import datetime

def copyright(request):
    
    return {
            'COPYRIGHT_YEARS': '2014-%s' % datetime.now().year,
            }