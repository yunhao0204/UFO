# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from record_processor.parser.demostration_record import DemostrationRecord
from .basic import BasicPrompter
import json


class DemostrationPrompter(BasicPrompter):
    """
    The DemostrationPrompter class is the prompter for the user behavior record learning.
    """

    def __init__(self, is_visual: bool, prompt_template: str, example_prompt_template: str, api_prompt_template: str):
        """
        Initialize the BehaviorRecordPrompter.
        :param is_visual: Whether the request is for visual model.
        :param prompt_template: The path of the prompt template.
        :param example_prompt_template: The path of the example prompt template.
        :param api_prompt_template: The path of the api prompt template.
        """
        super().__init__(is_visual, prompt_template, example_prompt_template)
        self.api_prompt_template = self.load_prompt_template(api_prompt_template)


    def system_prompt_construction(self) -> str:
        """
        Construct the prompt for app selection.
        return: The prompt for app selection.
        """
        apis = self.api_prompt_helper(verbose = 1)
        examples = self.examples_prompt_helper()     

        return self.prompt_template["system"].format(apis=apis, examples=examples)
    

    def user_prompt_construction(self, user_request: str) -> str:
        """
        Construct the prompt for action selection.
        :param user_request: The user request.
        return: The prompt for action selection.
        """
        prompt = self.prompt_template["user"].format(user_request=user_request)
        
        return prompt
    


    def user_content_construction(self, demo_record: DemostrationRecord) -> list[dict]:
        """
        Construct the prompt for LLMs.
        :param log_partition: The log partition.
        :param user_request: The user request.
        return: The prompt for LLMs.
        """

        user_content = []
        
        # Get the total steps of the log partition.
        step_num = demo_record.step_num

        if self.is_visual:
            user_content.append({
            "type": "text",
            "text": "[Initial Application Screenshot]:"
            })
            user_content.append({
                "type": "image_url",
                "image_url": {
                    "url": demo_record["step_0"]["screenshot"]
                }
            })

        user_content.append({
            "type": "text",
            "text": "[Agent Trajectory]:"
            })
        
        for num in range(step_num):
            step = demo_record["step_{num}".format(num=num)]
            step_content = {
                "application": step["application"],
                "description": step["description"],
                "action": step["action"],
            }
            if step["comment"]:
                step_content["comment"] = step["comment"]

            user_content.append({
            "type": "text",
            "text": json.dumps(step_content)
            })
                
        # Add the user request.
        user_content.append({
            "type": "text",
            "text": self.user_prompt_construction(demo_record.get("request"))
        })

        return user_content
    
    
    def api_prompt_helper(self, verbose: int = 1) -> str:
        """
        Construct the prompt for APIs.
        :param apis: The APIs.
        :param verbose: The verbosity level.
        return: The prompt for APIs.
        """

        # Construct the prompt for APIs
        api_list = ["- The action type are limited to {actions}.".format(actions=list(self.api_prompt_template.keys()))]
        
        # Construct the prompt for each API
        for key in self.api_prompt_template.keys():
            api = self.api_prompt_template[key]
            if verbose > 0:
                api_text = "{summary}\n{usage}".format(summary=api["summary"], usage=api["usage"])
            else:
                api_text = api["summary"]
                
            api_list.append(api_text)

        api_prompt = self.retrived_documents_prompt_helper("", "", api_list)
            
        return api_prompt
    


    def examples_prompt_helper(self, header: str = "## Summarization Examples", separator: str = "Example") -> str:
        """
        Construct the prompt for examples.
        :param examples: The examples.
        :param header: The header of the prompt.
        :param separator: The separator of the prompt.
        return: The prompt for examples.
        """
        
        template = """
        [User Request]:
            {request}
        [Response]:
            {response}
        """
        example_list = []

        for key in self.example_prompt_template.keys():
            if key.startswith("example"):
                response = self.example_prompt_template[key].get("Response")
                response["Tips"] = self.example_prompt_template[key].get("Tips")
                example = template.format(request=self.example_prompt_template[key].get("Request"), response=response)
                example_list.append(example)

        return self.retrived_documents_prompt_helper(header, separator, example_list)