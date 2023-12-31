from django.urls import path

from . import views

app_name = "calendarapp"


urlpatterns = [
    path("calender/", views.CalendarViewNew.as_view(), name="calendar"),
    path("calenders/", views.CalendarView.as_view(), name="calendars"),
    path("event/new/", views.create_event, name="event_new"),
    path("event/edit/<int:pk>/", views.EventEdit.as_view(), name="event_edit"),
    path("event/<int:event_id>/details/", views.event_details, name="event-detail"),
    path(
        "add_eventmember/<int:event_id>", views.add_eventmember, name="add_eventmember"
    ),
    path("search", views.search, name="search"),
    path("searchTitle", views.searchTitle, name="searchTitle"),
    path("importExcel", views.importExcel, name="importExcel"),
    path(
        "event/<int:pk>/remove",
        views.EventDelete.as_view(),
        name="remove_event",
    ),
    path(
        "event_member/<int:pk>/remove",
        views.EventMemberDeleteView.as_view(),
        name="remove_event_member",
    ),
    path("all-event-list/", views.AllEventsListView.as_view(), name="all_events"),
    path(
        "running-event-list/",
        views.RunningEventsListView.as_view(),
        name="running_events",
    ),
    path(
        "completed-event-list/",
        views.CompletedEventsListView.as_view(),
        name="completed_events",
    ),
]
