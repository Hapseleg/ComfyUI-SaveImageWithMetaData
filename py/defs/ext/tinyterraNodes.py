# https://github.com/TinyTerra/ComfyUI_tinyterraNodes

from ..meta import MetaField
from ..formatters import calc_model_hash, calc_lora_hash, convert_skip_clip
import re


def stitch_together_positive_prompt(node_id, obj, prompt, extra_data, outputs, input_data):
    positive_prompt = ""
    if "prepend_positive" in input_data[0]:
        positive_prompt += input_data[0]["prepend_positive"][0]
    if "prepend_positive_g" in input_data[0]:
        positive_prompt += input_data[0]["prepend_positive_g"][0]
        
    positive_prompt += input_data[0]["positive"][0]
    
    return positive_prompt

def stitch_together_negative_prompt(node_id, obj, prompt, extra_data, outputs, input_data):
    negative_prompt = ""
    if "prepend_negative" in input_data[0]:
        negative_prompt += input_data[0]["prepend_negative"][0]
    if "prepend_negative_g" in input_data[0]:
        negative_prompt += input_data[0]["prepend_negative_g"][0]
        
    negative_prompt += input_data[0]["negative"][0]
    
    return negative_prompt


SAMPLERS = {
    "ttN KSampler_v2": { #tinyKSampler
        
    },
    "ttN pipeKSampler_v2": { #pipeKSampler

    },
    "ttN pipeKSamplerAdvanced_v2": { #pipeKSamplerAdvanced
        
    },
    "ttN pipeKSamplerSDXL_v2": { #pipeKSamplerSDXL
        
    },
}


CAPTURE_FIELD_LIST = {
    "ttN tinyLoader": { # tinyLoader
        MetaField.MODEL_NAME: {"field_name": "ckpt_name"},
        MetaField.MODEL_HASH: {"field_name": "ckpt_name", "format": calc_model_hash},
        MetaField.CLIP_SKIP: {"field_name": "clip_skip", "format": convert_skip_clip},
        MetaField.IMAGE_WIDTH: {"field_name": "empty_latent_width"},
        MetaField.IMAGE_HEIGHT: {"field_name": "empty_latent_height"},
    },
    "ttN pipeLoader_v2": { # pipeLoader
        MetaField.MODEL_NAME: {"field_name": "ckpt_name"},
        MetaField.MODEL_HASH: {"field_name": "ckpt_name", "format": calc_model_hash},
        MetaField.CLIP_SKIP: {"field_name": "clip_skip", "format": convert_skip_clip},
        MetaField.POSITIVE_PROMPT: {"selector": stitch_together_positive_prompt},
        MetaField.NEGATIVE_PROMPT: {"selector": stitch_together_negative_prompt},
        MetaField.IMAGE_WIDTH: {"field_name": "empty_latent_width"},
        MetaField.IMAGE_HEIGHT: {"field_name": "empty_latent_height"},
    },
    "ttN pipeLoaderSDXL_v2": { # pipeLoaderSDXL
        MetaField.MODEL_NAME: {"field_name": "ckpt_name"},
        MetaField.MODEL_HASH: {"field_name": "ckpt_name", "format": calc_model_hash},
        MetaField.CLIP_SKIP: {"field_name": "clip_skip", "format": convert_skip_clip},
        MetaField.POSITIVE_PROMPT: {"selector": stitch_together_positive_prompt},
        MetaField.NEGATIVE_PROMPT: {"selector": stitch_together_negative_prompt},
        MetaField.IMAGE_WIDTH: {"field_name": "empty_latent_width"},
        MetaField.IMAGE_HEIGHT: {"field_name": "empty_latent_height"},
    },
    "ttN KSampler_v2": {
        MetaField.SEED: {"field_name": "seed"},
        MetaField.STEPS: {"field_name": "steps"},
        MetaField.CFG: {"field_name": "cfg"},
        MetaField.SAMPLER_NAME: {"field_name": "sampler_name"},
        MetaField.SCHEDULER: {"field_name": "scheduler"},
    },
    "ttN pipeKSampler_v2": {
        MetaField.SEED: {"field_name": "seed"},
        MetaField.STEPS: {"field_name": "steps"},
        MetaField.CFG: {"field_name": "cfg"},
        MetaField.SAMPLER_NAME: {"field_name": "sampler_name"},
        MetaField.SCHEDULER: {"field_name": "scheduler"},
    },
    "ttN pipeKSamplerAdvanced_v2": {
        MetaField.SEED: {"field_name": "seed"},
        MetaField.STEPS: {"field_name": "steps"},
        MetaField.CFG: {"field_name": "cfg"},
        MetaField.SAMPLER_NAME: {"field_name": "sampler_name"},
        MetaField.SCHEDULER: {"field_name": "scheduler"},
    },
    "ttN pipeKSamplerSDXL_v2": {
        MetaField.SEED: {"field_name": "seed"},
        MetaField.STEPS: {"field_name": "steps"},
        MetaField.CFG: {"field_name": "cfg"},
        MetaField.SAMPLER_NAME: {"field_name": "sampler_name"},
        MetaField.SCHEDULER: {"field_name": "scheduler"},
    },
}
