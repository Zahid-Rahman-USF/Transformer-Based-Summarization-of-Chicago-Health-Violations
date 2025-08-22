from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from peft import PeftModel, PeftConfig

def load_model_and_tokenizer(model_path):
    # First load the base flan-t5-small model
    base_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")

    # Then load the LoRA adapter on top
    model = PeftModel.from_pretrained(base_model, model_path)
    return model, tokenizer
