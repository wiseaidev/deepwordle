"""
| The following script implements all the necessary logic required for tweepy.

| This program and the accompanying materials are made available under the terms of the `MIT License`_.
| SPDX short identifier: MIT
| Contributors:
    Mahmoud Harmouch, mail_.
.. _MIT License: https://opensource.org/licenses/MIT
.. _mail: eng.mahmoudharmouch@gmail.com

"""

from attrs import (
    define,
    field,
)
import os
import tweepy
from typing import (
    Optional,
    TypeVar,
)

T = TypeVar("T", bound=tweepy.auth.OAuthHandler)
V = TypeVar("V", bound=type(tweepy.api))


@define
class Twitter:
    """Class that encapsulates twitter's api config."""

    _consumer_key: Optional[str] = field(default=os.environ.get("CONSUMER_KEY", ""))
    _consumer_secret: Optional[str] = field(
        default=os.environ.get("CONSUMER_SECRET", "")
    )
    _access_token: Optional[str] = field(default=os.environ.get("ACCESS_TOKEN", ""))
    _access_token_secret: Optional[str] = field(
        default=os.environ.get("ACCESS_TOKEN_SECRET", "")
    )
    _text: Optional[str] = field(default="automated tweet by deepwordle!")
    _auth: Optional[T] = field(default=None)
    _api: Optional[T] = field(default=None)

    @property
    def consumer_key(self) -> str:
        """
        A getter method that returns the value of the `consumer_key` attribute.
        :param self: Instance of the class.
        :return: A string that represents the value of the `consumer_key` attribute.
        """
        if not hasattr(self, "_consumer_key"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named consumer_key."
            )
        return self._consumer_key

    @consumer_key.setter
    def consumer_key(self, value: str) -> None:
        """
        A setter method that changes the value of the `consumer_key` attribute.
        :param value: A string that represents the value of the `consumer_key` attribute.
        :return: NoReturn.
        """
        setattr(self, "_consumer_key", value)

    @property
    def consumer_secret(self) -> str:
        """
        A getter method that returns the value of the `consumer_secret` attribute.
        :param self: Instance of the class.
        :return: A string that represents the value of the `consumer_secret` attribute.
        """
        if not hasattr(self, "_consumer_secret"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named consumer_secret."
            )
        return self._consumer_secret

    @consumer_secret.setter
    def consumer_secret(self, value: str) -> None:
        """
        A setter method that changes the value of the `consumer_secret` attribute.
        :param value: A string that represents the value of the `consumer_secret` attribute.
        :return: NoReturn.
        """
        setattr(self, "_consumer_secret", value)

    @property
    def access_token(self) -> str:
        """
        A getter method that returns the value of the `access_token` attribute.
        :param self: Instance of the class.
        :return: A string that represents the value of the `access_token` attribute.
        """
        if not hasattr(self, "_access_token"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named access_token."
            )
        return self._access_token

    @access_token.setter
    def access_token(self, value: str) -> None:
        """
        A setter method that changes the value of the `access_token` attribute.
        :param value: A string that represents the value of the `access_token` attribute.
        :return: NoReturn.
        """
        setattr(self, "_access_token", value)

    @property
    def access_token_secret(self) -> str:
        """
        A getter method that returns the value of the `access_token_secret` attribute.
        :param self: Instance of the class.
        :return: A string that represents the value of the `access_token_secret` attribute.
        """
        if not hasattr(self, "_access_token_secret"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named access_token_secret."
            )
        return self._access_token_secret

    @access_token_secret.setter
    def access_token_secret(self, value: str) -> None:
        """
        A setter method that changes the value of the `access_token_secret` attribute.
        :param value: A string that represents the value of the `access_token_secret` attribute.
        :return: NoReturn.
        """
        setattr(self, "_access_token_secret", value)

    @property
    def text(self) -> str:
        """
        A getter method that returns the value of the `text` attribute.
        :param self: Instance of the class.
        :return: A string that represents the value of the `text` attribute.
        """
        if not hasattr(self, "_text"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named text."
            )
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        """
        A setter method that changes the value of the `text` attribute.
        :param value: A string that represents the value of the `text` attribute.
        :return: NoReturn.
        """
        setattr(self, "_text", value)

    @property
    def auth(self) -> T:
        """
        A getter method that returns the value of the `auth` attribute.
        :param self: Instance of the class.
        :return: A tweepy OAuth Handler that represents the value of the `auth` attribute.
        """
        if not hasattr(self, "_auth"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named auth."
            )
        return self._auth

    @auth.setter
    def auth(self, value: T) -> None:
        """
        A setter method that changes the value of the `auth` attribute.
        :param value: A tweepy OAuth Handler that represents the value of the `auth` attribute.
        :return: NoReturn.
        """
        setattr(self, "_auth", value)

    @property
    def api(self) -> V:
        """
        A getter method that returns the value of the `api` attribute.
        :param self: Instance of the class.
        :return: A tweepy client api that represents the value of the `api` attribute.
        """
        if not hasattr(self, "_api"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named api."
            )
        return self._api

    @api.setter
    def api(self, value: V) -> None:
        """
        A setter method that changes the value of the `api` attribute.
        :param value: A tweepy client api that represents the value of the `api` attribute.
        :return: NoReturn.
        """
        setattr(self, "_api", value)

    def __attrs_post_init__(self):
        config = {
            "consumer_key": self.consumer_key,
            "consumer_secret": self.consumer_secret,
            "access_token": self.access_token,
            "access_token_secret": self.access_token_secret,
        }
        for key, value in config.items():
            assert len(value) > 0, f"Please provide a valid secret for: {key}"
        # Request User Authentication via the API.
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        # Create API object
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
        try:
            self.api.verify_credentials()
        except Exception as error:
            raise error

    def post_tweet(self):
        # Post a text based tweet
        self.api.update_status(self.text)
