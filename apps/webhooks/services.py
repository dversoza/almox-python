import hashlib
import hmac
import json

from django.conf import settings
from django.http import HttpRequest

from .exceptions import GithubWebhookValidationException


class GithubWebhookService:
    """Github webhook message handler."""

    def __init__(self, webhook: HttpRequest) -> None:
        self.webhook = self.__validate_webhook_signature(webhook)

    @staticmethod
    def __validate_webhook_signature(webhook: HttpRequest) -> HttpRequest:
        """
        Validate the signature of a WhatsApp webhook message.
        """
        if "X-Hub-Signature-256" not in webhook.headers:
            raise GithubWebhookValidationException("Missing X-Hub-Signature header")

        secret = settings.GITHUB_WEBHOOK_SECRET.encode("utf-8")
        digester = hmac.new(secret, webhook.body, hashlib.sha256)
        calculated_signature = digester.hexdigest()
        incoming_signature = webhook.headers["X-Hub-Signature-256"].split("=")[1]

        if not hmac.compare_digest(calculated_signature, incoming_signature):
            raise GithubWebhookValidationException("Invalid X-Hub-Signature")

        return webhook

    def handle_webhook(self) -> tuple[bool, str]:
        """
        Handle a WhatsApp webhook message.

        Args:
            webhook: The webhook request.

        Returns:
            A tuple containing a boolean indicating whether the webhook was handled successfully
            and a message.
        """
        event_type = self.__get_event_type()
        event_handler = self.__event_handler_factory(event_type)

        webhook_data = json.loads(self.webhook.body)

        return event_handler(webhook_data)

    def __get_event_type(self) -> str:
        """
        Get the event type from a webhook message.

        Returns:
            The event type.
        """
        try:
            return self.webhook.headers["X-GitHub-Event"]
        except KeyError:
            raise GithubWebhookValidationException("Missing X-GitHub-Event header")

    def __event_handler_factory(self, event_name: str) -> callable:
        """
        Create an event handler.

        Args:
            event_name: The event to be handled.

        Returns:
            A handler method.
        """
        try:
            return getattr(self, f"_{type(self).__name__}__handle_{event_name}")
        except AttributeError:
            raise KeyError(f"Unsupported event type: {event_name}")

    def __handle_ping(self, webhook_data: dict) -> tuple[bool, str]:
        """
        Handle a ping webhook message.

        Args:
            webhook_data: The webhook data.

        Returns:
            A tuple containing a boolean indicating whether the webhook was handled successfully
            and a message.
        """
        return True, "Pong!"

    def __handle_push(self, webhook_data: dict) -> tuple[bool, str]:
        """
        Handle a push webhook message.

        Args:
            webhook_data: The webhook data.

        Returns:
            A tuple containing a boolean indicating whether the webhook was handled successfully
            and a message.
        """
        if webhook_data["repository"]["name"] != "almox-python":
            return False, "Invalid webhook repository"

        commit_message = webhook_data["head_commit"]["message"]
        commit_pusher = webhook_data["pusher"]["name"]

        def deploy_app():
            """Deploy the app."""
            print("Deploying app...")
            print(f"For commit: {commit_message}\n\tpushed by: {commit_pusher}")

            import subprocess

            subprocess.run(["bash", "./rebuild.sh"])
            subprocess.run(["sudo", "bash", "./deploy.sh"])

            print("Done!")

        deploy_app()

        return True, f"Commit message: {commit_message}\nCommit pusher: {commit_pusher}"
