"""
Copyright 2018-2020 Jakub Kuczys (https://github.com/jack1142)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


class AutoGistException(Exception):
    """Base exception class for AutoGist cog exception."""


class HandledHTTPError(AutoGistException):
    """
    Exception indicating that HTTP request didn't succeed.

    This doesn't contain any metadata
    as it's only meant to be indicator of failure.
    """