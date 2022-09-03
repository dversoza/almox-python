""" This module contains the view for the Github Webhook. """
from typing import Any

from django.http import HttpRequest, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from apps.webhooks.services import GithubWebhookService


@method_decorator(csrf_exempt, name="dispatch")
class GithubWebhookView(View):
    """This class is used to handle the webhooks from Github."""

    def post(self, request: HttpRequest) -> HttpResponse:
        """Handle a Github webhook message."""
        github_webhook_service = GithubWebhookService(webhook=request)

        success, message = github_webhook_service.handle_webhook()

        return HttpResponse(status=200 if success else 400, content=message)
