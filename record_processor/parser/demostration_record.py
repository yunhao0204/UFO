# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

class DemostrationStep:
    """
    Class for the single step information in the user demostration record.
    Multiple steps will be recorded to achieve a specific request.
    """

    def __init__(self, application: str, description: str, action: str, screenshot: str, comment: str):
        """
        Create a new step.
        """
        self.application = application
        self.description = description
        self.action = action
        self.comment = comment
        self.screenshot = screenshot


class DemostrationRecord:
    """
    Class for the user demostration record.
    A serise of steps user performed to achieve a specific request will be recorded in this class.
    """

    def __init__(self, applications: list, step_num: int, **steps: DemostrationStep):
        """
        Create a new Record.
        """
        self.request = ""
        self.round = 0
        self.applications = applications
        self.step_num = step_num
        for index, step in steps.items():
            setattr(self, index, step.__dict__)

    def set_request(self, request: str):
        """
        Set the request.
        """
        self.request = request
    
    def get_request(self) -> str:
        """
        Get the request.
        """
        return self.request
    
    def get_applications(self) -> list:
        """
        Get the application.
        """
        return self.applications
