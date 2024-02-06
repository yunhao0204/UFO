<!-- <h1 align="center">
    UFO<img src="./assets/ufo.png" width="40px"/> :A <strong>U</strong>I-<strong>F</strong>ocused Multimodal Agent for Windows <strong>O</strong>S
</h1> -->

<!-- # **UFO** ![ufo](./assets/ufo_blue.png =x24): A **U**I-**F**ocused Agent for Windows **O**S Interaction -->


<h1 align="center">
    <b>UFO</b> <img src="./assets/ufo_blue.png" alt="UFO Image" width="36">: A <b>U</b>I-<b>F</b>ocused Agent for Windows <b>O</b>S Interaction
</h1>


<div align="center">

![Python Version](https://img.shields.io/badge/Python-3776AB?&logo=python&logoColor=white-blue&label=3.10%20%7C%203.11)&ensp;
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)&ensp;
![Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)

</div>

**UFO** is a **UI-Focused** dual-agent framework that seamlessly navigates and operates within individual applications and across them to fulfill user requests on **Windows OS**, even when spanning multiple applications.

<h1 align="center">
    <img src="./assets/overview.png"/> 
</h1>


## 🆕 News
- 📅 2024-02-30 UFO is released on GitHub🎈.


## 💥 Highlights

- [x] **First Windows Agent Framework** - UFO represents the first agent framework that can translate user request in natural language into grounded operation on Windows OS.
- [x] **Interactive Mode** - UFO allows for multiple sub-requests from users in the same session for completing complex task.
- [x] **Action Safeguard** - UFO supports safeguard to prompt for user confirmation when the action is sensitive.
- [x] **Easy Extension** - UFO is easy to extend to accomplish more complex tasks with different operations.


## ✨ Getting Started


### 🛠️ Step 1: Installation
UFO requires **Python >= 3.10** running on **Windows OS >= 10**. It can be installed by running the following command:
```bash
# [optional to create conda environment]
# conda create -n ufo python=3.10
# conda activate ufo

# clone the repository
git clone https://github.com/microsoft/UFO.git
cd UFO
# install the requirements
pip install -r requirements.txt
```

### 🖊️ Step 2: Configure the LLMs
Before running UFO, you need to provide your LLM configurations. Taking OpenAI as an example, you can configure `ufo/config/config.yaml` file as follows. 

#### OpenAI
```
OPENAI_API_BASE: Your OpenAI Endpoint # The base URL for the OpenAI API
OPENAI_API_KEY: Your OpenAI Key  # Set the value to sk-xxx if you host the openai interface for open llm model
OPENAI_API_MODEL: GPT Model Name  # The only OpenAI model by now that accepts visual input
```

### 🚩 Step 3: Start UFO

#### ⌨️ Command Line (CLI)

```bash
# assume you are in the cloned UFO folder
python -m ufo --task <your_task_name>
```

This will start the UFO process and you can interact with it through the command line interface. 
If everything goes well, you will see the following message:

```bash
Welcome to use UFO🛸, A UI-focused Multimodal Agent for Windows OS. 
 _   _  _____   ___
| | | ||  ___| / _ \
| | | || |_   | | | |
| |_| ||  _|  | |_| |
 \___/ |_|     \___/
Please enter your request to be completed🛸:
```
#### <**Reminder: Before inputing your request, please make sure the targeted applications are active on the system.**>


###  Step 4 🎥: Execution Logs 

You can find the screenshots taken and request and reponse logs in the following folder:
```
./ufo/logs/<your_task_name>/
```
You may use them to debug, replay, or analyze the agent output.


## ❓Get help 
* ❔GitHub Issues (prefered)
* For other communications, please contact ufo-agent@microsoft.com
---

## 🎬 Demo Examples

We present two demos videos that complete user request on Windows OS using UFO.

#### 1️⃣🗑️ Example 1: Deleting all notes on a PowerPoint presentation.
In this example, we will show you how to use UFO to deleting all notes on a PowerPoint presentation with just a few simple steps. Explore it to work smarter not harder!


https://github.com/microsoft/UFO/assets/11352048/cf60c643-04f7-4180-9a55-5fb240627834



#### 2️⃣📧 Example 2: Composing an email using text from multiple sources.
In this example, we will show you how to use UFO to extract texts from Word documents, description of an image, to compose an email and send. Enjoy your cross-application experiment with UFO!


https://github.com/microsoft/UFO/assets/11352048/aa41ad47-fae7-4334-8e0b-ba71c4fc32e0



## 📚 Citation
Our paper could be found [here](http://export.arxiv.org/abs/2311.17541). 
If you use UFO in your research, please cite our paper:
```
@article{ufo,
  title={UFO: A UI-Focused Agent for Windows OS Interaction},
  author={Chaoyun Zhang, Liqun Li, Shilin He, Xu Zhang,  Bo Qiao, Si Qin, Minghua Ma, Yu Kang, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Qi Zhang},
  journal={arXiv preprint arXiv:2311.17541},
  year={2024}
}
```


## Disclaimer
By choosing to run the provided code, you acknowledge and agree to the following terms and conditions regarding the functionality and data handling practices in [DISCLAIMER.md](./DISCLAIMER.md)


## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
