from django.shortcuts import render,get_object_or_404

from page.models import Page
FAKE_DB_CAROUSEL = [
    f"https://picsum.photos/id/{id}/1200/400" for id in range(24, 28)
]


def home_view(request):
    # print("request:::", request.META)
    # print("request:::", request.HEADERS)
    # context = {"platform": f"Django Platformu Kullanildi ve randint ile donen veri:{randint(1, 100)} "}
    context = dict(
        # FAKE_DB_PROJECTS=FAKE_DB_PROJECTS,
        FAKE_DB_CAROUSEL=FAKE_DB_CAROUSEL,
    )
    return render(request, "page/home_page.html", context)

def page_view(request, slug):
        page = get_object_or_404(Page,slug=slug)
        context = {"page":page}
        return render(request, "page/page_detail.html", context)